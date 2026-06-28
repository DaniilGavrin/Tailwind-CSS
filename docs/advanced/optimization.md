# ⚡ Оптимизация Tailwind CSS

> **Полное руководство по оптимизации production build:** от PurgeCSS и tree-shaking до минификации и анализа размера бандла

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Поймёте, как работает JIT-компилятор Tailwind
- ✅ Научитесь настраивать `content` для корректной очистки неиспользуемого CSS
- ✅ Освоите минификацию и оптимизацию CSS для production
- ✅ Научитесь анализировать размер бандла
- ✅ Поймёте, как кэшировать и доставлять CSS оптимально
- ✅ Освоите best practices для production
- ✅ Избежите типичных ошибок, раздувающих CSS

## 📊 Размеры Tailwind: до и после оптимизации

Посмотрим на разницу между dev и production:

| Состояние | Размер (gzip) | Описание |
| :-- | :-- | :-- |
| **Tailwind без очистки** | ~3-4 MB | Все 50 000+ утилит |
| **С JIT + content** | ~5-15 KB | Только используемые классы |
| **После минификации** | ~3-10 KB | Финальный production CSS |

> 💡 **Факт:** правильно настроенный Tailwind в production весит **меньше**, чем один файл Bootstrap (~25 KB gzip).

## 🚀 JIT-компилятор (Just-In-Time)

С Tailwind v3.0 JIT-компилятор включён **по умолчанию**. Это значит:

### Как работает JIT

```
1. Вы пишете HTML с классами:
   <div class="bg-blue-500 hover:bg-blue-600 p-4">

2. Tailwind сканирует ваши файлы (content)

3. Генерирует CSS ТОЛЬКО для использованных классов

4. Результат: минимальный CSS без мусора
```

### Преимущества JIT

- ⚡ **Мгновенная сборка** — не нужно ждать генерации всех 50 000 классов
- 🎯 **Точная очистка** — в CSS попадают только использованные классы
- 🎨 **Arbitrary values** — `bg-[#ff5722]`, `w-[237px]` работают из коробки
- 📦 **Маленький бандл** — обычно 5-15 KB gzip

## 📁 Настройка `content`

Параметр `content` в `tailwind.config.js` говорит Tailwind, **какие файлы сканировать**:

### Базовая настройка

```js
// tailwind.config.js
module.exports = {
  content: [
    './src/**/*.{html,js,jsx,ts,tsx,vue,svelte}',
    './public/**/*.html',
  ],
}
```

### Для разных фреймворков

#### React / Next.js

```js
module.exports = {
  content: [
    './src/**/*.{js,jsx,ts,tsx}',
    './app/**/*.{js,jsx,ts,tsx}',
    './pages/**/*.{js,jsx,ts,tsx}',
    './components/**/*.{js,jsx,ts,tsx}',
  ],
}
```

#### Vue / Nuxt

```js
module.exports = {
  content: [
    './src/**/*.{vue,js,ts}',
    './components/**/*.{vue,js,ts}',
    './pages/**/*.vue',
    './layouts/**/*.vue',
  ],
}
```

#### Svelte / SvelteKit

```js
module.exports = {
  content: [
    './src/**/*.{html,js,svelte,ts}',
  ],
}
```

#### Laravel / PHP

```js
module.exports = {
  content: [
    './resources/**/*.blade.php',
    './resources/**/*.js',
    './resources/**/*.vue',
  ],
}
```

#### WordPress

```js
module.exports = {
  content: [
    './**/*.php',
    './src/**/*.{js,jsx,ts,tsx}',
  ],
}
```

### Исключения в `content`

```js
module.exports = {
  content: [
    './src/**/*.{js,jsx,ts,tsx}',
    '!./src/**/*.test.{js,ts}',       // Исключаем тесты
    '!./src/**/*.stories.{js,tsx}',   // Исключаем Storybook
  ],
}
```

## 🧹 Safelist: защита классов от удаления

Иногда классы генерируются **динамически** (например, через JavaScript), и Tailwind не может их найти в файлах. Используйте `safelist`:

### Базовый safelist

```js
module.exports = {
  content: ['./src/**/*.{js,jsx}'],
  safelist: [
    'bg-red-500',
    'bg-green-500',
    'bg-blue-500',
    'text-white',
  ],
}
```

### Safelist с паттернами

