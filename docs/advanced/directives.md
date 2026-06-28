# 📝 Директивы в Tailwind CSS

> **Полное руководство по директивам Tailwind:** от базовых `@tailwind` до продвинутых `@apply`, `@layer`, `theme()` и `@screen`

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Поймёте, что такое директивы и зачем они нужны
- ✅ Освоите `@tailwind` — подключение базовых стилей
- ✅ Научитесь использовать `@apply` для переиспользования утилит
- ✅ Поймёте систему слоёв через `@layer`
- ✅ Освоите `theme()` для доступа к значениям темы в CSS
- ✅ Научитесь использовать `@screen` для медиа-запросов
- ✅ Поймёте, когда использовать директивы, а когда — утилиты
- ✅ Избежите типичных ошибок при работе с директивами

## 🎯 Что такое директивы?

**Директивы** — это специальные CSS-конструкции, которые Tailwind обрабатывает при сборке. Они позволяют:

- Подключать базовые стили Tailwind
- Переиспользовать утилиты в кастомном CSS
- Управлять порядком применения стилей
- Получать значения из конфигурации

## 📦 Директива `@tailwind`

### Базовое подключение

`@tailwind` — это **главная директива**, которая подключает стили Tailwind в ваш CSS-файл:

```css
/* styles.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### Что делает каждая директива

| Директива | Что подключает | Когда нужна |
| :-- | :-- | :-- |
| `@tailwind base` | CSS-сброс (Preflight), базовые стили HTML | Всегда |
| `@tailwind components` | Стили компонентов из плагинов | Всегда |
| `@tailwind utilities` | Все утилитарные классы | Всегда |

### Preflight (CSS Reset)

`@tailwind base` включает **Preflight** — современную версию CSS reset:

```css
/* Что делает Preflight: */
/* 1. Убирает margin у всех элементов */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
}

/* 2. Устанавливает line-height: 1.5 для html */
html {
  line-height: 1.5;
  -webkit-text-size-adjust: 100%;
}

/* 3. Делает изображения блочными */
img, picture, video, canvas, svg {
  display: block;
  max-width: 100%;
}

/* 4. Убирает стили у кнопок */
button, input, optgroup, select, textarea {
  font: inherit;
  color: inherit;
}

/* 5. Делает ссылки наследующими цвет */
a {
  color: inherit;
  text-decoration: inherit;
}
```

> 💡 **Важно:** Preflight **агрессивно сбрасывает стили**. Если вы не хотите его использовать, можно отключить:

```js
// tailwind.config.js
module.exports = {
  corePlugins: {
    preflight: false,
  },
}
```

### Порядок директив имеет значение

```css
/* ✅ Правильно: base → components → utilities */
@tailwind base;
@tailwind components;
@tailwind utilities;

/* ❌ Неправильно: утилиты перекроют компоненты */
@tailwind utilities;
@tailwind components;
@tailwind base;
```

## 🎨 Директива `@apply`

`@apply` позволяет **встраивать утилитарные классы** в кастомный CSS:

### Базовое использование

```css
/* styles.css */
.btn-primary {
  @apply bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600;
}

.card {
  @apply bg-white rounded-lg shadow-md p-6;
}
```

```html
<!-- Использование -->
<button class="btn-primary">Кнопка</button>
<div class="card">Карточка</div>
```

### Когда использовать `@apply`

#### ✅ Хорошо использовать для:

1. **Повторяющихся паттернов**

```css
/* Вместо дублирования */
.btn {
  @apply px-4 py-2 rounded font-medium transition-colors;
}

.btn-primary {
  @apply btn bg-blue-500 text-white hover:bg-blue-600;
}

.btn-secondary {
  @apply btn bg-gray-500 text-white hover:bg-gray-600;
}
```

2. **Интеграции с CMS** (WordPress, Ghost)

```css
/* Стили для контента из CMS */
.prose h1 {
  @apply text-4xl font-bold text-gray-900 mb-4;
}

.prose h2 {
  @apply text-2xl font-semibold text-gray-800 mb-3;
}

.prose p {
  @apply text-base text-gray-700 leading-relaxed mb-4;
}