```js
module.exports = {
  content: ['./src/**/*.{js,jsx}'],
  safelist: [
    {
      pattern: /bg-(red|green|blue)-500/,
      variants: ['hover', 'focus'],
    },
    {
      pattern: /text-(sm|base|lg|xl)/,
    },
    'grid-cols-[0-9]+',  // Все grid-cols-N
  ],
}
```

### Когда использовать safelist

#### ✅ Хорошие случаи

```jsx
// Классы генерируются динамически
const colors = ['red', 'green', 'blue', 'yellow'];
const color = colors[Math.floor(Math.random() * colors.length)];

<div className={`bg-${color}-500`}>...</div>
```

```js
// Tailwind не увидит `bg-${color}-500`, поэтому:
module.exports = {
  safelist: [
    { pattern: /bg-(red|green|blue|yellow)-500/ }
  ]
}
```

#### ❌ Плохие случаи

```js
// ❌ Плохо: слишком широкий safelist
module.exports = {
  safelist: [
    { pattern: /.*/ }  // Сохранит ВСЕ классы!
  ]
}
```

## ⚙️ Production build

### Через Tailwind CLI

```bash
# Development (с watch)
npx tailwindcss -i ./src/input.css -o ./src/output.css --watch

# Production (минифицированный)
npx tailwindcss -i ./src/input.css -o ./dist/output.css --minify
```

### Через PostCSS

```js
// postcss.config.js
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
    ...(process.env.NODE_ENV === 'production' ? { cssnano: {} } : {}),
  },
}
```

### Через Vite

```js
// vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  build: {
    cssMinify: true,
    rollupOptions: {
      output: {
        assetFileNames: 'assets/[name]-[hash].css',
      },
    },
  },
})
```

### Через Next.js

Next.js **автоматически** минифицирует CSS в production:

```bash
npm run build  # CSS уже минифицирован
```

## 📉 Минификация CSS

### Через cssnano

```bash
npm install -D cssnano postcss
```

```js
// postcss.config.js
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
    ...(process.env.NODE_ENV === 'production' ? { 
      cssnano: {
        preset: ['default', {
          discardComments: { removeAll: true },
          normalizeWhitespace: true,
        }]
      } 
    } : {}),
  },
}
```

### Через Tailwind CLI

```bash
npx tailwindcss -o output.css --minify
```

### Что делает минификация

**До:**
```css
.btn {
  background-color: #3b82f6;
  color: #ffffff;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  /* Это кнопка */
}

.btn:hover {
  background-color: #2563eb;
}
```

**После:**
```css
.btn{background-color:#3b82f6;color:#fff;padding:.5rem 1rem;border-radius:.375rem}.btn:hover{background-color:#2563eb}
```

## 📊 Анализ размера бандла

### Через bundle analyzer

```bash
# Для Vite
npm install -D rollup-plugin-visualizer

# Для Webpack
npm install -D webpack-bundle-analyzer
```

```js
// vite.config.js
import { visualizer } from 'rollup-plugin-visualizer'

export default defineConfig({
  plugins: [
    visualizer({
      filename: 'stats.html',
      open: true,
    }),
  ],
})
```

### Через PurgeCSS Standalone

```bash
npm install -g purgecss
purgecss --css output.css --content src/**/*.html --output purged/
```

### Ручная проверка

```bash
# Размер до gzip
ls -lh dist/assets/*.css

# Размер после gzip
gzip -c dist/assets/*.css | wc -c
```

### Chrome DevTools

1. Откройте DevTools → **Network**
2. Загрузите страницу
3. Найдите CSS-файл
4. Посмотрите **Size** (gzip) и **Transferred**

## 🎯 Практические паттерны

### 1. ⚡ Идеальный production build

```json
// package.json
{
  "scripts": {
    "dev": "tailwindcss -i src/input.css -o src/output.css --watch",
    "build": "NODE_ENV=production tailwindcss -i src/input.css -o dist/output.css --minify",
    "build:analyze": "npm run build && gzip -c dist/output.css | wc -c"
  }
}
```

### 2. 🎨 Динамические классы без safelist

Вместо safelist используйте **полные имена классов**:

```jsx
// ❌ Плохо: динамическое имя
const colors = {
  primary: 'blue',
  success: 'green',
  danger: 'red',
};
<div className={`bg-${colors[variant]}-500`}>

// ✅ Хорошо: полные имена
const colors = {
  primary: 'bg-blue-500',
  success: 'bg-green-500',
  danger: 'bg-red-500',
};
<div className={colors[variant]}>
```