.prose a {
  @apply text-blue-600 hover:underline;
}
```

3. **Компонентов в Vue/React**

```vue
<!-- Vue component -->
<template>
  <button :class="['btn', variant]">
    <slot />
  </button>
</template>

<style>
.btn {
  @apply px-4 py-2 rounded font-medium transition-colors;
}

.btn-primary {
  @apply bg-blue-500 text-white hover:bg-blue-600;
}

.btn-secondary {
  @apply bg-gray-500 text-white hover:bg-gray-600;
}
</style>
```

#### ❌ Не стоит использовать для:

1. **Одноразовых стилей**

```css
/* ❌ Плохо: это не переиспользуется */
.my-special-button {
  @apply bg-blue-500 text-white px-4 py-2 rounded;
}

/* ✅ Хорошо: просто используйте утилиты в HTML */
<button class="bg-blue-500 text-white px-4 py-2 rounded">
  Кнопка
</button>
```

2. **Когда можно использовать компоненты фреймворка**

```jsx
// ❌ Плохо: @apply в React
<style>
.special-card {
  @apply bg-white rounded-lg shadow-md p-6;
}
</style>

// ✅ Хорошо: компонент в React
function Card({ children }) {
  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      {children}
    </div>
  )
}
```

### Ограничения `@apply`

#### ❌ Нельзя использовать с arbitrary values

```css
/* ❌ Плохо: arbitrary values не работают с @apply */
.custom {
  @apply bg-[#ff5722] text-[15px];
}

/* ✅ Хорошо: используйте CSS-свойства напрямую */
.custom {
  background-color: #ff5722;
  font-size: 15px;
}
```

#### ❌ Нельзя использовать с модификаторами состояний

```css
/* ❌ Плохо: hover: не работает в @apply */
.btn {
  @apply bg-blue-500 hover:bg-blue-600;
}

/* ✅ Хорошо: выносите состояния отдельно */
.btn {
  @apply bg-blue-500;
}

.btn:hover {
  @apply bg-blue-600;
}
```

#### ❌ Нельзя использовать с responsive-модификаторами

```css
/* ❌ Плохо: md: не работает в @apply */
.container {
  @apply w-full md:w-1/2 lg:w-1/3;
}

/* ✅ Хорошо: используйте медиа-запросы */
.container {
  @apply w-full;
}

@media (min-width: 768px) {
  .container {
    @apply w-1/2;
  }
}

@media (min-width: 1024px) {
  .container {
    @apply w-1/3;
  }
}
```

## 📚 Директива `@layer`

`@layer` управляет **порядком применения стилей** и помогает избежать проблем со специфичностью:

### Базовое использование

```css
/* styles.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

/* Кастомные стили в слоях */
@layer base {
  h1 {
    @apply text-4xl font-bold;
  }
  h2 {
    @apply text-2xl font-semibold;
  }
}

@layer components {
  .btn {
    @apply px-4 py-2 rounded font-medium;
  }
  .card {
    @apply bg-white rounded-lg shadow-md p-6;
  }
}

@layer utilities {
  .text-shadow {
    text-shadow: 2px 2px 4px rgb(0 0 0 / 0.5);
  }
}
```

### Зачем нужны слои?

**Проблема без `@layer`:**

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

/* Этот стиль применится ПОСЛЕ утилит и может их переопределить */
.btn {
  background-color: blue;
}
```

```html
<!-- Ожидание: bg-red-500 -->
<!-- Реальность: синий фон (переопределён) -->
<button class="btn bg-red-500">Кнопка</button>
```

**Решение с `@layer`:**

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer components {
  .btn {
    background-color: blue;
  }
}
```

```html
<!-- Теперь bg-red-500 работает корректно -->
<button class="btn bg-red-500">Кнопка</button>
```

### Порядок слоёв

```
1. @layer base        (самый низкий приоритет)
2. @layer components
3. @layer utilities
4. Кастомный CSS      (самый высокий приоритет)
```

### Практический пример

```css
/* styles.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

/* Базовые стили для HTML-элементов */
@layer base {
  body {
    @apply bg-gray-50 text-gray-900;
  }

  h1 {
    @apply text-4xl font-bold tracking-tight;
  }

  h2 {
    @apply text-2xl font-semibold;
  }

  a {
    @apply text-blue-600 hover:underline;
  }
}

/* Компоненты */
@layer components {
  .btn {
    @apply inline-flex items-center justify-center px-4 py-2 rounded-lg font-medium transition-colors;
  }

  .btn-primary {
    @apply btn bg-blue-600 text-white hover:bg-blue-700;
  }

  .btn-secondary {
    @apply btn bg-gray-200 text-gray-900 hover:bg-gray-300;
  }

  .card {
    @apply bg-white rounded-xl shadow-md p-6;
  }

  .input {
    @apply w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500;
  }
}

/* Кастомные утилиты */
@layer utilities {
  .text-shadow {
    text-shadow: 2px 2px 4px rgb(0 0 0 / 0.5);
  }

  .scrollbar-hide {
    -ms-overflow-style: none;
    scrollbar-width: none;
  }

  .scrollbar-hide::-webkit-scrollbar {
    display: none;
  }
}
```

## 🎯 Функция `theme()`

`theme()` позволяет **получать значения из конфигурации** прямо в CSS:

### Базовое использование

```css
/* styles.css */
.custom-shadow {
  box-shadow: 0 4px 6px -1px theme('colors.blue.500');
}

.custom-font {
  font-family: theme('fontFamily.sans');
}

.custom-spacing {
  padding: theme('spacing.4');
}
```

### Доступ к значениям темы

```css
/* Цвета */
.btn-primary {
  background-color: theme('colors.blue.500');
}

/* Отступы */
.card {
  padding: theme('spacing.6');
}

/* Размеры шрифтов */
.heading {
  font-size: theme('fontSize.2xl');
}

/* Радиусы */
.badge {
  border-radius: theme('borderRadius.full');
}

/* Тени */
.card {
  box-shadow: theme('boxShadow.lg');
}

/* Breakpoints */
@media (min-width: theme('screens.md')) {
  .container {
    max-width: 768px;
  }
}
```

### Dot notation vs bracket notation

```css
/* Dot notation (проще) */
.btn {
  background-color: theme('colors.blue.500');
}

/* Bracket notation (для ключей с дефисами) */
.btn {
  background-color: theme('colors.blue-gray.500');
  /* или */
  background-color: theme('colors[blue-gray].500');
}
```

### Fallback значения

```css
/* С fallback значением */
.custom-color {
  color: theme('colors.brand.500', #ff5722);
}
```

### Практический пример

```css
/* styles.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer components {
  .btn-primary {
    @apply px-4 py-2 rounded-lg font-medium text-white;
    background-color: theme('colors.blue.600');
    transition: background-color 0.2s;
  }

  .btn-primary:hover {
    background-color: theme('colors.blue.700');
  }

  .btn-primary:focus {
    box-shadow: 0 0 0 3px theme('colors.blue.500 / 50%');
  }

  .card {
    @apply rounded-xl p-6;
    background-color: theme('colors.white');
    box-shadow: theme('boxShadow.md');
  }

  .card:hover {
    box-shadow: theme('boxShadow.lg');
  }
}
```

## 📱 Директива `@screen`

`@screen` позволяет создавать **медиа-запросы на основе breakpoints** из конфига:

### Базовое использование

```css
/* styles.css */
@screen md {
  .container {
    max-width: 768px;
  }
}

@screen lg {
  .container {
    max-width: 1024px;
  }
}
```

Это эквивалентно:

```css
@media (min-width: 768px) {
  .container {
    max-width: 768px;
  }
}

@media (min-width: 1024px) {
  .container {
    max-width: 1024px;
  }
}
```

### Преимущества `@screen`

1. **Синхронизация с конфигом**

```js
// tailwind.config.js
module.exports = {
  theme: {
    screens: {
      'tablet': '640px',
      'laptop': '1024px',
      'desktop': '1280px',
    },
  },
}
```

```css
/* Автоматически использует значения из конфига */
@screen tablet {
  .container {
    max-width: 640px;
  }
}

@screen laptop {
  .container {
    max-width: 1024px;
  }
}
```

2. **Меньше дублирования**

```css
/* ❌ Плохо: дублирование значений */
@media (min-width: 768px) {
  .card {
    @apply grid grid-cols-2;
  }
}

@media (min-width: 1024px) {
  .card {
    @apply grid grid-cols-3;
  }
}

/* ✅ Хорошо: используем @screen */
@screen md {
  .card {
    @apply grid grid-cols-2;
  }
}

@screen lg {
  .card {
    @apply grid grid-cols-3;
  }
}
```

### Комбинирование с `@apply`

```css
@screen md {
  .hero {
    @apply flex items-center justify-between;
  }

  .hero-title {
    @apply text-5xl;
  }
}

@screen lg {
  .hero {
    @apply gap-16;
  }

  .hero-title {
    @apply text-6xl;
  }
}
```

### Практический пример

```css
/* styles.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer components {
  .container {
    @apply w-full mx-auto px-4;
  }

  @screen sm {
    .container {
      @apply px-6;
    }
  }

  @screen md {
    .container {
      @apply px-8 max-w-3xl;
    }
  }

  @screen lg {
    .container {
      @apply px-10 max-w-5xl;
    }
  }

  @screen xl {
    .container {
      @apply px-12 max-w-7xl;
    }
  }
}
```

## 🔧 Директива `@config`

`@config` позволяет **указать путь к конфигу** прямо в CSS-файле:

```css
/* styles.css */
@config "./tailwind.config.js";

@tailwind base;
@tailwind components;
@tailwind utilities;
```

Это полезно, когда:
- У вас несколько CSS-файлов с разными конфигами
- Вы хотите явно указать, какой конфиг использовать

## 🎨 Практические паттерны

### 1. 🎨 Дизайн-система через `@layer`

```css
/* styles.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

/* Базовые стили */
@layer base {
  :root {
    --color-primary: 59 130 246;
    --color-secondary: 139 92 246;
  }

  body {
    @apply bg-white text-gray-900 antialiased;
    font-family: theme('fontFamily.sans');
  }

  h1 {
    @apply text-4xl font-bold tracking-tight;
  }

  h2 {
    @apply text-2xl font-semibold;
  }

  h3 {
    @apply text-xl font-medium;
  }
}

/* Компоненты */
@layer components {
  /* Кнопки */
  .btn {
    @apply inline-flex items-center justify-center px-4 py-2 rounded-lg font-medium transition-all duration-200;
  }

  .btn-primary {
    @apply btn bg-blue-600 text-white hover:bg-blue-700 active:bg-blue-800;
  }

  .btn-secondary {
    @apply btn bg-gray-100 text-gray-900 hover:bg-gray-200 active:bg-gray-300;
  }

  .btn-outline {
    @apply btn border border-gray-300 hover:bg-gray-50;
  }

  .btn-ghost {
    @apply btn hover:bg-gray-100;
  }

  .btn-sm {
    @apply px-3 py-1.5 text-sm;
  }

  .btn-lg {
    @apply px-6 py-3 text-lg;
  }

  /* Карточки */
  .card {
    @apply bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden;
  }

  .card-hover {
    @apply card hover:shadow-md transition-shadow;
  }

  /* Поля ввода */
  .input {
    @apply w-full px-4 py-2 border border-gray-300 rounded-lg bg-white transition-colors;
  }

  .input:focus {
    @apply outline-none ring-2 ring-blue-500 border-blue-500;
  }

  .input-error {
    @apply input border-red-500 focus:ring-red-500 focus:border-red-500;
  }

  /* Бейджи */
  .badge {
    @apply inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium;
  }

  .badge-primary {
    @apply badge bg-blue-100 text-blue-800;
  }

  .badge-success {
    @apply badge bg-green-100 text-green-800;
  }

  .badge-warning {
    @apply badge bg-yellow-100 text-yellow-800;
  }

  .badge-danger {
    @apply badge bg-red-100 text-red-800;
  }
}

/* Утилиты */
@layer utilities {
  .text-shadow {
    text-shadow: 2px 2px 4px rgb(0 0 0 / 0.5);
  }

  .text-shadow-sm {
    text-shadow: 1px 1px 2px rgb(0 0 0 / 0.3);
  }

  .scrollbar-hide {
    -ms-overflow-style: none;
    scrollbar-width: none;
  }

  .scrollbar-hide::-webkit-scrollbar {
    display: none;
  }
}
```

### 2. 🎨 Типографика для CMS

```css
/* styles.css */
@layer components {
  .prose {
    @apply text-gray-700 leading-relaxed;
  }

  .prose h1 {
    @apply text-4xl font-bold text-gray-900 mt-8 mb-4;
  }

  .prose h2 {
    @apply text-2xl font-semibold text-gray-900 mt-6 mb-3;
  }

  .prose h3 {
    @apply text-xl font-medium text-gray-900 mt-4 mb-2;
  }

  .prose p {
    @apply mb-4;
  }

  .prose a {
    @apply text-blue-600 hover:underline;
  }

  .prose ul {
    @apply list-disc list-inside mb-4 space-y-1;
  }

  .prose ol {
    @apply list-decimal list-inside mb-4 space-y-1;
  }

  .prose blockquote {
    @apply border-l-4 border-blue-500 pl-4 italic text-gray-600 my-4;
  }

  .prose code {
    @apply bg-gray-100 px-1.5 py-0.5 rounded text-sm font-mono;
  }

  .prose pre {
    @apply bg-gray-900 text-gray-100 p-4 rounded-lg overflow-x-auto my-4;
  }

  .prose pre code {
    @apply bg-transparent p-0;
  }

  .prose img {
    @apply rounded-lg my-4;
  }

  .prose table {
    @apply w-full border-collapse my-4;
  }

  .prose th {
    @apply bg-gray-100 border border-gray-300 px-4 py-2 text-left font-semibold;
  }

  .prose td {
    @apply border border-gray-300 px-4 py-2;
  }
}
```

### 3. 🎨 Анимации через `@layer`

```css
/* styles.css */
@layer utilities {
  @keyframes fade-in {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }

  @keyframes slide-up {
    from {
      transform: translateY(20px);
      opacity: 0;
    }
    to {
      transform: translateY(0);
      opacity: 1;
    }
  }

  @keyframes slide-down {
    from {
      transform: translateY(-20px);
      opacity: 0;
    }
    to {
      transform: translateY(0);
      opacity: 1;
    }
  }

  @keyframes scale-in {
    from {
      transform: scale(0.9);
      opacity: 0;
    }
    to {
      transform: scale(1);
      opacity: 1;
    }
  }

  .animate-fade-in {
    animation: fade-in 0.3s ease-out;
  }

  .animate-slide-up {
    animation: slide-up 0.3s ease-out;
  }

  .animate-slide-down {
    animation: slide-down 0.3s ease-out;
  }

  .animate-scale-in {
    animation: scale-in 0.2s ease-out;
  }
}
```

### 4. 🎨 Темизация через CSS-переменные

```css
/* styles.css */
@layer base {
  :root {
    --color-primary: 59 130 246;
    --color-secondary: 139 92 246;
    --color-background: 255 255 255;
    --color-surface: 249 250 251;
    --color-content: 17 24 39;
    --color-content-secondary: 75 85 99;
    --color-border: 229 231 235;
  }

  .dark {
    --color-primary: 96 165 250;
    --color-secondary: 167 139 250;
    --color-background: 17 24 39;
    --color-surface: 31 41 55;
    --color-content: 243 244 246;
    --color-content-secondary: 156 163 175;
    --color-border: 55 65 81;
  }

  body {
    background-color: rgb(var(--color-background));
    color: rgb(var(--color-content));
  }
}

@layer components {
  .card {
    background-color: rgb(var(--color-surface));
    border-color: rgb(var(--color-border));
    color: rgb(var(--color-content));
  }

  .btn-primary {
    background-color: rgb(var(--color-primary));
    color: white;
  }

  .btn-primary:hover {
    background-color: rgb(var(--color-primary) / 0.9);
  }

  .text-secondary {
    color: rgb(var(--color-content-secondary));
  }
}
```

### 5. 🎨 Печать стилей

```css
/* styles.css */
@media print {
  .no-print {
    @apply hidden;
  }

  body {
    @apply bg-white text-black;
  }

  a {
    @apply text-black no-underline;
  }

  .card {
    @apply shadow-none border border-gray-300;
  }

  .btn {
    @apply hidden;
  }
}
```

## 📊 Шпаргалка: что когда использовать

| Задача | Решение |
| :-- | :-- |
| Подключить Tailwind | `@tailwind base; @tailwind components; @tailwind utilities;` |
| Переиспользовать утилиты | `@apply bg-blue-500 text-white` |
| Управлять порядком стилей | `@layer base/components/utilities` |
| Получить значение из темы | `theme('colors.blue.500')` |
| Медиа-запрос из конфига | `@screen md { ... }` |
| Указать путь к конфигу | `@config "./tailwind.config.js"` |
| Отключить Preflight | `corePlugins: { preflight: false }` |
| Добавить кастомную утилиту | `@layer utilities { .my-utility { ... } }` |
| Добавить компонент | `@layer components { .my-component { ... } }` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: `@apply` с модификаторами состояний

```css
/* ❌ Плохо: hover: не работает в @apply */
.btn {
  @apply bg-blue-500 hover:bg-blue-600;
}

/* ✅ Хорошо: выносите состояния отдельно */
.btn {
  @apply bg-blue-500;
}

.btn:hover {
  @apply bg-blue-600;
}
```

### ❌ Ошибка 2: `@apply` с responsive-модификаторами

```css
/* ❌ Плохо: md: не работает в @apply */
.container {
  @apply w-full md:w-1/2;
}

/* ✅ Хорошо: используйте @screen */
.container {
  @apply w-full;
}

@screen md {
  .container {
    @apply w-1/2;
  }
}
```

### ❌ Ошибка 3: Забывают порядок `@tailwind`

```css
/* ❌ Плохо: утилиты перекроют компоненты */
@tailwind utilities;
@tailwind components;
@tailwind base;

/* ✅ Хорошо: правильный порядок */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### ❌ Ошибка 4: Кастомный CSS без `@layer`

```css
/* ❌ Плохо: кастомный CSS может переопределить утилиты */
@tailwind base;
@tailwind components;
@tailwind utilities;

.btn {
  background-color: blue;
}
```

```html
<!-- Ожидание: bg-red-500 -->
<!-- Реальность: синий фон -->
<button class="btn bg-red-500">Кнопка</button>
```

```css
/* ✅ Хорошо: используем @layer */
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer components {
  .btn {
    background-color: blue;
  }
}
```

### ❌ Ошибка 5: `theme()` без кавычек

```css
/* ❌ Плохо: синтаксическая ошибка */
.btn {
  background-color: theme(colors.blue.500);
}

/* ✅ Хорошо: кавычки обязательны */
.btn {
  background-color: theme('colors.blue.500');
}
```

### ❌ Ошибка 6: `@screen` с несуществующим breakpoint

```js
// tailwind.config.js
module.exports = {
  theme: {
    screens: {
      'md': '768px',
      'lg': '1024px',
    },
  },
}
```

```css
/* ❌ Плохо: breakpoint 'xl' не определён */
@screen xl {
  .container {
    max-width: 1280px;
  }
}

/* ✅ Хорошо: используем существующие breakpoints */
@screen lg {
  .container {
    max-width: 1024px;
  }
}
```

### ❌ Ошибка 7: `@apply` с arbitrary values

```css
/* ❌ Плохо: arbitrary values не работают */
.custom {
  @apply bg-[#ff5722] text-[15px];
}

/* ✅ Хорошо: используем CSS-свойства */
.custom {
  background-color: #ff5722;
  font-size: 15px;
}
```

### ❌ Ошибка 8: Забывают `@tailwind utilities`

```css
/* ❌ Плохо: утилиты не подключены */
@tailwind base;
@tailwind components;

/* ✅ Хорошо: все три директивы */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

## 🎯 Что дальше?

Теперь вы полностью владеете директивами Tailwind CSS! Но это только часть продвинутого уровня. Следующая важная тема — **оптимизация production build**.

**Следующий шаг:** [⚡ Оптимизация Tailwind CSS](optimization.md) — изучим PurgeCSS, tree-shaking и лучшие практики для production.

---