### 3. 📦 Разделение CSS на чанки

```js
// styles/critical.css — для above-the-fold
@tailwind base;
@tailwind components;
@layer utilities {
  .hero { @apply bg-blue-600 text-white p-8; }
  .nav { @apply flex items-center justify-between; }
}

// styles/deferred.css — для below-the-fold
@tailwind utilities;
@layer components {
  .footer { @apply bg-gray-900 text-white p-8; }
  .modal { @apply fixed inset-0 bg-black/50; }
}
```

```html
<head>
  <!-- Critical CSS inline -->
  <style>/* содержимое critical.css */</style>
  
  <!-- Deferred CSS async -->
  <link rel="preload" href="/deferred.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
</head>
```

### 4. 🚀 Кэширование CSS

```js
// vite.config.js
export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        // Хеш в имени файла для long-term кэширования
        assetFileNames: 'assets/[name]-[hash].css',
        chunkFileNames: 'assets/[name]-[hash].js',
      },
    },
  },
})
```

```nginx
# nginx.conf
location /assets/ {
  expires 1y;
  add_header Cache-Control "public, immutable";
}
```

### 5. 🎯 Preload critical CSS

```html
<head>
  <!-- Preload основного CSS -->
  <link rel="preload" href="/assets/main-abc123.css" as="style">
  <link rel="stylesheet" href="/assets/main-abc123.css">
  
  <!-- Prefetch для следующих страниц -->
  <link rel="prefetch" href="/assets/about-def456.css">
</head>
```

### 6. 📊 Мониторинг размера CSS в CI

```yaml
# .github/workflows/css-size.yml
name: CSS Size Check
on: [pull_request]
jobs:
  check-size:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install
      - run: npm run build
      - name: Check CSS size
        run: |
          SIZE=$(gzip -c dist/output.css | wc -c)
          echo "CSS size (gzip): $SIZE bytes"
          if [ $SIZE -gt 20000 ]; then
            echo "⚠️ CSS больше 20KB!"
            exit 1
          fi
```

## 📈 Performance метрики

### Целевые показатели

| Метрика | Цель | Инструмент |
| :-- | :-- | :-- |
| **CSS size (gzip)** | < 15 KB | `gzip -c` |
| **First Contentful Paint** | < 1.8s | Lighthouse |
| **Largest Contentful Paint** | < 2.5s | Lighthouse |
| **Total Blocking Time** | < 200ms | Lighthouse |
| **Cumulative Layout Shift** | < 0.1 | Lighthouse |

### Проверка через Lighthouse

```bash
# Установка
npm install -g lighthouse

# Запуск
lighthouse https://yoursite.com --view
```

### Проверка через PageSpeed Insights

🌐 [PageSpeed Insights](https://pagespeed.web.dev/) — бесплатный инструмент Google

## 📊 Шпаргалка: что когда использовать

| Задача | Решение |
| :-- | :-- |
| Production build | `tailwindcss -o output.css --minify` |
| Настроить сканирование | `content: ['./src/**/*.{js,jsx}']` |
| Защитить динамические классы | `safelist: [{ pattern: /bg-/ }]` |
| Минифицировать CSS | `cssnano` или `--minify` |
| Анализ бандла | `rollup-plugin-visualizer` |
| Разделить CSS | Critical + Deferred |
| Кэшировать CSS | Хеш в имени + `Cache-Control` |
| Проверить размер | `gzip -c file.css \| wc -c` |
| Использовать динамические классы | Полные имена вместо конкатенации |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Забывают указать `content`

```js
// ❌ Плохо: Tailwind не знает, что сканировать
module.exports = {
  theme: { extend: { ... } },
  // content отсутствует
}

// ✅ Хорошо: явно указываем файлы
module.exports = {
  content: ['./src/**/*.{js,jsx,ts,tsx}'],
  theme: { extend: { ... } },
}
```

**Результат:** CSS будет пустым или содержать все классы.

### ❌ Ошибка 2: Динамическая конкатенация классов

```jsx
// ❌ Плохо: Tailwind не увидит эти классы
const size = 'lg';
<button className={`btn-${size}`}>Кнопка</button>

// ✅ Хорошо: полные имена
const sizes = {
  sm: 'btn-sm',
  md: 'btn-md',
  lg: 'btn-lg',
};
<button className={sizes[size]}>Кнопка</button>
```

### ❌ Ошибка 3: Safelist со всем подряд

```js
// ❌ Плохо: CSS раздуется до мегабайт
module.exports = {
  safelist: [{ pattern: /.*/ }],
}

// ✅ Хорошо: только нужные паттерны
module.exports = {
  safelist: [
    { pattern: /bg-(red|green|blue)-500/ }
  ],
}
```

### ❌ Ошибка 4: Не минифицируют в production

```bash
# ❌ Плохо: обычный build в production
npx tailwindcss -o dist/output.css

# ✅ Хорошо: с минификацией
npx tailwindcss -o dist/output.css --minify
```

### ❌ Ошибка 5: Забывают `NODE_ENV=production`

```js
// postcss.config.js
module.exports = {
  plugins: {
    tailwindcss: {},
    // cssnano не применится без NODE_ENV
    cssnano: {},
  },
}
```

```bash
# ✅ Хорошо: устанавливаем переменную окружения
NODE_ENV=production npm run build

# Или cross-env для Windows
npm install -D cross-env
cross-env NODE_ENV=production npm run build
```

### ❌ Ошибка 6: Игнорируют gzip

```bash
# ❌ Плохо: смотрим только на "сырой" размер
ls -lh dist/output.css
# 50 KB

# ✅ Хорошо: gzip-размер (то, что получит пользователь)
gzip -c dist/output.css | wc -c
# 8 KB
```

### ❌ Ошибка 7: Весь CSS в одном файле

```html
<!-- ❌ Плохо: один огромный CSS-файл -->
<link rel="stylesheet" href="/app.css"> <!-- 200 KB -->

<!-- ✅ Хорошо: разделение на critical и deferred -->
<style>/* Critical CSS inline */</style>
<link rel="preload" href="/deferred.css" as="style">
```

### ❌ Ошибка 8: Не анализируют бандл

```bash
# ❌ Плохо: не знаем, что в бандле
npm run build

# ✅ Хорошо: регулярный анализ
npm run build
npx rollup-plugin-visualizer --open
# или
gzip -c dist/*.css | wc -c
```

### ❌ Ошибка 9: Используют `@import` для больших файлов

```css
/* ❌ Плохо: блокирует рендеринг */
@import url('https://fonts.googleapis.com/...');
@import url('large-library.css');
```

```html
<!-- ✅ Хорошо: async загрузка -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preload" href="large-library.css" as="style" onload="this.rel='stylesheet'">
```

### ❌ Ошибка 10: Нет кэширования

```nginx
# ❌ Плохо: CSS загружается каждый раз
location /assets/ {
  # без кэширования
}

# ✅ Хорошо: long-term кэширование
location /assets/ {
  expires 1y;
  add_header Cache-Control "public, immutable";
}
```

## 🎯 Checklist перед деплоем

Перед тем как запушить в production, проверьте:

- [ ] `content` в `tailwind.config.js` указывает на все нужные файлы
- [ ] Нет динамической конкатенации классов (или настроен safelist)
- [ ] CSS минифицирован (`--minify` или `cssnano`)
- [ ] `NODE_ENV=production` установлен
- [ ] Размер CSS (gzip) < 15 KB
- [ ] Critical CSS загружается inline или с `preload`
- [ ] Настроено кэширование (хеш в имени + `Cache-Control`)
- [ ] Lighthouse показывает LCP < 2.5s
- [ ] Нет блокирующих CSS-ресурсов
- [ ] Проверили в DevTools → Network размер передаваемого CSS

## 🎯 Что дальше?

Поздравляем! Вы прошли **весь путь** от основ Tailwind CSS до продвинутых техник оптимизации. Теперь вы владеете:

- 🎨 **Стилями** — цвета, типографика, фоны, границы, эффекты
- 📐 **Макетами** — flexbox, grid, отступы, размеры
- 📱 **Адаптивностью** — breakpoints, dark mode, состояния
- ⚙️ **Продвинутыми техниками** — кастомизация, плагины, директивы, оптимизация

### Что изучить дальше

1. **[Интеграции](../integrations/react.md)** — React, Vue, Next.js
2. **Дизайн-системы** — создание собственной DS на Tailwind
3. **Headless UI** — [Headless UI](https://headlessui.com/), [Radix UI](https://www.radix-ui.com/)
4. **Компонентные библиотеки** — [shadcn/ui](https://ui.shadcn.com/), [daisyUI](https://daisyui.com/)

---