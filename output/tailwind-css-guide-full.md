# 📘 Tailwind CSS Guide — Полная версия

> Автоматически сгенерированная версия всей документации
> Дата генерации: 29.06.2026 01:11:04
> Источник: https://github.com/DaniilGavrin/tailwind-css-guide

---


<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: index.md -->
<!-- ═══════════════════════════════════════════════════════════ -->

# 📘 Tailwind CSS Guide

> **Utility-first CSS фреймворк для быстрого создания современных интерфейсов**

## 🎯 Что такое Tailwind CSS?

**Tailwind CSS** — это CSS фреймворк, который предоставляет сотни утилитарных классов прямо в вашем HTML. Вместо того чтобы придумывать имена классов и писать кастомный CSS, вы собираете дизайн из готовых блоков.

### 💡 Ключевые преимущества

- ⚡ **Быстрая разработка** — не нужно переключаться между HTML и CSS файлами
- 🎨 **Консистентный дизайн** — встроенная система цветов, отступов и типографики
- 📱 **Адаптивность из коробки** — мобильная адаптация через префиксы (`sm:`, `md:`, `lg:`)
- 🌙 **Dark mode** — поддержка тёмной темы одной директивой
- 📦 **Маленький размер** — PurgeCSS удаляет неиспользуемые классы
- 🔧 **Полная кастомизация** — настройте всё под свой дизайн-систему

## 🚀 Пример использования

Посмотрите, как легко создать карточку на Tailwind:

```html
<div class="max-w-sm rounded-xl overflow-hidden shadow-lg bg-white p-6">
  <img class="w-full h-48 object-cover rounded-lg" src="image.jpg" alt="Превью">
  <h2 class="text-xl font-bold text-gray-800 mt-4 mb-2">Заголовок карточки</h2>
  <p class="text-gray-600 text-sm leading-relaxed">
    Описание карточки с полезной информацией о контенте.
  </p>
  <button class="mt-4 bg-cyan-500 hover:bg-cyan-600 text-white font-medium px-4 py-2 rounded-lg transition">
    Подробнее
  </button>
</div>
```

**Результат:** готовая карточка с изображением, текстом и кнопкой — без единой строки кастомного CSS!

## 📊 Сравнение с традиционным CSS

| Подход | Код | Время | Гибкость |
| :-- | :-- | :-- | :-- |
| **Tailwind CSS** | `class="bg-blue-500 p-4 rounded"` | ⚡ Мгновенно | 🟢 Высокая |
| **Обычный CSS** | `.card { background: blue; padding: 1rem; border-radius: 4px; }` | 🐢 Нужно писать | 🟡 Средняя |
| **CSS-in-JS** | `styled.div\`background: blue;\`` | 🐢 Настройка | 🔴 Очень высокая |

## 🎯 Для кого этот гайд?

### 🟢 Новички

- Изучите основы Tailwind CSS за 1-2 часа
- Поймёте философию utility-first подхода
- Начнёте верстать адаптивные макеты без боли

### 🟡 Уверенные пользователи

- Освоите продвинутые техники: Flexbox, Grid, анимации
- Настроите dark mode и кастомные темы
- Интегрируете Tailwind в React, Vue, Next.js

### 🔴 Профи

- Создадите собственные плагины и утилиты
- Оптимизируете production build
- Настроите дизайн-систему для команды

## 📚 Структура документации

| Раздел | Что внутри | Уровень |
| :-- | :-- | :-- |
| **[Основы](basics/introduction.md)** | Установка, конфигурация, первые шаги | 🟢 Новичок |
| **[Макет](layout/flexbox.md)** | Flexbox, Grid, отступы, размеры | 🟢 Новичок |
| **[Стили](styling/colors.md)** | Цвета, типографика, фоны, границы | 🟡 Уверенный |
| **[Адаптивность](responsive/breakpoints.md)** | Breakpoints, dark mode, состояния | 🟡 Уверенный |
| **[Продвинутое](advanced/customization.md)** | Кастомизация, плагины, директивы | 🔴 Профи |
| **[Интеграции](integrations/react.md)** | React, Vue, Next.js | 🔴 Профи |

## 🚀 Быстрый старт

### Вариант 1: Через CDN (для тестов)

```html
<!DOCTYPE html>
<html>
<head>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 p-8">
  <h1 class="text-3xl font-bold text-blue-600">
    Привет, Tailwind!
  </h1>
</body>
</html>
```

### Вариант 2: Через npm (для продакшена)

```bash
# Установка
npm install -D tailwindcss
npx tailwindcss init

# Создайте tailwind.config.js
```

Затем в вашем CSS файле:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### Вариант 3: Через Play CDN (для экспериментов)

```html
<script src="https://cdn.tailwindcss.com?plugins=forms,typography"></script>
```

## 📖 Как использовать этот гайд

1. **Читайте последовательно** — начните с раздела «Основы» и двигайтесь дальше
2. **Используйте как справочник** — ищите нужные классы через поиск (Ctrl+K)
3. **Копируйте примеры** — все сниппеты готовы к использованию
4. **Скачайте PDF** — распечатайте шпаргалку и держите под рукой

## 🎓 Что вы изучите

После прохождения этого гайда вы сможете:

- ✅ Создавать адаптивные макеты за минуты
- ✅ Настраивать дизайн-систему под проект
- ✅ Работать с тёмной темой и состояниями
- ✅ Интегрировать Tailwind в любой фреймворк
- ✅ Оптимизировать CSS для продакшена
- ✅ Создавать собственные плагины

## 🤝 Вклад в проект

Нашли ошибку или хотите улучшить документацию?

1. Создайте форк репозитория
2. Внесите изменения в `docs/`
3. Отправьте Pull Request

Все улучшения приветствуются! 🙌

## 📄 Лицензия

Материалы распространяются под лицензией **MIT**. Используйте знания во благо!

---

**Готовы начать?** Перейдите к разделу [Введение в Tailwind CSS](basics/introduction.md) →

---




---

# 🟢 Раздел: Basics

---



<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: basics\configuration.md -->
<!-- ═══════════════════════════════════════════════════════════ -->

# ⚙️ Конфигурация Tailwind CSS

> **Полное руководство по файлу `tailwind.config.js`:** от базовой структуры до настройки content, темы, плагинов и типичных конфигураций для разных проектов

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Поймёте структуру файла `tailwind.config.js`
- ✅ Научитесь правильно настраивать `content` (критически важно!)
- ✅ Освоите базовое расширение темы
- ✅ Настроите dark mode
- ✅ Подключите плагины
- ✅ Поймёте, когда использовать `important`, `prefix`, `corePlugins`
- ✅ Создадите типовую конфигурацию для своего проекта
- ✅ Избежите типичных ошибок при настройке

> 💡 **Примечание:** это базовая настройка. Продвинутая кастомизация (создание утилит, компонентов, сложных плагинов) разбирается в разделе [Кастомизация](../advanced/customization.md).

## 📁 Что такое `tailwind.config.js`

Это **главный конфигурационный файл** Tailwind CSS. Он говорит Tailwind:

- **Какие файлы сканировать** (чтобы генерировать только нужные классы)
- **Какую тему использовать** (цвета, шрифты, отступы)
- **Какие плагины подключить** (формы, типографика и т.д.)
- **Как себя вести** (dark mode, префиксы, важность)

### Где находится файл

```
my-project/
├── src/
├── tailwind.config.js   ← Вот он!
├── postcss.config.js
├── package.json
└── ...
```

### Как создать файл

Если вы забыли создать его при установке:

```bash
npx tailwindcss init
```

Или с PostCSS конфигом:

```bash
npx tailwindcss init -p
```

## 📋 Структура конфигурации

Полный конфиг выглядит так:

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  // 1. Какие файлы сканировать
  content: [],

  // 2. Тема (дизайн-система)
  theme: {
    extend: {},
  },

  // 3. Плагины
  plugins: [],

  // 4. Пресеты (базовая конфигурация)
  presets: [],

  // 5. Dark mode
  darkMode: 'class',

  // 6. Важность селекторов
  important: false,

  // 7. Префикс для всех классов
  prefix: '',

  // 8. Встроенные утилиты
  corePlugins: {},
}
```

Разберём каждую секцию подробно.

## 📂 Секция `content` — САМАЯ ВАЖНАЯ

**Это самая важная секция!** От неё зависит, будет ли Tailwind вообще работать.

### Что делает `content`

Tailwind сканирует файлы, указанные в `content`, и генерирует CSS **только для тех классов, которые реально используются** в вашем коде.

```
1. Вы указали: content: ['./src/**/*.html']
2. Tailwind сканирует все HTML файлы в src/
3. Находит классы: bg-blue-500, p-4, rounded
4. Генерирует CSS только для этих классов
5. Итоговый CSS весит 5-15 KB вместо 3-4 MB
```

### Базовая настройка

```js
// tailwind.config.js
module.exports = {
  content: [
    './src/**/*.{html,js,jsx,ts,tsx,vue,svelte}',
  ],
}
```

### Для разных фреймворков

#### HTML / Vanilla JS

```js
module.exports = {
  content: [
    './*.html',
    './src/**/*.{html,js}',
  ],
}
```

#### React / Vite

```js
module.exports = {
  content: [
    './index.html',
    './src/**/*.{js,ts,jsx,tsx}',
  ],
}
```

#### Vue / Vite

```js
module.exports = {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts}',
  ],
}
```

#### Next.js (App Router)

```js
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx}',
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
  ],
}
```

#### Next.js (Pages Router)

```js
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
  ],
}
```

#### Nuxt 3

```js
module.exports = {
  content: [
    './components/**/*.{vue,js,ts}',
    './layouts/**/*.vue',
    './pages/**/*.vue',
    './plugins/**/*.{js,ts}',
    './app.vue',
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

#### Laravel / Blade

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

#### Astro

```js
module.exports = {
  content: [
    './src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}',
  ],
}
```

### Исключения

Можно исключить файлы из сканирования с помощью `!`:

```js
module.exports = {
  content: {
    files: [
      './src/**/*.{html,js}',
      '!./src/**/*.test.{js,ts}',       // Исключаем тесты
      '!./src/**/*.stories.{js,tsx}',   // Исключаем Storybook
    ],
  },
}
```

### ⚠️ Что будет, если не настроить `content`

**Вариант 1:** CSS будет пустым — Tailwind не найдёт ни одного класса.

**Вариант 2:** CSS будет содержать все 50 000+ классов — размер 3-4 MB.

**Оба варианта — плохо!** Всегда настраивайте `content`.

## 🎨 Секция `theme` — базовое расширение

Тема определяет вашу дизайн-систему: цвета, шрифты, отступы и т.д.

### Расширение темы (рекомендуется)

Добавляет свои значения **к стандартным**:

```js
module.exports = {
  theme: {
    extend: {
      colors: {
        'brand': '#ff5722',
      },
      fontFamily: {
        'display': ['"Playfair Display"', 'serif'],
      },
    },
  },
}
```

Теперь можно использовать:

```html
<div class="bg-brand text-white">Брендовый цвет</div>
<h1 class="font-display">Заголовок</h1>
```

### Полная замена темы

Заменяет стандартные значения **полностью**:

```js
module.exports = {
  theme: {
    // Без extend — полная замена
    colors: {
      'primary': '#3b82f6',
      'secondary': '#8b5cf6',
    },
  },
}
```

> ⚠️ **Важно:** при полной замене вы теряете все стандартные цвета (blue, red, green и т.д.). Используйте только если действительно нужно.

### Что можно настроить в теме

| Свойство | Что определяет |
| :-- | :-- |
| `colors` | Цветовая палитра |
| `spacing` | Отступы (padding, margin, gap) |
| `fontSize` | Размеры шрифтов |
| `fontFamily` | Шрифты |
| `screens` | Breakpoints для responsive |
| `borderRadius` | Радиусы скругления |
| `boxShadow` | Тени |
| `animation` | Анимации |
| `transitionDuration` | Длительность transition |

> 💡 **Подробнее:** продвинутая работа с темой разбирается в разделе [Кастомизация](../advanced/customization.md).

## 🌙 Секция `darkMode` — тёмная тема

Управляет тем, как работает dark mode:

### Режим `class` (рекомендуется)

Тема переключается добавлением класса `dark` к `<html>`:

```js
module.exports = {
  darkMode: 'class',
}
```

```html
<!-- Светлая тема -->
<html>
  <body class="bg-white text-gray-900">...</body>
</html>

<!-- Тёмная тема -->
<html class="dark">
  <body class="bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100">
    ...
  </body>
</html>
```

### Режим `media`

Тема переключается автоматически по системным настройкам:

```js
module.exports = {
  darkMode: 'media', // по умолчанию
}
```

```html
<!-- Автоматически следует системным настройкам -->
<div class="bg-white dark:bg-gray-900">...</div>
```

### Сравнение режимов

| Режим | Плюсы | Минусы |
| :-- | :-- | :-- |
| `class` | Полный контроль, можно сохранить выбор | Нужен JavaScript |
| `media` | Работает из коробки | Нельзя переключить вручную |

> 💡 **Подробнее:** работа с dark mode разбирается в разделе [Dark Mode](../responsive/dark-mode.md).

## 🔌 Секция `plugins` — подключение плагинов

Плагины добавляют новую функциональность в Tailwind:

```js
module.exports = {
  plugins: [
    require('@tailwindcss/forms'),           // Улучшенные формы
    require('@tailwindcss/typography'),      // Типографика для статей
    require('@tailwindcss/aspect-ratio'),    // Aspect ratio
    require('@tailwindcss/container-queries'), // Container queries
  ],
}
```

### Установка плагинов

```bash
npm install -D @tailwindcss/forms @tailwindcss/typography
```

### Что дают плагины

| Плагин | Что добавляет |
| :-- | :-- |
| `@tailwindcss/forms` | Красивые стили для input, select, checkbox |
| `@tailwindcss/typography` | Класс `prose` для стилизации HTML-контента |
| `@tailwindcss/aspect-ratio` | Утилиты для aspect ratio |
| `@tailwindcss/container-queries` | Container queries |

> 💡 **Подробнее:** создание собственных плагинов разбирается в разделе [Плагины](../advanced/plugins.md).

## ⚡ Секция `important` — важность селекторов

Добавляет `!important` ко всем утилитам Tailwind:

```js
module.exports = {
  important: true,
}
```

### Когда использовать

**Хорошие случаи:**
- Интеграция Tailwind в существующий проект с конфликтующими стилями
- Работа с CSS-фреймворками (Bootstrap, Foundation)

**Плохие случаи:**
- Новые проекты (лучше решить конфликты правильно)
- Когда можно использовать специфичные селекторы

### Альтернатива: ID-селектор

Можно указать ID, к которому будут привязаны стили:

```js
module.exports = {
  important: '#app',
}
```

Все утилиты будут сгенерированы как `#app .bg-blue-500`, что повышает их специфичность без `!important`.

## 🔤 Секция `prefix` — префиксы классов

Добавляет префикс ко всем классам Tailwind:

```js
module.exports = {
  prefix: 'tw-',
}
```

```html
<!-- Было -->
<div class="bg-blue-500 p-4 rounded">

<!-- Стало -->
<div class="tw-bg-blue-500 tw-p-4 tw-rounded">
```

### Когда использовать

- Интеграция Tailwind в проект с существующими CSS-классами
- Избежание конфликтов имён

> ⚠️ **Не рекомендуется** для новых проектов — это усложняет код.

## 🎛 Секция `corePlugins` — управление утилитами

Позволяет **отключить** встроенные утилиты:

### Отключение всех утилит

```js
module.exports = {
  corePlugins: {
    // Пустой объект — все утилиты отключены
  },
}
```

### Отключение конкретных утилит

```js
module.exports = {
  corePlugins: {
    float: false,           // Отключаем float
    objectFit: false,       // Отключаем object-fit
    visibility: false,      // Отключаем visibility
  },
}
```

### Отключение Preflight (CSS Reset)

```js
module.exports = {
  corePlugins: {
    preflight: false,
  },
}
```

> ⚠️ **Осторожно:** Preflight сбрасывает стандартные стили браузера. Без него могут сломаться существующие стили.

### Когда отключать утилиты

- **Preflight** — при интеграции в существующий проект
- **Конкретные утилиты** — если они конфликтуют с вашим CSS
- **Все утилиты** — если используете только кастомные утилиты

## 📦 Секция `presets` — базовая конфигурация

Позволяет переиспользовать конфигурацию между проектами:

```js
// presets/company-preset.js
module.exports = {
  theme: {
    extend: {
      colors: {
        'brand': '#ff5722',
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
```

```js
// tailwind.config.js
module.exports = {
  presets: [
    require('./presets/company-preset.js'),
  ],
  // Можно расширить preset
  theme: {
    extend: {
      colors: {
        'accent': '#ec4899',
      },
    },
  },
}
```

> 💡 **Подробнее:** presets разбираются в разделе [Кастомизация](../advanced/customization.md).

## 🎯 Типовые конфигурации

### Минимальная конфигурация

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js}'],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

### React + Vite + TypeScript

```js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{js,ts,jsx,tsx}',
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        'brand': {
          50:  '#f0f9ff',
          500: '#0ea5e9',
          900: '#0c4a6e',
        },
      },
      fontFamily: {
        'sans': ['Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
```

### Next.js (App Router)

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx}',
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
  ],
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        'sans': ['var(--font-inter)'],
        'display': ['var(--font-playfair)'],
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
  ],
}
```

### Vue + Vite + TypeScript

```js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        'brand': '#ff5722',
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
```

### Laravel + Blade

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './resources/**/*.blade.php',
    './resources/**/*.js',
    './resources/**/*.vue',
  ],
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Figtree', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
```

### WordPress

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './**/*.php',
    './src/**/*.{js,jsx,ts,tsx}',
  ],
  darkMode: 'class',
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
}
```

## 📊 Шпаргалка: что когда использовать

| Задача | Решение |
| :-- | :-- |
| Настроить сканирование файлов | `content: ['./src/**/*.{html,js}']` |
| Добавить свой цвет | `theme.extend.colors` |
| Добавить свой шрифт | `theme.extend.fontFamily` |
| Добавить свой breakpoint | `theme.extend.screens` |
| Включить dark mode | `darkMode: 'class'` |
| Подключить плагин форм | `plugins: [require('@tailwindcss/forms')]` |
| Подключить плагин типографики | `plugins: [require('@tailwindcss/typography')]` |
| Повысить специфичность | `important: true` или `important: '#app'` |
| Добавить префикс | `prefix: 'tw-'` |
| Отключить Preflight | `corePlugins: { preflight: false }` |
| Отключить конкретные утилиты | `corePlugins: { float: false }` |
| Переиспользовать конфиг | `presets: [require('./preset.js')]` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Забывают настроить `content`

```js
// ❌ Плохо: content отсутствует
module.exports = {
  theme: {
    extend: {
      colors: {
        'brand': '#ff5722',
      },
    },
  },
}

// ✅ Хорошо: content настроен
module.exports = {
  content: ['./src/**/*.{html,js,jsx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        'brand': '#ff5722',
      },
    },
  },
}
```

**Результат:** CSS будет пустым или содержать все классы.

### ❌ Ошибка 2: Неправильные пути в `content`

```js
// ❌ Плохо: пути не существуют
module.exports = {
  content: ['./app/**/*.html'], // папки app нет
}

// ✅ Хорошо: правильные пути
module.exports = {
  content: ['./src/**/*.html'],
}
```

### ❌ Ошибка 3: Забывают расширения файлов

```js
// ❌ Плохо: Vue-файлы не сканируются
module.exports = {
  content: ['./src/**/*.js'],
}

// ✅ Хорошо: все нужные расширения
module.exports = {
  content: ['./src/**/*.{js,ts,vue}'],
}
```

### ❌ Ошибка 4: Полная замена вместо расширения

```js
// ❌ Плохо: теряем все стандартные цвета
module.exports = {
  theme: {
    colors: {
      'brand': '#ff5722',
    },
  },
}

// ✅ Хорошо: расширяем стандартные цвета
module.exports = {
  theme: {
    extend: {
      colors: {
        'brand': '#ff5722',
      },
    },
  },
}
```

### ❌ Ошибка 5: Забывают JSDoc тип

```js
// ❌ Плохо: нет автодополнения в IDE
module.exports = {
  content: ['./src/**/*.html'],
}

// ✅ Хорошо: есть автодополнение
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.html'],
}
```

### ❌ Ошибка 6: Изменяют конфиг без перезапуска

```bash
# ❌ Плохо: изменения не применятся
# Просто редактируем tailwind.config.js

# ✅ Хорошо: перезапускаем dev-сервер
npm run dev
# или
npx tailwindcss -i ./src/input.css -o ./src/output.css --watch
```

### ❌ Ошибка 7: `important: true` без необходимости

```js
// ❌ Плохо: !important везде — сложно переопределить
module.exports = {
  important: true,
}

// ✅ Хорошо: решаем конфликты правильно
// Используем специфичные селекторы или @layer
```

### ❌ Ошибка 8: Префикс для нового проекта

```js
// ❌ Плохо: усложняет код без необходимости
module.exports = {
  prefix: 'tw-',
}

// ✅ Хорошо: префикс только при интеграции
// Для новых проектов префикс не нужен
```

### ❌ Ошибка 9: Отключают Preflight без причины

```js
// ❌ Плохо: Preflight отключён, стили сломаны
module.exports = {
  corePlugins: {
    preflight: false,
  },
}

// ✅ Хорошо: Preflight включён (по умолчанию)
// Отключаем только при интеграции в существующий проект
```

### ❌ Ошибка 10: Забывают про `darkMode: 'class'`

```js
// ❌ Плохо: по умолчанию используется media
module.exports = {
  // darkMode не указан
}

// ✅ Хорошо: явно указываем class
module.exports = {
  darkMode: 'class',
}
```

## 🎯 Что дальше?

Теперь вы знаете, как настроить Tailwind CSS под свой проект! Следующий шаг — изучить **утилитарные классы**, чтобы начать верстать.

**Следующий раздел:** [🎨 Утилитарные классы](utility-classes.md) — обзор основных классов для стилизации.

---

---




<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: basics\installation.md -->
<!-- ═══════════════════════════════════════════════════════════ -->

# 📦 Установка Tailwind CSS

> **Полное руководство по установке Tailwind CSS:** от быстрого старта через CDN до production-ready настройки с PostCSS и интеграции с фреймворками

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Поймёте все способы установки Tailwind CSS
- ✅ Настроите Tailwind через CDN для быстрых экспериментов
- ✅ Установите Tailwind через npm для production-проекта
- ✅ Настроите Tailwind CLI для простых проектов
- ✅ Интегрируете Tailwind с PostCSS (рекомендуемый способ)
- ✅ Настроите Tailwind в Vite, Next.js, Vue, React, Laravel
- ✅ Проверите, что всё работает корректно
- ✅ Избежите типичных ошибок при установке
- ✅ Поймёте разницу между Tailwind v3 и v4

## 🎯 Какой способ установки выбрать?

Tailwind CSS можно установить несколькими способами. Выбор зависит от ваших целей:

| Способ | Когда использовать | Production-ready |
| :-- | :-- | :-- |
| **Play CDN** | Быстрые эксперименты, прототипы, CodePen | ❌ Нет |
| **Tailwind CLI** | Простые статические сайты без сборщика | ✅ Да |
| **PostCSS** (рекомендуется) | Production-проекты с фреймворками | ✅ Да |
| **Vite / Next.js / Nuxt** | Современные фронтенд-проекты | ✅ Да |
| **CDN (полный)** | Legacy-проекты, email-вёрстка | ⚠️ С ограничениями |

> 💡 **Рекомендация:** для новых проектов используйте **PostCSS** или **Vite**. Для экспериментов — **Play CDN**.

## 🚀 Вариант 1: Play CDN (для экспериментов)

Самый быстрый способ попробовать Tailwind — подключить его через CDN прямо в HTML:

### Шаг 1: Создайте HTML-файл

```html
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tailwind CDN</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 p-8">
  <h1 class="text-3xl font-bold text-blue-600">
    Привет, Tailwind!
  </h1>
  <p class="mt-4 text-gray-700">
    Это мой первый проект на Tailwind CSS
  </p>
  <button class="mt-4 bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-lg">
    Нажми меня
  </button>
</body>
</html>
```

### Шаг 2: Откройте в браузере

Просто откройте файл в браузере — Tailwind уже работает!

### ⚙️ Кастомизация Play CDN

Можно настроить Tailwind прямо в HTML:

```html
<script>
  tailwind.config = {
    theme: {
      extend: {
        colors: {
          'brand': '#ff5722',
        },
      },
    },
  }
</script>
```

### 📦 Подключение плагинов через CDN

```html
<script src="https://cdn.tailwindcss.com?plugins=forms,typography,aspect-ratio"></script>
```

### ⚠️ Ограничения Play CDN

- ❌ **Не для production** — нет оптимизации, большой размер
- ❌ **Нет JIT-компиляции** в полной мере
- ❌ **Нет кастомных плагинов** (только официальные)
- ❌ **Зависимость от CDN** — если CDN упадёт, сайт сломается

> 💡 **Используйте Play CDN только для:** прототипов, CodePen, быстрых экспериментов, email-вёрстки.

## 🛠️ Вариант 2: Tailwind CLI (для простых проектов)

Tailwind CLI — это standalone-инструмент, который не требует Node.js или PostCSS.

### Шаг 1: Установите Tailwind

```bash
# Через npm (нужен Node.js)
npm install -D tailwindcss

# Или скачайте standalone binary с GitHub
# https://github.com/tailwindlabs/tailwindcss/releases
```

### Шаг 2: Инициализируйте конфигурацию

```bash
npx tailwindcss init
```

Это создаст файл `tailwind.config.js`:

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

### Шаг 3: Создайте CSS-файл

Создайте `src/input.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### Шаг 4: Запустите CLI

```bash
# Однократная сборка
npx tailwindcss -i ./src/input.css -o ./src/output.css

# С watch-режимом (автоматическая пересборка)
npx tailwindcss -i ./src/input.css -o ./src/output.css --watch

# С минификацией (для production)
npx tailwindcss -i ./src/input.css -o ./src/output.css --minify
```

### Шаг 5: Подключите CSS в HTML

```html
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <link href="./src/output.css" rel="stylesheet">
</head>
<body class="bg-gray-100 p-8">
  <h1 class="text-3xl font-bold text-blue-600">Tailwind CLI</h1>
</body>
</html>
```

### 📁 Структура проекта

```
my-project/
├── src/
│   ├── input.css       ← Исходный CSS с директивами
│   ├── output.css      ← Сгенерированный CSS
│   └── index.html      ← Ваш HTML
├── tailwind.config.js  ← Конфигурация Tailwind
└── package.json
```

### ⚙️ Добавление в package.json

```json
{
  "scripts": {
    "dev": "npx tailwindcss -i ./src/input.css -o ./src/output.css --watch",
    "build": "npx tailwindcss -i ./src/input.css -o ./src/output.css --minify"
  }
}
```

```bash
# Разработка
npm run dev

# Production
npm run build
```

## ⚙️ Вариант 3: PostCSS (рекомендуется)

PostCSS — **официально рекомендуемый** способ установки Tailwind для production-проектов.

### Шаг 1: Установите зависимости

```bash
npm install -D tailwindcss postcss autoprefixer
```

### Шаг 2: Инициализируйте конфигурации

```bash
npx tailwindcss init -p
```

Флаг `-p` создаст оба файла: `tailwind.config.js` и `postcss.config.js`.

```js
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js,jsx,ts,tsx,vue,svelte}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

```js
// postcss.config.js
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
```

### Шаг 3: Настройте `content`

**Критически важный шаг!** Tailwind должен знать, какие файлы сканировать для генерации CSS:

```js
// tailwind.config.js
module.exports = {
  content: [
    // HTML
    "./src/**/*.html",
    // JavaScript / TypeScript
    "./src/**/*.{js,jsx,ts,tsx}",
    // Vue
    "./src/**/*.vue",
    // Svelte
    "./src/**/*.svelte",
    // PHP (Laravel)
    "./resources/**/*.blade.php",
    "./resources/**/*.js",
  ],
  // ...
}
```

> ⚠️ **Важно:** если не настроить `content`, Tailwind сгенерирует **пустой CSS** или **весь CSS** (3+ MB).

### Шаг 4: Добавьте директивы в CSS

Создайте `src/input.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### Шаг 5: Интегрируйте с вашим сборщиком

#### Vite

```js
// vite.config.js
import { defineConfig } from 'vite'

export default defineConfig({
  css: {
    postcss: './postcss.config.js',
  },
})
```

```js
// src/main.js
import './input.css'
```

#### Webpack

```js
// webpack.config.js
module.exports = {
  // ...
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          'style-loader',
          {
            loader: 'postcss-loader',
            options: {
              postcssOptions: {
                plugins: [
                  'tailwindcss',
                  'autoprefixer',
                ],
              },
            },
          },
          'css-loader',
        ],
      },
    ],
  },
}
```

#### Parcel

Parcel автоматически подхватывает PostCSS — просто создайте `postcss.config.js`.

#### Create React App

```bash
# CRA уже поддерживает PostCSS
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

### 📁 Структура проекта

```
my-project/
├── src/
│   ├── input.css        ← Директивы Tailwind
│   ├── index.html
│   └── main.js
├── tailwind.config.js   ← Конфигурация Tailwind
├── postcss.config.js    ← Конфигурация PostCSS
└── package.json
```

## 🎨 Вариант 4: Vite + React / Vue

Самый популярный современный стек.

### React + Vite

```bash
# Создание проекта
npm create vite@latest my-app -- --template react
cd my-app

# Установка Tailwind
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

```js
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

```css
/* src/index.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

```jsx
// src/main.jsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
```

```jsx
// src/App.jsx
function App() {
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="bg-white p-8 rounded-xl shadow-lg max-w-md">
        <h1 className="text-3xl font-bold text-gray-900">
          Привет, React + Tailwind!
        </h1>
        <p className="mt-4 text-gray-600">
          Это мой первый проект
        </p>
        <button className="mt-6 bg-blue-500 hover:bg-blue-600 text-white px-6 py-2 rounded-lg transition-colors">
          Нажми меня
        </button>
      </div>
    </div>
  )
}

export default App
```

```bash
# Запуск
npm run dev
```

### Vue 3 + Vite

```bash
# Создание проекта
npm create vite@latest my-app -- --template vue
cd my-app

# Установка Tailwind
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

```js
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

```css
/* src/style.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

```vue
<!-- src/App.vue -->
<template>
  <div class="min-h-screen bg-gray-100 flex items-center justify-center">
    <div class="bg-white p-8 rounded-xl shadow-lg max-w-md">
      <h1 class="text-3xl font-bold text-gray-900">
        Привет, Vue + Tailwind!
      </h1>
      <p class="mt-4 text-gray-600">
        Это мой первый проект
      </p>
      <button class="mt-6 bg-blue-500 hover:bg-blue-600 text-white px-6 py-2 rounded-lg transition-colors">
        Нажми меня
      </button>
    </div>
  </div>
</template>
```

> 📚 **Подробнее:** см. разделы [React + Tailwind](../integrations/react.md) и [Vue + Tailwind](../integrations/vue.md).

## 🚀 Вариант 5: Next.js

Next.js имеет **встроенную поддержку** Tailwind CSS.

### Шаг 1: Создание проекта

```bash
npx create-next-app@latest my-app
cd my-app

# Tailwind уже установлен по умолчанию!
# Если нет:
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

### Шаг 2: Настройка конфигурации

```js
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx}',
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
    './src/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

### Шаг 3: Добавление директив

```css
/* app/globals.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### Шаг 4: Подключение в layout

```tsx
// app/layout.tsx
import './globals.css'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="ru">
      <body>{children}</body>
    </html>
  )
}
```

### Шаг 5: Использование

```tsx
// app/page.tsx
export default function Home() {
  return (
    <main className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="bg-white p-8 rounded-xl shadow-lg max-w-md">
        <h1 className="text-3xl font-bold text-gray-900">
          Привет, Next.js!
        </h1>
      </div>
    </main>
  )
}
```

```bash
npm run dev
```

> 📚 **Подробнее:** см. раздел [Next.js + Tailwind](../integrations/nextjs.md).

## 🎭 Вариант 6: Nuxt 3

### Шаг 1: Установка модуля

```bash
npx nuxi@latest init my-app
cd my-app
npm install -D @nuxtjs/tailwindcss
```

### Шаг 2: Настройка

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  modules: ['@nuxtjs/tailwindcss'],
  tailwindcss: {
    configPath: 'tailwind.config.js',
  },
})
```

### Шаг 3: Конфигурация

```js
// tailwind.config.js
module.exports = {
  content: [
    './components/**/*.{vue,js,ts}',
    './layouts/**/*.vue',
    './pages/**/*.vue',
    './plugins/**/*.{js,ts}',
    './app.vue',
  ],
}
```

### Шаг 4: Использование

```vue
<!-- pages/index.vue -->
<template>
  <div class="min-h-screen bg-gray-100 flex items-center justify-center">
    <div class="bg-white p-8 rounded-xl shadow-lg max-w-md">
      <h1 class="text-3xl font-bold text-gray-900">
        Привет, Nuxt 3!
      </h1>
    </div>
  </div>
</template>
```

## 🐘 Вариант 7: Laravel

Laravel имеет **отличную интеграцию** с Tailwind через Vite.

### Шаг 1: Создание проекта

```bash
laravel new my-app
cd my-app
```

### Шаг 2: Установка зависимостей

```bash
npm install
```

### Шаг 3: Настройка Tailwind

```js
// tailwind.config.js
const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  content: [
    './vendor/laravel/framework/src/Illuminate/Pagination/resources/views/*.blade.php',
    './storage/framework/views/*.php',
    './resources/views/**/*.blade.php',
    './resources/js/**/*.vue',
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Figtree', ...defaultTheme.fontFamily.sans],
      },
    },
  },
  plugins: [require('@tailwindcss/forms')],
}
```

### Шаг 4: CSS-файл

```css
/* resources/css/app.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### Шаг 5: Подключение в шаблоне

```html
<!-- resources/views/layouts/app.blade.php -->
<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  @vite(['resources/css/app.css', 'resources/js/app.js'])
</head>
<body class="font-sans antialiased">
  {{ $slot }}
</body>
</html>
```

### Шаг 6: Запуск

```bash
# В одном терминале — Laravel
php artisan serve

# В другом — Vite
npm run dev
```

## 🎨 Вариант 8: Ruby on Rails

### Шаг 1: Установка

```bash
# Через importmap (Rails 7+)
./bin/importmap pin tailwindcss

# Или через npm
npm install -D tailwindcss postcss autoprefixer
```

### Шаг 2: Использование с gem

```bash
# Добавьте в Gemfile
gem 'tailwindcss-rails'

bundle install
rails tailwindcss:install
```

### Шаг 3: Запуск

```bash
# В одном терминале — Rails
bin/rails server

# В другом — Tailwind
bin/rails tailwindcss:watch
```

## 🎨 Вариант 9: Django

### Шаг 1: Установка

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

### Шаг 2: Настройка

```js
// tailwind.config.js
module.exports = {
  content: [
    './templates/**/*.html',
    './**/templates/**/*.html',
  ],
}
```

### Шаг 3: Сборка CSS

```json
// package.json
{
  "scripts": {
    "dev": "npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch",
    "build": "npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --minify"
  }
}
```

### Шаг 4: Подключение в шаблоне

```html
<!-- templates/base.html -->
{% load static %}
<!DOCTYPE html>
<html lang="ru">
<head>
  <link href="{% static 'css/output.css' %}" rel="stylesheet">
</head>
<body>
  {% block content %}{% endblock %}
</body>
</html>
```

## ✅ Проверка установки

После установки убедитесь, что всё работает:

### Тестовая страница

```html
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <link href="./output.css" rel="stylesheet">
</head>
<body class="bg-gray-100 min-h-screen flex items-center justify-center p-4">
  <div class="bg-white rounded-xl shadow-lg p-8 max-w-md w-full">
    <h1 class="text-3xl font-bold text-gray-900 mb-4">
      ✅ Tailwind работает!
    </h1>
    <p class="text-gray-600 mb-6">
      Если вы видите эту карточку со стилями — всё настроено правильно.
    </p>
    <div class="flex gap-2">
      <button class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-lg transition-colors">
        Primary
      </button>
      <button class="bg-gray-200 hover:bg-gray-300 text-gray-800 px-4 py-2 rounded-lg transition-colors">
        Secondary
      </button>
    </div>
  </div>
</body>
</html>
```

### Чеклист проверки

- [ ] CSS-файл сгенерирован и подключён
- [ ] Стили применяются (карточка имеет белый фон, тени, скругления)
- [ ] Hover-эффекты работают
- [ ] Responsive работает (уменьшите окно браузера)
- [ ] Консоль браузера не показывает ошибок 404

## 🔄 Tailwind v3 vs v4

В 2025 году вышел **Tailwind CSS v4** с новым движком Oxide. Вот основные отличия:

### Что нового в v4

- ⚡ **Новый движок Oxide** — в 10 раз быстрее
- 🎨 **CSS-first конфигурация** — настройка прямо в CSS
- 📦 **Zero-config установка** — `@import "tailwindcss"`
- 🚀 **Нативная поддержка cascade layers**
- 🎯 **Улучшенная производительность**

### Установка v4

```bash
npm install tailwindcss @tailwindcss/postcss postcss
```

```css
/* input.css */
@import "tailwindcss";
```

### Установка v3 (стабильная)

```bash
npm install -D tailwindcss postcss autoprefixer
```

```css
/* input.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

> 💡 **Рекомендация:** для новых проектов используйте **v4**. Для существующих — оставайтесь на **v3** до момента миграции.

## 📊 Сравнение способов установки

| Способ | Скорость настройки | Production | Сложность | Рекомендация |
| :-- | :--: | :--: | :--: | :-- |
| **Play CDN** | ⚡ 1 мин | ❌ | 🟢 Очень просто | Только для экспериментов |
| **Tailwind CLI** | ⚡ 5 мин | ✅ | 🟢 Просто | Для статических сайтов |
| **PostCSS** | ⏱ 10 мин | ✅ | 🟡 Средне | ✅ **Рекомендуется** |
| **Vite** | ⏱ 10 мин | ✅ | 🟡 Средне | ✅ **Для React/Vue** |
| **Next.js** | ⏱ 5 мин | ✅ | 🟢 Просто | ✅ **Для Next.js** |
| **Laravel** | ⏱ 10 мин | ✅ | 🟡 Средне | ✅ **Для Laravel** |

## 🎯 Практические паттерны

### 1. 📁 Базовая структура проекта

```
my-project/
├── src/
│   ├── input.css          ← Директивы Tailwind
│   ├── output.css         ← Сгенерированный CSS
│   ├── index.html
│   └── main.js
├── tailwind.config.js     ← Конфигурация Tailwind
├── postcss.config.js      ← Конфигурация PostCSS
├── package.json
└── .gitignore
```

### 2. 📝 package.json scripts

```json
{
  "scripts": {
    "dev": "npx tailwindcss -i ./src/input.css -o ./src/output.css --watch",
    "build": "npx tailwindcss -i ./src/input.css -o ./src/output.css --minify",
    "analyze": "npx tailwindcss -i ./src/input.css -o ./src/output.css --minify && gzip -c ./src/output.css | wc -c"
  }
}
```

### 3. 🎨 .gitignore для Tailwind

```gitignore
# Зависимости
node_modules/

# Сгенерированный CSS (не коммитим)
src/output.css
dist/
build/

# Логи
*.log

# OS
.DS_Store
Thumbs.db
```

### 4. 🔧 TypeScript + Tailwind

```bash
npm install -D tailwindcss @types/node
```

```js
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js,ts,jsx,tsx}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

## 📊 Шпаргалка: что когда использовать

| Задача | Команда |
| :-- | :-- |
| Быстрый эксперимент | `<script src="https://cdn.tailwindcss.com"></script>` |
| Установка через npm | `npm install -D tailwindcss postcss autoprefixer` |
| Инициализация конфига | `npx tailwindcss init -p` |
| Однократная сборка | `npx tailwindcss -i input.css -o output.css` |
| Watch-режим | `npx tailwindcss -i input.css -o output.css --watch` |
| Production build | `npx tailwindcss -i input.css -o output.css --minify` |
| Обновление Tailwind | `npm update tailwindcss` |
| Проверка версии | `npx tailwindcss --help` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Забывают настроить `content`

```js
// ❌ Плохо: Tailwind не знает, что сканировать
module.exports = {
  // content отсутствует
  theme: { extend: {} },
}

// ✅ Хорошо: указываем пути
module.exports = {
  content: ["./src/**/*.{html,js,jsx,ts,tsx,vue}"],
  theme: { extend: {} },
}
```

**Результат:** CSS будет пустым или содержать все классы (3+ MB).

### ❌ Ошибка 2: Путают `input.css` и `output.css`

```html
<!-- ❌ Плохо: подключаем исходный файл -->
<link href="./input.css" rel="stylesheet">

<!-- ✅ Хорошо: подключаем сгенерированный -->
<link href="./output.css" rel="stylesheet">
```

### ❌ Ошибка 3: Забывают директивы в CSS

```css
/* ❌ Плохо: нет директив */
body {
  background: blue;
}

/* ✅ Хорошо: директивы Tailwind */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### ❌ Ошибка 4: Используют Play CDN в production

```html
<!-- ❌ Плохо: CDN не для production -->
<script src="https://cdn.tailwindcss.com"></script>

<!-- ✅ Хорошо: локальный CSS -->
<link href="./output.css" rel="stylesheet">
```

### ❌ Ошибка 5: Не перезапускают dev-сервер после изменения конфига

```bash
# ❌ Плохо: изменения в tailwind.config.js не применятся
# Просто редактируем файл

# ✅ Хорошо: перезапускаем сервер
npm run dev
# или
npx tailwindcss -i input.css -o output.css --watch
```

### ❌ Ошибка 6: Неправильные пути в `content`

```js
// ❌ Плохо: пути не существуют
module.exports = {
  content: ["./app/**/*.html"], // папки app нет
}

// ✅ Хорошо: правильные пути
module.exports = {
  content: ["./src/**/*.html"],
}
```

### ❌ Ошибка 7: Забывают установить PostCSS и Autoprefixer

```bash
# ❌ Плохо: только Tailwind
npm install -D tailwindcss

# ✅ Хорошо: полный набор
npm install -D tailwindcss postcss autoprefixer
```

### ❌ Ошибка 8: Не используют `--watch` при разработке

```bash
# ❌ Плохо: нужно вручную пересобирать
npx tailwindcss -i input.css -o output.css

# ✅ Хорошо: автоматическая пересборка
npx tailwindcss -i input.css -o output.css --watch
```

### ❌ Ошибка 9: Забывают `--minify` в production

```bash
# ❌ Плохо: неминифицированный CSS
npx tailwindcss -i input.css -o output.css

# ✅ Хорошо: минифицированный CSS
npx tailwindcss -i input.css -o output.css --minify
```

### ❌ Ошибка 10: Конфликт версий Tailwind

```bash
# Проверка версии
npx tailwindcss --help

# Если нужно обновить
npm update tailwindcss

# Или переустановить
rm -rf node_modules package-lock.json
npm install
```

## 🎯 Checklist для нового проекта

Перед началом работы убедитесь:

- [ ] Выбрали подходящий способ установки
- [ ] Установили все зависимости (`tailwindcss`, `postcss`, `autoprefixer`)
- [ ] Создали `tailwind.config.js` с правильными путями в `content`
- [ ] Создали `postcss.config.js` (если используете PostCSS)
- [ ] Создали `input.css` с директивами `@tailwind`
- [ ] Настроили watch-режим для разработки
- [ ] Настроили минификацию для production
- [ ] Проверили, что стили применяются
- [ ] Добавили `output.css` в `.gitignore`
- [ ] Протестировали на разных устройствах

## 🎯 Что дальше?

Теперь у вас установлен и работает Tailwind CSS! Следующий шаг — **настройка конфигурации** под ваш проект.

**Следующий раздел:** [⚙️ Конфигурация Tailwind CSS](configuration.md) — изучим `tailwind.config.js`, как расширять тему, добавлять свои цвета, шрифты и breakpoints.

---

---




<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: basics\introduction.md -->
<!-- ═══════════════════════════════════════════════════════════ -->

# 📘 Введение в Tailwind CSS

> **Понимание философии utility-first подхода и того, почему Tailwind изменил правила игры в веб-разработке**

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Поймёте философию utility-first подхода
- ✅ Узнаете историю создания Tailwind CSS
- ✅ Сможете объяснить, чем Tailwind отличается от Bootstrap и BEM
- ✅ Определите, подходит ли Tailwind для вашего проекта
- ✅ Познакомитесь с основными принципами фреймворка

## 📜 История создания

**Tailwind CSS** был создан **Adam Wathan** в **2017 году** как побочный проект при разработке Laravel-приложения. Адам устал от:

- 🔄 Постоянного переключения между HTML и CSS файлами
- 🤯 Придумывания имён классов для каждого элемента
- 📦 Разрастания CSS-файлов до тысяч строк
- 🐛 Конфликтов специфичности и каскада

Решение пришло неожиданно: **а что если все стили будут прямо в HTML?**

```
2017 — Первый релиз Tailwind CSS v0.1.0
2019 — Tailwind CSS v1.0 (стабильная версия)
2020 — Tailwind CSS v2.0 (dark mode, extended color palette)
2021 — Tailwind CSS v3.0 (JIT-компилятор по умолчанию)
2022 — Tailwind CSS v3.2 (поддержка arbitrary variants)
2023 — Tailwind CSS v3.3 (добавлены новые утилиты)
2024 — Tailwind CSS v3.4 (стабильная версия с полным набором фич)
2025 — Tailwind CSS v4.0 (новый движок на Oxide, ещё быстрее)
```

Сегодня Tailwind — один из самых популярных CSS-фреймворков с **80k+ звёзд на GitHub** и миллионом загрузок в неделю.

## 🧠 Философия utility-first

### Что такое utility-first?

**Utility-first** — это подход, при котором вы стилизуете элементы, комбинируя **мелкие, одноцелевые классы** прямо в HTML.

#### ❌ Традиционный подход

```html
<!-- HTML -->
<div class="alert">
  <p class="alert-message">Ошибка!</p>
</div>

<!-- CSS -->
<style>
  .alert {
    background-color: #fee2e2;
    border: 1px solid #fecaca;
    border-radius: 0.5rem;
    padding: 1rem;
    color: #991b1b;
  }
  .alert-message {
    font-weight: 500;
  }
</style>
```

**Проблемы:**
- Нужно придумать имена классов (`alert`, `alert-message`)
- CSS разбросан по отдельному файлу
- При изменении дизайна нужно править два места
- Класс `.alert` может конфликтовать с другим `.alert`

#### ✅ Utility-first подход

```html
<div class="bg-red-100 border border-red-200 rounded-lg p-4 text-red-800">
  <p class="font-medium">Ошибка!</p>
</div>
```

**Преимущества:**
- 🎯 Всё видно сразу в HTML
- 🚫 Нет проблем с именами классов
- 🔄 Легко изменить стили — просто поменяйте классы
- 📦 Нет каскадных конфликтов

### Почему это работает?

Многие разработчики поначалу думают: **«Это же нечитаемый HTML!»**. Но на практике:

1. **Паттерны повторяются** — после 10-20 компонентов вы начинаете «читать» группы классов как единое целое
2. **Консистентность** — `p-4` всегда означает одно и то же (1rem padding)
3. **Рефакторинг проще** — не нужно искать, где используется `.alert`

## 🏛 Основные принципы Tailwind

### 1. 🎨 Ограниченная дизайн-система

Tailwind предоставляет **заранее определённые значения** для большинства свойств:

```html
<!-- Отступы: 0, 1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20... -->
<div class="p-4">...</div>

<!-- Цвета: red, blue, green, gray, slate, zinc... -->
<div class="bg-blue-500 text-white">...</div>

<!-- Размеры шрифтов: xs, sm, base, lg, xl, 2xl, 3xl... -->
<h1 class="text-2xl">...</h1>
```

**Зачем?** Это заставляет вас использовать **консистентные значения** вместо случайных чисел (`padding: 13px` — такое больше не пройдёт).

### 2. 📱 Mobile-first адаптивность

Все responsive-классы работают через **префиксы breakpoints**:

```html
<div class="w-full md:w-1/2 lg:w-1/3">
  <!-- На мобильных: 100% ширины -->
  <!-- На планшетах (md:): 50% ширины -->
  <!-- На десктопах (lg:): 33% ширины -->
</div>
```

### 3. 🌙 Состояния через префиксы

```html
<button class="bg-blue-500 hover:bg-blue-600 focus:ring-2 active:scale-95">
  Нажми меня
</button>
```

### 4. ⚡ JIT-компиляция (Just-In-Time)

Tailwind генерирует CSS **на лету** — только те классы, которые вы реально используете. Итоговый CSS-файл обычно весит **5-10 KB** вместо сотен килобайт.

## ⚔️ Tailwind vs другие подходы

### Tailwind vs Bootstrap

| Критерий | Tailwind CSS | Bootstrap |
| :-- | :-- | :-- |
| **Подход** | Utility-first | Компонентный |
| **Гибкость** | 🔴 Очень высокая | 🟡 Средняя |
| **Скорость старта** | 🟡 Нужна настройка | 🟢 Готовые компоненты |
| **Кастомизация** | 🟢 Из коробки | 🔴 Нужно переопределять |
| **Итоговый CSS** | 🟢 5-10 KB | 🔴 150+ KB |
| **Уникальность дизайна** | 🟢 Легко | 🔴 Все сайты похожи |

**Когда выбрать Bootstrap:**
- Нужен прототип за час
- Не важен уникальный дизайн
- Команда не знакома с CSS

**Когда выбрать Tailwind:**
- Нужен кастомный дизайн
- Важен размер бандла
- Проект будет долго поддерживаться

### Tailwind vs BEM (Block Element Modifier)

```html
<!-- BEM -->
<div class="card">
  <div class="card__header card__header--highlighted">
    <h2 class="card__title">Заголовок</h2>
  </div>
</div>

<!-- Tailwind -->
<div class="rounded-lg shadow-md bg-white">
  <div class="p-4 border-b border-gray-200 bg-blue-50">
    <h2 class="text-xl font-bold text-gray-800">Заголовок</h2>
  </div>
</div>
```

| Критерий | BEM | Tailwind |
| :-- | :-- | :-- |
| **Именование** | Сложное (`block__element--modifier`) | Отсутствует |
| **Специфичность** | Нужно следить | Не проблема |
| **Переиспользование** | Через компоненты | Через `@apply` или компоненты фреймворка |
| **Порог входа** | 🟡 Нужно учить соглашение | 🟢 Интуитивно |

### Tailwind vs CSS Modules / Styled Components

| Критерий | CSS Modules | Styled Components | Tailwind |
| :-- | :-- | :-- | :-- |
| **Локальность** | ✅ Да | ✅ Да | ✅ Да (через утилиты) |
| **Динамические стили** | 🟡 Сложно | 🟢 Легко | 🟡 Через arbitrary values |
| **Производительность** | 🟢 Высокая | 🟡 Runtime overhead | 🟢 Очень высокая |
| **Интеграция** | Любой фреймворк | Только React-подобные | Любой фреймворк |

## ✅ Когда использовать Tailwind

### 🟢 Идеально подходит для:

- **SaaS-продуктов** — где важен уникальный дизайн
- **Дашбордов и админок** — много повторяющихся UI-паттернов
- **Лендингов** — быстрая вёрстка с кастомным дизайном
- **Дизайн-систем** — Tailwind как основа для компонентов
- **Прототипов** — когда нужно быстро и красиво
- **Командной разработки** — консистентность без code review стилей

### 🟡 Подходит с оговорками:

- **Контентные сайты** (блоги, новости) — можно, но избыточно
- **Email-вёрстка** — нужны инлайновые стили (есть плагин)
- **Legacy-проекты** — интеграция может быть сложной

### 🔴 Не подходит для:

- **Микро-проектов на 1 страницу** — проще написать CSS вручную
- **Проектов с очень сложными анимациями** — GSAP/Framer Motion удобнее
- **Когда команда категорически против** — навязывать технологии бессмысленно

## 🎓 Основные концепции, которые мы разберём

В следующих разделах вы изучите:

### 🟢 Основы

- **Установка и настройка** — как подключить Tailwind в проект
- **Конфигурация** — `tailwind.config.js` и кастомные значения
- **Утилитарные классы** — основные классы для стилизации

### 🟡 Средний уровень

- **Flexbox и Grid** — создание сложных макетов
- **Responsive дизайн** — адаптация под разные устройства
- **Состояния** — hover, focus, active, group-hover
- **Dark mode** — тёмная тема из коробки

### 🔴 Продвинутый уровень

- **Кастомизация** — создание собственных утилит
- **Директивы** — `@apply`, `@layer`, `theme()`
- **Плагины** — расширение функциональности
- **Оптимизация** — PurgeCSS и production build

## 💡 Лучшие практики с самого начала

Чтобы не переучиваться позже, сразу привыкайте к правильному подходу:

### 1. 📏 Используйте значения из дизайн-системы

```html
<!-- ❌ Плохо -->
<div class="p-[13px] text-[15px]">

<!-- ✅ Хорошо -->
<div class="p-3 text-sm">
```

### 2. 🧹 Группируйте классы логически

```html
<!-- ✅ Хорошо: сгруппировано по смыслу -->
<button
  class="
    bg-blue-500 hover:bg-blue-600
    text-white font-medium
    px-4 py-2 rounded-lg
    transition-colors duration-200
  "
>
  Нажми меня
</button>
```

### 3. 📦 Выносите повторяющиеся паттерны в компоненты

```html
<!-- ❌ Плохо: дублирование -->
<button class="bg-blue-500 text-white px-4 py-2 rounded">Сохранить</button>
<button class="bg-blue-500 text-white px-4 py-2 rounded">Отмена</button>

<!-- ✅ Хорошо: React-компонент -->
<Button variant="primary">Сохранить</Button>
<Button variant="primary">Отмена</Button>
```

### 4. 🎨 Используйте arbitrary values только при необходимости

```html
<!-- ✅ Хорошо: из дизайн-системы -->
<div class="w-64 h-48">

<!-- 🟡 Допустимо: если реально нужно кастомное значение -->
<div class="w-[267px] h-[183px]">
```

---

> 💬 **Вопрос для размышления:** какой из подходов (BEM, CSS Modules, Tailwind) вам ближе и почему? Попробуйте переписать один из своих старых компонентов на Tailwind и сравните ощущения.

---




<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: basics\utility-classes.md -->
<!-- ═══════════════════════════════════════════════════════════ -->

# 🎨 Утилитарные классы

> **Обзор всех категорий утилитарных классов Tailwind CSS:** от макета и типографики до эффектов и интерактивности. Этот раздел — карта, которая поможет ориентироваться в 50 000+ классах Tailwind.

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Поймёте, что такое утилитарный класс и как он устроен
- ✅ Узнаете все основные категории утилит
- ✅ Получите обзор самых используемых классов в каждой категории
- ✅ Поймёте паттерны именования классов
- ✅ Научитесь быстро находить нужный класс
- ✅ Узнаете, где искать детали по каждой теме

## 🧠 Что такое утилитарный класс?

**Утилитарный класс** — это маленький CSS-класс, который делает **одну конкретную вещь**:

```html
<!-- Каждый класс = одно CSS-свойство -->
<div class="bg-blue-500 p-4 rounded-lg text-white font-bold">
  <!-- bg-blue-500 → background-color: #3b82f6 -->
  <!-- p-4 → padding: 1rem -->
  <!-- rounded-lg → border-radius: 0.5rem -->
  <!-- text-white → color: #ffffff -->
  <!-- font-bold → font-weight: 700 -->
</div>
```

### Анатомия утилитарного класса

```
[модификатор:]утилита-значение

Примеры:
  bg-blue-500          → утилита: bg, значение: blue-500
  p-4                  → утилита: p, значение: 4
  hover:bg-blue-600    → модификатор: hover, утилита: bg, значение: blue-600
  md:text-lg           → модификатор: md, утилита: text, значение: lg
  dark:bg-gray-900     → модификатор: dark, утилита: bg, значение: gray-900
```

### Паттерны именования

| Паттерн | Пример | CSS |
| :-- | :-- | :-- |
| `{свойство}-{значение}` | `bg-blue-500` | `background-color: #3b82f6` |
| `{свойство}-{сторона}-{значение}` | `pt-4` | `padding-top: 1rem` |
| `{свойство}-{ось}-{значение}` | `px-4` | `padding-left: 1rem; padding-right: 1rem` |
| `{свойство}-{размер}` | `text-lg` | `font-size: 1.125rem` |
| `{модификатор}:{утилита}` | `hover:bg-blue-600` | `:hover { background-color: #2563eb }` |

## 📂 Категории утилит

Tailwind делит утилиты на **основные категории**. Ниже — обзор каждой с самыми важными классами.

---

### 🏗️ 1. Layout (Макет)

Управляют расположением элементов на странице.

#### Display

| Класс | CSS | Когда использовать |
| :-- | :-- | :-- |
| `block` | `display: block` | Блочные элементы |
| `inline-block` | `display: inline-block` | Инлайновый блок |
| `inline` | `display: inline` | Инлайновые элементы |
| `flex` | `display: flex` | Flexbox-контейнер |
| `inline-flex` | `display: inline-flex` | Инлайновый flex |
| `grid` | `display: grid` | Grid-контейнер |
| `hidden` | `display: none` | Скрыть элемент |
| `contents` | `display: contents` | «Прозрачный» контейнер |

#### Position

| Класс | CSS | Когда использовать |
| :-- | :-- | :-- |
| `static` | `position: static` | По умолчанию |
| `relative` | `position: relative` | Позиционирование относительно себя |
| `absolute` | `position: absolute` | Позиционирование относительно родителя |
| `fixed` | `position: fixed` | Фиксированным на экране |
| `sticky` | `position: sticky` | Прилипает при прокрутке |

#### Z-Index

| Класс | CSS |
| :-- | :-- |
| `z-0` | `z-index: 0` |
| `z-10` | `z-index: 10` |
| `z-20` | `z-index: 20` |
| `z-30` | `z-index: 30` |
| `z-40` | `z-index: 40` |
| `z-50` | `z-index: 50` |
| `z-auto` | `z-index: auto` |

> 📚 **Подробнее:** [Flexbox](../layout/flexbox.md), [Grid](../layout/grid.md)

---

### 📏 2. Spacing (Отступы)

Управляют внутренними и внешними отступами.

#### Padding (внутренний отступ)

| Класс | CSS |
| :-- | :-- |
| `p-{size}` | padding со всех сторон |
| `px-{size}` | padding по горизонтали |
| `py-{size}` | padding по вертикали |
| `pt-{size}` | padding сверху |
| `pb-{size}` | padding снизу |
| `pl-{size}` | padding слева |
| `pr-{size}` | padding справа |

#### Margin (внешний отступ)

| Класс | CSS |
| :-- | :-- |
| `m-{size}` | margin со всех сторон |
| `mx-{size}` | margin по горизонтали |
| `my-{size}` | margin по вертикали |
| `mx-auto` | центрирование блока |
| `-m-{size}` | отрицательный margin |

#### Space (отступы между элементами)

| Класс | CSS |
| :-- | :-- |
| `space-x-{size}` | отступы по горизонтали |
| `space-y-{size}` | отступы по вертикали |

#### Значения размеров

`0`, `px`, `0.5`, `1`, `2`, `3`, `4`, `5`, `6`, `8`, `10`, `12`, `16`, `20`, `24`, `32`, `40`, `48`, `56`, `64`, `96`

> 📚 **Подробнее:** [Отступы](../layout/spacing.md)

---

### 📐 3. Sizing (Размеры)

Управляют шириной и высотой элементов.

#### Width

| Класс | CSS |
| :-- | :-- |
| `w-{size}` | фиксированная ширина |
| `w-full` | `width: 100%` |
| `w-screen` | `width: 100vw` |
| `w-1/2` | `width: 50%` |
| `w-1/3` | `width: 33.333%` |
| `w-fit` | `width: fit-content` |
| `w-min` | `width: min-content` |
| `w-max` | `width: max-content` |

#### Height

| Класс | CSS |
| :-- | :-- |
| `h-{size}` | фиксированная высота |
| `h-full` | `height: 100%` |
| `h-screen` | `height: 100vh` |
| `h-dvh` | `height: 100dvh` |
| `h-1/2` | `height: 50%` |

#### Min/Max

| Класс | CSS |
| :-- | :-- |
| `min-w-{size}` | минимальная ширина |
| `max-w-{size}` | максимальная ширина |
| `max-w-prose` | `max-width: 65ch` (для текста) |
| `min-h-screen` | `min-height: 100vh` |
| `max-h-{size}` | максимальная высота |

#### Aspect Ratio

| Класс | CSS |
| :-- | :-- |
| `aspect-auto` | по содержимому |
| `aspect-square` | `1 / 1` |
| `aspect-video` | `16 / 9` |
| `aspect-[4/3]` | кастомный |

> 📚 **Подробнее:** [Размеры](../layout/sizing.md)

---

### 🔤 4. Typography (Типографика)

Управляют внешним видом текста.

#### Font Size

| Класс | Размер | Применение |
| :-- | :-- | :-- |
| `text-xs` | 12px | Подписи, бейджи |
| `text-sm` | 14px | Второстепенный текст |
| `text-base` | 16px | Основной текст |
| `text-lg` | 18px | Подзаголовки |
| `text-xl` | 20px | Заголовки разделов |
| `text-2xl` | 24px | Подзаголовки страниц |
| `text-3xl` | 30px | Заголовки страниц |
| `text-4xl` | 36px | Большие заголовки |
| `text-5xl` | 48px | Hero-заголовки |

#### Font Weight

| Класс | CSS |
| :-- | :-- |
| `font-light` | 300 |
| `font-normal` | 400 |
| `font-medium` | 500 |
| `font-semibold` | 600 |
| `font-bold` | 700 |
| `font-extrabold` | 800 |

#### Text Alignment

`text-left`, `text-center`, `text-right`, `text-justify`

#### Text Decoration

`underline`, `line-through`, `no-underline`, `overline`

#### Line Height

`leading-none`, `leading-tight`, `leading-normal`, `leading-relaxed`, `leading-loose`

#### Letter Spacing

`tracking-tight`, `tracking-normal`, `tracking-wide`, `tracking-wider`

#### Text Transform

`uppercase`, `lowercase`, `capitalize`, `normal-case`

#### Text Overflow

`truncate` (обрезка с многоточием), `line-clamp-{n}` (многострочная обрезка)

#### Font Family

| Класс | Применение |
| :-- | :-- |
| `font-sans` | Основной текст |
| `font-serif` | Статьи, книги |
| `font-mono` | Код, технические данные |

> 📚 **Подробнее:** [Типографика](../styling/typography.md)

---

### 🎨 5. Colors (Цвета)

Управляют цветом текста, фона, границ и других свойств.

#### Применение цвета

| Класс | Что окрашивает |
| :-- | :-- |
| `text-{color}` | Цвет текста |
| `bg-{color}` | Цвет фона |
| `border-{color}` | Цвет границы |
| `ring-{color}` | Цвет ring-обводки |
| `divide-{color}` | Цвет разделителей |
| `accent-{color}` | Цвет чекбоксов/радио |
| `fill-{color}` | Цвет SVG fill |
| `stroke-{color}` | Цвет SVG stroke |

#### Палитра

22 цвета: `red`, `orange`, `amber`, `yellow`, `lime`, `green`, `emerald`, `teal`, `cyan`, `sky`, `blue`, `indigo`, `violet`, `purple`, `fuchsia`, `pink`, `rose`, `slate`, `gray`, `zinc`, `neutral`, `stone`

Каждый имеет 11 оттенков: `50`, `100`, `200`, `300`, `400`, `500`, `600`, `700`, `800`, `900`, `950`

#### Прозрачность

```html
<div class="bg-blue-500/50">50% прозрачности</div>
<p class="text-gray-900/80">80% непрозрачности</p>
```

> 📚 **Подробнее:** [Цвета](../styling/colors.md)

---

### 🖼️ 6. Backgrounds (Фоны)

Управляют фоновыми изображениями, градиентами и эффектами.

| Класс | CSS |
| :-- | :-- |
| `bg-{color}` | Цвет фона |
| `bg-[url('...')]` | Фоновое изображение |
| `bg-cover` | Изображение заполняет контейнер |
| `bg-contain` | Изображение целиком |
| `bg-center` | Центрирование фона |
| `bg-no-repeat` | Без повторения |
| `bg-fixed` | Фиксированный фон (параллакс) |
| `bg-gradient-to-{dir}` | Линейный градиент |

> 📚 **Подробнее:** [Фоны](../styling/backgrounds.md)

---

### 🔲 7. Borders (Границы)

Управляют границами, скруглениями и обводками.

#### Ширина

`border`, `border-0`, `border-2`, `border-4`, `border-8`

#### Отдельные стороны

`border-t`, `border-r`, `border-b`, `border-l`, `border-x`, `border-y`

#### Скругление

| Класс | Радиус |
| :-- | :-- |
| `rounded-none` | 0px |
| `rounded-sm` | 2px |
| `rounded` | 4px |
| `rounded-md` | 6px |
| `rounded-lg` | 8px |
| `rounded-xl` | 12px |
| `rounded-2xl` | 16px |
| `rounded-3xl` | 24px |
| `rounded-full` | 9999px (круг) |

#### Ring

`ring-1`, `ring-2`, `ring`, `ring-4`, `ring-8`, `ring-offset-{size}`

#### Divide

`divide-x`, `divide-y`, `divide-{color}`, `divide-dashed`

> 📚 **Подробнее:** [Границы](../styling/borders.md)

---

### ✨ 8. Effects (Эффекты)

Управляют тенями, прозрачностью и фильтрами.

#### Box Shadow

`shadow-sm`, `shadow`, `shadow-md`, `shadow-lg`, `shadow-xl`, `shadow-2xl`, `shadow-inner`, `shadow-none`

#### Opacity

`opacity-0`, `opacity-25`, `opacity-50`, `opacity-75`, `opacity-100`

#### Blur

`blur-sm`, `blur`, `blur-md`, `blur-lg`, `blur-xl`, `blur-2xl`, `blur-3xl`

#### Фильтры

| Класс | Эффект |
| :-- | :-- |
| `brightness-{value}` | Яркость |
| `contrast-{value}` | Контрастность |
| `grayscale` | Оттенки серого |
| `sepia` | Сепия |
| `hue-rotate-{angle}` | Поворот тона |
| `saturate-{value}` | Насыщенность |
| `invert` | Инверсия |

#### Backdrop

`backdrop-blur-{size}`, `backdrop-brightness-{value}`

#### Mix Blend Mode

`mix-blend-multiply`, `mix-blend-screen`, `mix-blend-overlay`

> 📚 **Подробнее:** [Эффекты](../styling/effects.md)

---

### 📐 9. Flexbox

Управляют flexbox-раскладкой.

| Класс | CSS |
| :-- | :-- |
| `flex` | `display: flex` |
| `flex-row` | горизонтальное направление |
| `flex-col` | вертикальное направление |
| `flex-wrap` | перенос элементов |
| `items-center` | вертикальное центрирование |
| `items-start` | выравнивание по верху |
| `items-end` | выравнивание по низу |
| `justify-center` | горизонтальное центрирование |
| `justify-between` | распределение по краям |
| `justify-around` | равные промежутки вокруг |
| `justify-evenly` | равные промежутки |
| `flex-1` | занять доступное пространство |
| `flex-none` | не растягиваться |
| `gap-{size}` | отступы между элементами |
| `order-{n}` | порядок элемента |

> 📚 **Подробнее:** [Flexbox](../layout/flexbox.md)

---

### 🔲 10. Grid

Управляют grid-раскладкой.

| Класс | CSS |
| :-- | :-- |
| `grid` | `display: grid` |
| `grid-cols-{n}` | количество колонок (1-12) |
| `grid-rows-{n}` | количество строк (1-6) |
| `col-span-{n}` | объединение колонок |
| `row-span-{n}` | объединение строк |
| `col-span-full` | на всю ширину |
| `col-start-{n}` | начало колонки |
| `grid-flow-col` | заполнение по колонкам |
| `grid-flow-dense` | заполнение пустот |
| `gap-{size}` | отступы между элементами |

> 📚 **Подробнее:** [Grid](../layout/grid.md)

---

### 🎯 11. Interactivity (Интерактивность)

Управляют поведением элементов при взаимодействии.

#### Cursor

| Класс | Вид курсора |
| :-- | :-- |
| `cursor-pointer` | Указатель (ссылка) |
| `cursor-default` | Обычный |
| `cursor-not-allowed` | Запрещено |
| `cursor-wait` | Ожидание |
| `cursor-grab` | Захват |
| `cursor-text` | Текст |

#### User Select

`select-none`, `select-text`, `select-all`, `select-auto`

#### Pointer Events

`pointer-events-none`, `pointer-events-auto`

#### Resize

`resize-none`, `resize`, `resize-x`, `resize-y`

#### Appearance

`appearance-none` (убирает стандартный вид элементов)

---

### 🔄 12. Transitions (Переходы)

Управляют плавными переходами между состояниями.

#### Transition Property

| Класс | Что анимируется |
| :-- | :-- |
| `transition` | Основные свойства |
| `transition-all` | Все свойства |
| `transition-colors` | Цвета |
| `transition-opacity` | Прозрачность |
| `transition-shadow` | Тени |
| `transition-transform` | Трансформации |
| `transition-none` | Без анимации |

#### Duration

| Класс | Длительность |
| :-- | :-- |
| `duration-75` | 75ms |
| `duration-100` | 100ms |
| `duration-150` | 150ms |
| `duration-200` | 200ms |
| `duration-300` | 300ms |
| `duration-500` | 500ms |
| `duration-700` | 700ms |
| `duration-1000` | 1000ms |

#### Easing

`ease-linear`, `ease-in`, `ease-out`, `ease-in-out`

---

### 🔄 13. Transforms (Трансформации)

Управляют трансформациями элементов.

#### Scale (масштаб)

`scale-0`, `scale-50`, `scale-75`, `scale-90`, `scale-95`, `scale-100`, `scale-105`, `scale-110`, `scale-125`, `scale-150`

#### Rotate (поворот)

`rotate-0`, `rotate-1`, `rotate-2`, `rotate-3`, `rotate-6`, `rotate-12`, `rotate-45`, `rotate-90`, `rotate-180`

#### Translate (смещение)

`translate-x-{size}`, `translate-y-{size}`, `translate-x-1/2`, `translate-y-1/2`

#### Origin (точка трансформации)

`origin-center`, `origin-top`, `origin-bottom`, `origin-left`, `origin-right`

---

### 🖱️ 14. Модификаторы состояний

Добавляются **перед** утилитой через двоеточие:

| Модификатор | Когда применяется |
| :-- | :-- |
| `hover:` | При наведении мыши |
| `focus:` | При фокусе |
| `focus-visible:` | При фокусе клавиатурой |
| `focus-within:` | При фокусе дочернего элемента |
| `active:` | При нажатии |
| `disabled:` | Когда элемент disabled |
| `visited:` | Для посещённых ссылок |
| `first:` | Для первого элемента |
| `last:` | Для последнего элемента |
| `odd:` | Для нечётных элементов |
| `even:` | Для чётных элементов |
| `group-hover:` | При hover на родителе с `group` |
| `peer-checked:` | При checked предыдущего `peer` |

#### Responsive-модификаторы

| Модификатор | Экран |
| :-- | :-- |
| `sm:` | от 640px |
| `md:` | от 768px |
| `lg:` | от 1024px |
| `xl:` | от 1280px |
| `2xl:` | от 1536px |

#### Тема

| Модификатор | Когда |
| :-- | :-- |
| `dark:` | В тёмной теме |

> 📚 **Подробнее:** [Состояния](../responsive/states.md), [Breakpoints](../responsive/breakpoints.md), [Dark Mode](../responsive/dark-mode.md)

---

## 🎨 Пример: сборка компонента из утилит

Посмотрим, как из отдельных утилит собирается реальный UI-элемент:

### Карточка товара

```html
<div class="
  bg-white
  rounded-xl
  shadow-md
  hover:shadow-lg
  transition-shadow
  duration-300
  overflow-hidden
  max-w-sm
">
  <img
    src="product.jpg"
    alt="Товар"
    class="w-full h-48 object-cover"
  >
  <div class="p-6">
    <span class="
      inline-block
      bg-blue-100
      text-blue-800
      text-xs
      font-semibold
      px-2
      py-1
      rounded-full
      mb-2
    ">Новинка</span>
    <h3 class="text-xl font-bold text-gray-900 mb-2">
      Название товара
    </h3>
    <p class="text-gray-600 text-sm mb-4 line-clamp-2">
      Описание товара с подробной информацией.
    </p>
    <div class="flex items-center justify-between">
      <span class="text-2xl font-bold text-gray-900">2 990 ₽</span>
      <button class="
        bg-blue-600
        hover:bg-blue-700
        active:bg-blue-800
        text-white
        font-medium
        px-4
        py-2
        rounded-lg
        transition-colors
        duration-200
        focus:outline-none
        focus:ring-2
        focus:ring-blue-500
        focus:ring-offset-2
      ">
        В корзину
      </button>
    </div>
  </div>
</div>
```

### Какие категории утилит использованы

| Утилита | Категория |
| :-- | :-- |
| `bg-white`, `bg-blue-100`, `bg-blue-600` | Colors / Backgrounds |
| `rounded-xl`, `rounded-lg`, `rounded-full` | Borders |
| `shadow-md`, `hover:shadow-lg` | Effects |
| `transition-shadow`, `transition-colors`, `duration-300` | Transitions |
| `overflow-hidden` | Layout |
| `max-w-sm` | Sizing |
| `w-full`, `h-48` | Sizing |
| `object-cover` | Layout |
| `p-6`, `px-2`, `py-1`, `px-4`, `py-2`, `mb-2`, `mb-4` | Spacing |
| `text-xs`, `text-sm`, `text-xl`, `text-2xl` | Typography |
| `font-semibold`, `font-bold`, `font-medium` | Typography |
| `text-blue-800`, `text-gray-900`, `text-gray-600`, `text-white` | Colors |
| `line-clamp-2` | Typography |
| `inline-block` | Layout |
| `flex`, `items-center`, `justify-between` | Flexbox |
| `hover:bg-blue-700`, `active:bg-blue-800` | States |
| `focus:outline-none`, `focus:ring-2`, `focus:ring-offset-2` | States / Borders |

## 🗺️ Карта документации

Используйте эту таблицу, чтобы быстро найти нужный раздел:

| Что нужно сделать | Раздел |
| :-- | :-- |
| Выровнять элементы в ряд | [Flexbox](../layout/flexbox.md) |
| Создать сетку колонок | [Grid](../layout/grid.md) |
| Добавить отступы | [Отступы](../layout/spacing.md) |
| Задать размеры | [Размеры](../layout/sizing.md) |
| Покрасить текст/фон | [Цвета](../styling/colors.md) |
| Настроить шрифты | [Типографика](../styling/typography.md) |
| Добавить фоновое изображение | [Фоны](../styling/backgrounds.md) |
| Добавить границы/скругления | [Границы](../styling/borders.md) |
| Добавить тень/эффект | [Эффекты](../styling/effects.md) |
| Сделать адаптивный дизайн | [Breakpoints](../responsive/breakpoints.md) |
| Добавить тёмную тему | [Dark Mode](../responsive/dark-mode.md) |
| Добавить hover/focus-эффекты | [Состояния](../responsive/states.md) |
| Настроить свою тему | [Кастомизация](../advanced/customization.md) |
| Создать плагин | [Плагины](../advanced/plugins.md) |
| Использовать @apply, @layer | [Директивы](../advanced/directives.md) |
| Оптимизировать CSS | [Оптимизация](../advanced/optimization.md) |

## 📊 Шпаргалка: самые используемые классы

### Топ-20 классов, которые вы будете использовать постоянно

| # | Класс | Применение |
| :-- | :-- | :-- |
| 1 | `flex` | Включить flexbox |
| 2 | `items-center` | Вертикальное центрирование |
| 3 | `justify-between` | Распределение по краям |
| 4 | `gap-4` | Отступы между элементами |
| 5 | `p-4` | Внутренний отступ |
| 6 | `px-4 py-2` | Отступы для кнопок |
| 7 | `rounded-lg` | Скругление углов |
| 8 | `bg-white` | Белый фон |
| 9 | `text-gray-900` | Тёмный текст |
| 10 | `text-sm` | Маленький текст |
| 11 | `font-bold` | Жирный текст |
| 12 | `w-full` | На всю ширину |
| 13 | `hidden md:block` | Скрыть на мобильных |
| 14 | `hover:bg-blue-600` | Hover-эффект |
| 15 | `transition` | Плавный переход |
| 16 | `shadow-md` | Средняя тень |
| 17 | `max-w-7xl mx-auto` | Контейнер по центру |
| 18 | `grid grid-cols-3` | Сетка из 3 колонок |
| 19 | `border border-gray-200` | Тонкая граница |
| 20 | `focus:ring-2 focus:ring-blue-500` | Focus-обводка |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Поиск «волшебного» класса

```html
<!-- ❌ Плохо: нет класса "card" в Tailwind -->
<div class="card">...</div>

<!-- ✅ Хорошо: собираем из утилит -->
<div class="bg-white rounded-lg shadow-md p-6">...</div>
```

### ❌ Ошибка 2: Слишком много классов в одном элементе

```html
<!-- ❌ Плохо: нечитаемо -->
<button class="bg-blue-500 hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 text-white font-medium px-4 py-2 rounded-lg transition-colors duration-200 disabled:opacity-50 disabled:cursor-not-allowed">

<!-- ✅ Хорошо: вынести в компонент (React/Vue) -->
<Button variant="primary" size="md">Текст</Button>
```

### ❌ Ошибка 3: Забывают, что классы комбинируются

```html
<!-- ❌ Плохо: два конфликтующих класса -->
<div class="p-4 p-8">Непонятно, какой применится</div>

<!-- ✅ Хорошо: один класс -->
<div class="p-8">Понятно</div>
```

### ❌ Ошибка 4: Изобретение своих имён вместо утилит

```css
/* ❌ Плохо: писать CSS вручную */
.my-button {
  background-color: #3b82f6;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
}
```

```html
<!-- ✅ Хорошо: использовать утилиты -->
<button class="bg-blue-500 text-white px-4 py-2 rounded-lg">
  Кнопка
</button>
```

### ❌ Ошибка 5: Забывают про модификаторы

```html
<!-- ❌ Плохо: кнопка не реагирует на hover -->
<button class="bg-blue-500 text-white px-4 py-2 rounded">
  Нет hover-эффекта
</button>

<!-- ✅ Хорошо: добавляем hover -->
<button class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded transition-colors">
  Плавный hover-эффект
</button>
```

## 🎯 Что дальше?

Теперь у вас есть **полная карта** всех утилитарных классов Tailwind CSS! Вы знаете:

- 📂 Какие категории утилит существуют
- 🔍 Где искать детали по каждой теме
- 🧩 Как комбинировать утилиты в реальные компоненты
- ⚡ Какие классы используются чаще всего

**Поздравляем! Вы завершили секцию «Основы»!** 🎉

### Что вы изучили в секции Basics

- 📘 **Введение** — философия utility-first
- 📦 **Установка** — как подключить Tailwind
- ⚙️ **Конфигурация** — как настроить `tailwind.config.js`
- 🎨 **Утилитарные классы** — обзор всех категорий

### Следующий шаг

Теперь вы готовы к созданию реальных макетов!

**Следующая секция:** [📐 Макет → Flexbox](../layout/flexbox.md)

---

---




---

# 📐 Раздел: Layout

---



<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: layout\flexbox.md -->
<!-- ═══════════════════════════════════════════════════════════ -->

# 📐 Flexbox в Tailwind CSS

> **Полное руководство по Flexbox-утилитам Tailwind:** от базового выравнивания до сложных адаптивных макетов

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Поймёте, как работает Flexbox в Tailwind
- ✅ Научитесь выравнивать элементы по осям
- ✅ Сможете создавать адаптивные макеты без медиа-запросов
- ✅ Освоите `flex`, `grow`, `shrink` и `order`
- ✅ Поймёте разницу между `gap`, `space-x` и `space-y`
- ✅ Научитесь решать типовые задачи: центрирование, навбары, карточки

## 🧠 Краткое напоминание: что такое Flexbox?

**Flexbox** (Flexible Box Layout) — это модель CSS для одномерной раскладки элементов в строку или колонку. Tailwind предоставляет **все основные свойства Flexbox** в виде утилитарных классов.

```
Контейнер (parent)          Элементы (children)
┌─────────────────────┐     ┌───┐ ┌───┐ ┌───┐
│  display: flex      │ ──▶ │ A │ │ B │ │ C │
│  justify-content    │     └───┘ └───┘ └───┘
│  align-items        │
└─────────────────────┘
```

## 🚀 Основы: включаем Flexbox

### `display: flex` и `display: inline-flex`

```html
<!-- Блочный flex-контейнер (занимает всю ширину) -->
<div class="flex">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>

<!-- Инлайновый flex-контейнер (занимает только нужное место) -->
<div class="inline-flex">
  <div>1</div>
  <div>2</div>
</div>
```

> 💡 **Правило:** в 95% случаев используйте `flex`. `inline-flex` нужен только когда контейнер должен вести себя как инлайновый элемент (например, кнопка с иконкой).

## 🧭 Направление: `flex-direction`

По умолчанию flex-элементы располагаются **в строку** (слева направо). Tailwind позволяет менять направление:

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `flex-row` | `flex-direction: row` | → По горизонтали (по умолчанию) |
| `flex-row-reverse` | `flex-direction: row-reverse` | ← Справа налево |
| `flex-col` | `flex-direction: column` | ↓ По вертикали |
| `flex-col-reverse` | `flex-direction: column-reverse` | ↑ Снизу вверх |

```html
<!-- Горизонтальный список -->
<div class="flex flex-row gap-2">
  <span>Главная</span>
  <span>О нас</span>
  <span>Контакты</span>
</div>

<!-- Вертикальный список (мобильная версия) -->
<div class="flex flex-col gap-2">
  <span>Главная</span>
  <span>О нас</span>
  <span>Контакты</span>
</div>
```

## 🔄 Перенос: `flex-wrap`

По умолчанию flex-элементы **не переносятся** — они сжимаются, чтобы поместиться в одну строку. Чтобы разрешить перенос:

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `flex-wrap` | `flex-wrap: wrap` | Перенос на новую строку |
| `flex-nowrap` | `flex-wrap: nowrap` | Без переноса (по умолчанию) |
| `flex-wrap-reverse` | `flex-wrap: wrap-reverse` | Перенос в обратном порядке |

```html
<!-- Теги, которые переносятся на новую строку -->
<div class="flex flex-wrap gap-2">
  <span class="bg-blue-100 text-blue-800 px-2 py-1 rounded">HTML</span>
  <span class="bg-blue-100 text-blue-800 px-2 py-1 rounded">CSS</span>
  <span class="bg-blue-100 text-blue-800 px-2 py-1 rounded">JavaScript</span>
  <span class="bg-blue-100 text-blue-800 px-2 py-1 rounded">React</span>
  <span class="bg-blue-100 text-blue-800 px-2 py-1 rounded">Tailwind</span>
  <span class="bg-blue-100 text-blue-800 px-2 py-1 rounded">TypeScript</span>
</div>
```

## 📏 Выравнивание по главной оси: `justify-content`

Главная ось — это направление, в котором идут элементы (по умолчанию — горизонталь).

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `justify-start` | `justify-content: flex-start` | К началу |
| `justify-end` | `justify-content: flex-end` | К концу |
| `justify-center` | `justify-content: center` | По центру |
| `justify-between` | `justify-content: space-between` | Равные промежутки между |
| `justify-around` | `justify-content: space-around` | Равные промежутки вокруг |
| `justify-evenly` | `justify-content: space-evenly` | Равные промежутки (включая края) |

```html
<!-- Навбар: логотип слева, меню справа -->
<nav class="flex justify-between items-center p-4 bg-white shadow">
  <div class="font-bold text-xl">Logo</div>
  <div class="flex gap-4">
    <a href="#">Главная</a>
    <a href="#">О нас</a>
    <a href="#">Контакты</a>
  </div>
</nav>

<!-- Кнопки по центру -->
<div class="flex justify-center gap-3 mt-6">
  <button class="bg-blue-500 text-white px-4 py-2 rounded">Сохранить</button>
  <button class="bg-gray-200 px-4 py-2 rounded">Отмена</button>
</div>
```

## 📐 Выравнивание по поперечной оси: `align-items`

Поперечная ось — перпендикулярна главной (по умолчанию — вертикаль).

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `items-start` | `align-items: flex-start` | К верху |
| `items-end` | `align-items: flex-end` | К низу |
| `items-center` | `align-items: center` | По центру |
| `items-baseline` | `align-items: baseline` | По базовой линии текста |
| `items-stretch` | `align-items: stretch` | Растянуть (по умолчанию) |

```html
<!-- Карточки одинаковой высоты -->
<div class="flex items-stretch gap-4">
  <div class="bg-white p-4 rounded shadow">
    <h3>Короткий заголовок</h3>
  </div>
  <div class="bg-white p-4 rounded shadow">
    <h3>Очень длинный заголовок, который занимает несколько строк</h3>
  </div>
</div>

<!-- Иконка и текст по центру -->
<div class="flex items-center gap-2">
  <svg class="w-5 h-5">...</svg>
  <span>Текст рядом с иконкой</span>
</div>
```

## 🎯 Выравнивание одного элемента: `align-self`

Если нужно выровнять **один конкретный элемент** внутри flex-контейнера:

| Класс | CSS |
| :-- | :-- |
| `self-start` | `align-self: flex-start` |
| `self-end` | `align-self: flex-end` |
| `self-center` | `align-self: center` |
| `self-stretch` | `align-self: stretch` |
| `self-auto` | `align-self: auto` |

```html
<div class="flex items-center gap-4 h-32 bg-gray-100">
  <div class="bg-blue-500 p-4">Обычный</div>
  <div class="bg-green-500 p-4 self-start">Вверху</div>
  <div class="bg-red-500 p-4 self-end">Внизу</div>
</div>
```

## 📦 Размер элементов: `flex`, `grow`, `shrink`

Это одна из самых мощных (и самых сложных для понимания) частей Flexbox.

### `flex` — сокращённая запись

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `flex-1` | `flex: 1 1 0%` | Равномерно занимает доступное пространство |
| `flex-auto` | `flex: 1 1 auto` | Растягивается с учётом содержимого |
| `flex-initial` | `flex: 0 1 auto` | Может сжиматься, но не расти |
| `flex-none` | `flex: none` | Не растёт и не сжимается |

```html
<!-- Сайдбар фиксированной ширины, контент занимает всё остальное -->
<div class="flex h-screen">
  <aside class="flex-none w-64 bg-gray-800 text-white p-4">
    Меню
  </aside>
  <main class="flex-1 p-6 bg-gray-100">
    Основной контент
  </main>
</div>
```

### `grow` и `shrink` — по отдельности

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `grow` | `flex-grow: 1` | Разрешить рост |
| `grow-0` | `flex-grow: 0` | Запретить рост |
| `shrink` | `flex-shrink: 1` | Разрешить сжатие |
| `shrink-0` | `flex-shrink: 0` | Запретить сжатие |

```html
<!-- Кнопка не сжимается, поле ввода растягивается -->
<div class="flex gap-2">
  <input type="text" class="flex-1 border rounded px-3 py-2" placeholder="Поиск...">
  <button class="shrink-0 bg-blue-500 text-white px-4 py-2 rounded">
    Искать
  </button>
</div>
```

## 🔢 Порядок элементов: `order`

Меняет визуальный порядок элементов **без изменения HTML**:

| Класс | CSS |
| :-- | :-- |
| `order-first` | `order: -9999` |
| `order-last` | `order: 9999` |
| `order-none` | `order: 0` |
| `order-1` ... `order-12` | `order: 1` ... `order: 12` |

```html
<!-- На мобильных: кнопка внизу -->
<!-- На десктопе: кнопка в начале -->
<div class="flex flex-col md:flex-row">
  <button class="order-last md:order-first bg-blue-500 text-white px-4 py-2">
    Купить
  </button>
  <div class="order-first md:order-last">
    <h2>Описание товара</h2>
    <p>Много полезного текста...</p>
  </div>
</div>
```

## 🕳️ Отступы между элементами: `gap`

`gap` — это **современный и предпочтительный** способ добавлять отступы между flex-элементами.

| Класс | Размер |
| :-- | :-- |
| `gap-0` | `0` |
| `gap-1` | `0.25rem` (4px) |
| `gap-2` | `0.5rem` (8px) |
| `gap-4` | `1rem` (16px) |
| `gap-8` | `2rem` (32px) |
| `gap-x-4` | Горизонтальный отступ |
| `gap-y-4` | Вертикальный отступ |

```html
<!-- Сетка карточек с одинаковыми отступами -->
<div class="flex flex-wrap gap-6">
  <div class="flex-1 min-w-[250px] bg-white p-4 rounded shadow">Карточка 1</div>
  <div class="flex-1 min-w-[250px] bg-white p-4 rounded shadow">Карточка 2</div>
  <div class="flex-1 min-w-[250px] bg-white p-4 rounded shadow">Карточка 3</div>
</div>
```

### ⚠️ `gap` vs `space-x` / `space-y`

Tailwind предлагает **два способа** добавить отступы:

```html
<!-- Способ 1: gap (рекомендуется) -->
<div class="flex gap-4">
  <div>A</div>
  <div>B</div>
</div>

<!-- Способ 2: space-x (старый подход) -->
<div class="flex space-x-4">
  <div>A</div>
  <div>B</div>
</div>
```

| Критерий | `gap` | `space-x/y` |
| :-- | :-- | :-- |
| **Работа с `flex-wrap`** | ✅ Корректно | ❌ Лишние отступы на краях |
| **Производительность** | 🟢 Нативный CSS | 🟡 Через `> * + *` |
| **Поддержка браузеров** | 🟢 Все современные | 🟢 Все |
| **Рекомендация** | ✅ Использовать всегда | 🟡 Только для legacy |

> 💡 **Правило:** всегда используйте `gap`. `space-x/y` оставьте для случаев, когда нужно поддерживать IE11 (хотя Tailwind v3 его уже не поддерживает).

## 🎨 Практические паттерны

### 1. 🎯 Идеальное центрирование

```html
<div class="flex items-center justify-center h-screen bg-gray-100">
  <div class="bg-white p-8 rounded-lg shadow-xl">
    <h1 class="text-2xl font-bold">Добро пожаловать!</h1>
  </div>
</div>
```

### 2. 📱 Адаптивная навигация

```html
<nav class="flex flex-col md:flex-row md:items-center md:justify-between p-4 bg-white shadow">
  <div class="font-bold text-xl mb-2 md:mb-0">Logo</div>
  <div class="flex flex-col md:flex-row gap-4">
    <a href="#" class="hover:text-blue-500">Главная</a>
    <a href="#" class="hover:text-blue-500">О нас</a>
    <a href="#" class="hover:text-blue-500">Контакты</a>
  </div>
</nav>
```

### 3. 💬 Чат-сообщения

```html
<div class="flex flex-col gap-3 p-4 max-w-md">
  <!-- Сообщение собеседника -->
  <div class="flex items-end gap-2">
    <img src="avatar.jpg" class="w-8 h-8 rounded-full">
    <div class="bg-gray-200 rounded-lg px-3 py-2 max-w-xs">
      Привет! Как дела?
    </div>
  </div>

  <!-- Моё сообщение -->
  <div class="flex items-end gap-2 self-end">
    <div class="bg-blue-500 text-white rounded-lg px-3 py-2 max-w-xs">
      Отлично, спасибо!
    </div>
  </div>
</div>
```

### 4. 🏆 Holy Grail Layout

```html
<div class="flex flex-col min-h-screen">
  <!-- Header -->
  <header class="bg-gray-800 text-white p-4">
    Header
  </header>

  <!-- Main content -->
  <div class="flex flex-1">
    <!-- Sidebar -->
    <aside class="flex-none w-48 bg-gray-200 p-4">
      Sidebar
    </aside>

    <!-- Content -->
    <main class="flex-1 p-6">
      Main Content
    </main>

    <!-- Right sidebar -->
    <aside class="flex-none w-48 bg-gray-200 p-4">
      Right Sidebar
    </aside>
  </div>

  <!-- Footer -->
  <footer class="bg-gray-800 text-white p-4">
    Footer
  </footer>
</div>
```

### 5. 🏷️ Список с иконкой и бейджем

```html
<div class="flex items-center justify-between p-3 bg-white rounded-lg shadow">
  <div class="flex items-center gap-3">
    <div class="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center">
      📧
    </div>
    <div>
      <div class="font-medium">Email уведомления</div>
      <div class="text-sm text-gray-500">Получать письма о новых событиях</div>
    </div>
  </div>
  <span class="bg-red-500 text-white text-xs px-2 py-1 rounded-full">3</span>
</div>
```

## 📱 Responsive Flexbox

Одна из самых мощных фишек — менять направление и выравнивание на разных экранах:

```html
<!-- Мобильные: колонка -->
<!-- Планшеты: 2 в ряд -->
<!-- Десктоп: 4 в ряд -->
<div class="flex flex-col sm:flex-row sm:flex-wrap gap-4">
  <div class="w-full sm:w-1/2 lg:w-1/4 bg-white p-4 rounded">Карточка 1</div>
  <div class="w-full sm:w-1/2 lg:w-1/4 bg-white p-4 rounded">Карточка 2</div>
  <div class="w-full sm:w-1/2 lg:w-1/4 bg-white p-4 rounded">Карточка 3</div>
  <div class="w-full sm:w-1/2 lg:w-1/4 bg-white p-4 rounded">Карточка 4</div>
</div>
```

## ⚡ Шпаргалка: что когда использовать

| Задача | Классы |
| :-- | :-- |
| Элементы в ряд | `flex gap-4` |
| Элементы в колонку | `flex flex-col gap-4` |
| Центрировать всё | `flex items-center justify-center` |
| Распределить по краям | `flex justify-between` |
| Один элемент растянуть | `flex-1` |
| Запретить сжатие | `shrink-0` |
| Перенос на новую строку | `flex-wrap` |
| Поменять порядок | `order-first`, `order-last`, `order-N` |
| Выровнять один элемент | `self-center`, `self-end` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Забывают `min-w-0` для переполненного текста

```html
<!-- ❌ Текст выходит за пределы -->
<div class="flex">
  <div class="flex-1 truncate">
    Очень-очень-длинный-текст-который-не-помещается
  </div>
</div>

<!-- ✅ Работает корректно -->
<div class="flex">
  <div class="flex-1 min-w-0 truncate">
    Очень-очень-длинный-текст-который-не-помещается
  </div>
</div>
```

> 💡 **Почему:** flex-элементы по умолчанию имеют `min-width: auto`, что мешает `truncate` работать.

### ❌ Ошибка 2: `flex-1` без `min-w-0` в карточках

```html
<!-- ❌ Карточки могут не сжиматься -->
<div class="flex gap-4">
  <div class="flex-1">Длинный контент...</div>
</div>

<!-- ✅ Карточки сжимаются корректно -->
<div class="flex gap-4">
  <div class="flex-1 min-w-0">Длинный контент...</div>
</div>
```

### ❌ Ошибка 3: `space-x` с `flex-wrap`

```html
<!-- ❌ Лишние отступы на краях строк -->
<div class="flex flex-wrap space-x-4">...</div>

<!-- ✅ Корректные отступы -->
<div class="flex flex-wrap gap-4">...</div>
```

## 🎯 Что дальше?

Теперь вы мастерски владеете Flexbox! Но что если нужна **двумерная раскладка** — с колонками и строками одновременно?

**Следующий шаг:** [🔲 Grid в Tailwind CSS](grid.md) — изучим мощную систему гридов для сложных макетов.

---

> 💬 **Упражнение:** попробуйте сверстать карточку товара с изображением, заголовком, ценой и кнопкой «Купить», используя только flex-утилиты. Убедитесь, что она адаптивна!

---




<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: layout\grid.md -->
<!-- ═══════════════════════════════════════════════════════════ -->

# 🔲 Grid в Tailwind CSS

> **Полное руководство по CSS Grid в Tailwind:** от базовых сеток до сложных макетов с именованными областями и адаптивными колонками

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Поймёте разницу между Flexbox и Grid
- ✅ Освоите все grid-утилиты Tailwind
- ✅ Научитесь создавать сложные макеты с `col-span`, `row-span`
- ✅ Сможете управлять позиционированием элементов через `col-start`, `col-end`
- ✅ Освоите `grid-flow` для автоматической раскладки
- ✅ Создадите адаптивные сетки без медиа-запросов
- ✅ Поймёте, когда использовать Grid, а когда Flexbox
- ✅ Избежите типичных ошибок при работе с Grid

## 🧠 Grid vs Flexbox: когда что использовать

| Критерий | Flexbox | Grid |
| :-- | :-- | :-- |
| **Измерения** | Одномерный (строка ИЛИ колонка) | Двумерный (строки И колонки) |
| **Подходит для** | Компонентов, навигации, списков | Страничных макетов, галерей, форм |
| **Размер элементов** | По содержимому | По сетке |
| **Наложение** | Нет | Да (через позиции) |
| **Сложность** | Простой | Мощный, но сложнее |

> 💡 **Правило:** используйте **Flexbox для компонентов** (кнопки, карточки, навигация), **Grid для макетов** (страница, галерея, дашборд).

## 🚀 Основы: включаем Grid

### `display: grid` и `display: inline-grid`

```html
<!-- Блочный grid-контейнер -->
<div class="grid">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>

<!-- Инлайновый grid-контейнер -->
<div class="inline-grid">
  <div>1</div>
  <div>2</div>
</div>
```

## 📊 Определение колонок: `grid-cols-{n}`

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `grid-cols-1` | `grid-template-columns: repeat(1, minmax(0, 1fr))` | 1 колонка |
| `grid-cols-2` | `grid-template-columns: repeat(2, minmax(0, 1fr))` | 2 колонки |
| `grid-cols-3` | `grid-template-columns: repeat(3, minmax(0, 1fr))` | 3 колонки |
| `grid-cols-4` | `grid-template-columns: repeat(4, minmax(0, 1fr))` | 4 колонки |
| `grid-cols-5` | `grid-template-columns: repeat(5, minmax(0, 1fr))` | 5 колонок |
| `grid-cols-6` | `grid-template-columns: repeat(6, minmax(0, 1fr))` | 6 колонок |
| `grid-cols-7` | `grid-template-columns: repeat(7, minmax(0, 1fr))` | 7 колонок |
| `grid-cols-8` | `grid-template-columns: repeat(8, minmax(0, 1fr))` | 8 колонок |
| `grid-cols-9` | `grid-template-columns: repeat(9, minmax(0, 1fr))` | 9 колонок |
| `grid-cols-10` | `grid-template-columns: repeat(10, minmax(0, 1fr))` | 10 колонок |
| `grid-cols-11` | `grid-template-columns: repeat(11, minmax(0, 1fr))` | 11 колонок |
| `grid-cols-12` | `grid-template-columns: repeat(12, minmax(0, 1fr))` | 12 колонок |
| `grid-cols-none` | `grid-template-columns: none` | Без колонок |

```html
<!-- Сетка из 3 колонок -->
<div class="grid grid-cols-3 gap-4">
  <div class="bg-blue-500 p-4 text-white">1</div>
  <div class="bg-blue-500 p-4 text-white">2</div>
  <div class="bg-blue-500 p-4 text-white">3</div>
  <div class="bg-blue-500 p-4 text-white">4</div>
  <div class="bg-blue-500 p-4 text-white">5</div>
  <div class="bg-blue-500 p-4 text-white">6</div>
</div>
```

### Адаптивные сетки

```html
<!-- Мобильные: 1 колонка -->
<!-- Планшеты: 2 колонки -->
<!-- Десктопы: 4 колонки -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
  <div class="bg-white p-4 rounded shadow">Карточка 1</div>
  <div class="bg-white p-4 rounded shadow">Карточка 2</div>
  <div class="bg-white p-4 rounded shadow">Карточка 3</div>
  <div class="bg-white p-4 rounded shadow">Карточка 4</div>
</div>
```

## 📐 Определение строк: `grid-rows-{n}`

| Класс | CSS |
| :-- | :-- |
| `grid-rows-1` | `grid-template-rows: repeat(1, minmax(0, 1fr))` |
| `grid-rows-2` | `grid-template-rows: repeat(2, minmax(0, 1fr))` |
| `grid-rows-3` | `grid-template-rows: repeat(3, minmax(0, 1fr))` |
| `grid-rows-4` | `grid-template-rows: repeat(4, minmax(0, 1fr))` |
| `grid-rows-5` | `grid-template-rows: repeat(5, minmax(0, 1fr))` |
| `grid-rows-6` | `grid-template-rows: repeat(6, minmax(0, 1fr))` |
| `grid-rows-none` | `grid-template-rows: none` |

```html
<!-- Сетка 3×3 -->
<div class="grid grid-cols-3 grid-rows-3 gap-2 h-96">
  <div class="bg-blue-500 p-4">1</div>
  <div class="bg-blue-500 p-4">2</div>
  <div class="bg-blue-500 p-4">3</div>
  <div class="bg-blue-500 p-4">4</div>
  <div class="bg-blue-500 p-4">5</div>
  <div class="bg-blue-500 p-4">6</div>
  <div class="bg-blue-500 p-4">7</div>
  <div class="bg-blue-500 p-4">8</div>
  <div class="bg-blue-500 p-4">9</div>
</div>
```

## 🔀 Объединение колонок: `col-span-{n}`

| Класс | CSS |
| :-- | :-- |
| `col-auto` | `grid-column: auto` |
| `col-span-1` | `grid-column: span 1 / span 1` |
| `col-span-2` | `grid-column: span 2 / span 2` |
| `col-span-3` | `grid-column: span 3 / span 3` |
| `col-span-4` | `grid-column: span 4 / span 4` |
| `col-span-5` | `grid-column: span 5 / span 5` |
| `col-span-6` | `grid-column: span 6 / span 6` |
| `col-span-7` | `grid-column: span 7 / span 7` |
| `col-span-8` | `grid-column: span 8 / span 8` |
| `col-span-9` | `grid-column: span 9 / span 9` |
| `col-span-10` | `grid-column: span 10 / span 10` |
| `col-span-11` | `grid-column: span 11 / span 11` |
| `col-span-12` | `grid-column: span 12 / span 12` |
| `col-span-full` | `grid-column: 1 / -1` |

```html
<!-- Карточка на 2 колонки -->
<div class="grid grid-cols-3 gap-4">
  <div class="col-span-2 bg-blue-500 p-4 text-white">
    Широкая карточка (2 колонки)
  </div>
  <div class="bg-blue-500 p-4 text-white">Обычная</div>
  <div class="bg-blue-500 p-4 text-white">Обычная</div>
  <div class="bg-blue-500 p-4 text-white">Обычная</div>
  <div class="bg-blue-500 p-4 text-white">Обычная</div>
</div>

<!-- Карточка на всю ширину -->
<div class="grid grid-cols-4 gap-4">
  <div class="col-span-full bg-purple-500 p-4 text-white">
    На всю ширину (col-span-full)
  </div>
  <div class="bg-blue-500 p-4 text-white">1</div>
  <div class="bg-blue-500 p-4 text-white">2</div>
  <div class="bg-blue-500 p-4 text-white">3</div>
  <div class="bg-blue-500 p-4 text-white">4</div>
</div>
```

## 🔄 Объединение строк: `row-span-{n}`

| Класс | CSS |
| :-- | :-- |
| `row-auto` | `grid-row: auto` |
| `row-span-1` | `grid-row: span 1 / span 1` |
| `row-span-2` | `grid-row: span 2 / span 2` |
| `row-span-3` | `grid-row: span 3 / span 3` |
| `row-span-4` | `grid-row: span 4 / span 4` |
| `row-span-5` | `grid-row: span 5 / span 5` |
| `row-span-6` | `grid-row: span 6 / span 6` |
| `row-span-full` | `grid-row: 1 / -1` |

```html
<!-- Сетка с элементом на 2 строки -->
<div class="grid grid-cols-3 grid-rows-3 gap-2 h-96">
  <div class="row-span-2 bg-blue-500 p-4 text-white">
    На 2 строки
  </div>
  <div class="bg-blue-500 p-4 text-white">2</div>
  <div class="bg-blue-500 p-4 text-white">3</div>
  <div class="bg-blue-500 p-4 text-white">5</div>
  <div class="bg-blue-500 p-4 text-white">6</div>
  <div class="col-span-2 bg-purple-500 p-4 text-white">
    На 2 колонки
  </div>
</div>
```

## 📍 Позиционирование: `col-start-{n}` и `col-end-{n}`

Для точного контроля позиций используйте start/end:

### Column start

| Класс | CSS |
| :-- | :-- |
| `col-start-1` | `grid-column-start: 1` |
| `col-start-2` | `grid-column-start: 2` |
| ... | ... |
| `col-start-13` | `grid-column-start: 13` |
| `col-start-auto` | `grid-column-start: auto` |

### Column end

| Класс | CSS |
| :-- | :-- |
| `col-end-1` | `grid-column-end: 1` |
| `col-end-2` | `grid-column-end: 2` |
| ... | ... |
| `col-end-13` | `grid-column-end: 13` |
| `col-end-auto` | `grid-column-end: auto` |

```html
<!-- Точное позиционирование -->
<div class="grid grid-cols-6 gap-2">
  <div class="col-start-2 col-end-5 bg-blue-500 p-4 text-white">
    С 2-й по 5-ю колонку
  </div>
  <div class="col-start-1 col-end-3 bg-green-500 p-4 text-white">
    С 1-й по 3-ю
  </div>
  <div class="col-start-5 col-end-7 bg-purple-500 p-4 text-white">
    С 5-й по 7-ю
  </div>
</div>
```

### Row start/end

Аналогично для строк:

```html
<div class="grid grid-cols-3 grid-rows-3 gap-2 h-96">
  <div class="col-start-1 col-end-3 row-start-1 row-end-3 bg-blue-500 p-4 text-white">
    Занимает 2×2
  </div>
  <div class="bg-gray-300 p-4">2</div>
  <div class="bg-gray-300 p-4">3</div>
  <div class="bg-gray-300 p-4">4</div>
  <div class="bg-gray-300 p-4">5</div>
  <div class="bg-gray-300 p-4">6</div>
  <div class="bg-gray-300 p-4">7</div>
</div>
```

## 🌊 Auto-flow: `grid-flow-{direction}`

Управляет тем, как элементы автоматически размещаются в сетке:

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `grid-flow-row` | `grid-auto-flow: row` | Заполнение по строкам (по умолчанию) |
| `grid-flow-col` | `grid-auto-flow: column` | Заполнение по колонкам |
| `grid-flow-dense` | `grid-auto-flow: dense` | Заполнение пустых мест |
| `grid-flow-row-dense` | `grid-auto-flow: row dense` | По строкам + заполнение пустот |
| `grid-flow-col-dense` | `grid-auto-flow: column dense` | По колонкам + заполнение пустот |

```html
<!-- По строкам (по умолчанию) -->
<div class="grid grid-cols-3 grid-flow-row gap-2">
  <div class="bg-blue-500 p-4">1</div>
  <div class="bg-blue-500 p-4">2</div>
  <div class="bg-blue-500 p-4">3</div>
  <div class="bg-blue-500 p-4">4</div>
</div>

<!-- По колонкам -->
<div class="grid grid-rows-3 grid-flow-col gap-2 h-48">
  <div class="bg-blue-500 p-4">1</div>
  <div class="bg-blue-500 p-4">2</div>
  <div class="bg-blue-500 p-4">3</div>
  <div class="bg-blue-500 p-4">4</div>
  <div class="bg-blue-500 p-4">5</div>
  <div class="bg-blue-500 p-4">6</div>
</div>
```

### Dense: заполнение пустот

```html
<!-- Без dense: пустота в углу -->
<div class="grid grid-cols-3 gap-2">
  <div class="col-span-2 bg-blue-500 p-4 text-white">1 (2 колонки)</div>
  <div class="bg-blue-500 p-4 text-white">2</div>
  <div class="bg-blue-500 p-4 text-white">3</div>
  <div class="bg-blue-500 p-4 text-white">4</div>
  <!-- Пустое место в конце первой строки -->
</div>

<!-- С dense: пустота заполняется -->
<div class="grid grid-cols-3 grid-flow-dense gap-2">
  <div class="col-span-2 bg-blue-500 p-4 text-white">1 (2 колонки)</div>
  <div class="bg-blue-500 p-4 text-white">2</div>
  <div class="bg-blue-500 p-4 text-white">3</div>
  <div class="bg-blue-500 p-4 text-white">4</div>
  <!-- Элемент 4 заполнит пустоту -->
</div>
```

## 📏 Auto columns/rows: `auto-cols-{size}` и `auto-rows-{size}`

Управляют размером **автоматически созданных** треков:

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `auto-cols-auto` | `grid-auto-columns: auto` | По содержимому |
| `auto-cols-min` | `grid-auto-columns: min-content` | Минимальный |
| `auto-cols-max` | `grid-auto-columns: max-content` | Максимальный |
| `auto-cols-fr` | `grid-auto-columns: minmax(0, 1fr)` | Равные доли |

```html
<!-- Автоматические колонки равной ширины -->
<div class="grid grid-flow-col auto-cols-fr gap-2">
  <div class="bg-blue-500 p-4 text-white">1</div>
  <div class="bg-blue-500 p-4 text-white">2</div>
  <div class="bg-blue-500 p-4 text-white">3</div>
  <div class="bg-blue-500 p-4 text-white">4</div>
</div>
```

Аналогично для строк:

| Класс | CSS |
| :-- | :-- |
| `auto-rows-auto` | `grid-auto-rows: auto` |
| `auto-rows-min` | `grid-auto-rows: min-content` |
| `auto-rows-max` | `grid-auto-rows: max-content` |
| `auto-rows-fr` | `grid-auto-rows: minmax(0, 1fr)` |

## 🕳️ Отступы: `gap-{size}`

`gap` добавляет отступы **между** grid-элементами (не по краям):

```html
<!-- Одинаковые отступы -->
<div class="grid grid-cols-3 gap-4">
  <div class="bg-blue-500 p-4">1</div>
  <div class="bg-blue-500 p-4">2</div>
  <div class="bg-blue-500 p-4">3</div>
</div>

<!-- Разные отступы по осям -->
<div class="grid grid-cols-3 gap-x-8 gap-y-4">
  <div class="bg-blue-500 p-4">1</div>
  <div class="bg-blue-500 p-4">2</div>
  <div class="bg-blue-500 p-4">3</div>
</div>
```

## 🎯 Выравнивание элементов

### `justify-items` — по горизонтали

| Класс | CSS |
| :-- | :-- |
| `justify-items-start` | `justify-items: start` |
| `justify-items-end` | `justify-items: end` |
| `justify-items-center` | `justify-items: center` |
| `justify-items-stretch` | `justify-items: stretch` (по умолчанию) |

### `align-items` — по вертикали

| Класс | CSS |
| :-- | :-- |
| `items-start` | `align-items: start` |
| `items-end` | `align-items: end` |
| `items-center` | `align-items: center` |
| `items-stretch` | `align-items: stretch` (по умолчанию) |

### `place-items` — оба сразу

| Класс | CSS |
| :-- | :-- |
| `place-items-start` | `place-items: start` |
| `place-items-end` | `place-items: end` |
| `place-items-center` | `place-items: center` |
| `place-items-stretch` | `place-items: stretch` |

```html
<!-- Центрирование всех элементов -->
<div class="grid grid-cols-3 gap-4 h-64 place-items-center bg-gray-100">
  <div class="bg-blue-500 p-4 text-white">1</div>
  <div class="bg-blue-500 p-4 text-white">2</div>
  <div class="bg-blue-500 p-4 text-white">3</div>
</div>
```

## 📦 Выравнивание содержимого сетки

### `justify-content` — горизонтальное распределение

| Класс | CSS |
| :-- | :-- |
| `justify-start` | `justify-content: start` |
| `justify-end` | `justify-content: end` |
| `justify-center` | `justify-content: center` |
| `justify-between` | `justify-content: space-between` |
| `justify-around` | `justify-content: space-around` |
| `justify-evenly` | `justify-content: space-evenly` |

### `align-content` — вертикальное распределение

| Класс | CSS |
| :-- | :-- |
| `content-start` | `align-content: start` |
| `content-end` | `align-content: end` |
| `content-center` | `align-content: center` |
| `content-between` | `align-content: space-between` |
| `content-around` | `align-content: space-around` |
| `content-evenly` | `align-content: space-evenly` |
| `content-baseline` | `align-content: baseline` |

```html
<!-- Сетка по центру контейнера -->
<div class="grid grid-cols-3 gap-2 h-96 content-center justify-center bg-gray-100">
  <div class="bg-blue-500 p-4 text-white">1</div>
  <div class="bg-blue-500 p-4 text-white">2</div>
  <div class="bg-blue-500 p-4 text-white">3</div>
</div>
```

## 🎯 Позиционирование одного элемента

### `justify-self` и `align-self`

| Класс | CSS |
| :-- | :-- |
| `justify-self-auto` | `justify-self: auto` |
| `justify-self-start` | `justify-self: start` |
| `justify-self-end` | `justify-self: end` |
| `justify-self-center` | `justify-self: center` |
| `justify-self-stretch` | `justify-self: stretch` |

```html
<!-- Один элемент выровнен иначе -->
<div class="grid grid-cols-3 gap-4 h-64 bg-gray-100">
  <div class="bg-blue-500 p-4 text-white">1</div>
  <div class="bg-green-500 p-4 text-white justify-self-end">2 (вправо)</div>
  <div class="bg-blue-500 p-4 text-white">3</div>
  <div class="bg-blue-500 p-4 text-white">4</div>
  <div class="bg-purple-500 p-4 text-white self-end">5 (вниз)</div>
  <div class="bg-blue-500 p-4 text-white">6</div>
</div>
```

## 🎨 Arbitrary values

Если стандартных значений недостаточно:

```html
<!-- Кастомное количество колонок -->
<div class="grid grid-cols-[repeat(15,minmax(0,1fr))] gap-2">
  <!-- 15 колонок -->
</div>

<!-- Кастомные размеры колонок -->
<div class="grid grid-cols-[200px_1fr_200px] gap-4">
  <aside>Сайдбар 200px</aside>
  <main>Контент (остальное)</main>
  <aside>Сайдбар 200px</aside>
</div>

<!-- Смешанные размеры -->
<div class="grid grid-cols-[auto_1fr_auto] gap-4">
  <div>По содержимому</div>
  <div>Растягивается</div>
  <div>По содержимому</div>
</div>
```

## 🎨 Практические паттерны

### 1. 🏆 Holy Grail Layout

```html
<div class="grid grid-cols-[200px_1fr_200px] grid-rows-[auto_1fr_auto] min-h-screen">
  <!-- Header -->
  <header class="col-span-full bg-gray-800 text-white p-4">
    Header
  </header>

  <!-- Sidebar left -->
  <aside class="bg-gray-200 p-4">
    Left Sidebar
  </aside>

  <!-- Main content -->
  <main class="bg-white p-6">
    Main Content
  </main>

  <!-- Sidebar right -->
  <aside class="bg-gray-200 p-4">
    Right Sidebar
  </aside>

  <!-- Footer -->
  <footer class="col-span-full bg-gray-800 text-white p-4">
    Footer
  </footer>
</div>
```

### 2. 🖼️ Masonry-подобная галерея

```html
<div class="grid grid-cols-2 md:grid-cols-4 gap-4 auto-rows-[100px]">
  <div class="row-span-2 bg-blue-500 rounded-lg p-4 text-white">
    Высокая карточка
  </div>
  <div class="bg-green-500 rounded-lg p-4 text-white">
    Обычная
  </div>
  <div class="col-span-2 bg-purple-500 rounded-lg p-4 text-white">
    Широкая карточка
  </div>
  <div class="row-span-2 bg-yellow-500 rounded-lg p-4 text-white">
    Высокая
  </div>
  <div class="bg-red-500 rounded-lg p-4 text-white">
    Обычная
  </div>
  <div class="bg-pink-500 rounded-lg p-4 text-white">
    Обычная
  </div>
  <div class="col-span-2 bg-indigo-500 rounded-lg p-4 text-white">
    Широкая
  </div>
</div>
```

### 3. 📊 Dashboard с виджетами

```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 p-4">
  <!-- Большая статистика -->
  <div class="lg:col-span-2 bg-gradient-to-br from-blue-500 to-purple-600 rounded-xl p-6 text-white">
    <h3 class="text-xl font-bold mb-2">Общий доход</h3>
    <div class="text-4xl font-bold">1 234 567 ₽</div>
    <div class="mt-2 text-blue-100">+12% за месяц</div>
  </div>

  <!-- Два маленьких виджета -->
  <div class="bg-white rounded-xl shadow p-6">
    <h3 class="text-sm font-medium text-gray-500">Пользователи</h3>
    <div class="text-2xl font-bold mt-2">12 345</div>
  </div>
  <div class="bg-white rounded-xl shadow p-6">
    <h3 class="text-sm font-medium text-gray-500">Заказы</h3>
    <div class="text-2xl font-bold mt-2">1 234</div>
  </div>

  <!-- Широкий график -->
  <div class="lg:col-span-3 bg-white rounded-xl shadow p-6">
    <h3 class="text-lg font-bold mb-4">График продаж</h3>
    <div class="h-48 bg-gray-100 rounded flex items-center justify-center text-gray-400">
      Место для графика
    </div>
  </div>

  <!-- Боковая панель -->
  <div class="bg-white rounded-xl shadow p-6">
    <h3 class="text-lg font-bold mb-4">Последние действия</h3>
    <ul class="space-y-2 text-sm text-gray-600">
      <li>Новый заказ #1234</li>
      <li>Регистрация пользователя</li>
      <li>Обновление товара</li>
    </ul>
  </div>
</div>
```

### 4. 📝 Форма с grid

```html
<form class="grid grid-cols-1 md:grid-cols-2 gap-4 max-w-2xl mx-auto bg-white p-6 rounded-xl shadow">
  <!-- На всю ширину -->
  <div class="md:col-span-2">
    <label class="block text-sm font-medium text-gray-700 mb-1">Название компании</label>
    <input type="text" class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500">
  </div>

  <!-- По колонкам -->
  <div>
    <label class="block text-sm font-medium text-gray-700 mb-1">Имя</label>
    <input type="text" class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500">
  </div>
  <div>
    <label class="block text-sm font-medium text-gray-700 mb-1">Фамилия</label>
    <input type="text" class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500">
  </div>

  <!-- Email на всю ширину -->
  <div class="md:col-span-2">
    <label class="block text-sm font-medium text-gray-700 mb-1">Email</label>
    <input type="email" class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500">
  </div>

  <!-- Город и индекс -->
  <div class="md:col-span-2">
    <label class="block text-sm font-medium text-gray-700 mb-1">Адрес</label>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <input type="text" placeholder="Город" class="md:col-span-2 border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500">
      <input type="text" placeholder="Индекс" class="border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500">
    </div>
  </div>

  <!-- Кнопка -->
  <div class="md:col-span-2 flex justify-end gap-2">
    <button type="button" class="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50">Отмена</button>
    <button type="submit" class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg">Сохранить</button>
  </div>
</form>
```

### 5. 🎴 Карточка с наложением

```html
<div class="grid grid-cols-1 md:grid-cols-2 gap-0 max-w-4xl mx-auto rounded-xl overflow-hidden shadow-xl">
  <!-- Изображение -->
  <div class="relative h-64 md:h-auto">
    <img src="product.jpg" class="absolute inset-0 w-full h-full object-cover" alt="Товар">
  </div>

  <!-- Контент -->
  <div class="bg-white p-8 flex flex-col justify-center">
    <span class="text-xs font-semibold uppercase tracking-wider text-blue-600">Премиум</span>
    <h2 class="mt-2 text-3xl font-bold text-gray-900">Название товара</h2>
    <p class="mt-4 text-gray-600 leading-relaxed">
      Подробное описание товара с преимуществами и особенностями.
    </p>
    <div class="mt-6 flex items-center gap-4">
      <span class="text-3xl font-bold text-gray-900">9 990 ₽</span>
      <button class="bg-blue-600 hover:bg-blue-700 text-white font-medium px-6 py-3 rounded-lg transition">
        Купить
      </button>
    </div>
  </div>
</div>
```

### 6. 📱 Адаптивная сетка с auto-fit

```html
<!-- Автоматическая адаптивная сетка -->
<div class="grid gap-4" style="grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));">
  <div class="bg-white p-6 rounded-lg shadow">Карточка 1</div>
  <div class="bg-white p-6 rounded-lg shadow">Карточка 2</div>
  <div class="bg-white p-6 rounded-lg shadow">Карточка 3</div>
  <div class="bg-white p-6 rounded-lg shadow">Карточка 4</div>
  <div class="bg-white p-6 rounded-lg shadow">Карточка 5</div>
</div>
```

> 💡 **Совет:** `auto-fit` + `minmax()` — мощный приём для адаптивных сеток без медиа-запросов.

## 📊 Шпаргалка: что когда использовать

| Задача | Классы |
| :-- | :-- |
| Включить grid | `grid` |
| N колонок | `grid-cols-3` |
| N строк | `grid-rows-3` |
| Объединить N колонок | `col-span-2` |
| Объединить N строк | `row-span-2` |
| На всю ширину | `col-span-full` |
| Точная позиция | `col-start-2 col-end-5` |
| Направление автозаполнения | `grid-flow-col` |
| Заполнение пустот | `grid-flow-dense` |
| Размер авто-колонок | `auto-cols-fr` |
| Отступы | `gap-4`, `gap-x-4`, `gap-y-4` |
| Выравнивание элементов | `place-items-center` |
| Выравнивание сетки | `place-content-center` |
| Один элемент иначе | `justify-self-end`, `self-end` |
| Кастомные колонки | `grid-cols-[200px_1fr_200px]` |
| Адаптивная сетка | `grid-cols-1 md:grid-cols-2 lg:grid-cols-4` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Grid без `grid-cols-*`

```html
<!-- ❌ Плохо: все элементы в одну колонку -->
<div class="grid gap-4">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>

<!-- ✅ Хорошо: указываем количество колонок -->
<div class="grid grid-cols-3 gap-4">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>
```

### ❌ Ошибка 2: `col-span` больше, чем колонок в сетке

```html
<!-- ❌ Плохо: col-span-4 в сетке из 3 колонок -->
<div class="grid grid-cols-3 gap-4">
  <div class="col-span-4">Не работает как ожидается</div>
</div>

<!-- ✅ Хорошо: span соответствует сетке -->
<div class="grid grid-cols-3 gap-4">
  <div class="col-span-3">На всю ширину</div>
</div>
```

### ❌ Ошибка 3: Grid для простых компонентов

```html
<!-- ❌ Плохо: избыточно для кнопки с иконкой -->
<div class="grid grid-cols-[auto_1fr] gap-2">
  <span>🔔</span>
  <span>Уведомления</span>
</div>

<!-- ✅ Хорошо: flexbox проще -->
<div class="flex items-center gap-2">
  <span>🔔</span>
  <span>Уведомления</span>
</div>
```

### ❌ Ошибка 4: Забывают про `min-h` для grid с `h-` у родителя

```html
<!-- ❌ Плохо: grid может схлопнуться -->
<div class="grid grid-cols-3 gap-4">
  <div class="bg-blue-500">1</div>
</div>

<!-- ✅ Хорошо: указываем высоту -->
<div class="grid grid-cols-3 gap-4 min-h-64">
  <div class="bg-blue-500">1</div>
</div>
```

### ❌ Ошибка 5: `gap` вместо `padding` для внешних отступов

```html
<!-- ❌ Плохо: gap не создаёт отступов по краям -->
<div class="grid grid-cols-3 gap-4">
  <div class="bg-blue-500">1</div>
</div>

<!-- ✅ Хорошо: gap для внутренних + padding для внешних -->
<div class="grid grid-cols-3 gap-4 p-4">
  <div class="bg-blue-500">1</div>
</div>
```

### ❌ Ошибка 6: Забывают про responsive

```html
<!-- ❌ Плохо: 4 колонки на мобильных -->
<div class="grid grid-cols-4 gap-4">
  <div>1</div>
  <div>2</div>
  <div>3</div>
  <div>4</div>
</div>

<!-- ✅ Хорошо: адаптивная сетка -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
  <div>1</div>
  <div>2</div>
  <div>3</div>
  <div>4</div>
</div>
```

### ❌ Ошибка 7: `grid-flow-col` без явных строк

```html
<!-- ❌ Плохо: все элементы в одну строку -->
<div class="grid grid-flow-col gap-2">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>

<!-- ✅ Хорошо: указываем количество строк -->
<div class="grid grid-rows-2 grid-flow-col gap-2">
  <div>1</div>
  <div>2</div>
  <div>3</div>
  <div>4</div>
</div>
```

## 🎯 Что дальше?

Теперь вы полностью владеете Grid! Но макет — это не только расположение элементов. Следующий важный аспект — **отступы и размеры**.

**Следующий шаг:** [📏 Отступы в Tailwind CSS](spacing.md) — изучим работу с padding, margin и пространством между элементами.

---

> 💬 **Упражнение:** создайте dashboard с 6 виджетами: один большой (на 2 колонки и 2 строки), два средних (на 2 колонки) и три обычных. Используйте grid с адаптивной сеткой (1 колонка на мобильных, 4 на десктопе).

---




<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: layout\sizing.md -->
<!-- ═══════════════════════════════════════════════════════════ -->

# 📐 Размеры в Tailwind CSS

> **Полное руководство по управлению размерами:** от ширины и высоты до aspect-ratio и адаптивных размеров

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Освоите все утилиты для управления шириной и высотой
- ✅ Научитесь использовать min/max значения для гибких размеров
- ✅ Поймёте разницу между фиксированными, процентными и viewport-размерами
- ✅ Освоите `aspect-ratio` для пропорциональных элементов
- ✅ Научитесь создавать адаптивные размеры
- ✅ Поймёте, когда использовать `size-*` вместо `w-*` + `h-*`
- ✅ Избежите типичных ошибок при работе с размерами

## 📏 Ширина: `w-{size}`

Tailwind использует **единую шкалу** для размеров (как и для отступов):

### Фиксированные размеры

| Класс | CSS | Визуально |
| :-- | :-- | :-- |
| `w-0` | `width: 0px` | Нет ширины |
| `w-px` | `width: 1px` | 1 пиксель |
| `w-0.5` | `width: 0.125rem` (2px) | Очень узкий |
| `w-1` | `width: 0.25rem` (4px) | Узкий |
| `w-4` | `width: 1rem` (16px) | Средний |
| `w-8` | `width: 2rem` (32px) | Широкий |
| `w-16` | `width: 4rem` (64px) | Очень широкий |
| `w-32` | `width: 8rem` (128px) | Огромный |
| `w-64` | `width: 16rem` (256px) | Максимальный фиксированный |

### Дробные размеры (проценты)

| Класс | CSS | Применение |
| :-- | :-- | :-- |
| `w-1/2` | `width: 50%` | Половина родителя |
| `w-1/3` | `width: 33.333%` | Треть родителя |
| `w-2/3` | `width: 66.667%` | Две трети |
| `w-1/4` | `width: 25%` | Четверть |
| `w-3/4` | `width: 75%` | Три четверти |
| `w-1/5` | `width: 20%` | Пятая часть |
| `w-2/5` | `width: 40%` | Две пятых |
| `w-3/5` | `width: 60%` | Три пятых |
| `w-4/5` | `width: 80%` | Четыре пятых |
| `w-full` | `width: 100%` | Вся ширина родителя |
| `w-screen` | `width: 100vw` | Вся ширина viewport |
| `w-min` | `width: min-content` | По содержимому (мин) |
| `w-max` | `width: max-content` | По содержимому (макс) |
| `w-fit` | `width: fit-content` | Автоматически по содержимому |

```html
<!-- Фиксированная ширина -->
<div class="w-64 bg-blue-500">Ширина 256px</div>

<!-- Процентная ширина -->
<div class="w-1/2 bg-green-500">Половина родителя</div>

<!-- На всю ширину -->
<div class="w-full bg-purple-500">На всю ширину</div>

<!-- По содержимому -->
<div class="w-fit bg-orange-500">Подстроится под текст</div>
```

### Viewport-размеры

```html
<!-- На всю ширину экрана -->
<section class="w-screen bg-gray-900 text-white p-8">
  Hero на всю ширину экрана
</section>
```

## 📐 Минимальная ширина: `min-w-{size}`

| Класс | CSS | Применение |
| :-- | :-- | :-- |
| `min-w-0` | `min-width: 0px` | Сброс минимальной ширины |
| `min-w-full` | `min-width: 100%` | Минимум — вся ширина родителя |
| `min-w-min` | `min-width: min-content` | По минимальному содержимому |
| `min-w-max` | `min-width: max-content` | По максимальному содержимому |
| `min-w-fit` | `min-width: fit-content` | Автоматически |
| `min-w-{size}` | `min-width: {size}` | Фиксированное значение |

```html
<!-- Элемент не может быть уже 200px -->
<div class="min-w-[200px] w-1/2 bg-blue-500">
  Минимум 200px, но может растянуться
</div>

<!-- Кнопка не сжимается -->
<button class="min-w-max bg-blue-600 text-white px-4 py-2 rounded">
  Текст кнопки не переносится
</button>
```

> 💡 **Важно:** `min-w-0` критически важен в flex-контейнерах для работы `truncate` и переполнения текста.

## 📏 Максимальная ширина: `max-w-{size}`

### Предустановленные значения

| Класс | CSS | Применение |
| :-- | :-- | :-- |
| `max-w-0` | `max-width: 0rem` | Нет ширины |
| `max-w-none` | `max-width: none` | Без ограничений |
| `max-w-xs` | `max-width: 20rem` (320px) | Очень узкий |
| `max-w-sm` | `max-width: 24rem` (384px) | Узкий |
| `max-w-md` | `max-width: 28rem` (448px) | Средний |
| `max-w-lg` | `max-width: 32rem` (512px) | Широкий |
| `max-w-xl` | `max-width: 36rem` (576px) | Очень широкий |
| `max-w-2xl` | `max-width: 42rem` (672px) | Широкий контент |
| `max-w-3xl` | `max-width: 48rem` (768px) | Контент статей |
| `max-w-4xl` | `max-width: 56rem` (896px) | Широкие статьи |
| `max-w-5xl` | `max-width: 64rem` (1024px) | Очень широкий |
| `max-w-6xl` | `max-width: 72rem` (1152px) | Огромный |
| `max-w-7xl` | `max-width: 80rem` (1280px) | Максимальный |
| `max-w-full` | `max-width: 100%` | 100% родителя |
| `max-w-min` | `max-width: min-content` | По минимальному содержимому |
| `max-w-max` | `max-width: max-content` | По максимальному содержимому |
| `max-w-fit` | `max-width: fit-content` | Автоматически |
| `max-w-prose` | `max-width: 65ch` | Оптимально для чтения |
| `max-w-screen-sm` | `max-width: 640px` | Breakpoint sm |
| `max-w-screen-md` | `max-width: 768px` | Breakpoint md |
| `max-w-screen-lg` | `max-width: 1024px` | Breakpoint lg |
| `max-w-screen-xl` | `max-width: 1280px` | Breakpoint xl |
| `max-w-screen-2xl` | `max-width: 1536px` | Breakpoint 2xl |

```html
<!-- Контейнер с максимальной шириной -->
<div class="max-w-7xl mx-auto px-4">
  Контент не шире 1280px, центрирован
</div>

<!-- Статья с оптимальной шириной для чтения -->
<article class="max-w-prose mx-auto">
  Длинный текст статьи, комфортный для чтения
</article>

<!-- Модальное окно -->
<div class="max-w-md mx-auto bg-white p-6 rounded-lg shadow-lg">
  Модальное окно шириной до 448px
</div>
```

> 💡 **max-w-prose** — это **65ch** (65 символов), оптимальная ширина для чтения длинного текста по исследованиям читаемости.

## 📐 Высота: `h-{size}`

Синтаксис идентичен ширине:

### Фиксированные размеры

```html
<div class="h-16 bg-blue-500">Высота 64px</div>
<div class="h-32 bg-green-500">Высота 128px</div>
<div class="h-64 bg-purple-500">Высота 256px</div>
```

### Дробные и viewport

| Класс | CSS | Применение |
| :-- | :-- | :-- |
| `h-1/2` | `height: 50%` | Половина родителя |
| `h-1/3` | `height: 33.333%` | Треть |
| `h-2/3` | `height: 66.667%` | Две трети |
| `h-1/4` | `height: 25%` | Четверть |
| `h-3/4` | `height: 75%` | Три четверти |
| `h-1/5` | `height: 20%` | Пятая часть |
| `h-full` | `height: 100%` | Вся высота родителя |
| `h-screen` | `height: 100vh` | Вся высота viewport |
| `h-svh` | `height: 100svh` | Small viewport height (мобильные) |
| `h-lvh` | `height: 100lvh` | Large viewport height |
| `h-dvh` | `height: 100dvh` | Dynamic viewport height |
| `h-min` | `height: min-content` | По содержимому (мин) |
| `h-max` | `height: max-content` | По содержимому (макс) |
| `h-fit` | `height: fit-content` | Автоматически |

```html
<!-- Hero на всю высоту экрана -->
<section class="h-screen bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center">
  <h1 class="text-5xl font-bold text-white">Добро пожаловать!</h1>
</section>

<!-- Половина высоты родителя -->
<div class="h-64 relative">
  <div class="h-1/2 bg-blue-500">Половина высоты</div>
</div>
```

> 💡 **svh/lvh/dvh** — современные viewport-единицы, которые корректно работают на мобильных с адресной строкой. Используйте `dvh` для мобильных приложений.

## 📏 Минимальная высота: `min-h-{size}`

| Класс | CSS | Применение |
| :-- | :-- | :-- |
| `min-h-0` | `min-height: 0px` | Сброс |
| `min-h-full` | `min-height: 100%` | 100% родителя |
| `min-h-screen` | `min-height: 100vh` | 100vh |
| `min-h-svh` | `min-height: 100svh` | Small viewport |
| `min-h-lvh` | `min-height: 100lvh` | Large viewport |
| `min-h-dvh` | `min-height: 100dvh` | Dynamic viewport |
| `min-h-min` | `min-height: min-content` | По содержимому |
| `min-h-max` | `min-height: max-content` | По содержимому |
| `min-h-fit` | `min-height: fit-content` | Автоматически |

```html
<!-- Страница минимум на весь экран, но может расти -->
<main class="min-h-screen bg-gray-50">
  <!-- Контент может быть длиннее экрана -->
</main>

<!-- Input не сжимается -->
<input class="min-h-[44px] w-full border rounded-lg px-4">
```

## 📐 Максимальная высота: `max-h-{size}`

| Класс | CSS |
| :-- | :-- |
| `max-h-full` | `max-height: 100%` |
| `max-h-screen` | `max-height: 100vh` |
| `max-h-svh` | `max-height: 100svh` |
| `max-h-lvh` | `max-height: 100lvh` |
| `max-h-dvh` | `max-height: 100dvh` |
| `max-h-min` | `max-height: min-content` |
| `max-h-max` | `max-height: max-content` |
| `max-h-fit` | `max-height: fit-content` |
| `max-h-{size}` | Фиксированные значения |

```html
<!-- Контейнер со скроллом -->
<div class="max-h-64 overflow-y-auto border rounded-lg p-4">
  <!-- Длинный список, который будет скроллиться -->
  <ul class="space-y-2">
    <li>Пункт 1</li>
    <li>Пункт 2</li>
    <!-- ... много пунктов -->
  </ul>
</div>

<!-- Модальное окно не выше экрана -->
<div class="max-h-[90vh] overflow-y-auto bg-white rounded-lg p-6">
  <!-- Длинный контент -->
</div>
```

## 📦 Size: `size-{size}`

`size-*` — это **сокращение** для одновременной установки `width` и `height`:

```html
<!-- ❌ Длинная запись -->
<div class="w-16 h-16 bg-blue-500">Квадрат</div>

<!-- ✅ Короткая запись -->
<div class="size-16 bg-blue-500">Квадрат</div>
```

### Доступные значения

Аналогичны `w-*` и `h-*`:

```html
<!-- Фиксированные размеры -->
<div class="size-8 bg-blue-500">32×32</div>
<div class="size-16 bg-blue-500">64×64</div>
<div class="size-32 bg-blue-500">128×128</div>

<!-- Full -->
<div class="size-full bg-blue-500">100%×100%</div>
```

> 💡 **Когда использовать:** для квадратных элементов (иконки, аватары, кнопки-иконки). Для прямоугольников используйте `w-*` и `h-*` отдельно.

## 🖼️ Aspect Ratio: `aspect-{ratio}`

Управляет **соотношением сторон** элемента:

| Класс | CSS | Применение |
| :-- | :-- | :-- |
| `aspect-auto` | `aspect-ratio: auto` | По содержимому (по умолчанию) |
| `aspect-square` | `aspect-ratio: 1 / 1` | Квадрат |
| `aspect-video` | `aspect-ratio: 16 / 9` | Видео |

```html
<!-- Квадратное изображение -->
<div class="aspect-square w-64 bg-blue-500">
  <img src="photo.jpg" class="w-full h-full object-cover" alt="">
</div>

<!-- Видео 16:9 -->
<div class="aspect-video w-full bg-gray-900">
  <iframe src="..." class="w-full h-full" frameborder="0"></iframe>
</div>
```

### Кастомные соотношения

```html
<!-- 4:3 (старое ТВ) -->
<div class="aspect-[4/3] w-full bg-gray-200">
  Контент в формате 4:3
</div>

<!-- 21:9 (ультраширокий) -->
<div class="aspect-[21/9] w-full bg-gray-200">
  Ультраширокий формат
</div>

<!-- 2:3 (портрет) -->
<div class="aspect-[2/3] w-64 bg-gray-200">
  Портретная ориентация
</div>

<!-- 3:2 (фото) -->
<div class="aspect-[3/2] w-full bg-gray-200">
  Фотографический формат
</div>
```

## 🎯 Практические паттерны

### 1. 🎴 Карточка товара с квадратным изображением

```html
<div class="bg-white rounded-xl shadow-md overflow-hidden max-w-sm">
  <!-- Квадратное изображение -->
  <div class="aspect-square bg-gray-100">
    <img
      src="product.jpg"
      alt="Товар"
      class="w-full h-full object-cover"
    >
  </div>

  <div class="p-4">
    <h3 class="font-bold text-lg">Название товара</h3>
    <p class="text-gray-600 text-sm mt-1">Описание</p>
    <div class="mt-3 flex items-center justify-between">
      <span class="text-xl font-bold">2 990 ₽</span>
      <button class="bg-blue-600 text-white px-4 py-2 rounded-lg">
        Купить
      </button>
    </div>
  </div>
</div>
```

### 2. 🎬 Hero-секция на весь экран

```html
<section class="min-h-screen bg-gradient-to-br from-blue-600 to-purple-700 flex items-center justify-center p-4">
  <div class="max-w-4xl text-center">
    <h1 class="text-4xl sm:text-5xl md:text-6xl font-bold text-white mb-6">
      Создавайте красивые интерфейсы
    </h1>
    <p class="text-lg sm:text-xl text-blue-100 mb-8 max-w-2xl mx-auto">
      Utility-first CSS фреймворк для быстрой разработки
    </p>
    <div class="flex flex-col sm:flex-row gap-4 justify-center">
      <button class="bg-white text-blue-600 font-semibold px-8 py-3 rounded-lg">
        Начать
      </button>
      <button class="border-2 border-white text-white font-semibold px-8 py-3 rounded-lg">
        Документация
      </button>
    </div>
  </div>
</section>
```

### 3. 🖼️ Галерея с aspect-ratio

```html
<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
  <div class="aspect-square overflow-hidden rounded-lg">
    <img src="photo1.jpg" class="w-full h-full object-cover hover:scale-110 transition-transform" alt="">
  </div>
  <div class="aspect-square overflow-hidden rounded-lg">
    <img src="photo2.jpg" class="w-full h-full object-cover hover:scale-110 transition-transform" alt="">
  </div>
  <div class="aspect-square overflow-hidden rounded-lg">
    <img src="photo3.jpg" class="w-full h-full object-cover hover:scale-110 transition-transform" alt="">
  </div>
  <div class="aspect-square overflow-hidden rounded-lg">
    <img src="photo4.jpg" class="w-full h-full object-cover hover:scale-110 transition-transform" alt="">
  </div>
</div>
```

### 4. 📊 Dashboard с виджетами

```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
  <!-- Виджет статистики -->
  <div class="bg-white rounded-xl shadow-sm border p-6 min-h-[140px]">
    <div class="flex items-center justify-between">
      <div>
        <p class="text-sm text-gray-500">Пользователи</p>
        <p class="text-3xl font-bold mt-1">12 345</p>
      </div>
      <div class="size-12 bg-blue-100 rounded-full flex items-center justify-center">
        <svg class="size-6 text-blue-600" fill="currentColor" viewBox="0 0 24 24">
          <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>
        </svg>
      </div>
    </div>
    <p class="text-sm text-green-600 mt-2">+12% за месяц</p>
  </div>

  <!-- Повторить для других виджетов -->
</div>
```

### 5. 🎥 Видео-плеер с aspect-ratio

```html
<div class="max-w-4xl mx-auto">
  <div class="aspect-video bg-black rounded-xl overflow-hidden shadow-2xl">
    <video
      class="w-full h-full object-cover"
      controls
      poster="poster.jpg"
    >
      <source src="video.mp4" type="video/mp4">
    </video>
  </div>
  <div class="mt-4">
    <h2 class="text-2xl font-bold">Название видео</h2>
    <p class="text-gray-600 mt-1">Описание видео</p>
  </div>
</div>
```

### 6. 👤 Аватары разных размеров

```html
<div class="flex items-center gap-4">
  <!-- XS -->
  <div class="size-8 rounded-full bg-blue-500 flex items-center justify-center text-white text-xs font-bold">
    A
  </div>

  <!-- SM -->
  <div class="size-10 rounded-full bg-green-500 flex items-center justify-center text-white text-sm font-bold">
    B
  </div>

  <!-- MD -->
  <div class="size-12 rounded-full bg-purple-500 flex items-center justify-center text-white font-bold">
    C
  </div>

  <!-- LG -->
  <div class="size-16 rounded-full bg-orange-500 flex items-center justify-center text-white text-xl font-bold">
    D
  </div>

  <!-- XL -->
  <div class="size-20 rounded-full bg-red-500 flex items-center justify-center text-white text-2xl font-bold">
    E
  </div>
</div>
```

### 7. 📋 Таблица с max-height и скроллом

```html
<div class="bg-white rounded-xl shadow-sm border overflow-hidden">
  <div class="px-6 py-4 border-b">
    <h3 class="font-bold text-lg">Последние действия</h3>
  </div>

  <div class="max-h-96 overflow-y-auto">
    <ul class="divide-y divide-gray-200">
      <li class="px-6 py-3 hover:bg-gray-50">
        <p class="font-medium">Новый заказ #1234</p>
        <p class="text-sm text-gray-500">2 минуты назад</p>
      </li>
      <li class="px-6 py-3 hover:bg-gray-50">
        <p class="font-medium">Регистрация пользователя</p>
        <p class="text-sm text-gray-500">5 минут назад</p>
      </li>
      <!-- Много пунктов -->
    </ul>
  </div>
</div>
```

### 8. 📱 Адаптивный контейнер

```html
<!-- Контейнер с разной шириной на разных экранах -->
<div class="w-full max-w-sm sm:max-w-md md:max-w-lg lg:max-w-xl xl:max-w-2xl mx-auto px-4">
  <h2 class="text-2xl font-bold mb-4">Адаптивный контейнер</h2>
  <p class="text-gray-600">
    Ширина контейнера меняется в зависимости от размера экрана
  </p>
</div>
```

## 📊 Шпаргалка: что когда использовать

| Задача | Классы |
| :-- | :-- |
| Фиксированная ширина | `w-64`, `w-32` |
| Процентная ширина | `w-1/2`, `w-1/3`, `w-full` |
| Ширина viewport | `w-screen` |
| Максимальная ширина | `max-w-7xl`, `max-w-prose` |
| Минимальная ширина | `min-w-[200px]`, `min-w-max` |
| Фиксированная высота | `h-64`, `h-32` |
| Высота viewport | `h-screen`, `h-dvh` |
| Минимальная высота | `min-h-screen` |
| Максимальная высота | `max-h-64`, `max-h-screen` |
| Квадратный элемент | `size-16`, `size-full` |
| Соотношение сторон | `aspect-square`, `aspect-video` |
| Кастомное соотношение | `aspect-[4/3]`, `aspect-[21/9]` |
| По содержимому | `w-fit`, `h-fit`, `w-max`, `h-max` |
| Центрирование контейнера | `max-w-7xl mx-auto` |
| Оптимальная ширина текста | `max-w-prose` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: `h-full` без высоты у родителя

```html
<!-- ❌ Плохо: h-full не работает, если у родителя нет высоты -->
<div>
  <div class="h-full bg-blue-500">Не работает</div>
</div>

<!-- ✅ Хорошо: у родителя указана высота -->
<div class="h-64 relative">
  <div class="h-full bg-blue-500">Работает</div>
</div>
```

### ❌ Ошибка 2: Забывают `min-w-0` в flex для truncate

```html
<!-- ❌ Плохо: truncate не работает -->
<div class="flex">
  <div class="flex-1 truncate">
    Очень-очень-длинный-текст
  </div>
</div>

<!-- ✅ Хорошо: min-w-0 позволяет сжиматься -->
<div class="flex">
  <div class="flex-1 min-w-0 truncate">
    Очень-очень-длинный-текст
  </div>
</div>
```

### ❌ Ошибка 3: `w-screen` с горизонтальным скроллом

```html
<!-- ❌ Плохо: может появиться горизонтальный скролл из-за scrollbar -->
<div class="w-screen bg-blue-500">
  На всю ширину экрана
</div>

<!-- ✅ Хорошо: используйте w-full для контейнеров внутри body -->
<div class="w-full bg-blue-500">
  На всю ширину родителя
</div>
```

### ❌ Ошибка 4: `h-screen` на мобильных с адресной строкой

```html
<!-- ❌ Плохо: на мобильных адресная строка "съедает" часть высоты -->
<section class="h-screen">
  Hero-секция
</section>

<!-- ✅ Хорошо: используйте dvh для мобильных -->
<section class="h-dvh">
  Hero-секция корректно работает на мобильных
</section>
```

### ❌ Ошибка 5: `aspect-ratio` без ширины

```html
<!-- ❌ Плохо: aspect-ratio не работает без ширины -->
<div class="aspect-video bg-blue-500">
  Не работает
</div>

<!-- ✅ Хорошо: указываем ширину -->
<div class="aspect-video w-full bg-blue-500">
  Работает
</div>
```

### ❌ Ошибка 6: Фиксированная ширина для адаптивного контента

```html
<!-- ❌ Плохо: на мобильных не влезет -->
<div class="w-[800px]">
  Контент
</div>

<!-- ✅ Хорошо: адаптивная ширина с максимумом -->
<div class="w-full max-w-4xl mx-auto px-4">
  Контент
</div>
```

### ❌ Ошибка 7: Забывают `overflow` с `max-h`

```html
<!-- ❌ Плохо: контент выйдет за пределы, но не будет скролла -->
<div class="max-h-64">
  <!-- Длинный контент -->
</div>

<!-- ✅ Хорошо: добавляем overflow -->
<div class="max-h-64 overflow-y-auto">
  <!-- Длинный контент со скроллом -->
</div>
```

### ❌ Ошибка 8: `size-*` для прямоугольников

```html
<!-- ❌ Плохо: size устанавливает одинаковые width и height -->
<div class="size-64 bg-blue-500">
  Получится квадрат, а не прямоугольник
</div>

<!-- ✅ Хорошо: для прямоугольников используйте w-* и h-* -->
<div class="w-64 h-32 bg-blue-500">
  Прямоугольник 256×128
</div>
```

### ❌ Ошибка 9: `max-w-prose` для UI-элементов

```html
<!-- ❌ Плохо: max-w-prose (65ch) слишком узкий для UI -->
<div class="max-w-prose bg-white p-6 rounded-lg shadow">
  <!-- Карточка с UI-элементами -->
</div>

<!-- ✅ Хорошо: max-w-prose для текста, max-w-{size} для UI -->
<article class="max-w-prose">
  <!-- Статья с длинным текстом -->
</article>

<div class="max-w-md bg-white p-6 rounded-lg shadow">
  <!-- Карточка с UI -->
</div>
```

### ❌ Ошибка 10: Забывают про responsive размеры

```html
<!-- ❌ Плохо: одинаковый размер на всех экранах -->
<div class="w-64 h-64 bg-blue-500">
  Фиксированный размер
</div>

<!-- ✅ Хорошо: адаптивные размеры -->
<div class="w-full sm:w-1/2 lg:w-1/3 h-64 md:h-96 bg-blue-500">
  Адаптивный размер
</div>
```

## 🎯 Что дальше?

Поздравляем! Вы полностью освоили секцию **Layout** — от flexbox и grid до отступов и размеров. Теперь вы можете создавать любые макеты.

### Что вы изучили в секции Layout

- 📐 **Flexbox** — одномерная раскладка
- 🔲 **Grid** — двумерная раскладка
- 📏 **Отступы** — padding, margin, space, gap
- 📐 **Размеры** — width, height, min/max, aspect-ratio

### Следующий шаг

Теперь переходим к основам — установка и конфигурация Tailwind CSS.

**Следующий раздел:** [📦 Установка Tailwind CSS](../basics/installation.md) — научимся подключать Tailwind в различные проекты.

---

---




<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: layout\spacing.md -->
<!-- ═══════════════════════════════════════════════════════════ -->

# 📏 Отступы в Tailwind CSS

> **Полное руководство по работе с отступами:** от padding и margin до space-between и логических свойств для RTL

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Освоите всю шкалу отступов Tailwind (от 0 до 96)
- ✅ Научитесь управлять padding со всех сторон
- ✅ Поймёте разницу между padding, margin и space
- ✅ Освоите отрицательные margin для сложных макетов
- ✅ Узнаете про логические свойства (ps, pe, ms, me) для RTL
- ✅ Создадите консистентные spacing-системы
- ✅ Избежите типичных ошибок при работе с отступами

## 📐 Шкала отступов

Tailwind использует **единую шкалу** для padding и margin. Все значения основаны на rem (1rem = 16px по умолчанию):

| Класс | Rem | Px | Визуально |
| :-- | :-- | :-- | :-- |
| `0` | `0rem` | `0px` | Без отступа |
| `px` | `1px` | `1px` | 1 пиксель |
| `0.5` | `0.125rem` | `2px` | Очень маленький |
| `1` | `0.25rem` | `4px` | Маленький |
| `1.5` | `0.375rem` | `6px` | |
| `2` | `0.5rem` | `8px` | Средний маленький |
| `2.5` | `0.625rem` | `10px` | |
| `3` | `0.75rem` | `12px` | Средний |
| `3.5` | `0.875rem` | `14px` | |
| `4` | `1rem` | `16px` | Стандартный |
| `5` | `1.25rem` | `20px` | |
| `6` | `1.5rem` | `24px` | Большой |
| `7` | `1.75rem` | `28px` | |
| `8` | `2rem` | `32px` | Очень большой |
| `9` | `2.25rem` | `36px` | |
| `10` | `2.5rem` | `40px` | Огромный |
| `11` | `2.75rem` | `44px` | |
| `12` | `3rem` | `48px` | |
| `14` | `3.5rem` | `56px` | |
| `16` | `4rem` | `64px` | |
| `20` | `5rem` | `80px` | |
| `24` | `6rem` | `96px` | |
| `28` | `7rem` | `112px` | |
| `32` | `8rem` | `128px` | |
| `36` | `9rem` | `144px` | |
| `40` | `10rem` | `160px` | |
| `44` | `11rem` | `176px` | |
| `48` | `12rem` | `192px` | |
| `52` | `13rem` | `208px` | |
| `56` | `14rem` | `224px` | |
| `60` | `15rem` | `240px` | |
| `64` | `16rem` | `256px` | |
| `72` | `18rem` | `288px` | |
| `80` | `20rem` | `320px` | |
| `96` | `24rem` | `384px` | Максимальный |

> 💡 **Правило:** `p-4` = `1rem` = `16px`. Эта шкала используется везде: padding, margin, width, height, gap, top/right/bottom/left.

## 📦 Padding: `p-{size}`

Padding — внутренний отступ **внутри** элемента, между содержимым и границей.

### Со всех сторон

```html
<!-- Одинаковый отступ со всех сторон -->
<div class="p-4 bg-blue-500 text-white">
  Отступ 16px со всех сторон
</div>

<!-- Без отступов -->
<div class="p-0 bg-blue-500 text-white">
  Без отступов
</div>
```

### По осям

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `px-{size}` | `padding-left` + `padding-right` | Горизонтальные отступы |
| `py-{size}` | `padding-top` + `padding-bottom` | Вертикальные отступы |

```html
<!-- Горизонтальные отступы -->
<div class="px-8 py-2 bg-blue-500 text-white">
  Большие горизонтальные, маленькие вертикальные
</div>

<!-- Типичная кнопка -->
<button class="px-4 py-2 bg-blue-600 text-white rounded">
  Кнопка
</button>
```

### По сторонам

| Класс | CSS |
| :-- | :-- |
| `pt-{size}` | `padding-top` |
| `pr-{size}` | `padding-right` |
| `pb-{size}` | `padding-bottom` |
| `pl-{size}` | `padding-left` |

```html
<!-- Отступ только сверху -->
<div class="pt-8 bg-blue-500 text-white">
  Отступ только сверху
</div>

<!-- Асимметричные отступы -->
<div class="pl-8 pr-4 py-2 bg-blue-500 text-white">
  Больше слева, меньше справа
</div>
```

### Логические свойства (для RTL)

Если ваш сайт поддерживает языки с письмом справа налево (арабский, иврит), используйте логические свойства:

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `ps-{size}` | `padding-inline-start` | Начальная сторона (слева в LTR) |
| `pe-{size}` | `padding-inline-end` | Конечная сторона (справа в LTR) |

```html
<!-- В LTR: отступ слева -->
<!-- В RTL: отступ справа -->
<div class="ps-4 pe-2 bg-blue-500 text-white">
  Логический отступ
</div>
```

## 🧲 Margin: `m-{size}`

Margin — внешний отступ **между** элементами.

### Синтаксис идентичен padding

```html
<!-- Со всех сторон -->
<div class="m-4 bg-blue-500 text-white">
  Отступ 16px снаружи
</div>

<!-- По осям -->
<div class="mx-auto bg-blue-500 text-white max-w-md">
  Центрирование через mx-auto
</div>

<!-- По сторонам -->
<div class="mt-8 mb-4 bg-blue-500 text-white">
  Отступ сверху и снизу
</div>
```

### Центрирование блока

```html
<!-- Классический способ центрирования -->
<div class="mx-auto max-w-4xl">
  Центрированный контент
</div>
```

### Отрицательные margin

Tailwind поддерживает отрицательные значения для создания сложных макетов:

| Класс | CSS |
| :-- | :-- |
| `-m-{size}` | Отрицательный margin со всех сторон |
| `-mx-{size}` | Отрицательный горизонтальный |
| `-my-{size}` | Отрицательный вертикальный |
| `-mt-{size}` | Отрицательный сверху |
| `-mr-{size}` | Отрицательный справа |
| `-mb-{size}` | Отрицательный снизу |
| `-ml-{size}` | Отрицательный слева |

```html
<!-- Карточка "выходит" за границы контейнера -->
<div class="max-w-2xl mx-auto p-8">
  <div class="bg-blue-500 p-8 -mx-8 text-white">
    Карточка выходит за границы
  </div>
</div>

<!-- Наложение элементов -->
<div class="relative">
  <img src="photo.jpg" class="w-full h-64 object-cover">
  <div class="bg-white p-6 -mt-12 mx-4 rounded-lg shadow-lg relative">
    Карточка поверх изображения
  </div>
</div>
```

> ⚠️ **Используйте отрицательные margin с осторожностью!** Это может сломать layout. Часто лучше использовать `transform: translate` или absolute positioning.

### Логические свойства для margin

| Класс | CSS |
| :-- | :-- |
| `ms-{size}` | `margin-inline-start` |
| `me-{size}` | `margin-inline-end` |

## 🕳️ Space between: `space-x-{size}` и `space-y-{size}`

`space` добавляет отступы **между дочерними элементами** (но не по краям контейнера):

### Вертикальные отступы

```html
<div class="space-y-4">
  <div class="bg-blue-500 p-4 text-white">Элемент 1</div>
  <div class="bg-blue-500 p-4 text-white">Элемент 2</div>
  <div class="bg-blue-500 p-4 text-white">Элемент 3</div>
</div>
```

### Горизонтальные отступы

```html
<div class="flex space-x-4">
  <button class="bg-blue-500 text-white px-4 py-2 rounded">Кнопка 1</button>
  <button class="bg-blue-500 text-white px-4 py-2 rounded">Кнопка 2</button>
  <button class="bg-blue-500 text-white px-4 py-2 rounded">Кнопка 3</button>
</div>
```

### Reverse (для RTL)

```html
<!-- Для RTL языков -->
<div class="flex space-x-reverse space-x-4">
  <div>Элемент 1</div>
  <div>Элемент 2</div>
</div>
```

### `space` vs `gap`

| Критерий | `space-x/y` | `gap` |
| :-- | :-- | :-- |
| **Работает с** | Flexbox | Flexbox и Grid |
| **Реализация** | `> * + *` (margin) | Нативный CSS |
| **`flex-wrap`** | ❌ Лишние отступы | ✅ Корректно |
| **Рекомендация** | 🟡 Legacy | ✅ Современный подход |

```html
<!-- ❌ space-x с flex-wrap — лишние отступы -->
<div class="flex flex-wrap space-x-4">
  <div class="bg-blue-500 p-4">1</div>
  <div class="bg-blue-500 p-4">2</div>
  <div class="bg-blue-500 p-4">3</div>
</div>

<!-- ✅ gap с flex-wrap — корректно -->
<div class="flex flex-wrap gap-4">
  <div class="bg-blue-500 p-4">1</div>
  <div class="bg-blue-500 p-4">2</div>
  <div class="bg-blue-500 p-4">3</div>
</div>
```

> 💡 **Правило:** используйте `gap` для flex и grid. `space-x/y` оставьте для случаев, когда нельзя использовать gap (старые браузеры).

## 🎯 Arbitrary значения

Если стандартной шкалы недостаточно:

```html
<!-- Точные значения в px -->
<div class="p-[23px]">Кастомный padding</div>

<!-- В rem -->
<div class="m-[1.75rem]">Кастомный margin</div>

<!-- В процентах -->
<div class="p-[15%]">Процентный padding</div>

<!-- Отрицательные arbitrary -->
<div class="-mt-[100px]">Кастомный отрицательный margin</div>
```

## 📱 Responsive отступы

```html
<!-- Mobile-first: маленькие → большие -->
<div class="p-4 sm:p-6 md:p-8 lg:p-12">
  Адаптивные отступы
</div>

<!-- Разные отступы по осям -->
<div class="px-4 py-8 md:px-8 md:py-12 lg:px-16">
  Адаптивные отступы по осям
</div>
```

## 🎨 Практические паттерны

### 1. 🎴 Стандартная карточка

```html
<div class="bg-white rounded-xl shadow-md overflow-hidden max-w-sm">
  <img src="product.jpg" class="w-full h-48 object-cover" alt="Товар">
  <div class="p-6">
    <h3 class="text-xl font-bold mb-2">Название товара</h3>
    <p class="text-gray-600 text-sm mb-4">
      Описание товара с подробной информацией о характеристиках.
    </p>
    <div class="flex items-center justify-between">
      <span class="text-2xl font-bold">2 990 ₽</span>
      <button class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg transition">
        В корзину
      </button>
    </div>
  </div>
</div>
```

### 2. 📝 Форма с консистентными отступами

```html
<form class="bg-white rounded-lg shadow-md p-6 max-w-md space-y-4">
  <h2 class="text-2xl font-bold mb-6">Регистрация</h2>

  <div class="space-y-2">
    <label class="block text-sm font-medium text-gray-700">Имя</label>
    <input type="text" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500">
  </div>

  <div class="space-y-2">
    <label class="block text-sm font-medium text-gray-700">Email</label>
    <input type="email" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500">
  </div>

  <div class="space-y-2">
    <label class="block text-sm font-medium text-gray-700">Пароль</label>
    <input type="password" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500">
  </div>

  <div class="pt-4">
    <button type="submit" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-3 rounded-lg transition">
      Зарегистрироваться
    </button>
  </div>
</form>
```

### 3. 🧭 Навигация с отступами

```html
<nav class="bg-white shadow-sm">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">
      <div class="flex-shrink-0 font-bold text-xl">
        Logo
      </div>
      <div class="hidden md:flex space-x-8">
        <a href="#" class="text-gray-700 hover:text-blue-600 px-3 py-2 rounded-md transition">Главная</a>
        <a href="#" class="text-gray-700 hover:text-blue-600 px-3 py-2 rounded-md transition">О нас</a>
        <a href="#" class="text-gray-700 hover:text-blue-600 px-3 py-2 rounded-md transition">Услуги</a>
        <a href="#" class="text-gray-700 hover:text-blue-600 px-3 py-2 rounded-md transition">Контакты</a>
      </div>
    </div>
  </div>
</nav>
```

### 4. 🎨 Секция с адаптивными отступами

```html
<section class="py-12 sm:py-16 md:py-20 lg:py-24 bg-gray-50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center max-w-3xl mx-auto">
      <h2 class="text-3xl sm:text-4xl md:text-5xl font-bold mb-4 sm:mb-6">
        Заголовок секции
      </h2>
      <p class="text-lg sm:text-xl text-gray-600 mb-8 sm:mb-12">
        Подзаголовок с описанием. Отступы адаптируются под размер экрана.
      </p>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <button class="bg-blue-600 hover:bg-blue-700 text-white font-medium px-8 py-3 rounded-lg transition">
          Начать
        </button>
        <button class="border-2 border-blue-600 text-blue-600 hover:bg-blue-50 font-medium px-8 py-3 rounded-lg transition">
          Подробнее
        </button>
      </div>
    </div>
  </div>
</section>
```

### 5. 🎯 Вложенные списки с разными отступами

```html
<ul class="space-y-1">
  <li class="py-2 px-4 hover:bg-gray-50 rounded cursor-pointer">
    Пункт меню 1
  </li>
  <li>
    <ul class="ml-6 space-y-1 border-l-2 border-gray-200">
      <li class="py-2 px-4 hover:bg-gray-50 rounded cursor-pointer">
        Подпункт 1.1
      </li>
      <li class="py-2 px-4 hover:bg-gray-50 rounded cursor-pointer">
        Подпункт 1.2
      </li>
      <li class="py-2 px-4 hover:bg-gray-50 rounded cursor-pointer">
        Подпункт 1.3
      </li>
    </ul>
  </li>
  <li class="py-2 px-4 hover:bg-gray-50 rounded cursor-pointer">
    Пункт меню 2
  </li>
</ul>
```

### 6. 🖼️ Галерея с отрицательными margin

```html
<div class="max-w-4xl mx-auto">
  <div class="grid grid-cols-2 gap-4">
    <div class="space-y-4">
      <img src="photo1.jpg" class="rounded-lg" alt="Фото 1">
      <img src="photo2.jpg" class="rounded-lg" alt="Фото 2">
    </div>
    <div class="space-y-4 mt-8">
      <img src="photo3.jpg" class="rounded-lg" alt="Фото 3">
      <img src="photo4.jpg" class="rounded-lg" alt="Фото 4">
    </div>
  </div>
</div>
```

### 7. 📊 Статистика с отступами

```html
<div class="grid grid-cols-1 md:grid-cols-3 gap-6 md:gap-8">
  <div class="bg-white rounded-xl shadow p-6 text-center">
    <div class="text-4xl font-bold text-blue-600 mb-2">12K+</div>
    <div class="text-sm text-gray-500 uppercase tracking-wider">
      Пользователей
    </div>
  </div>
  <div class="bg-white rounded-xl shadow p-6 text-center">
    <div class="text-4xl font-bold text-green-600 mb-2">98%</div>
    <div class="text-sm text-gray-500 uppercase tracking-wider">
      Довольных клиентов
    </div>
  </div>
  <div class="bg-white rounded-xl shadow p-6 text-center">
    <div class="text-4xl font-bold text-purple-600 mb-2">24/7</div>
    <div class="text-sm text-gray-500 uppercase tracking-wider">
      Поддержка
    </div>
  </div>
</div>
```

### 8. 💬 Чат с отступами

```html
<div class="bg-gray-100 p-4 rounded-lg max-w-md space-y-3">
  <!-- Сообщение собеседника -->
  <div class="flex items-end gap-2">
    <img src="avatar.jpg" class="w-8 h-8 rounded-full" alt="">
    <div class="bg-white rounded-lg rounded-bl-none px-4 py-2 max-w-xs shadow-sm">
      Привет! Как дела?
    </div>
  </div>

  <!-- Моё сообщение -->
  <div class="flex items-end gap-2 flex-row-reverse">
    <img src="my-avatar.jpg" class="w-8 h-8 rounded-full" alt="">
    <div class="bg-blue-500 text-white rounded-lg rounded-br-none px-4 py-2 max-w-xs shadow-sm">
      Отлично, спасибо!
    </div>
  </div>

  <!-- Ещё сообщение -->
  <div class="flex items-end gap-2">
    <img src="avatar.jpg" class="w-8 h-8 rounded-full" alt="">
    <div class="bg-white rounded-lg rounded-bl-none px-4 py-2 max-w-xs shadow-sm">
      Может встретимся сегодня?
    </div>
  </div>
</div>
```

## 📊 Шпаргалка: что когда использовать

| Задача | Классы |
| :-- | :-- |
| Одинаковый padding | `p-4` |
| Горизонтальный padding | `px-4` |
| Вертикальный padding | `py-4` |
| Padding сверху | `pt-4` |
| Padding справа | `pr-4` |
| Padding снизу | `pb-4` |
| Padding слева | `pl-4` |
| Логический padding start | `ps-4` |
| Логический padding end | `pe-4` |
| Одинаковый margin | `m-4` |
| Центрирование блока | `mx-auto` |
| Отрицательный margin | `-mt-4` |
| Отступы между flex-элементами | `space-x-4` или `gap-4` |
| Отступы между flex-элементами (вертикально) | `space-y-4` |
| Адаптивные отступы | `p-4 md:p-8 lg:p-12` |
| Кастомные отступы | `p-[23px]` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: `space-x` без `flex`

```html
<!-- ❌ Плохо: space-x не работает без flex -->
<div class="space-x-4">
  <div>1</div>
  <div>2</div>
</div>

<!-- ✅ Хорошо: добавляем flex -->
<div class="flex space-x-4">
  <div>1</div>
  <div>2</div>
</div>
```

### ❌ Ошибка 2: `space-x` с `flex-wrap`

```html
<!-- ❌ Плохо: лишние отступы на краях строк -->
<div class="flex flex-wrap space-x-4">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>

<!-- ✅ Хорошо: используем gap -->
<div class="flex flex-wrap gap-4">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>
```

### ❌ Ошибка 3: Margin вместо padding для внутренних отступов

```html
<!-- ❌ Плохо: margin создаёт отступ снаружи -->
<div class="bg-blue-500">
  <p class="m-4 text-white">Текст</p>
</div>

<!-- ✅ Хорошо: padding создаёт отступ внутри -->
<div class="bg-blue-500 p-4">
  <p class="text-white">Текст</p>
</div>
```

### ❌ Ошибка 4: Забывают про responsive отступы

```html
<!-- ❌ Плохо: одинаковые отступы на всех экранах -->
<div class="p-4">
  Контент
</div>

<!-- ✅ Хорошо: адаптивные отступы -->
<div class="p-4 md:p-8 lg:p-12">
  Контент
</div>
```

### ❌ Ошибка 5: `mx-auto` без ширины

```html
<!-- ❌ Плохо: блок на всю ширину, центрирование не работает -->
<div class="mx-auto bg-blue-500">
  Не центрируется
</div>

<!-- ✅ Хорошо: указываем max-w -->
<div class="mx-auto max-w-4xl bg-blue-500">
  Центрируется
</div>
```

### ❌ Ошибка 6: Использование `space-y` для grid

```html
<!-- ❌ Плохо: space-y не работает с grid -->
<div class="grid grid-cols-2 space-y-4">
  <div>1</div>
  <div>2</div>
  <div>3</div>
  <div>4</div>
</div>

<!-- ✅ Хорошо: используем gap -->
<div class="grid grid-cols-2 gap-4">
  <div>1</div>
  <div>2</div>
  <div>3</div>
  <div>4</div>
</div>
```

### ❌ Ошибка 7: Противоречивые отступы

```html
<!-- ❌ Плохо: p-4 и pt-8 конфликтуют -->
<div class="p-4 pt-8">
  Непонятный результат
</div>

<!-- ✅ Хорошо: используем одно свойство -->
<div class="px-4 pt-8 pb-4">
  Понятный результат
</div>
```

### ❌ Ошибка 8: Чрезмерное использование отрицательных margin

```html
<!-- ❌ Плохо: слишком много отрицательных margin -->
<div class="-mt-4 -mb-4 -mx-8">
  Сложно поддерживать
</div>

<!-- ✅ Хорошо: используем transform или absolute -->
<div class="relative">
  <div class="absolute -top-4">Элемент</div>
</div>
```

## 🎯 Что дальше?

Теперь вы полностью владеете отступами! Но layout — это не только отступы. Следующий важный аспект — **размеры элементов**: ширина, высота, минимальные и максимальные значения.

**Следующий шаг:** [📐 Размеры в Tailwind CSS](sizing.md) — изучим работу с width, height, min/max значениями и aspect-ratio.


---




---

# 🎨 Раздел: Styling

---



<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: styling\backgrounds.md -->
<!-- ═══════════════════════════════════════════════════════════ -->

# 🖼️ Фоны в Tailwind CSS

> **Полное руководство по работе с фонами:** от простых цветов до фоновых изображений, градиентов, паттернов и эффектов размытия

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Освоите все способы задания фона: цвета, изображения, градиенты
- ✅ Научитесь управлять размером, позицией и повторением фоновых изображений
- ✅ Поймёте разницу между `bg-cover` и `bg-contain`
- ✅ Создадите красивые hero-секции с изображениями
- ✅ Освоите эффекты размытия и затемнения
- ✅ Настроите кастомные фоновые изображения через конфиг
- ✅ Избежите типичных ошибок при работе с фонами

## 🎨 Цвет фона: `bg-{color}`

Базовый способ — использовать цвета из палитры Tailwind (подробнее в разделе [Цвета](../styling/colors.md)):

```html
<div class="bg-white">Белый фон</div>
<div class="bg-gray-50">Очень светлый серый</div>
<div class="bg-gray-100">Светло-серый</div>
<div class="bg-gray-900">Почти чёрный</div>
<div class="bg-blue-500">Синий</div>
<div class="bg-red-50">Светло-красный (для алертов)</div>
```

### Прозрачный фон

```html
<div class="bg-transparent">Прозрачный (по умолчанию)</div>
<div class="bg-white/50">Белый с 50% прозрачности</div>
<div class="bg-black/80">Чёрный с 80% непрозрачности</div>
```

## 🖼️ Фоновые изображения

### Подключение через arbitrary values

```html
<div class="bg-[url('/images/hero.jpg')]">
  Фон с изображением
</div>

<!-- С кавычками внутри URL -->
<div class="bg-[url('https://example.com/image.png')]">
  Внешнее изображение
</div>

<!-- SVG inline -->
<div class="bg-[url('data:image/svg+xml,...')]">
  SVG фон
</div>
```

### Через конфигурацию (рекомендуется)

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      backgroundImage: {
        'hero-pattern': "url('/images/hero-pattern.svg')",
        'footer-texture': "url('/images/footer-texture.png')",
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'gradient-conic': 'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',
      },
    },
  },
}
```

```html
<div class="bg-hero-pattern">Использование кастомного фона</div>
<div class="bg-footer-texture">Текстура в футере</div>
```

## 📐 Размер фона: `bg-{size}`

Управляет тем, как изображение масштабируется внутри контейнера:

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `bg-auto` | `background-size: auto` | Оригинальный размер |
| `bg-cover` | `background-size: cover` | Заполняет контейнер, обрезая края |
| `bg-contain` | `background-size: contain` | Вписывается целиком, может оставить пустоты |

```html
<!-- Cover: изображение заполняет весь блок, часть может быть обрезана -->
<div class="bg-[url('/photo.jpg')] bg-cover h-64">
  Идеально для hero-секций
</div>

<!-- Contain: изображение видно целиком, могут быть пустые полосы -->
<div class="bg-[url('/logo.svg')] bg-contain bg-no-repeat h-64">
  Логотип целиком виден
</div>

<!-- Auto: оригинальный размер (может не поместиться) -->
<div class="bg-[url('/pattern.png')] bg-auto bg-repeat">
  Паттерн в оригинальном размере
</div>
```

### Arbitrary значения

```html
<!-- Точные размеры -->
<div class="bg-[url('/icon.svg')] bg-[length:32px_32px] bg-no-repeat">
  Иконка 32×32
</div>

<!-- Процентные значения -->
<div class="bg-[url('/photo.jpg')] bg-[length:150%_auto]">
  Увеличенное изображение
</div>
```

> 💡 **Когда что использовать:**
> - `bg-cover` — для фотографий, hero-секций, карточек
> - `bg-contain` — для логотипов, иконок, когда важно видеть изображение целиком
> - `bg-auto` — для паттернов и текстур

## 🎯 Позиционирование: `bg-{position}`

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `bg-bottom` | `background-position: bottom` | Снизу |
| `bg-center` | `background-position: center` | По центру |
| `bg-left` | `background-position: left` | Слева |
| `bg-left-bottom` | `background-position: left bottom` | Слева снизу |
| `bg-left-top` | `background-position: left top` | Слева сверху |
| `bg-right` | `background-position: right` | Справа |
| `bg-right-bottom` | `background-position: right bottom` | Справа снизу |
| `bg-right-top` | `background-position: right top` | Справа сверху |
| `bg-top` | `background-position: top` | Сверху |

```html
<!-- Фото с фокусом на лице (сверху) -->
<div class="bg-[url('/portrait.jpg')] bg-cover bg-top h-64">
  Портрет
</div>

<!-- Логотип по центру -->
<div class="bg-[url('/logo.svg')] bg-contain bg-center bg-no-repeat h-32">
  Логотип
</div>

<!-- Декоративный элемент в правом верхнем углу -->
<div class="bg-[url('/decoration.svg')] bg-right-top bg-no-repeat">
  Контент
</div>
```

### Arbitrary позиционирование

```html
<!-- Точные проценты -->
<div class="bg-[url('/photo.jpg')] bg-cover bg-[position:20%_30%]">
  Смещение к конкретному месту фото
</div>

<!-- В пикселях -->
<div class="bg-[url('/icon.svg')] bg-[position:16px_16px] bg-no-repeat">
  Отступ 16px от левого верхнего угла
</div>
```

## 🔁 Повторение: `bg-repeat`

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `bg-repeat` | `background-repeat: repeat` | По обеим осям (по умолчанию) |
| `bg-no-repeat` | `background-repeat: no-repeat` | Без повторения |
| `bg-repeat-x` | `background-repeat: repeat-x` | Только по горизонтали |
| `bg-repeat-y` | `background-repeat: repeat-y` | Только по вертикали |
| `bg-repeat-round` | `background-repeat: round` | Масштабируется для заполнения |
| `bg-repeat-space` | `background-repeat: space` | Равные промежутки без обрезки |

```html
<!-- Паттерн на весь экран -->
<div class="bg-[url('/pattern.png')] bg-repeat min-h-screen">
  Фоновый паттерн
</div>

<!-- Горизонтальная полоса декоративных элементов -->
<div class="bg-[url('/dots.svg')] bg-repeat-x bg-center h-8">
  Декоративная полоса
</div>

<!-- Одно изображение без повторения -->
<div class="bg-[url('/hero.jpg')] bg-no-repeat bg-cover">
  Hero-секция
</div>
```

## 📌 Прикрепление: `bg-{attachment}`

Управляет тем, как фон ведёт себя при прокрутке:

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `bg-fixed` | `background-attachment: fixed` | Фиксирован относительно viewport |
| `bg-local` | `background-attachment: local` | Фиксирован относительно содержимого |
| `bg-scroll` | `background-attachment: scroll` | Прокручивается с элементом (по умолчанию) |

```html
<!-- Параллакс-эффект: фон остаётся на месте при прокрутке -->
<div class="bg-[url('/landscape.jpg')] bg-fixed bg-cover bg-center h-screen">
  <div class="flex items-center justify-center h-full text-white text-4xl font-bold">
    Параллакс
  </div>
</div>

<!-- Прокручивается вместе с контентом -->
<div class="bg-[url('/pattern.png')] bg-scroll">
  Обычный фон
</div>
```

> ⚠️ **Важно:** `bg-fixed` может вызывать проблемы с производительностью на мобильных устройствах и часто отключается в iOS Safari. Используйте с осторожностью.

## 🎭 Background origin и clip

### Origin: откуда считается фон

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `bg-origin-border` | `background-origin: border-box` | От края границы |
| `bg-origin-padding` | `background-origin: padding-box` | От края padding (по умолчанию) |
| `bg-origin-content` | `background-origin: content-box` | От края контента |

### Clip: где обрезается фон

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `bg-clip-border` | `background-clip: border-box` | Включая границу |
| `bg-clip-padding` | `background-clip: padding-box` | До padding |
| `bg-clip-content` | `background-clip: content-box` | Только контент |
| `bg-clip-text` | `background-clip: text` | Только внутри текста |

```html
<!-- Градиентный текст -->
<h1 class="text-6xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-purple-600">
  Градиентный текст
</h1>
```

## 🌫️ Эффекты размытия и затемнения

### Backdrop blur (размытие заднего плана)

```html
<!-- Стеклянный эффект (glassmorphism) -->
<div class="relative h-96 bg-[url('/photo.jpg')] bg-cover">
  <div class="absolute inset-0 bg-white/30 backdrop-blur-md">
    <div class="p-8">
      <h2 class="text-2xl font-bold">Стеклянная карточка</h2>
      <p>Контент поверх размытого фона</p>
    </div>
  </div>
</div>
```

Размеры размытия:

| Класс | CSS |
| :-- | :-- |
| `backdrop-blur-none` | `blur(0)` |
| `backdrop-blur-sm` | `blur(4px)` |
| `backdrop-blur` | `blur(8px)` |
| `backdrop-blur-md` | `blur(12px)` |
| `backdrop-blur-lg` | `blur(16px)` |
| `backdrop-blur-xl` | `blur(24px)` |
| `backdrop-blur-2xl` | `blur(40px)` |
| `backdrop-blur-3xl` | `blur(64px)` |

### Затемнение через overlay

```html
<!-- Затемнение для читаемости текста поверх фото -->
<div class="relative h-96 bg-[url('/photo.jpg')] bg-cover">
  <!-- Overlay -->
  <div class="absolute inset-0 bg-black/50"></div>

  <!-- Контент -->
  <div class="relative z-10 flex items-center justify-center h-full text-white">
    <h2 class="text-4xl font-bold">Читаемый заголовок</h2>
  </div>
</div>
```

### Градиентный overlay

```html
<!-- Градиент от прозрачного к чёрному снизу -->
<div class="relative h-96 bg-[url('/photo.jpg')] bg-cover">
  <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent"></div>

  <div class="relative z-10 flex items-end h-full p-6">
    <h2 class="text-3xl font-bold text-white">Заголовок поверх фото</h2>
  </div>
</div>
```

## 🌈 Градиенты как фон

Подробно про градиенты — в разделе [Цвета](../styling/colors.md#градиенты). Краткая сводка:

```html
<!-- Линейный градиент -->
<div class="bg-gradient-to-r from-blue-500 to-purple-600 h-32">
  Линейный
</div>

<!-- Трёхцветный градиент -->
<div class="bg-gradient-to-br from-pink-500 via-red-500 to-yellow-500 h-32">
  Трёхцветный
</div>

<!-- Радиальный градиент -->
<div class="bg-radial from-blue-500 to-purple-600 h-32">
  Радиальный
</div>

<!-- Конический градиент -->
<div class="bg-conic from-red-500 via-yellow-500 to-green-500 h-32">
  Конический
</div>
```

### Градиент + изображение

```html
<!-- Градиент поверх изображения -->
<div class="bg-[url('/photo.jpg')] bg-cover">
  <div class="bg-gradient-to-r from-blue-600/80 to-purple-600/80 h-64">
    <div class="flex items-center justify-center h-full text-white text-2xl font-bold">
      Градиент поверх фото
    </div>
  </div>
</div>
```

## 🎨 SVG-паттерны и текстуры

### Inline SVG в CSS

```html
<div class="bg-[url('data:image/svg+xml,%3Csvg%20...')] bg-repeat">
  SVG паттерн
</div>
```

### Через конфиг

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      backgroundImage: {
        'dots': "url(\"data:image/svg+xml,%3Csvg width='20' height='20' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='2' cy='2' r='1' fill='%23cbd5e1'/%3E%3C/svg%3E\")",
        'grid': "url(\"data:image/svg+xml,%3Csvg width='40' height='40' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 0h40v40H0z' fill='none' stroke='%23e5e7eb'/%3E%3C/svg%3E\")",
      },
    },
  },
}
```

```html
<div class="bg-dots bg-repeat min-h-screen">
  Фон с точками
</div>

<div class="bg-grid bg-repeat min-h-screen">
  Фон с сеткой
</div>
```

### Готовые ресурсы для паттернов

- 🌐 [Hero Patterns](https://heropatterns.com/) — коллекция SVG-паттернов
- 🌐 [Transparent Textures](https://www.transparenttextures.com/) — текстуры
- 🌐 [Patternico](https://patternico.com/) — генератор паттернов
- 🌐 [Haikei](https://haikei.app/) — генератор SVG-фонов

## 📱 Responsive фоны

Меняйте фоны на разных экранах:

```html
<!-- Мобильные: одно фото -->
<!-- Десктоп: другое фото -->
<div class="bg-[url('/mobile-hero.jpg')] md:bg-[url('/desktop-hero.jpg')] bg-cover bg-center h-96">
  Адаптивный фон
</div>

<!-- Мобильные: паттерн -->
<!-- Десктоп: сплошной цвет -->
<div class="bg-[url('/pattern.png')] md:bg-blue-500 min-h-screen">
  Адаптивный фон
</div>
```

## 🎨 Практические паттерны

### 1. 🎬 Hero-секция с фото и затемнением

```html
<section class="relative h-[600px] bg-[url('/hero.jpg')] bg-cover bg-center">
  <!-- Затемнение -->
  <div class="absolute inset-0 bg-gradient-to-b from-black/60 to-black/30"></div>

  <!-- Контент -->
  <div class="relative z-10 flex flex-col items-center justify-center h-full text-center text-white px-4">
    <h1 class="text-5xl md:text-6xl font-bold mb-4">
      Добро пожаловать
    </h1>
    <p class="text-xl md:text-2xl text-gray-200 max-w-2xl">
      Создавайте красивые интерфейсы с Tailwind CSS
    </p>
    <button class="mt-8 bg-white text-gray-900 font-semibold px-8 py-3 rounded-lg hover:bg-gray-100 transition">
      Начать
    </button>
  </div>
</section>
```

### 2. 🪟 Glassmorphism карточка

```html
<div class="relative h-96 bg-gradient-to-br from-purple-500 via-pink-500 to-orange-500">
  <!-- Декоративные круги -->
  <div class="absolute top-10 left-10 w-32 h-32 bg-yellow-300 rounded-full blur-2xl"></div>
  <div class="absolute bottom-10 right-10 w-40 h-40 bg-blue-400 rounded-full blur-2xl"></div>

  <!-- Стеклянная карточка -->
  <div class="absolute inset-0 flex items-center justify-center">
    <div class="bg-white/20 backdrop-blur-lg border border-white/30 rounded-2xl p-8 shadow-2xl max-w-md">
      <h2 class="text-2xl font-bold text-white mb-4">Glassmorphism</h2>
      <p class="text-white/90">
        Современный эффект матового стекла с размытием заднего плана.
      </p>
    </div>
  </div>
</div>
```

### 3. 📄 Страница с декоративным фоном

```html
<div class="min-h-screen bg-gray-50">
  <!-- Декоративные элементы -->
  <div class="fixed top-0 left-0 w-96 h-96 bg-purple-300 rounded-full mix-blend-multiply filter blur-3xl opacity-30 -translate-x-1/2 -translate-y-1/2"></div>
  <div class="fixed top-0 right-0 w-96 h-96 bg-yellow-300 rounded-full mix-blend-multiply filter blur-3xl opacity-30 translate-x-1/2 -translate-y-1/2"></div>
  <div class="fixed bottom-0 left-1/2 w-96 h-96 bg-pink-300 rounded-full mix-blend-multiply filter blur-3xl opacity-30 translate-x-1/2 translate-y-1/2"></div>

  <!-- Контент -->
  <div class="relative z-10 max-w-4xl mx-auto py-16 px-4">
    <h1 class="text-4xl font-bold text-gray-900 mb-8">
      Страница с декоративным фоном
    </h1>
    <div class="bg-white/80 backdrop-blur-sm rounded-xl shadow-xl p-8">
      <p>Контент на полупрозрачной карточке</p>
    </div>
  </div>
</div>
```

### 4. 🎴 Карточка товара с изображением

```html
<div class="bg-white rounded-xl shadow-lg overflow-hidden max-w-sm">
  <!-- Изображение -->
  <div class="relative h-64 bg-[url('/product.jpg')] bg-cover bg-center">
    <!-- Бейдж -->
    <span class="absolute top-4 left-4 bg-red-500 text-white text-xs font-bold px-2 py-1 rounded">
      -30%
    </span>
    <!-- Градиент снизу для плавного перехода -->
    <div class="absolute inset-x-0 bottom-0 h-20 bg-gradient-to-t from-white to-transparent"></div>
  </div>

  <!-- Контент -->
  <div class="p-6">
    <h3 class="text-xl font-bold text-gray-900">Название товара</h3>
    <p class="mt-2 text-gray-600 text-sm">Краткое описание товара</p>
    <div class="mt-4 flex items-baseline gap-2">
      <span class="text-2xl font-bold text-gray-900">2 990 ₽</span>
      <span class="text-sm text-gray-400 line-through">4 270 ₽</span>
    </div>
    <button class="mt-4 w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 rounded-lg transition">
      В корзину
    </button>
  </div>
</div>
```

### 5. 🎨 Секция с паттерном

```html
<section class="relative py-20 bg-blue-600 overflow-hidden">
  <!-- SVG паттерн поверх цвета -->
  <div class="absolute inset-0 opacity-10 bg-[url('data:image/svg+xml,...')] bg-repeat"></div>

  <!-- Контент -->
  <div class="relative z-10 max-w-4xl mx-auto px-4 text-center text-white">
    <h2 class="text-4xl font-bold mb-4">Секция с паттерном</h2>
    <p class="text-xl text-blue-100">
      Паттерн добавляет текстуру и глубину фону
    </p>
  </div>
</section>
```

## 📊 Шпаргалка: что когда использовать

| Задача | Классы |
| :-- | :-- |
| Цвет фона | `bg-blue-500` |
| Прозрачный цвет | `bg-blue-500/50` |
| Фоновое изображение | `bg-[url('/img.jpg')]` |
| Изображение на весь блок | `bg-cover bg-center` |
| Изображение целиком | `bg-contain bg-center bg-no-repeat` |
| Паттерн | `bg-repeat` |
| Параллакс | `bg-fixed` |
| Градиент | `bg-gradient-to-r from-... to-...` |
| Стеклянный эффект | `bg-white/30 backdrop-blur-md` |
| Затемнение поверх фото | `bg-black/50` |
| Градиентный текст | `bg-clip-text text-transparent bg-gradient-to-r` |
| Позиция фона | `bg-top`, `bg-center`, `bg-[position:20%_30%]` |
| Размер фона | `bg-[length:32px_32px]` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: `bg-cover` без `bg-center`

```html
<!-- ❌ Плохо: изображение может быть обрезано некрасиво -->
<div class="bg-[url('/photo.jpg')] bg-cover h-64">...</div>

<!-- ✅ Хорошо: центрирование даёт предсказуемый результат -->
<div class="bg-[url('/photo.jpg')] bg-cover bg-center h-64">...</div>
```

### ❌ Ошибка 2: Фоновое изображение без высоты

```html
<!-- ❌ Плохо: блок схлопнется, фона не будет видно -->
<div class="bg-[url('/photo.jpg')] bg-cover">...</div>

<!-- ✅ Хорошо: указана высота -->
<div class="bg-[url('/photo.jpg')] bg-cover h-64">...</div>
```

### ❌ Ошибка 3: `bg-fixed` на мобильных

```html
<!-- ❌ Плохо: на iOS может не работать или тормозить -->
<div class="bg-[url('/photo.jpg')] bg-fixed bg-cover h-screen">...</div>

<!-- ✅ Хорошо: используем только на десктопе -->
<div class="bg-[url('/photo.jpg')] md:bg-fixed bg-cover bg-scroll h-screen">...</div>
```

### ❌ Ошибка 4: Текст на фото без overlay

```html
<!-- ❌ Плохо: текст может сливаться с фото -->
<div class="bg-[url('/photo.jpg')] bg-cover h-64">
  <h2 class="text-white text-4xl">Заголовок</h2>
</div>

<!-- ✅ Хорошо: overlay для читаемости -->
<div class="relative bg-[url('/photo.jpg')] bg-cover h-64">
  <div class="absolute inset-0 bg-black/50"></div>
  <h2 class="relative z-10 text-white text-4xl">Заголовок</h2>
</div>
```

### ❌ Ошибка 5: Забывают `bg-no-repeat` для одиночных изображений

```html
<!-- ❌ Плохо: изображение может повториться -->
<div class="bg-[url('/logo.svg')] bg-contain h-32">...</div>

<!-- ✅ Хорошо: явно запрещаем повторение -->
<div class="bg-[url('/logo.svg')] bg-contain bg-no-repeat h-32">...</div>
```

### ❌ Ошибка 6: Тяжёлые изображения без оптимизации

```html
<!-- ❌ Плохо: 5MB JPEG на фон -->
<div class="bg-[url('/huge-photo.jpg')] bg-cover h-96">...</div>

<!-- ✅ Хорошо: оптимизированное изображение (WebP, сжатие, ресайз) -->
<div class="bg-[url('/optimized-photo.webp')] bg-cover h-96">...</div>
```

> 💡 **Совет:** используйте WebP/AVIF, сжимайте через [Squoosh](https://squoosh.app/) или [TinyPNG](https://tinypng.com/), ресайзьте до нужного размера.

## 🎯 Что дальше?

Теперь вы полностью владеете фонами! Следующий важный аспект визуального стиля — **границы и обводки**.

**Следующий шаг:** [🔲 Границы в Tailwind CSS](borders.md) — изучим работу с границами, радиусами скругления, ring-эффектами и разделителями.

---

> 💬 **Упражнение:** создайте hero-секцию с фоновым изображением, градиентным overlay, заголовком, подзаголовком и кнопкой. Добавьте glassmorphism-карточку поверх с размытием фона. Убедитесь, что всё читаемо и красиво!

---




<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: styling\borders.md -->
<!-- ═══════════════════════════════════════════════════════════ -->

# 🔲 Границы в Tailwind CSS

> **Полное руководство по работе с границами:** от базовых border и radius до ring-эффектов, разделителей и outline

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Освоите все способы задания границ: ширина, цвет, стиль
- ✅ Научитесь управлять скруглением углов (border-radius)
- ✅ Поймёте разницу между `border`, `ring` и `outline`
- ✅ Создадите красивые карточки, кнопки и разделители
- ✅ Освоите отдельные стороны границ (top, right, bottom, left)
- ✅ Настроите кастомные радиусы и цвета границ
- ✅ Избежите типичных ошибок при работе с границами

## 📏 Ширина границы: `border-{width}`

Tailwind предоставляет **5 предустановленных ширин** границ:

| Класс | CSS | Визуально |
| :-- | :-- | :-- |
| `border` | `border-width: 1px` | Тонкая граница (по умолчанию) |
| `border-0` | `border-width: 0` | Без границы |
| `border-2` | `border-width: 2px` | Средняя граница |
| `border-4` | `border-width: 4px` | Толстая граница |
| `border-8` | `border-width: 8px` | Очень толстая граница |

```html
<div class="border border-gray-300 p-4">Тонкая граница (1px)</div>
<div class="border-2 border-gray-300 p-4">Средняя граница (2px)</div>
<div class="border-4 border-gray-300 p-4">Толстая граница (4px)</div>
<div class="border-8 border-gray-300 p-4">Очень толстая граница (8px)</div>
```

### Отдельные стороны

Если нужна граница только с определённой стороны:

| Класс | CSS |
| :-- | :-- |
| `border-t` | `border-top-width: 1px` |
| `border-r` | `border-right-width: 1px` |
| `border-b` | `border-bottom-width: 1px` |
| `border-l` | `border-left-width: 1px` |
| `border-x` | `border-left-width: 1px; border-right-width: 1px` |
| `border-y` | `border-top-width: 1px; border-bottom-width: 1px` |

```html
<!-- Только нижняя граница (для разделителей) -->
<div class="border-b border-gray-200 pb-4 mb-4">
  Элемент с нижней границей
</div>

<!-- Только левая граница (для акцентов) -->
<div class="border-l-4 border-blue-500 pl-4">
  Важная информация
</div>

<!-- Горизонтальные границы (сверху и снизу) -->
<div class="border-y border-gray-300 py-4">
  Элемент с границами сверху и снизу
</div>
```

### Arbitrary значения

```html
<!-- Точная ширина в пикселях -->
<div class="border-[3px] border-gray-300 p-4">Граница 3px</div>
```

## 🎨 Цвет границы: `border-{color}`

Используйте цвета из палитры Tailwind (подробнее в разделе [Цвета](../styling/colors.md)):

```html
<div class="border-2 border-gray-300 p-4">Серая граница</div>
<div class="border-2 border-blue-500 p-4">Синяя граница</div>
<div class="border-2 border-red-500 p-4">Красная граница</div>
<div class="border-2 border-green-500 p-4">Зелёная граница</div>
<div class="border-2 border-transparent p-4">Прозрачная граница</div>
```

### Прозрачность

```html
<div class="border-2 border-blue-500/50 p-4">Синяя с 50% прозрачности</div>
<div class="border-2 border-white/20 p-4 bg-gray-900">Белая с 20% прозрачности</div>
```

### Отдельные стороны с цветом

```html
<!-- Разные цвета для разных сторон -->
<div class="border-t-2 border-t-red-500 border-b-2 border-b-blue-500 p-4">
  Красная сверху, синяя снизу
</div>
```

## 🎭 Стиль границы: `border-{style}`

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `border-solid` | `border-style: solid` | Сплошная линия (по умолчанию) |
| `border-dashed` | `border-style: dashed` | Пунктирная |
| `border-dotted` | `border-style: dotted` | Точечная |
| `border-double` | `border-style: double` | Двойная линия |
| `border-hidden` | `border-style: hidden` | Скрытая (как none, но для таблиц) |
| `border-none` | `border-style: none` | Без границы |

```html
<div class="border-2 border-dashed border-gray-400 p-4">Пунктирная граница</div>
<div class="border-2 border-dotted border-gray-400 p-4">Точечная граница</div>
<div class="border-4 border-double border-gray-400 p-4">Двойная граница</div>
```

> 💡 **Совет:** `border-dashed` часто используется для drag-and-drop зон и placeholder-элементов.

## 🔄 Скругление углов: `rounded-{size}`

Tailwind предоставляет **8 предустановленных радиусов**:

| Класс | CSS | Визуально |
| :-- | :-- | :-- |
| `rounded-none` | `border-radius: 0` | Без скругления (острые углы) |
| `rounded-sm` | `border-radius: 0.125rem` (2px) | Очень маленькое скругление |
| `rounded` | `border-radius: 0.25rem` (4px) | Маленькое скругление |
| `rounded-md` | `border-radius: 0.375rem` (6px) | Среднее скругление |
| `rounded-lg` | `border-radius: 0.5rem` (8px) | Большое скругление |
| `rounded-xl` | `border-radius: 0.75rem` (12px) | Очень большое скругление |
| `rounded-2xl` | `border-radius: 1rem` (16px) | Огромное скругление |
| `rounded-3xl` | `border-radius: 1.5rem` (24px) | Максимальное скругление |
| `rounded-full` | `border-radius: 9999px` | Полное скругление (круг/пилюля) |

```html
<!-- Без скругления -->
<div class="border-2 border-gray-300 p-4 rounded-none">Острые углы</div>

<!-- Маленькое скругление -->
<div class="border-2 border-gray-300 p-4 rounded">Немного скруглено</div>

<!-- Среднее скругление -->
<div class="border-2 border-gray-300 p-4 rounded-lg">Скруглено</div>

<!-- Большое скругление -->
<div class="border-2 border-gray-300 p-4 rounded-xl">Сильно скруглено</div>

<!-- Полное скругление (для кнопок-пилюль) -->
<button class="border-2 border-blue-500 px-6 py-2 rounded-full">
  Кнопка-пилюля
</button>

<!-- Круг (для аватаров) -->
<img src="avatar.jpg" class="w-16 h-16 rounded-full border-2 border-white">
```

### Отдельные углы

Если нужно скруглить только определённые углы:

| Класс | CSS |
| :-- | :-- |
| `rounded-t` | `border-top-left-radius` + `border-top-right-radius` |
| `rounded-r` | `border-top-right-radius` + `border-bottom-right-radius` |
| `rounded-b` | `border-bottom-left-radius` + `border-bottom-right-radius` |
| `rounded-l` | `border-top-left-radius` + `border-bottom-left-radius` |
| `rounded-tl` | `border-top-left-radius` |
| `rounded-tr` | `border-top-right-radius` |
| `rounded-br` | `border-bottom-right-radius` |
| `rounded-bl` | `border-bottom-left-radius` |

```html
<!-- Скруглены только верхние углы -->
<div class="border-2 border-gray-300 p-4 rounded-t-lg">
  Скруглённые верхние углы
</div>

<!-- Скруглён только правый верхний угол -->
<div class="border-2 border-gray-300 p-4 rounded-tr-lg">
  Только правый верхний угол
</div>

<!-- Асимметричное скругление -->
<div class="border-2 border-gray-300 p-4 rounded-tl-lg rounded-br-lg">
  Диагональное скругление
</div>
```

### Arbitrary значения

```html
<!-- Точный радиус в пикселях -->
<div class="border-2 border-gray-300 p-4 rounded-[10px]">Радиус 10px</div>

<!-- Процентный радиус -->
<div class="border-2 border-gray-300 p-4 rounded-[50%]">Радиус 50%</div>
```

## 💍 Ring-эффекты: `ring-{width}`

`ring` — это **внешняя обводка**, которая не занимает места (в отличие от `border`). Идеально для focus-состояний.

| Класс | CSS |
| :-- | :-- |
| `ring-0` | `box-shadow: 0 0 0 0px` |
| `ring-1` | `box-shadow: 0 0 0 1px` |
| `ring-2` | `box-shadow: 0 0 0 2px` |
| `ring` | `box-shadow: 0 0 0 3px` (по умолчанию) |
| `ring-4` | `box-shadow: 0 0 0 4px` |
| `ring-8` | `box-shadow: 0 0 0 8px` |
| `ring-inset` | `box-shadow: inset 0 0 0 3px` |

### Цвет ring

```html
<input
  type="text"
  class="border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
  placeholder="Фокус с синим ring"
>
```

### Ring offset (отступ от элемента)

```html
<input
  type="text"
  class="border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
  placeholder="Ring с отступом"
>
```

| Класс | CSS |
| :-- | :-- |
| `ring-offset-0` | `--tw-ring-offset-width: 0px` |
| `ring-offset-1` | `--tw-ring-offset-width: 1px` |
| `ring-offset-2` | `--tw-ring-offset-width: 2px` |
| `ring-offset-4` | `--tw-ring-offset-width: 4px` |
| `ring-offset-8` | `--tw-ring-offset-width: 8px` |

### Цвет ring offset

```html
<input
  type="text"
  class="bg-gray-100 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 focus:ring-offset-gray-100"
  placeholder="Ring offset того же цвета, что и фон"
>
```

> 💡 **Важно:** `ring` использует `box-shadow`, поэтому не влияет на layout. `border` занимает место.

## 📏 Outline: `outline-{width}`

`outline` — это **внешняя обводка** (как `ring`), но с другим синтаксисом и поведением:

| Класс | CSS |
| :-- | :-- |
| `outline-none` | `outline: 2px solid transparent; outline-offset: 2px` |
| `outline` | `outline-style: solid` |
| `outline-dashed` | `outline-style: dashed` |
| `outline-dotted` | `outline-style: dotted` |
| `outline-double` | `outline-style: double` |

```html
<!-- Focus с outline -->
<button class="focus:outline-none focus:outline-2 focus:outline-blue-500">
  Кнопка с outline при фокусе
</button>

<!-- Outline с отступом -->
<button class="focus:outline-2 focus:outline-blue-500 focus:outline-offset-2">
  Кнопка с отступом outline
</button>
```

### Разница между `ring` и `outline`

| Критерий | `ring` | `outline` |
| :-- | :-- | :-- |
| **Реализация** | `box-shadow` | `outline` CSS property |
| **Скругление** | Следует `border-radius` | Не следует `border-radius` |
| **Отступ** | `ring-offset-{size}` | `outline-offset-{size}` |
| **Рекомендация** | ✅ Для focus-состояний | 🟡 Для accessibility |

> 💡 **Правило:** используйте `ring` для focus-состояний в UI. `outline` оставьте для случаев, когда нужно следовать нативному поведению браузера.

## 🔗 Разделители: `divide-{width}` и `divide-{color}`

`divide` добавляет границы **между дочерними элементами**:

### Ширина

| Класс | CSS |
| :-- | :-- |
| `divide-x` | `border-left-width: 1px` между элементами |
| `divide-x-0` | Без горизонтальных разделителей |
| `divide-x-2` | `border-left-width: 2px` |
| `divide-x-4` | `border-left-width: 4px` |
| `divide-x-8` | `border-left-width: 8px` |
| `divide-y` | `border-top-width: 1px` между элементами |
| `divide-y-0` | Без вертикальных разделителей |
| `divide-y-2` | `border-top-width: 2px` |
| `divide-y-4` | `border-top-width: 4px` |
| `divide-y-8` | `border-top-width: 8px` |

### Цвет

```html
<!-- Вертикальные разделители -->
<div class="divide-y divide-gray-200">
  <div class="py-2">Пункт 1</div>
  <div class="py-2">Пункт 2</div>
  <div class="py-2">Пункт 3</div>
</div>

<!-- Горизонтальные разделители -->
<div class="flex divide-x divide-gray-200">
  <div class="px-4 py-2">Элемент 1</div>
  <div class="px-4 py-2">Элемент 2</div>
  <div class="px-4 py-2">Элемент 3</div>
</div>

<!-- Цветные разделители -->
<div class="divide-y divide-blue-200">
  <div class="py-2">Пункт 1</div>
  <div class="py-2">Пункт 2</div>
</div>
```

### Стиль разделителей

```html
<!-- Пунктирные разделители -->
<div class="divide-y divide-dashed divide-gray-300">
  <div class="py-2">Пункт 1</div>
  <div class="py-2">Пункт 2</div>
</div>
```

### Reverse (для RTL)

```html
<!-- Разделители справа (для RTL языков) -->
<div class="divide-x divide-x-reverse divide-gray-200 flex">
  <div class="px-4">Элемент 1</div>
  <div class="px-4">Элемент 2</div>
</div>
```

## 🎨 Практические паттерны

### 1. 🎴 Карточка с границей

```html
<div class="bg-white border border-gray-200 rounded-xl shadow-sm p-6 max-w-sm">
  <h3 class="text-xl font-bold text-gray-900 mb-2">Название карточки</h3>
  <p class="text-gray-600 text-sm">
    Описание карточки с границей и скруглением.
  </p>
  <button class="mt-4 w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 rounded-lg transition">
    Действие
  </button>
</div>
```

### 2. 🎯 Input с focus ring

```html
<div class="space-y-4 max-w-md">
  <div>
    <label class="block text-sm font-medium text-gray-700 mb-1">Email</label>
    <input
      type="email"
      class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
      placeholder="you@example.com"
    >
  </div>

  <div>
    <label class="block text-sm font-medium text-gray-700 mb-1">Пароль</label>
    <input
      type="password"
      class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
      placeholder="••••••••"
    >
  </div>
</div>
```

### 3. 📊 Список с разделителями

```html
<div class="bg-white border border-gray-200 rounded-lg divide-y divide-gray-200 max-w-md">
  <div class="flex items-center justify-between p-4">
    <div>
      <div class="font-medium text-gray-900">Профиль</div>
      <div class="text-sm text-gray-500">Настройки аккаунта</div>
    </div>
    <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
    </svg>
  </div>

  <div class="flex items-center justify-between p-4">
    <div>
      <div class="font-medium text-gray-900">Уведомления</div>
      <div class="text-sm text-gray-500">Email и push-уведомления</div>
    </div>
    <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
    </svg>
  </div>

  <div class="flex items-center justify-between p-4">
    <div>
      <div class="font-medium text-gray-900">Безопасность</div>
      <div class="text-sm text-gray-500">Пароль и 2FA</div>
    </div>
    <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
    </svg>
  </div>
</div>
```

### 4. 🏷️ Бейдж с границей

```html
<div class="flex flex-wrap gap-2">
  <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-blue-100 text-blue-800 border border-blue-200">
    Новое
  </span>
  <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-green-100 text-green-800 border border-green-200">
    Активно
  </span>
  <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-yellow-100 text-yellow-800 border border-yellow-200">
    В процессе
  </span>
  <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-red-100 text-red-800 border border-red-200">
    Закрыто
  </span>
</div>
```

### 5. 🎨 Карточка с акцентной границей слева

```html
<div class="bg-white border-l-4 border-blue-500 rounded-r-lg shadow-sm p-6 max-w-md">
  <h3 class="text-lg font-bold text-gray-900 mb-2">Важная информация</h3>
  <p class="text-gray-600 text-sm">
    Этот блок выделен акцентной границей слева для привлечения внимания.
  </p>
</div>
```

### 6. 🔘 Группа кнопок с разделителями

```html
<div class="inline-flex border border-gray-300 rounded-lg divide-x divide-gray-300">
  <button class="px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50">
    День
  </button>
  <button class="px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50">
    Неделя
  </button>
  <button class="px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50">
    Месяц
  </button>
</div>
```

### 7. 🖼️ Аватар с границей

```html
<div class="flex items-center gap-3">
  <img
    src="avatar.jpg"
    alt="Аватар"
    class="w-12 h-12 rounded-full border-2 border-white shadow-md"
  >
  <div>
    <div class="font-medium text-gray-900">Иван Иванов</div>
    <div class="text-sm text-gray-500">Разработчик</div>
  </div>
</div>
```

### 8. 🎯 Drag-and-drop зона

```html
<div class="border-2 border-dashed border-gray-300 rounded-lg p-12 text-center hover:border-blue-500 transition-colors">
  <svg class="mx-auto w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"/>
  </svg>
  <p class="mt-2 text-sm text-gray-600">
    Перетащите файлы сюда или
    <button class="text-blue-600 hover:text-blue-700 font-medium">выберите</button>
  </p>
  <p class="mt-1 text-xs text-gray-500">PNG, JPG до 10MB</p>
</div>
```

## 📊 Шпаргалка: что когда использовать

| Задача | Классы |
| :-- | :-- |
| Тонкая граница | `border border-gray-300` |
| Толстая граница | `border-4 border-gray-300` |
| Только снизу | `border-b border-gray-200` |
| Только слева (акцент) | `border-l-4 border-blue-500` |
| Пунктирная граница | `border-2 border-dashed border-gray-400` |
| Скругление углов | `rounded-lg`, `rounded-xl`, `rounded-full` |
| Только верхние углы | `rounded-t-lg` |
| Focus ring | `focus:ring-2 focus:ring-blue-500` |
| Ring с отступом | `focus:ring-2 focus:ring-blue-500 focus:ring-offset-2` |
| Разделители между элементами | `divide-y divide-gray-200` |
| Горизонтальные разделители | `divide-x divide-gray-200` |
| Аватар | `rounded-full border-2 border-white` |
| Кнопка-пилюля | `rounded-full` |
| Drag-and-drop зона | `border-2 border-dashed` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Забывают `border` при указании цвета

```html
<!-- ❌ Плохо: цвет границы не применится без width -->
<div class="border-gray-300 p-4">Нет границы</div>

<!-- ✅ Хорошо: указываем ширину -->
<div class="border border-gray-300 p-4">Есть граница</div>
```

### ❌ Ошибка 2: `ring` вместо `border` для постоянной границы

```html
<!-- ❌ Плохо: ring занимает место и может обрезаться -->
<div class="ring-2 ring-gray-300 p-4">Кольцо</div>

<!-- ✅ Хорошо: border для постоянной границы -->
<div class="border-2 border-gray-300 p-4">Граница</div>
```

### ❌ Ошибка 3: Забывают `focus:outline-none` при использовании `focus:ring`

```html
<!-- ❌ Плохо: двойная обводка (outline + ring) -->
<input
  type="text"
  class="border border-gray-300 focus:ring-2 focus:ring-blue-500"
>

<!-- ✅ Хорошо: убираем стандартный outline -->
<input
  type="text"
  class="border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
>
```

### ❌ Ошибка 4: `rounded-full` для неквадратных элементов

```html
<!-- ❌ Плохо: получится овал, не круг -->
<div class="w-32 h-16 rounded-full bg-blue-500">Овал</div>

<!-- ✅ Хорошо: квадратные пропорции -->
<div class="w-16 h-16 rounded-full bg-blue-500">Круг</div>

<!-- ✅ Или используйте rounded-{size} для прямоугольников -->
<div class="w-32 h-16 rounded-lg bg-blue-500">Прямоугольник со скруглением</div>
```

### ❌ Ошибка 5: `divide` без flex или grid контейнера

```html
<!-- ❌ Плохо: divide не работает без flex/grid -->
<div class="divide-y divide-gray-200">
  <div>Пункт 1</div>
  <div>Пункт 2</div>
</div>

<!-- ✅ Хорошо: добавляем flex flex-col -->
<div class="divide-y divide-gray-200 flex flex-col">
  <div>Пункт 1</div>
  <div>Пункт 2</div>
</div>
```

### ❌ Ошибка 6: Забывают про responsive границы

```html
<!-- ❌ Плохо: граница на всех экранах -->
<div class="border border-gray-300 p-4">Граница всегда</div>

<!-- ✅ Хорошо: граница только на десктопе -->
<div class="border-0 md:border border-gray-300 p-4">Граница только на md+</div>
```

### ❌ Ошибка 7: `ring-offset` без учёта фона

```html
<!-- ❌ Плохо: ring offset на белом фоне выглядит странно -->
<div class="bg-white p-4">
  <input
    type="text"
    class="border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
  >
</div>

<!-- ✅ Хорошо: ring offset того же цвета, что и фон -->
<div class="bg-white p-4">
  <input
    type="text"
    class="border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 focus:ring-offset-white"
  >
</div>
```

## 🎯 Что дальше?

Теперь вы полностью владеете границами и обводками! Но визуальный стиль — это не только границы. Следующий важный аспект — **эффекты и тени**.

**Следующий шаг:** [✨ Эффекты и тени в Tailwind CSS](effects.md) — изучим работу с box-shadow, opacity, mix-blend-mode и другими визуальными эффектами.

---

> 💬 **Упражнение:** создайте карточку профиля с аватаром (круглая граница), именем, должностью, списком настроек (с разделителями) и кнопкой действия (с focus ring). Используйте только border-утилиты Tailwind!

---




<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: styling\colors.md -->
<!-- ═══════════════════════════════════════════════════════════ -->

# 🎨 Цвета в Tailwind CSS

> **Полное руководство по работе с цветами:** от базовой палитры до кастомных тем, градиентов и темизации

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Поймёте структуру палитры Tailwind CSS
- ✅ Научитесь применять цвета к тексту, фону, границам и другим свойствам
- ✅ Освоите модификаторы прозрачности (`/50`, `/75`)
- ✅ Сможете создавать красивые градиенты
- ✅ Настроите кастомную цветовую палитру под свой бренд
- ✅ Поймёте принципы доступности и контрастности
- ✅ Избежите типичных ошибок при работе с цветом

## 🌈 Структура палитры Tailwind

Tailwind предоставляет **22 цветовые палитры**, каждая из которых содержит **11 оттенков** (от 50 до 950).

### Нейтральные цвета

| Палитра | Характер | Когда использовать |
| :-- | :-- | :-- |
| `slate` | Холодный серый с синим подтоном | Современный tech-дизайн |
| `gray` | Нейтральный серый | Универсальный выбор |
| `zinc` | Тёплый серый | Мягкий, приятный глазу |
| `neutral` | Чистый серый | Минимализм |
| `stone` | Тёплый серый с коричневым | Органичный, природный |

### Цветовые палитры

| Палитра | Оттенки | Ассоциации |
| :-- | :-- | :-- |
| `red` | 50–950 | Ошибки, опасность, страсть |
| `orange` | 50–950 | Энергия, предупреждения |
| `amber` | 50–950 | Внимание, тёплые акценты |
| `yellow` | 50–950 | Оптимизм,.highlight |
| `lime` | 50–950 | Свежесть, экология |
| `green` | 50–950 | Успех, природа, деньги |
| `emerald` | 50–950 | Премиум, рост |
| `teal` | 50–950 | Спокойствие, медицина |
| `cyan` | 50–950 | Технологии, вода |
| `sky` | 50–950 | Лёгкость, небо |
| `blue` | 50–950 | Доверие, корпоративный |
| `indigo` | 50–950 | Креативность, премиум |
| `violet` | 50–950 | Роскошь, магия |
| `purple` | 50–950 | Творчество, духовность |
| `fuchsia` | 50–950 | Яркость, мода |
| `pink` | 50–950 | Романтика, мягкость |
| `rose` | 50–950 | Элегантность, женственность |

### Что означают числа оттенков?

```
50   → Очень светлый (фоны, hover-состояния)
100  → Светлый (альтернативные фоны)
200  → Светло-средний (границы)
300  → Средне-светлый (placeholder)
400  → Средний (иконки, второстепенный текст)
500  → Базовый цвет (основные элементы)
600  → Средне-тёмный (hover-состояния кнопок)
700  → Тёмный (текст на светлом фоне)
800  → Очень тёмный (заголовки)
900  → Почти чёрный (основной текст)
950  → Самый тёмный (контрастные элементы)
```

## 🖌 Применение цветов

### Текст: `text-{color}`

```html
<p class="text-gray-900">Основной текст</p>
<p class="text-gray-600">Второстепенный текст</p>
<p class="text-gray-400">Placeholder</p>
<p class="text-blue-600">Ссылка</p>
<p class="text-red-500">Ошибка</p>
<p class="text-green-600">Успех</p>
```

### Фон: `bg-{color}`

```html
<div class="bg-white">Белый фон</div>
<div class="bg-gray-50">Очень светлый серый</div>
<div class="bg-blue-500">Синий (основной)</div>
<div class="bg-blue-600">Синий (hover)</div>
<div class="bg-red-50">Светло-красный (для алертов)</div>
```

### Границы: `border-{color}`

```html
<div class="border border-gray-200">Светлая граница</div>
<div class="border-2 border-blue-500">Синяя граница</div>
<div class="border-l-4 border-red-500">Красная левая граница</div>
```

### Ring (обводка для focus): `ring-{color}`

```html
<input
  class="border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
  type="text"
  placeholder="Фокус с синим ring"
>
```

### Разделители: `divide-{color}`

```html
<div class="divide-y divide-gray-200">
  <div class="py-2">Пункт 1</div>
  <div class="py-2">Пункт 2</div>
  <div class="py-2">Пункт 3</div>
</div>
```

### Акцент (чекбоксы, радиокнопки): `accent-{color}`

```html
<input type="checkbox" class="accent-blue-500">
<input type="radio" class="accent-green-500">
```

### SVG: `fill-{color}` и `stroke-{color}`

```html
<svg class="w-6 h-6 fill-blue-500" viewBox="0 0 24 24">
  <path d="..."/>
</svg>

<svg class="w-6 h-6 stroke-red-500 fill-none" viewBox="0 0 24 24">
  <path d="..." stroke-width="2"/>
</svg>
```

## 💧 Прозрачность: модификатор `/{opacity}`

Tailwind позволяет легко задавать прозрачность любому цвету через слэш:

```html
<!-- Фон с прозрачностью -->
<div class="bg-blue-500/10">10% синий</div>
<div class="bg-blue-500/25">25% синий</div>
<div class="bg-blue-500/50">50% синий</div>
<div class="bg-blue-500/75">75% синий</div>
<div class="bg-blue-500">100% синий</div>

<!-- Текст с прозрачностью -->
<p class="text-gray-900/80">Текст с 80% непрозрачности</p>

<!-- Граница с прозрачностью -->
<div class="border border-white/20">Полупрозрачная граница</div>
```

### Доступные значения прозрачности

```
/0   → 0%   (полностью прозрачный)
/5   → 5%
/10  → 10%
/20  → 20%
/25  → 25%
/30  → 30%
/40  → 40%
/50  → 50%
/60  → 60%
/70  → 70%
/75  → 75%
/80  → 80%
/90  → 90%
/95  → 95%
/100 → 100% (без прозрачности)
```

## 🌈 Градиенты

### Линейные градиенты

```html
<!-- По умолчанию: сверху вниз -->
<div class="bg-gradient-to-b from-blue-500 to-purple-600 h-32">
  Градиент сверху вниз
</div>

<!-- Справа налево -->
<div class="bg-gradient-to-l from-green-400 to-blue-500 h-32">
  Градиент справа налево
</div>

<!-- По диагонали -->
<div class="bg-gradient-to-br from-pink-500 via-red-500 to-yellow-500 h-32">
  Трёхцветный градиент
</div>
```

### Направления градиентов

| Класс | Направление |
| :-- | :-- |
| `bg-gradient-to-t` | ↑ Снизу вверх |
| `bg-gradient-to-tr` | ↗ Снизу-слева вверх-вправо |
| `bg-gradient-to-r` | → Слева направо |
| `bg-gradient-to-br` | ↘ Сверху-слева вниз-вправо |
| `bg-gradient-to-b` | ↓ Сверху вниз |
| `bg-gradient-to-bl` | ↙ Сверху-справа вниз-влево |
| `bg-gradient-to-l` | ← Справа налево |
| `bg-gradient-to-tl` | ↖ Снизу-справа вверх-влево |

### Радиальные и конические градиенты

```html
<!-- Радиальный градиент -->
<div class="bg-radial from-blue-500 to-purple-600 h-32">
  Радиальный
</div>

<!-- Конический градиент -->
<div class="bg-conic from-red-500 via-yellow-500 to-green-500 h-32">
  Конический
</div>
```

## 🎨 Arbitrary values: кастомные цвета

Если нужного цвета нет в палитре, используйте квадратные скобки:

```html
<!-- HEX -->
<div class="bg-[#f97316]">Оранжевый #f97316</div>

<!-- RGB -->
<div class="text-[rgb(239,68,68)]">Красный RGB</div>

<!-- HSL -->
<div class="border-[hsl(210,100%,50%)]">Синий HSL</div>

<!-- С прозрачностью -->
<div class="bg-[#3b82f6]/30">Синий с 30% прозрачности</div>
```

> ⚠️ **Не злоупотребляйте arbitrary values!** Если цвет используется часто — добавьте его в `tailwind.config.js`.

## ⚙️ Кастомизация палитры

### Добавление своих цветов

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        // Простой цвет
        'brand': '#ff5722',

        // Палитра с оттенками
        'brand': {
          50:  '#fff3ed',
          100: '#ffe4d6',
          200: '#ffc5ac',
          300: '#ffa082',
          400: '#ff7a58',
          500: '#ff5722', // основной
          600: '#e64a19',
          700: '#c43e14',
          800: '#a33310',
          900: '#7a260c',
          950: '#4d1808',
        },

        // Семантические цвета
        'success': '#10b981',
        'warning': '#f59e0b',
        'error':   '#ef4444',
        'info':    '#3b82f6',
      },
    },
  },
}
```

После этого можно использовать:

```html
<div class="bg-brand-500 text-white">Брендовый цвет</div>
<button class="bg-success hover:bg-success/90 text-white">Успех</button>
```

### Переопределение стандартной палитры

```js
// tailwind.config.js
module.exports = {
  theme: {
    // Полностью заменить палитру
    colors: {
      'primary': '#3b82f6',
      'secondary': '#8b5cf6',
      'neutral': '#6b7280',
    },
    // Или расширить существующую
    extend: {
      colors: {
        'accent': '#ec4899',
      },
    },
  },
}
```

## 🎭 CSS-переменные и темизация

Современный подход — использовать CSS-переменные для динамической смены темы:

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        'primary': 'rgb(var(--color-primary) / <alpha-value>)',
        'secondary': 'rgb(var(--color-secondary) / <alpha-value>)',
        'background': 'rgb(var(--color-background) / <alpha-value>)',
      },
    },
  },
}
```

```css
/* styles.css */
:root {
  --color-primary: 59 130 246;    /* #3b82f6 */
  --color-secondary: 139 92 246;  /* #8b5cf6 */
  --color-background: 255 255 255;
}

.dark {
  --color-primary: 96 165 250;    /* #60a5fa */
  --color-secondary: 167 139 250; /* #a78bfa */
  --color-background: 17 24 39;   /* #111827 */
}
```

```html
<!-- Автоматически меняет цвет в dark mode -->
<div class="bg-primary text-background">Тема</div>
```

## ♿ Доступность и контрастность

### WCAG 2.1: минимальные требования

| Тип текста | Минимальный контраст |
| :-- | :-- |
| **Обычный текст** (до 18pt) | 4.5:1 |
| **Крупный текст** (от 18pt или 14pt bold) | 3:1 |
| **UI-компоненты** (кнопки, иконки) | 3:1 |

### Примеры хороших комбинаций

```html
<!-- ✅ Белый текст на синем (контраст 4.6:1) -->
<button class="bg-blue-600 text-white px-4 py-2">
  Нажми меня
</button>

<!-- ✅ Тёмный текст на светлом фоне (контраст 15:1) -->
<p class="text-gray-900 bg-white p-4">
  Отлично читается
</p>

<!-- ✅ Белый текст на тёмном (контраст 17:1) -->
<div class="bg-gray-900 text-white p-4">
  Тёмная тема
</div>
```

### Примеры плохих комбинаций

```html
<!-- ❌ Светло-серый на белом (контраст 1.6:1) -->
<p class="text-gray-300 bg-white">
  Не читается!
</p>

<!-- ❌ Жёлтый на белом (контраст 1.1:1) -->
<span class="text-yellow-300 bg-white">
  Невидимый текст
</span>

<!-- ❌ Красный на синем (контраст 2.1:1) -->
<button class="bg-blue-500 text-red-500">
  Плохая комбинация
</button>
```

### Инструменты для проверки

- 🔍 [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- 🔍 [Colour Contrast Analyser](https://www.tpgi.com/color-contrast-checker/) (десктоп)
- 🔍 DevTools → Accessibility panel (встроен в Chrome)

## 🎨 Практические паттерны

### 1. 🎯 Цветовая схема для статусов

```html
<!-- Success -->
<div class="bg-green-50 border border-green-200 text-green-800 p-4 rounded-lg">
  <div class="flex items-center gap-2">
    <span class="text-green-500">✓</span>
    <strong>Успешно!</strong>
  </div>
  <p class="mt-1 text-green-700 text-sm">Операция выполнена успешно.</p>
</div>

<!-- Warning -->
<div class="bg-yellow-50 border border-yellow-200 text-yellow-800 p-4 rounded-lg">
  <div class="flex items-center gap-2">
    <span class="text-yellow-500">⚠</span>
    <strong>Внимание!</strong>
  </div>
  <p class="mt-1 text-yellow-700 text-sm">Проверьте введённые данные.</p>
</div>

<!-- Error -->
<div class="bg-red-50 border border-red-200 text-red-800 p-4 rounded-lg">
  <div class="flex items-center gap-2">
    <span class="text-red-500">✕</span>
    <strong>Ошибка!</strong>
  </div>
  <p class="mt-1 text-red-700 text-sm">Не удалось выполнить операцию.</p>
</div>

<!-- Info -->
<div class="bg-blue-50 border border-blue-200 text-blue-800 p-4 rounded-lg">
  <div class="flex items-center gap-2">
    <span class="text-blue-500">ℹ</span>
    <strong>Информация</strong>
  </div>
  <p class="mt-1 text-blue-700 text-sm">Доступно обновление.</p>
</div>
```

### 2. 🌙 Светлая и тёмная тема

```html
<div class="bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100 p-6 rounded-lg">
  <h2 class="text-xl font-bold mb-2">Адаптивная карточка</h2>
  <p class="text-gray-600 dark:text-gray-400">
    Этот текст автоматически меняет цвет в зависимости от темы.
  </p>
  <button class="mt-4 bg-blue-500 hover:bg-blue-600 dark:bg-blue-600 dark:hover:bg-blue-700 text-white px-4 py-2 rounded">
    Действие
  </button>
</div>
```

### 3. 🏷️ Бейджи и теги

```html
<div class="flex flex-wrap gap-2">
  <span class="bg-blue-100 text-blue-800 text-xs font-medium px-2.5 py-0.5 rounded">
    Новое
  </span>
  <span class="bg-green-100 text-green-800 text-xs font-medium px-2.5 py-0.5 rounded">
    Активно
  </span>
  <span class="bg-yellow-100 text-yellow-800 text-xs font-medium px-2.5 py-0.5 rounded">
    В процессе
  </span>
  <span class="bg-red-100 text-red-800 text-xs font-medium px-2.5 py-0.5 rounded">
    Закрыто
  </span>
  <span class="bg-gray-100 text-gray-800 text-xs font-medium px-2.5 py-0.5 rounded">
    Черновик
  </span>
</div>
```

### 4. 🎨 Градиентные кнопки

```html
<!-- Простой градиент -->
<button class="bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 text-white font-medium px-6 py-3 rounded-lg shadow-lg transition">
  Премиум кнопка
</button>

<!-- Градиент с анимацией -->
<button class="bg-gradient-to-r from-pink-500 via-red-500 to-yellow-500 bg-[length:200%_auto] animate-gradient text-white font-bold px-6 py-3 rounded-lg">
  Радужная кнопка
</button>
```

### 5. 🎯 Semantic colors в дизайн-системе

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        // Семантические токены
        'surface': {
          DEFAULT: 'var(--surface)',
          secondary: 'var(--surface-secondary)',
          tertiary: 'var(--surface-tertiary)',
        },
        'content': {
          DEFAULT: 'var(--content)',
          secondary: 'var(--content-secondary)',
          disabled: 'var(--content-disabled)',
        },
        'border': {
          DEFAULT: 'var(--border)',
          focus: 'var(--border-focus)',
        },
      },
    },
  },
}
```

## 📊 Шпаргалка: что когда использовать

| Задача | Класс |
| :-- | :-- |
| Цвет текста | `text-blue-600` |
| Цвет фона | `bg-blue-500` |
| Цвет границы | `border-blue-500` |
| Focus ring | `ring-blue-500` |
| Прозрачность | `bg-blue-500/50` |
| Градиент | `bg-gradient-to-r from-blue-500 to-purple-600` |
| Кастомный цвет | `bg-[#ff5722]` |
| Dark mode | `bg-white dark:bg-gray-900` |
| Hover | `hover:bg-blue-600` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Использование слишком светлых оттенков для текста

```html
<!-- ❌ Плохо: не читается -->
<p class="text-blue-200 bg-white">Текст</p>

<!-- ✅ Хорошо: контрастно -->
<p class="text-blue-700 bg-white">Текст</p>
```

### ❌ Ошибка 2: Смешение разных палитр без системы

```html
<!-- ❌ Плохо: каша из цветов -->
<div class="bg-blue-500">
  <button class="bg-green-500">Кнопка</button>
  <span class="text-purple-500">Текст</span>
</div>

<!-- ✅ Хорошо: единая палитра -->
<div class="bg-blue-50">
  <button class="bg-blue-500 hover:bg-blue-600 text-white">Кнопка</button>
  <span class="text-blue-700">Текст</span>
</div>
```

### ❌ Ошибка 3: Забывают про dark mode

```html
<!-- ❌ Плохо: в тёмной теме не видно -->
<div class="bg-white text-gray-900">Карточка</div>

<!-- ✅ Хорошо: работает в обеих темах -->
<div class="bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100">
  Карточка
</div>
```

### ❌ Ошибка 4: Arbitrary values для часто используемых цветов

```html
<!-- ❌ Плохо: дублирование, нет консистентности -->
<div class="bg-[#ff5722]">...</div>
<div class="bg-[#ff5722]">...</div>
<div class="bg-[#ff5722]">...</div>

<!-- ✅ Хорошо: добавлено в конфиг -->
<div class="bg-brand">...</div>
```

## 🎯 Что дальше?

Теперь вы полностью владеете цветом в Tailwind! Но дизайн — это не только цвет. Следующий важный аспект — **типографика**.

**Следующий шаг:** [🔤 Типографика в Tailwind CSS](typography.md) — изучим работу со шрифтами, размерами, межстрочным интервалом и выравниванием.

---

> 💬 **Упражнение:** создайте карточку товара с градиентным фоном, бейджем статуса, ценой и кнопкой «Купить». Убедитесь, что все цветовые комбинации проходят проверку на контрастность!

---




<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: styling\effects.md -->
<!-- ═══════════════════════════════════════════════════════════ -->

# ✨ Эффекты и тени в Tailwind CSS

> **Полное руководство по визуальным эффектам:** от теней и прозрачности до фильтров размытия, яркости и режимов наложения

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Освоите все уровни теней (box-shadow)
- ✅ Научитесь управлять прозрачностью элементов
- ✅ Поймёте режимы наложения (mix-blend-mode)
- ✅ Освоите CSS-фильтры: blur, brightness, contrast, grayscale
- ✅ Создадите эффекты размытия фона (backdrop-filter)
- ✅ Настроите кастомные тени и фильтры
- ✅ Избежите типичных ошибок при работе с эффектами

## 🌫️ Тени: `shadow-{size}`

Tailwind предоставляет **8 предустановленных уровней теней**:

| Класс | CSS | Визуально |
| :-- | :-- | :-- |
| `shadow-sm` | `box-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05)` | Очень лёгкая тень |
| `shadow` | `box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)` | Лёгкая тень (по умолчанию) |
| `shadow-md` | `box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)` | Средняя тень |
| `shadow-lg` | `box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)` | Большая тень |
| `shadow-xl` | `box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1)` | Очень большая тень |
| `shadow-2xl` | `box-shadow: 0 25px 50px -12px rgb(0 0 0 / 0.25)` | Огромная тень |
| `shadow-inner` | `box-shadow: inset 0 2px 4px 0 rgb(0 0 0 / 0.05)` | Внутренняя тень |
| `shadow-none` | `box-shadow: 0 0 #0000` | Без тени |

```html
<!-- Без тени -->
<div class="bg-white p-6 rounded-lg shadow-none">Без тени</div>

<!-- Лёгкая тень -->
<div class="bg-white p-6 rounded-lg shadow-sm">Лёгкая тень</div>

<!-- Обычная тень -->
<div class="bg-white p-6 rounded-lg shadow">Обычная тень</div>

<!-- Средняя тень -->
<div class="bg-white p-6 rounded-lg shadow-md">Средняя тень</div>

<!-- Большая тень -->
<div class="bg-white p-6 rounded-lg shadow-lg">Большая тень</div>

<!-- Очень большая тень -->
<div class="bg-white p-6 rounded-lg shadow-xl">Очень большая тень</div>

<!-- Огромная тень -->
<div class="bg-white p-6 rounded-lg shadow-2xl">Огромная тень</div>

<!-- Внутренняя тень -->
<div class="bg-gray-100 p-6 rounded-lg shadow-inner">Внутренняя тень</div>
```

### Цветные тени

```html
<!-- Синяя тень -->
<div class="bg-blue-500 text-white p-6 rounded-lg shadow-lg shadow-blue-500/50">
  Синяя тень
</div>

<!-- Красная тень -->
<div class="bg-red-500 text-white p-6 rounded-lg shadow-lg shadow-red-500/50">
  Красная тень
</div>

<!-- Зелёная тень -->
<div class="bg-green-500 text-white p-6 rounded-lg shadow-lg shadow-green-500/50">
  Зелёная тень
</div>
```

### Arbitrary значения

```html
<!-- Кастомная тень -->
<div class="shadow-[0_10px_30px_-10px_rgba(59,130,246,0.5)] p-6 rounded-lg">
  Кастомная синяя тень
</div>
```

## 💧 Прозрачность: `opacity-{value}`

Управляет прозрачностью элемента (включая содержимое):

| Класс | CSS | Визуально |
| :-- | :-- | :-- |
| `opacity-0` | `opacity: 0` | Полностью прозрачный |
| `opacity-5` | `opacity: 0.05` | Почти невидимый |
| `opacity-10` | `opacity: 0.1` | Очень прозрачный |
| `opacity-20` | `opacity: 0.2` | Прозрачный |
| `opacity-25` | `opacity: 0.25` | |
| `opacity-30` | `opacity: 0.3` | |
| `opacity-40` | `opacity: 0.4` | |
| `opacity-50` | `opacity: 0.5` | Наполовину прозрачный |
| `opacity-60` | `opacity: 0.6` | |
| `opacity-70` | `opacity: 0.7` | |
| `opacity-75` | `opacity: 0.75` | |
| `opacity-80` | `opacity: 0.8` | Почти непрозрачный |
| `opacity-90` | `opacity: 0.9` | |
| `opacity-95` | `opacity: 0.95` | |
| `opacity-100` | `opacity: 1` | Полностью непрозрачный (по умолчанию) |

```html
<!-- Полностью непрозрачный -->
<div class="bg-blue-500 text-white p-4 opacity-100">100%</div>

<!-- 75% непрозрачности -->
<div class="bg-blue-500 text-white p-4 opacity-75">75%</div>

<!-- 50% непрозрачности -->
<div class="bg-blue-500 text-white p-4 opacity-50">50%</div>

<!-- 25% непрозрачности -->
<div class="bg-blue-500 text-white p-4 opacity-25">25%</div>

<!-- 10% непрозрачности -->
<div class="bg-blue-500 text-white p-4 opacity-10">10%</div>
```

### Hover-эффекты с прозрачностью

```html
<!-- Кнопка становится полупрозрачной при hover -->
<button class="bg-blue-500 text-white px-4 py-2 rounded hover:opacity-80 transition">
  Наведи на меня
</button>

<!-- Изображение становится полупрозрачным при hover -->
<img
  src="photo.jpg"
  class="rounded-lg hover:opacity-75 transition"
  alt="Фото"
>
```

### Disabled состояние

```html
<button class="bg-blue-500 text-white px-4 py-2 rounded disabled:opacity-50 disabled:cursor-not-allowed" disabled>
  Недоступная кнопка
</button>
```

## 🎨 Режимы наложения: `mix-blend-{mode}`

`mix-blend-mode` определяет, как элемент накладывается на фон:

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `mix-blend-normal` | `mix-blend-mode: normal` | Обычное наложение (по умолчанию) |
| `mix-blend-multiply` | `mix-blend-mode: multiply` | Умножение (темнее) |
| `mix-blend-screen` | `mix-blend-mode: screen` | Экран (светлее) |
| `mix-blend-overlay` | `mix-blend-mode: overlay` | Перекрытие |
| `mix-blend-darken` | `mix-blend-mode: darken` | Затемнение |
| `mix-blend-lighten` | `mix-blend-mode: lighten` | Осветление |
| `mix-blend-color-dodge` | `mix-blend-mode: color-dodge` | Осветление цвета |
| `mix-blend-color-burn` | `mix-blend-mode: color-burn` | Затемнение цвета |
| `mix-blend-hard-light` | `mix-blend-mode: hard-light` | Жёсткий свет |
| `mix-blend-soft-light` | `mix-blend-mode: soft-light` | Мягкий свет |
| `mix-blend-difference` | `mix-blend-mode: difference` | Разница |
| `mix-blend-exclusion` | `mix-blend-mode: exclusion` | Исключение |
| `mix-blend-hue` | `mix-blend-mode: hue` | Тон |
| `mix-blend-saturation` | `mix-blend-mode: saturation` | Насыщенность |
| `mix-blend-color` | `mix-blend-mode: color` | Цвет |
| `mix-blend-luminosity` | `mix-blend-mode: luminosity` | Светимость |

```html
<!-- Изображение с текстом поверх -->
<div class="relative">
  <img src="photo.jpg" class="w-full h-64 object-cover" alt="Фото">
  <div class="absolute inset-0 bg-blue-600 mix-blend-multiply flex items-center justify-center">
    <h2 class="text-4xl font-bold text-white">Multiply</h2>
  </div>
</div>

<!-- Текстовый эффект -->
<div class="relative bg-gradient-to-r from-purple-500 to-pink-500 p-8">
  <h1 class="text-6xl font-bold text-white mix-blend-overlay">
    Overlay Effect
  </h1>
</div>
```

### Background blend mode

```html
<!-- Градиент с изображением -->
<div
  class="h-64 bg-[url('/photo.jpg')] bg-cover"
  style="background-blend-mode: overlay; background-color: rgba(59, 130, 246, 0.5);"
>
  <!-- Контент -->
</div>
```

## 🔍 CSS-фильтры: `filter` и `blur`, `brightness`, `contrast`

Tailwind предоставляет утилиты для применения CSS-фильтров:

### Размытие: `blur-{size}`

| Класс | CSS |
| :-- | :-- |
| `blur-none` | `blur(0)` |
| `blur-sm` | `blur(4px)` |
| `blur` | `blur(8px)` |
| `blur-md` | `blur(12px)` |
| `blur-lg` | `blur(16px)` |
| `blur-xl` | `blur(24px)` |
| `blur-2xl` | `blur(40px)` |
| `blur-3xl` | `blur(64px)` |

```html
<!-- Размытое изображение -->
<img src="photo.jpg" class="blur-md rounded-lg" alt="Размытое фото">

<!-- Размытый фон -->
<div class="relative h-64">
  <img src="photo.jpg" class="absolute inset-0 w-full h-full object-cover blur-xl" alt="Фон">
  <div class="relative z-10 flex items-center justify-center h-full text-white text-2xl font-bold">
    Контент поверх размытого фона
  </div>
</div>
```

### Яркость: `brightness-{value}`

| Класс | CSS |
| :-- | :-- |
| `brightness-0` | `brightness(0)` |
| `brightness-50` | `brightness(.5)` |
| `brightness-75` | `brightness(.75)` |
| `brightness-90` | `brightness(.9)` |
| `brightness-95` | `brightness(.95)` |
| `brightness-100` | `brightness(1)` (по умолчанию) |
| `brightness-105` | `brightness(1.05)` |
| `brightness-110` | `brightness(1.1)` |
| `brightness-125` | `brightness(1.25)` |
| `brightness-150` | `brightness(1.5)` |
| `brightness-200` | `brightness(2)` |

```html
<!-- Затемнённое изображение -->
<img src="photo.jpg" class="brightness-75 rounded-lg" alt="Затемнённое фото">

<!-- Осветлённое изображение -->
<img src="photo.jpg" class="brightness-125 rounded-lg" alt="Осветлённое фото">
```

### Контрастность: `contrast-{value}`

| Класс | CSS |
| :-- | :-- |
| `contrast-0` | `contrast(0)` |
| `contrast-50` | `contrast(.5)` |
| `contrast-75` | `contrast(.75)` |
| `contrast-100` | `contrast(1)` (по умолчанию) |
| `contrast-125` | `contrast(1.25)` |
| `contrast-150` | `contrast(1.5)` |
| `contrast-200` | `contrast(2)` |

```html
<!-- Низкий контраст -->
<img src="photo.jpg" class="contrast-75 rounded-lg" alt="Низкий контраст">

<!-- Высокий контраст -->
<img src="photo.jpg" class="contrast-150 rounded-lg" alt="Высокий контраст">
```

### Оттенки серого: `grayscale-{value}`

| Класс | CSS |
| :-- | :-- |
| `grayscale-0` | `grayscale(0)` |
| `grayscale` | `grayscale(100%)` |

```html
<!-- Чёрно-белое изображение -->
<img src="photo.jpg" class="grayscale rounded-lg" alt="Ч/Б фото">

<!-- Hover-эффект: ч/б → цветное -->
<img
  src="photo.jpg"
  class="grayscale hover:grayscale-0 transition rounded-lg"
  alt="Фото"
>
```

### Поворот тона: `hue-rotate-{angle}`

| Класс | CSS |
| :-- | :-- |
| `hue-rotate-0` | `hue-rotate(0deg)` |
| `hue-rotate-15` | `hue-rotate(15deg)` |
| `hue-rotate-30` | `hue-rotate(30deg)` |
| `hue-rotate-60` | `hue-rotate(60deg)` |
| `hue-rotate-90` | `hue-rotate(90deg)` |
| `hue-rotate-180` | `hue-rotate(180deg)` |

```html
<!-- Изменение цвета изображения -->
<img src="photo.jpg" class="hue-rotate-90 rounded-lg" alt="Поворот тона">
```

### Инверсия: `invert-{value}`

| Класс | CSS |
| :-- | :-- |
| `invert-0` | `invert(0)` |
| `invert` | `invert(100%)` |

```html
<!-- Инвертированное изображение -->
<img src="photo.jpg" class="invert rounded-lg" alt="Инвертированное фото">
```

### Насыщенность: `saturate-{value}`

| Класс | CSS |
| :-- | :-- |
| `saturate-0` | `saturate(0)` |
| `saturate-50` | `saturate(.5)` |
| `saturate-100` | `saturate(1)` (по умолчанию) |
| `saturate-150` | `saturate(1.5)` |
| `saturate-200` | `saturate(2)` |

```html
<!-- Низкая насыщенность -->
<img src="photo.jpg" class="saturate-50 rounded-lg" alt="Низкая насыщенность">

<!-- Высокая насыщенность -->
<img src="photo.jpg" class="saturate-200 rounded-lg" alt="Высокая насыщенность">
```

### Сепия: `sepia-{value}`

| Класс | CSS |
| :-- | :-- |
| `sepia-0` | `sepia(0)` |
| `sepia` | `sepia(100%)` |

```html
<!-- Эффект сепии (старое фото) -->
<img src="photo.jpg" class="sepia rounded-lg" alt="Сепия">
```

### Комбинирование фильтров

```html
<!-- Несколько фильтров одновременно -->
<img
  src="photo.jpg"
  class="blur-sm brightness-110 contrast-125 saturate-150 rounded-lg"
  alt="Комбинированные фильтры"
>
```

## 🌫️ Backdrop-фильтры: `backdrop-blur`, `backdrop-brightness`

`backdrop-filter` применяет фильтры к **фону за элементом**, а не к самому элементу:

### Backdrop blur

```html
<!-- Стеклянный эффект -->
<div class="relative h-96 bg-[url('/photo.jpg')] bg-cover">
  <div class="absolute inset-0 bg-white/30 backdrop-blur-md">
    <div class="p-8">
      <h2 class="text-2xl font-bold">Стеклянная карточка</h2>
      <p>Контент поверх размытого фона</p>
    </div>
  </div>
</div>
```

Размеры backdrop blur такие же, как у обычного `blur`:

| Класс | CSS |
| :-- | :-- |
| `backdrop-blur-none` | `blur(0)` |
| `backdrop-blur-sm` | `blur(4px)` |
| `backdrop-blur` | `blur(8px)` |
| `backdrop-blur-md` | `blur(12px)` |
| `backdrop-blur-lg` | `blur(16px)` |
| `backdrop-blur-xl` | `blur(24px)` |
| `backdrop-blur-2xl` | `blur(40px)` |
| `backdrop-blur-3xl` | `blur(64px)` |

### Backdrop brightness, contrast и другие

```html
<!-- Затемнённый фон за элементом -->
<div class="relative h-96 bg-[url('/photo.jpg')] bg-cover">
  <div class="absolute inset-0 backdrop-brightness-50">
    <div class="p-8 text-white">
      <h2 class="text-2xl font-bold">Затемнённый фон</h2>
    </div>
  </div>
</div>
```

Доступные backdrop-фильтры:

- `backdrop-blur-{size}`
- `backdrop-brightness-{value}`
- `backdrop-contrast-{value}`
- `backdrop-grayscale-{value}`
- `backdrop-hue-rotate-{angle}`
- `backdrop-invert-{value}`
- `backdrop-opacity-{value}`
- `backdrop-saturate-{value}`
- `backdrop-sepia-{value}`

## 🎨 Практические паттерны

### 1. 🎴 Карточка с тенью при hover

```html
<div class="bg-white rounded-xl shadow-md hover:shadow-xl transition-shadow duration-300 p-6 max-w-sm">
  <h3 class="text-xl font-bold text-gray-900 mb-2">Интерактивная карточка</h3>
  <p class="text-gray-600 text-sm">
    Тень усиливается при наведении, создавая эффект поднятия.
  </p>
  <button class="mt-4 w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 rounded-lg transition">
    Действие
  </button>
</div>
```

### 2. 🖼️ Галерея с hover-эффектами

```html
<div class="grid grid-cols-3 gap-4">
  <div class="relative overflow-hidden rounded-lg group">
    <img
      src="photo1.jpg"
      class="w-full h-48 object-cover group-hover:scale-110 group-hover:brightness-75 transition duration-300"
      alt="Фото 1"
    >
    <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition">
      <span class="text-white text-lg font-bold">Просмотр</span>
    </div>
  </div>

  <div class="relative overflow-hidden rounded-lg group">
    <img
      src="photo2.jpg"
      class="w-full h-48 object-cover group-hover:scale-110 group-hover:brightness-75 transition duration-300"
      alt="Фото 2"
    >
    <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition">
      <span class="text-white text-lg font-bold">Просмотр</span>
    </div>
  </div>

  <div class="relative overflow-hidden rounded-lg group">
    <img
      src="photo3.jpg"
      class="w-full h-48 object-cover group-hover:scale-110 group-hover:brightness-75 transition duration-300"
      alt="Фото 3"
    >
    <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition">
      <span class="text-white text-lg font-bold">Просмотр</span>
    </div>
  </div>
</div>
```

### 3. 🪟 Glassmorphism навигация

```html
<nav class="sticky top-0 z-50 bg-white/80 backdrop-blur-lg border-b border-white/20 shadow-sm">
  <div class="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between">
    <div class="font-bold text-xl">Logo</div>
    <div class="flex gap-6">
      <a href="#" class="hover:text-blue-600 transition">Главная</a>
      <a href="#" class="hover:text-blue-600 transition">О нас</a>
      <a href="#" class="hover:text-blue-600 transition">Контакты</a>
    </div>
  </div>
</nav>
```

### 4. 🎨 Фильтры для изображений

```html
<div class="grid grid-cols-2 md:grid-cols-4 gap-4">
  <!-- Оригинал -->
  <div class="text-center">
    <img src="photo.jpg" class="rounded-lg mb-2" alt="Оригинал">
    <span class="text-sm text-gray-600">Оригинал</span>
  </div>

  <!-- Ч/Б -->
  <div class="text-center">
    <img src="photo.jpg" class="rounded-lg mb-2 grayscale" alt="Ч/Б">
    <span class="text-sm text-gray-600">Ч/Б</span>
  </div>

  <!-- Сепия -->
  <div class="text-center">
    <img src="photo.jpg" class="rounded-lg mb-2 sepia" alt="Сепия">
    <span class="text-sm text-gray-600">Сепия</span>
  </div>

  <!-- Размытие -->
  <div class="text-center">
    <img src="photo.jpg" class="rounded-lg mb-2 blur-sm" alt="Размытие">
    <span class="text-sm text-gray-600">Размытие</span>
  </div>
</div>
```

### 5. 🎯 Кнопка с цветной тенью

```html
<button class="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-6 py-3 rounded-lg shadow-lg shadow-blue-500/50 hover:shadow-xl hover:shadow-blue-500/60 transition-all duration-300">
  Кнопка с цветной тенью
</button>

<button class="bg-red-600 hover:bg-red-700 text-white font-semibold px-6 py-3 rounded-lg shadow-lg shadow-red-500/50 hover:shadow-xl hover:shadow-red-500/60 transition-all duration-300">
  Красная кнопка
</button>

<button class="bg-green-600 hover:bg-green-700 text-white font-semibold px-6 py-3 rounded-lg shadow-lg shadow-green-500/50 hover:shadow-xl hover:shadow-green-500/60 transition-all duration-300">
  Зелёная кнопка
</button>
```

### 6. 🌙 Затемнение изображения для текста

```html
<div class="relative h-96 bg-[url('/hero.jpg')] bg-cover bg-center">
  <!-- Градиентное затемнение -->
  <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/40 to-transparent"></div>

  <!-- Контент -->
  <div class="relative z-10 flex flex-col justify-end h-full p-8 text-white">
    <h2 class="text-4xl font-bold mb-2">Заголовок поверх фото</h2>
    <p class="text-lg text-gray-200">
      Подзаголовок с хорошим контрастом благодаря затемнению
    </p>
  </div>
</div>
```

### 7. 🎨 Изображение с mix-blend-mode

```html
<div class="relative bg-gradient-to-br from-purple-500 via-pink-500 to-orange-500 p-12">
  <img
    src="pattern.svg"
    class="w-full h-64 object-contain mix-blend-overlay"
    alt="Паттерн"
  >
  <h2 class="absolute inset-0 flex items-center justify-center text-6xl font-bold text-white mix-blend-overlay">
    Overlay Effect
  </h2>
</div>
```

## 📊 Шпаргалка: что когда использовать

| Задача | Классы |
| :-- | :-- |
| Лёгкая тень | `shadow-sm` |
| Обычная тень | `shadow` |
| Большая тень | `shadow-lg`, `shadow-xl` |
| Цветная тень | `shadow-lg shadow-blue-500/50` |
| Внутренняя тень | `shadow-inner` |
| Без тени | `shadow-none` |
| Прозрачность 50% | `opacity-50` |
| Hover прозрачность | `hover:opacity-80` |
| Disabled состояние | `disabled:opacity-50` |
| Размытие изображения | `blur-md`, `blur-lg` |
| Ч/Б изображение | `grayscale` |
| Сепия | `sepia` |
| Затемнение | `brightness-75` |
| Осветление | `brightness-125` |
| Контраст | `contrast-150` |
| Насыщенность | `saturate-150` |
| Стеклянный эффект | `bg-white/30 backdrop-blur-md` |
| Режим наложения | `mix-blend-multiply`, `mix-blend-overlay` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: `opacity` вместо `bg-{color}/{opacity}`

```html
<!-- ❌ Плохо: opacity делает прозрачным весь элемент вместе с содержимым -->
<div class="bg-blue-500 opacity-50 p-4">
  <p class="text-white">Текст тоже станет прозрачным!</p>
</div>

<!-- ✅ Хорошо: прозрачен только фон -->
<div class="bg-blue-500/50 p-4">
  <p class="text-white">Текст остаётся непрозрачным</p>
</div>
```

### ❌ Ошибка 2: Забывают `transition` для hover-эффектов

```html
<!-- ❌ Плохо: резкое изменение тени -->
<div class="shadow-md hover:shadow-xl">Карточка</div>

<!-- ✅ Хорошо: плавное изменение -->
<div class="shadow-md hover:shadow-xl transition-shadow duration-300">Карточка</div>
```

### ❌ Ошибка 3: `backdrop-blur` без полупрозрачного фона

```html
<!-- ❌ Плохо: backdrop-blur не виден на непрозрачном фоне -->
<div class="bg-white backdrop-blur-md">
  Размытие не работает
</div>

<!-- ✅ Хорошо: полупрозрачный фон -->
<div class="bg-white/50 backdrop-blur-md">
  Размытие видно
</div>
```

### ❌ Ошибка 4: Слишком много фильтров одновременно

```html
<!-- ❌ Плохо: перебор фильтров -->
<img
  src="photo.jpg"
  class="blur-sm brightness-150 contrast-200 grayscale sepia hue-rotate-180"
>

<!-- ✅ Хорошо: 2-3 фильтра максимум -->
<img
  src="photo.jpg"
  class="brightness-110 contrast-125 saturate-150"
>
```

### ❌ Ошибка 5: `backdrop-blur` на мобильных без проверки

```html
<!-- ❌ Плохо: backdrop-blur может тормозить на мобильных -->
<div class="backdrop-blur-xl bg-white/50">
  Тяжёлый эффект
</div>

<!-- ✅ Хорошо: используем только на десктопе -->
<div class="backdrop-blur-none md:backdrop-blur-xl bg-white/50 md:bg-white/30">
  Оптимизировано для мобильных
</div>
```

### ❌ Ошибка 6: Цветные тени без `shadow-{size}`

```html
<!-- ❌ Плохо: цветная тень без размера не видна -->
<div class="shadow-blue-500/50 p-4">Нет тени</div>

<!-- ✅ Хорошо: указываем размер + цвет -->
<div class="shadow-lg shadow-blue-500/50 p-4">Цветная тень видна</div>
```

## 🎯 Что дальше?

Теперь вы полностью владеете визуальными эффектами! Но дизайн — это не только эффекты. Следующий важный аспект — **адаптивность и responsive-дизайн**.

**Следующий шаг:** [📱 Breakpoints и адаптивный дизайн](../responsive/breakpoints.md) — изучим, как создавать интерфейсы, которые отлично выглядят на всех устройствах.

---

> 💬 **Упражнение:** создайте карточку товара с изображением, которое при hover становится ч/Б, усиливается тень карточки, и появляется стеклянная панель с информацией о товаре (с backdrop-blur). Используйте только effect-утилиты Tailwind!

---




<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: styling\typography.md -->
<!-- ═══════════════════════════════════════════════════════════ -->

# 🔤 Типографика в Tailwind CSS

> **Полное руководство по работе с текстом:** от размеров шрифтов до кастомных гарнитур, межстрочных интервалов и адаптивной типографики

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Освоите всю шкалу размеров шрифтов Tailwind
- ✅ Научитесь управлять жирностью, межстрочным интервалом и трекингом
- ✅ Сможете правильно выравнивать и декорировать текст
- ✅ Настроите кастомные шрифты (Google Fonts, локальные)
- ✅ Поймёте принципы иерархии и читаемости
- ✅ Освоите responsive-типографику
- ✅ Избежите типичных ошибок в работе с текстом

## 📏 Размеры шрифтов: `text-{size}`

Tailwind предоставляет **10 предустановленных размеров**, основанных на рем-единицах:

| Класс | Размер | Строка | Когда использовать |
| :-- | :-- | :-- | :-- |
| `text-xs` | 0.75rem (12px) | 1rem | Подписи, метки, бейджи |
| `text-sm` | 0.875rem (14px) | 1.25rem | Второстепенный текст, хелперы |
| `text-base` | 1rem (16px) | 1.5rem | Основной текст (по умолчанию) |
| `text-lg` | 1.125rem (18px) | 1.75rem | Вводные абзацы, подзаголовки |
| `text-xl` | 1.25rem (20px) | 1.75rem | Заголовки разделов |
| `text-2xl` | 1.5rem (24px) | 2rem | Подзаголовки страниц |
| `text-3xl` | 1.875rem (30px) | 2.25rem | Заголовки страниц |
| `text-4xl` | 2.25rem (36px) | 2.5rem | Большие заголовки |
| `text-5xl` | 3rem (48px) | 1 | Hero-секции |
| `text-6xl` | 3.75rem (60px) | 1 | Огромные заголовки |
| `text-7xl` | 4.5rem (72px) | 1 | Дисплейные заголовки |
| `text-8xl` | 6rem (96px) | 1 | Очень крупные акценты |
| `text-9xl` | 8rem (128px) | 1 | Экстремальные размеры |

```html
<!-- Типовая иерархия страницы -->
<h1 class="text-4xl font-bold">Главный заголовок</h1>
<h2 class="text-2xl font-semibold">Подзаголовок</h2>
<h3 class="text-xl font-medium">Заголовок раздела</h3>
<p class="text-base">Обычный текст параграфа.</p>
<small class="text-sm text-gray-500">Подпись или метка времени</small>
```

### Arbitrary значения для размеров

```html
<!-- Точный размер в пикселях -->
<h1 class="text-[42px]">Кастомный размер</h1>

<!-- В rem -->
<p class="text-[1.375rem]">Точный rem</p>
```

## 💪 Жирность шрифта: `font-{weight}`

| Класс | CSS | Визуально |
| :-- | :-- | :-- |
| `font-thin` | `font-weight: 100` | Очень тонкий |
| `font-extralight` | `font-weight: 200` | Extra light |
| `font-light` | `font-weight: 300` | Тонкий |
| `font-normal` | `font-weight: 400` | Обычный (по умолчанию) |
| `font-medium` | `font-weight: 500` | Средний |
| `font-semibold` | `font-weight: 600` | Полужирный |
| `font-bold` | `font-weight: 700` | Жирный |
| `font-extrabold` | `font-weight: 800` | Очень жирный |
| `font-black` | `font-weight: 900` | Чёрный (максимум) |

```html
<p class="font-light">Тонкий текст — для элегантности</p>
<p class="font-normal">Обычный текст — для читаемости</p>
<p class="font-medium">Средний — для акцентов</p>
<p class="font-semibold">Полужирный — для подзаголовков</p>
<p class="font-bold">Жирный — для заголовков</p>
```

> 💡 **Совет:** не все шрифты имеют все начертания. Google Fonts часто ограничивается 4–5 вариантами. Проверяйте доступность перед использованием.

## 📐 Межстрочный интервал: `leading-{value}`

`leading` управляет `line-height` — расстоянием между строками.

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `leading-none` | `line-height: 1` | Без отступов (для заголовков) |
| `leading-tight` | `line-height: 1.25` | Плотный (заголовки) |
| `leading-snug` | `line-height: 1.375` | Умеренно плотный |
| `leading-normal` | `line-height: 1.5` | Нормальный (по умолчанию) |
| `leading-relaxed` | `line-height: 1.625` | Свободный (для длинных текстов) |
| `leading-loose` | `line-height: 2` | Очень свободный |
| `leading-3` ... `leading-10` | Фиксированные rem | Точный контроль |

```html
<!-- Заголовок: плотный интервал -->
<h1 class="text-4xl font-bold leading-tight">
  Заголовок с плотным межстрочным интервалом
</h1>

<!-- Параграф: свободный интервал для читаемости -->
<p class="text-base leading-relaxed max-w-prose">
  Длинный текст с комфортным межстрочным интервалом.
  Чем длиннее абзац, тем важнее свободный leading.
  Это улучшает читаемость и снижает усталость глаз.
</p>
```

> 💡 **Правило:** для заголовков — `leading-tight` или `leading-none`. Для параграфов — `leading-relaxed` или `leading-loose`.

## 🔠 Трекинг (межбуквенный интервал): `tracking-{value}`

| Класс | CSS | Когда использовать |
| :-- | :-- | :-- |
| `tracking-tighter` | `-0.05em` | Крупные заголовки |
| `tracking-tight` | `-0.025em` | Заголовки |
| `tracking-normal` | `0em` | Обычный текст |
| `tracking-wide` | `0.025em` | Подзаголовки |
| `tracking-wider` | `0.05em` | UPPERCASE-подписи |
| `tracking-widest` | `0.1em` | Декоративные элементы |

```html
<!-- Заголовок с узким трекингом — выглядит компактнее -->
<h1 class="text-5xl font-bold tracking-tight">
  Заголовок
</h1>

<!-- Подпись капсом с широким трекингом -->
<span class="text-xs font-semibold uppercase tracking-widest text-gray-500">
  Категория статьи
</span>
```

## 🎯 Выравнивание текста: `text-{align}`

| Класс | CSS |
| :-- | :-- |
| `text-left` | `text-align: left` |
| `text-center` | `text-align: center` |
| `text-right` | `text-align: right` |
| `text-justify` | `text-align: justify` |
| `text-start` | `text-align: start` (с учётом RTL) |
| `text-end` | `text-align: end` (с учётом RTL) |

```html
<p class="text-left">По левому краю (по умолчанию)</p>
<p class="text-center">По центру</p>
<p class="text-right">По правому краю</p>
<p class="text-justify">
  По ширине — текст растягивается на всю строку.
  Используется в книжной вёрстке, но в вебе с осторожностью.
</p>
```

## ✏️ Декорирование текста: `underline`, `line-through`

| Класс | CSS |
| :-- | :-- |
| `underline` | `text-decoration-line: underline` |
| `overline` | `text-decoration-line: overline` |
| `line-through` | `text-decoration-line: line-through` |
| `no-underline` | `text-decoration-line: none` |

### Стиль подчёркивания

| Класс | CSS |
| :-- | :-- |
| `decoration-solid` | Сплошная линия |
| `decoration-double` | Двойная линия |
| `decoration-dotted` | Точечная |
| `decoration-dashed` | Пунктирная |
| `decoration-wavy` | Волнистая (для ошибок) |

### Толщина и отступ

```html
<!-- Толщина -->
<a href="#" class="underline decoration-1">Тонкое подчёркивание</a>
<a href="#" class="underline decoration-2">Среднее</a>
<a href="#" class="underline decoration-4">Толстое</a>

<!-- Отступ от текста -->
<a href="#" class="underline underline-offset-2">С отступом 2px</a>
<a href="#" class="underline underline-offset-4">С отступом 4px</a>
<a href="#" class="underline underline-offset-8">С большим отступом</a>

<!-- Цвет подчёркивания -->
<a href="#" class="underline decoration-blue-500">Синее подчёркивание</a>
```

```html
<!-- Зачёркнутая цена (скидка) -->
<div class="flex items-center gap-2">
  <span class="text-gray-400 line-through">2 990 ₽</span>
  <span class="text-red-500 font-bold">1 990 ₽</span>
</div>
```

## 🔄 Трансформация текста: `uppercase`, `lowercase`, `capitalize`

| Класс | Результат |
| :-- | :-- |
| `uppercase` | `ВСЕ БУКВЫ ЗАГЛАВНЫЕ` |
| `lowercase` | `все буквы строчные` |
| `capitalize` | `Каждое Слово С Заглавной` |
| `normal-case` | `Как в оригинале` |

```html
<!-- Бейдж категории -->
<span class="text-xs font-semibold uppercase tracking-wider text-blue-600">
  Новинка
</span>

<!-- Заголовок с капитализацией -->
<h2 class="text-2xl capitalize">заголовок статьи</h2>
```

> ⚠️ **Важно:** `capitalize` работает только с латиницей. Для кириллицы и других языков используйте CSS `text-transform` с осторожностью или преобразуйте текст на стороне сервера/клиента.

## 📦 Перенос слов и обрезка: `truncate`, `break-*`

### Обрезка с многоточием

```html
<!-- Однострочная обрезка -->
<p class="truncate max-w-xs">
  Очень длинный заголовок, который не помещается в одну строку и будет обрезан с многоточием
</p>
```

`truncate` = `overflow-hidden` + `text-ellipsis` + `whitespace-nowrap`

### Перенос слов

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `break-normal` | `overflow-wrap: normal` | Без переноса |
| `break-words` | `overflow-wrap: break-word` | Перенос по словам |
| `break-all` | `word-break: break-all` | Перенос в любом месте |
| `break-keep` | `word-break: keep-all` | Сохранять слова |

```html
<!-- Длинная ссылка переносится -->
<a href="#" class="break-words text-blue-500">
  https://example.com/very/long/url/that/needs/to/break/properly
</a>

<!-- Код или хеши — перенос в любом месте -->
<code class="break-all text-sm">
  550e8400e29b41d4a716446655440000
</code>
```

### Многострочная обрезка (line-clamp)

```html
<!-- Обрезать после 2 строк -->
<p class="line-clamp-2">
  Очень длинный текст, который будет обрезан после второй строки.
  Остальной текст не будет виден, а в конце появится многоточие.
  Это полезно для карточек с превью контента.
</p>

<!-- 3 строки -->
<p class="line-clamp-3">...</p>

<!-- Без ограничений -->
<p class="line-clamp-none">...</p>
```

## 🔤 Шрифты: `font-{family}`

По умолчанию Tailwind предоставляет три семейства:

| Класс | CSS | Применение |
| :-- | :-- | :-- |
| `font-sans` | `ui-sans-serif, system-ui, ...` | Основной текст, UI |
| `font-serif` | `ui-serif, Georgia, ...` | Статьи, блоги, книги |
| `font-mono` | `ui-monospace, SFMono-Regular, ...` | Код, технические данные |

```html
<p class="font-sans">Основной текст без засечек</p>
<p class="font-serif">Текст с засечками для статей</p>
<code class="font-mono bg-gray-100 px-1">const x = 42;</code>
```

### Подключение кастомных шрифтов

#### Вариант 1: Google Fonts через CDN

```html
<!-- В <head> -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
```

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Inter', 'system-ui', 'sans-serif'],
        'display': ['"Playfair Display"', 'serif'],
      },
    },
  },
}
```

```html
<h1 class="font-display text-5xl">Заголовок с засечками</h1>
<p class="font-sans">Обычный текст с Inter</p>
```

#### Вариант 2: Локальные шрифты

```css
/* styles.css */
@font-face {
  font-family: 'CustomFont';
  src: url('/fonts/custom.woff2') format('woff2');
  font-weight: 400;
  font-display: swap;
}
```

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        'custom': ['CustomFont', 'sans-serif'],
      },
    },
  },
}
```

## 📝 Отступ первой строки: `indent-{size}`

```html
<!-- Красная строка -->
<p class="indent-8">
  Первая строка этого абзаца будет иметь отступ.
  Это классический приём книжной вёрстки.
  Остальные строки начинаются с левого края.
</p>
```

## 📏 Вертикальное выравнивание: `align-{value}`

Работает для инлайновых и inline-block элементов:

| Класс | CSS |
| :-- | :-- |
| `align-baseline` | `vertical-align: baseline` |
| `align-top` | `vertical-align: top` |
| `align-middle` | `vertical-align: middle` |
| `align-bottom` | `vertical-align: bottom` |
| `align-text-top` | `vertical-align: text-top` |
| `align-text-bottom` | `vertical-align: text-bottom` |
| `align-sub` | `vertical-align: sub` |
| `align-super` | `vertical-align: super` |

```html
<!-- Иконка по центру текста -->
<p>
  Текст
  <svg class="inline w-4 h-4 align-middle" viewBox="0 0 24 24">...</svg>
  и иконка
</p>

<!-- Верхний индекс -->
<p>E = mc<sup class="align-super text-xs">2</sup></p>
```

## 🌫️ Белый пробел: `whitespace-{value}`

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `whitespace-normal` | `white-space: normal` | Переносы работают |
| `whitespace-nowrap` | `white-space: nowrap` | Без переносов |
| `whitespace-pre` | `white-space: pre` | Как `<pre>` |
| `whitespace-pre-line` | `white-space: pre-line` | Сохраняет переносы строк |
| `whitespace-pre-wrap` | `white-space: pre-wrap` | Сохраняет всё + переносы |
| `whitespace-break-spaces` | `white-space: break-spaces` | Как pre-wrap + перенос по пробелам |

```html
<!-- Код с сохранением форматирования -->
<pre class="whitespace-pre-wrap bg-gray-100 p-4 rounded">
function hello() {
  console.log("Привет!");
}
</pre>

<!-- Однострочный текст без переносов -->
<div class="whitespace-nowrap overflow-hidden">
  Очень длинная строка, которая не будет переноситься на новую строку
</div>
```

## 📱 Responsive типограграфика

Меняйте размеры и параметры на разных экранах:

```html
<!-- Mobile-first подход -->
<h1 class="text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-bold">
  Адаптивный заголовок
</h1>

<p class="text-sm sm:text-base md:text-lg leading-relaxed">
  Адаптивный параграф с комфортной читаемостью на всех устройствах.
</p>
```

### Clamp для плавной типографики

```html
<!-- Плавное изменение размера от 1.5rem до 3rem -->
<h1 class="text-[clamp(1.5rem,5vw,3rem)] font-bold">
  Плавный заголовок
</h1>
```

## 🎨 Практические паттерны

### 1. 📰 Типовая иерархия статьи

```html
<article class="max-w-prose mx-auto px-4">
  <!-- Категория -->
  <span class="text-xs font-semibold uppercase tracking-wider text-blue-600">
    Технологии
  </span>

  <!-- Заголовок -->
  <h1 class="mt-2 text-4xl font-bold tracking-tight text-gray-900">
    Как правильно использовать типографику в вебе
  </h1>

  <!-- Метаданные -->
  <div class="mt-4 flex items-center gap-2 text-sm text-gray-500">
    <span>Иван Иванов</span>
    <span>·</span>
    <time>5 июня 2026</time>
    <span>·</span>
    <span>7 мин чтения</span>
  </div>

  <!-- Вводный абзац -->
  <p class="mt-6 text-lg text-gray-600 leading-relaxed">
    Типографика — это основа любого интерфейса. Правильно подобранные
    шрифты, размеры и интервалы делают контент читаемым и приятным.
  </p>

  <!-- Подзаголовок -->
  <h2 class="mt-8 text-2xl font-semibold text-gray-900">
    Размеры шрифтов
  </h2>

  <!-- Параграф -->
  <p class="mt-4 text-base text-gray-700 leading-relaxed">
    Tailwind предлагает удобную шкалу размеров от <code class="font-mono text-sm bg-gray-100 px-1">text-xs</code>
    до <code class="font-mono text-sm bg-gray-100 px-1">text-9xl</code>.
  </p>

  <!-- Цитата -->
  <blockquote class="mt-6 border-l-4 border-blue-500 pl-4 italic text-gray-600">
    «Типографика — это одежда языка.»
    <footer class="mt-2 text-sm not-italic text-gray-500">— Эрик Шпикерман</footer>
  </blockquote>
</article>
```

### 2. 🏷️ Карточка с иерархией

```html
<div class="bg-white rounded-xl shadow-md p-6 max-w-sm">
  <span class="text-xs font-semibold uppercase tracking-wider text-purple-600">
    Премиум
  </span>
  <h3 class="mt-2 text-xl font-bold text-gray-900">
    Название продукта
  </h3>
  <p class="mt-2 text-sm text-gray-600 leading-relaxed line-clamp-3">
    Краткое описание продукта, которое может быть длинным и занимать несколько строк.
  </p>
  <div class="mt-4 flex items-baseline gap-2">
    <span class="text-2xl font-bold text-gray-900">2 990 ₽</span>
    <span class="text-sm text-gray-400 line-through">3 990 ₽</span>
  </div>
  <button class="mt-4 w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 rounded-lg">
    Купить
  </button>
</div>
```

### 3. 💻 Блок кода

```html
<div class="bg-gray-900 rounded-lg p-4 overflow-x-auto">
  <div class="flex items-center justify-between mb-3">
    <span class="text-xs font-mono text-gray-400">script.js</span>
    <button class="text-xs text-gray-400 hover:text-white">Копировать</button>
  </div>
  <pre class="text-sm font-mono text-gray-100 leading-relaxed"><code>function greet(name) {
  console.log(`Hello, ${name}!`);
}

greet('World');</code></pre>
</div>
```

### 4. 📊 Статистика с крупной цифрой

```html
<div class="text-center">
  <div class="text-5xl font-bold tracking-tight text-blue-600">
    80K+
  </div>
  <div class="mt-2 text-sm font-medium uppercase tracking-wider text-gray-500">
    Звёзд на GitHub
  </div>
</div>
```

## 📊 Шпаргалка: что когда использовать

| Задача | Классы |
| :-- | :-- |
| Заголовок H1 | `text-4xl font-bold tracking-tight` |
| Заголовок H2 | `text-2xl font-semibold` |
| Заголовок H3 | `text-xl font-medium` |
| Основной текст | `text-base leading-relaxed` |
| Мелкий текст | `text-sm text-gray-600` |
| Подпись | `text-xs uppercase tracking-wider` |
| Ссылка | `text-blue-600 underline underline-offset-2` |
| Код inline | `font-mono text-sm bg-gray-100 px-1` |
| Блок кода | `font-mono text-sm bg-gray-900 text-gray-100` |
| Зачёркнутая цена | `line-through text-gray-400` |
| Обрезка 1 строка | `truncate` |
| Обрезка N строк | `line-clamp-2`, `line-clamp-3` |
| Красная строка | `indent-8` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Слишком много размеров шрифтов на странице

```html
<!-- ❌ Плохо: 8 разных размеров — хаос -->
<h1 class="text-5xl">...</h1>
<h2 class="text-[28px]">...</h2>
<h3 class="text-[19px]">...</h3>
<p class="text-[15px]">...</p>

<!-- ✅ Хорошо: 4-5 размеров из шкалы -->
<h1 class="text-4xl">...</h1>
<h2 class="text-2xl">...</h2>
<h3 class="text-xl">...</h3>
<p class="text-base">...</p>
<small class="text-sm">...</small>
```

### ❌ Ошибка 2: Забывают про `max-w-prose` для длинных текстов

```html
<!-- ❌ Плохо: строка на весь экран — тяжело читать -->
<p class="text-base">Очень длинный текст на всю ширину экрана...</p>

<!-- ✅ Хорошо: комфортная ширина 65-75 символов -->
<p class="text-base leading-relaxed max-w-prose">
  Длинный текст с комфортной шириной строки.
</p>
```

### ❌ Ошибка 3: `text-justify` без hyphens

```html
<!-- ❌ Плохо: большие пробелы между словами -->
<p class="text-justify">Длинный текст...</p>

<!-- ✅ Хорошо: добавить переносы -->
<p class="text-justify hyphens-auto">Длинный текст...</p>
```

### ❌ Ошибка 4: Неподходящий leading для заголовков

```html
<!-- ❌ Плохо: заголовок с обычным leading выглядит рыхло -->
<h1 class="text-5xl leading-relaxed">Заголовок</h1>

<!-- ✅ Хорошо: плотный leading для крупных заголовков -->
<h1 class="text-5xl leading-tight">Заголовок</h1>
```

### ❌ Ошибка 5: Игнорируют `font-display: swap`

```css
/* ❌ Плохо: текст не виден, пока шрифт грузится */
@font-face {
  font-family: 'Custom';
  src: url('custom.woff2');
}

/* ✅ Хорошо: сразу показываем fallback */
@font-face {
  font-family: 'Custom';
  src: url('custom.woff2');
  font-display: swap;
}
```

## 🎯 Что дальше?

Теперь вы мастерски владеете типографикой! Но визуальный стиль — это не только текст. Следующий важный аспект — **фоны и фоновые изображения**.

**Следующий шаг:** [🖼️ Фоны в Tailwind CSS](backgrounds.md) — изучим работу с фонами, изображениями, градиентами и эффектами размытия.

---

> 💬 **Упражнение:** сверстайте карточку блога с категорией, заголовком, мета-данными (автор, дата), вводным абзацем (обрезанным до 3 строк) и кнопкой «Читать далее». Используйте только типографические утилиты Tailwind!

---




---

# 📱 Раздел: Responsive

---



<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: responsive\breakpoints.md -->
<!-- ═══════════════════════════════════════════════════════════ -->

# 📱 Breakpoints и адаптивный дизайн в Tailwind CSS

> **Полное руководство по созданию адаптивных интерфейсов:** от mobile-first подхода до сложных responsive-паттернов и container queries

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Поймёте философию mobile-first подхода в Tailwind
- ✅ Освоите все 6 предустановленных breakpoints
- ✅ Научитесь создавать адаптивные макеты без медиа-запросов
- ✅ Сможете управлять скрытием/показом элементов на разных экранах
- ✅ Освоите адаптивную типографику и отступы
- ✅ Поймёте разницу между responsive и container queries
- ✅ Избежите типичных ошибок при создании адаптивных интерфейсов

## 🎯 Mobile-first подход

**Tailwind CSS использует mobile-first подход** — это означает, что **базовые стили применяются ко всем экранам**, а **responsive-модификаторы добавляются для больших экранов**.

```
┌─────────────────────────────────────────────────────────┐
│  Базовые стили (работают везде)                         │
│  + sm:  → от 640px                                      │
│  + md:  → от 768px                                      │
│  + lg:  → от 1024px                                     │
│  + xl:  → от 1280px                                     │
│  + 2xl: → от 1536px                                     │
└─────────────────────────────────────────────────────────┘
```

### Почему mobile-first?

1. 📱 **Мобильный трафик доминирует** — 60%+ пользователей заходят с мобильных
2. ⚡ **Производительность** — мобильные устройства получают минимальный CSS
3. 🎯 **Прогрессивное улучшение** — начинаем с базового опыта, добавляем сложность
4. 🧠 **Проще думать** — легче добавлять стили для больших экранов, чем переписывать для мобильных

## 📏 Предустановленные breakpoints

Tailwind предоставляет **6 breakpoints** по умолчанию:

| Префикс | Минимальная ширина | Типичное устройство |
| :-- | :-- | :-- |
| *(без префикса)* | `0px` | Мобильные (базовые стили) |
| `sm:` | `640px` (40rem) | Большие мобильные, маленькие планшеты |
| `md:` | `768px` (48rem) | Планшеты |
| `lg:` | `1024px` (64rem) | Маленькие ноутбуки, ландшафтные планшеты |
| `xl:` | `1280px` (80rem) | Десктопы, ноутбуки |
| `2xl:` | `1536px` (96rem) | Большие десктопы |

### Как это работает

```html
<!-- Базовый стиль: 1 колонка на всех экранах -->
<!-- sm: 2 колонки от 640px -->
<!-- md: 3 колонки от 768px -->
<!-- lg: 4 колонки от 1024px -->
<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
  <div class="bg-blue-500 p-4 text-white">1</div>
  <div class="bg-blue-500 p-4 text-white">2</div>
  <div class="bg-blue-500 p-4 text-white">3</div>
  <div class="bg-blue-500 p-4 text-white">4</div>
</div>
```

## 🔧 Синтаксис responsive-классов

Responsive-модификаторы добавляются **перед любым утилитарным классом** через двоеточие:

```html
<!-- Формат: breakpoint:utility-class -->
<div class="text-sm md:text-base lg:text-lg xl:text-xl">
  Адаптивный размер текста
</div>

<div class="p-4 md:p-6 lg:p-8">
  Адаптивные отступы
</div>

<div class="flex flex-col md:flex-row lg:flex-row-reverse">
  Адаптивное направление flex
</div>
```

### Комбинирование нескольких breakpoints

```html
<!-- Мобильные: красный фон -->
<!-- Планшеты: синий фон -->
<!-- Десктопы: зелёный фон -->
<div class="bg-red-500 md:bg-blue-500 lg:bg-green-500 p-4 text-white">
  Меняет цвет на разных экранах
</div>
```

## 🎨 Адаптивная типограграфика

### Размеры шрифтов

```html
<!-- Mobile-first: маленький → большой -->
<h1 class="text-2xl sm:text-3xl md:text-4xl lg:text-5xl xl:text-6xl font-bold">
  Адаптивный заголовок
</h1>

<p class="text-sm sm:text-base md:text-lg leading-relaxed">
  Адаптивный параграф с комфортной читаемостью на всех устройствах.
</p>
```

### Межстрочный интервал

```html
<!-- Плотный на мобильных, свободный на десктопе -->
<p class="text-base leading-snug md:leading-relaxed lg:leading-loose">
  Длинный текст с адаптивным межстрочным интервалом.
  На мобильных — плотный, на десктопе — свободный.
</p>
```

### Выравнивание

```html
<!-- Мобильные: по центру -->
<!-- Десктоп: по левому краю -->
<h2 class="text-center md:text-left text-2xl font-bold">
  Адаптивное выравнивание
</h2>
```

## 📐 Адаптивные отступы и размеры

### Padding и margin

```html
<!-- Мобильные: маленькие отступы -->
<!-- Десктоп: большие отступы -->
<div class="p-4 sm:p-6 md:p-8 lg:p-12">
  Адаптивные отступы
</div>

<!-- Асимметричные отступы -->
<div class="px-4 py-8 md:px-8 md:py-12 lg:px-16 lg:py-16">
  Контент с адаптивными отступами
</div>
```

### Ширина и высота

```html
<!-- Мобильные: 100% ширины -->
<!-- Планшеты: 50% ширины -->
<!-- Десктоп: 33% ширины -->
<div class="w-full md:w-1/2 lg:w-1/3 bg-blue-500 p-4 text-white">
  Адаптивная ширина
</div>

<!-- Фиксированная ширина на десктопе -->
<div class="w-full md:w-96 bg-gray-100 p-4">
  Контент
</div>
```

### Max-width

```html
<!-- Ограничение ширины контента -->
<article class="max-w-sm md:max-w-2xl lg:max-w-4xl mx-auto px-4">
  <h1 class="text-2xl md:text-4xl font-bold mb-4">Статья</h1>
  <p class="text-base md:text-lg leading-relaxed">
    Длинный текст статьи с комфортной шириной для чтения.
  </p>
</article>
```

## 🎭 Скрытие и показ элементов

### `hidden` и `block`

```html
<!-- Показывать только на мобильных -->
<div class="block md:hidden">
  Мобильное меню (гамбургер)
</div>

<!-- Показывать только на десктопе -->
<div class="hidden md:block">
  Десктопное меню (горизонтальное)
</div>

<!-- Скрыть на мобильных, показать на планшетах+ -->
<div class="hidden sm:block">
  Контент для планшетов и десктопов
</div>
```

### Таблица видимости

| Класс | Мобильные | Планшеты | Десктоп |
| :-- | :--: | :--: | :--: |
| `block` | ✅ | ✅ | ✅ |
| `hidden` | ❌ | ❌ | ❌ |
| `sm:hidden` | ✅ | ❌ | ❌ |
| `md:hidden` | ✅ | ✅ | ❌ |
| `lg:hidden` | ✅ | ✅ | ✅ |
| `sm:block` | ❌ | ✅ | ✅ |
| `md:block` | ❌ | ❌ | ✅ |

```html
<!-- Показывать только на мобильных и планшетах -->
<div class="block lg:hidden">
  Контент для мобильных и планшетов
</div>

<!-- Показывать только на планшетах -->
<div class="hidden md:block lg:hidden">
  Контент только для планшетов
</div>
```

### Inline, flex, grid и другие display

```html
<!-- Адаптивный display -->
<div class="block md:flex lg:grid grid-cols-3 gap-4">
  <div>Элемент 1</div>
  <div>Элемент 2</div>
  <div>Элемент 3</div>
</div>
```

## 🎯 Практические паттерны

### 1. 📱 Адаптивная навигация

```html
<nav class="bg-white shadow-md">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">
      <!-- Логотип -->
      <div class="flex-shrink-0 font-bold text-xl">Logo</div>

      <!-- Десктопное меню -->
      <div class="hidden md:flex space-x-8">
        <a href="#" class="text-gray-700 hover:text-blue-600 transition">Главная</a>
        <a href="#" class="text-gray-700 hover:text-blue-600 transition">О нас</a>
        <a href="#" class="text-gray-700 hover:text-blue-600 transition">Услуги</a>
        <a href="#" class="text-gray-700 hover:text-blue-600 transition">Контакты</a>
      </div>

      <!-- Мобильная кнопка меню -->
      <div class="md:hidden">
        <button class="text-gray-700 hover:text-blue-600">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
          </svg>
        </button>
      </div>
    </div>
  </div>
</nav>
```

### 2. 🎴 Адаптивная сетка карточек

```html
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
  <!-- Карточка 1 -->
  <div class="bg-white rounded-lg shadow-md overflow-hidden">
    <img src="product1.jpg" class="w-full h-48 object-cover" alt="Товар 1">
    <div class="p-4">
      <h3 class="text-lg font-bold mb-2">Товар 1</h3>
      <p class="text-gray-600 text-sm mb-4">Описание товара</p>
      <div class="flex items-center justify-between">
        <span class="text-xl font-bold text-blue-600">1 990 ₽</span>
        <button class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded transition">
          Купить
        </button>
      </div>
    </div>
  </div>

  <!-- Карточка 2 -->
  <div class="bg-white rounded-lg shadow-md overflow-hidden">
    <img src="product2.jpg" class="w-full h-48 object-cover" alt="Товар 2">
    <div class="p-4">
      <h3 class="text-lg font-bold mb-2">Товар 2</h3>
      <p class="text-gray-600 text-sm mb-4">Описание товара</p>
      <div class="flex items-center justify-between">
        <span class="text-xl font-bold text-blue-600">2 490 ₽</span>
        <button class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded transition">
          Купить
        </button>
      </div>
    </div>
  </div>

  <!-- Карточка 3 -->
  <div class="bg-white rounded-lg shadow-md overflow-hidden">
    <img src="product3.jpg" class="w-full h-48 object-cover" alt="Товар 3">
    <div class="p-4">
      <h3 class="text-lg font-bold mb-2">Товар 3</h3>
      <p class="text-gray-600 text-sm mb-4">Описание товара</p>
      <div class="flex items-center justify-between">
        <span class="text-xl font-bold text-blue-600">3 290 ₽</span>
        <button class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded transition">
          Купить
        </button>
      </div>
    </div>
  </div>
</div>
```

### 3. 📄 Адаптивный layout с сайдбаром

```html
<div class="min-h-screen bg-gray-100">
  <div class="flex flex-col lg:flex-row">
    <!-- Сайдбар -->
    <aside class="w-full lg:w-64 bg-white shadow-md lg:min-h-screen">
      <div class="p-4">
        <h2 class="text-lg font-bold mb-4">Меню</h2>
        <nav class="space-y-2">
          <a href="#" class="block py-2 px-4 rounded hover:bg-gray-100">Главная</a>
          <a href="#" class="block py-2 px-4 rounded hover:bg-gray-100">Профиль</a>
          <a href="#" class="block py-2 px-4 rounded hover:bg-gray-100">Настройки</a>
        </nav>
      </div>
    </aside>

    <!-- Основной контент -->
    <main class="flex-1 p-4 lg:p-8">
      <h1 class="text-2xl lg:text-3xl font-bold mb-6">Дашборд</h1>
      <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
        <!-- Виджеты -->
        <div class="bg-white rounded-lg shadow p-6">
          <h3 class="font-bold mb-2">Виджет 1</h3>
          <p class="text-gray-600">Содержимое виджета</p>
        </div>
        <div class="bg-white rounded-lg shadow p-6">
          <h3 class="font-bold mb-2">Виджет 2</h3>
          <p class="text-gray-600">Содержимое виджета</p>
        </div>
        <div class="bg-white rounded-lg shadow p-6">
          <h3 class="font-bold mb-2">Виджет 3</h3>
          <p class="text-gray-600">Содержимое виджета</p>
        </div>
      </div>
    </main>
  </div>
</div>
```

### 4. 🖼️ Адаптивная hero-секция

```html
<section class="relative bg-gradient-to-br from-blue-600 to-purple-700 text-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 md:py-20 lg:py-32">
    <div class="flex flex-col lg:flex-row items-center gap-8 lg:gap-16">
      <!-- Текст -->
      <div class="flex-1 text-center lg:text-left">
        <h1 class="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-bold mb-4 leading-tight">
          Создавайте красивые интерфейсы
        </h1>
        <p class="text-lg sm:text-xl md:text-2xl text-blue-100 mb-8 max-w-2xl mx-auto lg:mx-0">
          Tailwind CSS — utility-first фреймворк для быстрой разработки
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start">
          <button class="bg-white text-blue-600 font-semibold px-8 py-3 rounded-lg hover:bg-gray-100 transition">
            Начать
          </button>
          <button class="border-2 border-white text-white font-semibold px-8 py-3 rounded-lg hover:bg-white/10 transition">
            Документация
          </button>
        </div>
      </div>

      <!-- Изображение -->
      <div class="flex-1 w-full max-w-md lg:max-w-lg">
        <img src="hero-illustration.svg" alt="Иллюстрация" class="w-full">
      </div>
    </div>
  </div>
</section>
```

### 5. 📊 Адаптивная таблица

```html
<!-- Мобильные: карточки -->
<!-- Десктоп: таблица -->
<div class="space-y-4 md:hidden">
  <!-- Карточка 1 -->
  <div class="bg-white rounded-lg shadow p-4">
    <div class="flex justify-between items-start mb-2">
      <h3 class="font-bold">Пользователь 1</h3>
      <span class="bg-green-100 text-green-800 text-xs px-2 py-1 rounded">Активен</span>
    </div>
    <p class="text-sm text-gray-600">user1@example.com</p>
    <p class="text-sm text-gray-600">Роль: Администратор</p>
  </div>

  <!-- Карточка 2 -->
  <div class="bg-white rounded-lg shadow p-4">
    <div class="flex justify-between items-start mb-2">
      <h3 class="font-bold">Пользователь 2</h3>
      <span class="bg-yellow-100 text-yellow-800 text-xs px-2 py-1 rounded">Ожидает</span>
    </div>
    <p class="text-sm text-gray-600">user2@example.com</p>
    <p class="text-sm text-gray-600">Роль: Пользователь</p>
  </div>
</div>

<!-- Десктоп: таблица -->
<div class="hidden md:block overflow-x-auto">
  <table class="w-full bg-white rounded-lg shadow">
    <thead class="bg-gray-50 border-b">
      <tr>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Имя</th>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Email</th>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Роль</th>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Статус</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-gray-200">
      <tr>
        <td class="px-6 py-4 font-medium">Пользователь 1</td>
        <td class="px-6 py-4 text-gray-600">user1@example.com</td>
        <td class="px-6 py-4 text-gray-600">Администратор</td>
        <td class="px-6 py-4">
          <span class="bg-green-100 text-green-800 text-xs px-2 py-1 rounded">Активен</span>
        </td>
      </tr>
      <tr>
        <td class="px-6 py-4 font-medium">Пользователь 2</td>
        <td class="px-6 py-4 text-gray-600">user2@example.com</td>
        <td class="px-6 py-4 text-gray-600">Пользователь</td>
        <td class="px-6 py-4">
          <span class="bg-yellow-100 text-yellow-800 text-xs px-2 py-1 rounded">Ожидает</span>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

## ⚙️ Кастомные breakpoints

Если стандартных breakpoints недостаточно, добавьте свои в `tailwind.config.js`:

```js
// tailwind.config.js
module.exports = {
  theme: {
    screens: {
      'sm': '640px',
      'md': '768px',
      'lg': '1024px',
      'xl': '1280px',
      '2xl': '1536px',

      // Кастомные breakpoints
      'xs': '480px',           // Очень маленькие мобильные
      '3xl': '1920px',         // Очень большие экраны
      'tablet': '640px',       // Семантические имена
      'laptop': '1024px',
      'desktop': '1280px',
    },
  },
}
```

```html
<!-- Использование кастомных breakpoints -->
<div class="text-sm xs:text-base md:text-lg laptop:text-xl">
  Адаптивный текст с кастомными breakpoints
</div>
```

## 📦 Container queries (Tailwind v3.2+)

**Container queries** позволяют стилизовать элементы на основе **размера родительского контейнера**, а не viewport:

```js
// tailwind.config.js
module.exports = {
  theme: {
    containers: {
      'card': '400px',
      'sidebar': '300px',
    },
  },
}
```

```html
<!-- Родительский контейнер -->
<div class="@container/card">
  <!-- Дочерний элемент меняет стили при ширине контейнера > 400px -->
  <div class="@md/card:flex @md/card:gap-4">
    <img src="product.jpg" class="@md/card:w-32" alt="Товар">
    <div class="@md/card:flex-1">
      <h3 class="@lg/card:text-2xl">Название товара</h3>
      <p class="text-gray-600">Описание</p>
    </div>
  </div>
</div>
```

### Когда использовать container queries

- ✅ **Переиспользуемые компоненты** — карточки, виджеты, которые могут быть в разных контекстах
- ✅ **Sidebar vs main content** — один компонент, разное поведение
- ❌ **Глобальный layout** — для этого используйте обычные breakpoints

## 🎯 Responsive spacing scale

Создайте консистентную систему отступов для всех экранов:

```html
<!-- Секция с адаптивными отступами -->
<section class="py-8 sm:py-12 md:py-16 lg:py-20 xl:py-24">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-2xl sm:text-3xl md:text-4xl font-bold mb-4 sm:mb-6 md:mb-8">
      Заголовок секции
    </h2>
    <p class="text-base sm:text-lg md:text-xl text-gray-600 max-w-3xl">
      Описание секции с адаптивной типографикой и отступами.
    </p>
  </div>
</section>
```

## 📊 Шпаргалка: что когда использовать

| Задача | Классы |
| :-- | :-- |
| Мобильная версия | Базовые классы (без префикса) |
| Планшеты | `md:` |
| Десктопы | `lg:`, `xl:` |
| Большие экраны | `2xl:` |
| Скрыть на мобильных | `hidden md:block` |
| Показать только на мобильных | `block md:hidden` |
| Адаптивная сетка | `grid-cols-1 md:grid-cols-2 lg:grid-cols-3` |
| Адаптивные отступы | `p-4 md:p-6 lg:p-8` |
| Адаптивная типографика | `text-lg md:text-xl lg:text-2xl` |
| Адаптивное направление | `flex-col md:flex-row` |
| Адаптивное выравнивание | `text-center md:text-left` |
| Адаптивная ширина | `w-full md:w-1/2 lg:w-1/3` |
| Container queries | `@container`, `@md:`, `@lg:` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Desktop-first вместо mobile-first

```html
<!-- ❌ Плохо: desktop-first (нужно переопределять для мобильных) -->
<div class="text-xl md:text-lg sm:text-base">
  Неправильный подход
</div>

<!-- ✅ Хорошо: mobile-first (прогрессивное улучшение) -->
<div class="text-base md:text-lg xl:text-xl">
  Правильный подход
</div>
```

### ❌ Ошибка 2: Забывают про промежуточные размеры

```html
<!-- ❌ Плохо: прыжок от мобильного к десктопу -->
<div class="text-sm lg:text-xl">
  Слишком большой скачок
</div>

<!-- ✅ Хорошо: плавная градация -->
<div class="text-sm md:text-base lg:text-lg xl:text-xl">
  Плавное увеличение
</div>
```

### ❌ Ошибка 3: Фиксированная ширина без responsive

```html
<!-- ❌ Плохо: на мобильных будет горизонтальный скролл -->
<div class="w-[1200px]">
  Фиксированная ширина
</div>

<!-- ✅ Хорошо: адаптивная ширина -->
<div class="w-full max-w-7xl mx-auto px-4">
  Адаптивная ширина с ограничениями
</div>
```

### ❌ Ошибка 4: `hidden` без альтернативы

```html
<!-- ❌ Плохо: элемент скрыт на всех экранах -->
<div class="hidden">
  Невидимый контент
</div>

<!-- ✅ Хорошо: скрыт на мобильных, виден на десктопе -->
<div class="hidden md:block">
  Контент для десктопа
</div>
```

### ❌ Ошибка 5: Игнорируют `max-w` для контента

```html
<!-- ❌ Плохо: текст на весь экран на больших мониторах -->
<p class="text-lg leading-relaxed">
  Очень длинный текст, который на больших экранах будет неудобно читать.
</p>

<!-- ✅ Хорошо: ограничение ширины для читаемости -->
<p class="text-lg leading-relaxed max-w-prose mx-auto">
  Длинный текст с комфортной шириной для чтения.
</p>
```

### ❌ Ошибка 6: Забывают про `min-w` для flex-элементов

```html
<!-- ❌ Плохо: flex-элементы могут сжиматься слишком сильно -->
<div class="flex gap-4">
  <div class="flex-1">Длинный контент...</div>
</div>

<!-- ✅ Хорошо: минимальная ширина для предотвращения сжатия -->
<div class="flex gap-4">
  <div class="flex-1 min-w-0">Длинный контент...</div>
</div>
```

### ❌ Ошибка 7: Используют `sm:` для мобильных

```html
<!-- ❌ Плохо: sm: — это не мобильные, это от 640px -->
<div class="sm:text-base">
  Этот стиль применится только от 640px, на мобильных будет дефолтный
</div>

<!-- ✅ Хорошо: базовые стили для мобильных, sm: для больших -->
<div class="text-sm sm:text-base">
  Mobile-first подход
</div>
```

## 🎯 Что дальше?

Теперь вы полностью владеете адаптивным дизайном! Но современный UI — это не только адаптивность. Следующий важный аспект — **тёмная тема**.

**Следующий шаг:** [🌙 Dark Mode в Tailwind CSS](dark-mode.md) — изучим, как добавить поддержку тёмной темы в ваш проект.

---

---




<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: responsive\dark-mode.md -->
<!-- ═══════════════════════════════════════════════════════════ -->

# 🌙 Dark Mode в Tailwind CSS

> **Полное руководство по тёмной теме:** от базовой настройки до переключателя, сохранения выбора пользователя и продвинутых паттернов

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Поймёте два режима работы dark mode: `media` и `class`
- ✅ Настроите dark mode в `tailwind.config.js`
- ✅ Освоите синтаксис модификатора `dark:`
- ✅ Создадите полноценный переключатель темы
- ✅ Научитесь сохранять выбор пользователя в localStorage
- ✅ Оптимизируете изображения и цвета для тёмной темы
- ✅ Избежите типичных ошибок при реализации dark mode
- ✅ Реализуете поддержку системных настроек + ручного переключения

## 🎯 Два режима работы

Tailwind CSS поддерживает **два способа** включения dark mode:

### 1. `media` — по системным настройкам

Тема переключается автоматически в зависимости от настроек ОС/браузера.

```js
// tailwind.config.js
module.exports = {
  darkMode: 'media', // по умолчанию
}
```

**Плюсы:**
- ✅ Работает из коробки
- ✅ Следует системным настройкам пользователя
- ✅ Не нужен JavaScript

**Минусы:**
- ❌ Пользователь не может переключить тему вручную
- ❌ Нельзя сохранить выбор

### 2. `class` — ручное переключение

Тема переключается добавлением класса `dark` к `<html>` или `<body>`.

```js
// tailwind.config.js
module.exports = {
  darkMode: 'class',
}
```

```html
<!-- Светлая тема -->
<html>
  <body class="bg-white text-gray-900">...</body>
</html>

<!-- Тёмная тема -->
<html class="dark">
  <body class="bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100">
    ...
  </body>
</html>
```

**Плюсы:**
- ✅ Полный контроль над темой
- ✅ Можно сохранить выбор пользователя
- ✅ Можно комбинировать с системными настройками

**Минусы:**
- ❌ Нужен JavaScript
- ❌ Нужно писать логику переключения

> 💡 **Рекомендация:** используйте `class` — это самый гибкий подход. В этом разделе мы сосредоточимся именно на нём.

## 🎨 Синтаксис `dark:`

Модификатор `dark:` добавляется **перед любым утилитарным классом**:

```html
<!-- Фон -->
<div class="bg-white dark:bg-gray-900">...</div>

<!-- Текст -->
<p class="text-gray-900 dark:text-gray-100">...</p>

<!-- Граница -->
<div class="border-gray-200 dark:border-gray-700">...</div>

<!-- Hover -->
<button class="hover:bg-gray-100 dark:hover:bg-gray-800">...</button>

<!-- Focus -->
<input class="focus:ring-blue-500 dark:focus:ring-blue-400">
```

### Комбинирование с другими модификаторами

```html
<!-- Dark + responsive -->
<div class="bg-white md:bg-gray-50 dark:bg-gray-900 md:dark:bg-gray-800">
  Адаптивная тёмная тема
</div>

<!-- Dark + hover -->
<button class="bg-blue-500 hover:bg-blue-600 dark:bg-blue-600 dark:hover:bg-blue-700">
  Кнопка
</button>

<!-- Dark + group-hover -->
<div class="group">
  <span class="text-gray-600 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-gray-100">
    Текст
  </span>
</div>
```

## 🎯 Типовая цветовая схема

### Светлая тема

```
Фоны:
  - Основной: white
  - Вторичный: gray-50
  - Третичный: gray-100

Текст:
  - Основной: gray-900
  - Вторичный: gray-600
  - Третичный: gray-400

Границы: gray-200
```

### Тёмная тема

```
Фоны:
  - Основной: gray-900
  - Вторичный: gray-800
  - Третичный: gray-700

Текст:
  - Основной: gray-100
  - Вторичный: gray-400
  - Третичный: gray-500

Границы: gray-700
```

### Пример реализации

```html
<div class="bg-white dark:bg-gray-900 p-6 rounded-lg shadow-md">
  <h2 class="text-xl font-bold text-gray-900 dark:text-gray-100 mb-2">
    Заголовок карточки
  </h2>
  <p class="text-gray-600 dark:text-gray-400 mb-4">
    Описание карточки с поддержкой тёмной темы.
  </p>
  <div class="border-t border-gray-200 dark:border-gray-700 pt-4">
    <button class="bg-blue-600 hover:bg-blue-700 dark:bg-blue-500 dark:hover:bg-blue-600 text-white px-4 py-2 rounded">
      Действие
    </button>
  </div>
</div>
```

## 🔄 Переключатель темы

### Базовый переключатель

```html
<button
  id="theme-toggle"
  type="button"
  class="text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 rounded-lg text-sm p-2.5"
>
  <!-- Иконка солнца (для тёмной темы) -->
  <svg id="theme-toggle-dark-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
    <path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"/>
  </svg>
  <!-- Иконка луны (для светлой темы) -->
  <svg id="theme-toggle-light-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
    <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/>
  </svg>
</button>

<script>
  var themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
  var themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');

  // Показываем правильную иконку при загрузке
  if (localStorage.getItem('color-theme') === 'dark' ||
      (!('color-theme' in localStorage) &&
       window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    themeToggleLightIcon.classList.remove('hidden');
  } else {
    themeToggleDarkIcon.classList.remove('hidden');
  }

  var themeToggleBtn = document.getElementById('theme-toggle');
  themeToggleBtn.addEventListener('click', function() {
    // Переключаем иконки
    themeToggleDarkIcon.classList.toggle('hidden');
    themeToggleLightIcon.classList.toggle('hidden');

    // Переключаем тему
    if (localStorage.getItem('color-theme')) {
      if (localStorage.getItem('color-theme') === 'light') {
        document.documentElement.classList.add('dark');
        localStorage.setItem('color-theme', 'dark');
      } else {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('color-theme', 'light');
      }
    } else {
      if (document.documentElement.classList.contains('dark')) {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('color-theme', 'light');
      } else {
        document.documentElement.classList.add('dark');
        localStorage.setItem('color-theme', 'dark');
      }
    }
  });
</script>
```

### Улучшенный переключатель с инициализацией до рендера

Чтобы избежать «мигания» темы при загрузке, добавьте этот скрипт в `<head>` **до** рендеринга body:

```html
<!DOCTYPE html>
<html>
<head>
  <script>
    // Применяем тему ДО рендеринга страницы
    if (localStorage.theme === 'dark' ||
        (!('theme' in localStorage) &&
         window.matchMedia('(prefers-color-scheme: dark)').matches)) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  </script>
  <!-- Остальной head -->
</head>
<body>
  <!-- Контент -->
</body>
</html>
```

### React-компонент переключателя

```jsx
import { useEffect, useState } from 'react';

function ThemeToggle() {
  const [theme, setTheme] = useState(() => {
    if (typeof window !== 'undefined') {
      return localStorage.getItem('theme') ||
        (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    }
    return 'light';
  });

  useEffect(() => {
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
    localStorage.setItem('theme', theme);
  }, [theme]);

  return (
    <button
      onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
      className="p-2 rounded-lg bg-gray-200 dark:bg-gray-700 hover:bg-gray-300 dark:hover:bg-gray-600 transition"
      aria-label="Переключить тему"
    >
      {theme === 'dark' ? (
        <svg className="w-5 h-5 text-yellow-500" fill="currentColor" viewBox="0 0 20 20">
          <path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"/>
        </svg>
      ) : (
        <svg className="w-5 h-5 text-gray-700" fill="currentColor" viewBox="0 0 20 20">
          <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/>
        </svg>
      )}
    </button>
  );
}

export default ThemeToggle;
```

### Vue-компонент переключателя

```vue
<template>
  <button
    @click="toggleTheme"
    class="p-2 rounded-lg bg-gray-200 dark:bg-gray-700 hover:bg-gray-300 dark:hover:bg-gray-600 transition"
    aria-label="Переключить тему"
  >
    <svg v-if="theme === 'dark'" class="w-5 h-5 text-yellow-500" fill="currentColor" viewBox="0 0 20 20">
      <path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"/>
    </svg>
    <svg v-else class="w-5 h-5 text-gray-700" fill="currentColor" viewBox="0 0 20 20">
      <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/>
    </svg>
  </button>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const theme = ref('light');

onMounted(() => {
  theme.value = localStorage.getItem('theme') ||
    (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');

  applyTheme();
});

function toggleTheme() {
  theme.value = theme.value === 'dark' ? 'light' : 'dark';
  localStorage.setItem('theme', theme.value);
  applyTheme();
}

function applyTheme() {
  if (theme.value === 'dark') {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
}
</script>
```

## 🎨 Три состояния: light / dark / system

Самый продвинутый подход — поддержка трёх режимов:

```js
// theme.js
const ThemeManager = {
  init() {
    const saved = localStorage.getItem('theme');
    const system = window.matchMedia('(prefers-color-scheme: dark)').matches;

    if (saved === 'dark' || (!saved && system)) {
      document.documentElement.classList.add('dark');
    }

    // Следим за изменениями системной темы
    window.matchMedia('(prefers-color-scheme: dark)')
      .addEventListener('change', (e) => {
        if (!localStorage.getItem('theme')) {
          document.documentElement.classList.toggle('dark', e.matches);
        }
      });
  },

  setTheme(mode) {
    localStorage.setItem('theme', mode);

    if (mode === 'dark') {
      document.documentElement.classList.add('dark');
    } else if (mode === 'light') {
      document.documentElement.classList.remove('dark');
    } else {
      // system
      const system = window.matchMedia('(prefers-color-scheme: dark)').matches;
      document.documentElement.classList.toggle('dark', system);
    }
  },

  getTheme() {
    return localStorage.getItem('theme') || 'system';
  }
};

ThemeManager.init();
```

```html
<!-- Переключатель с тремя режимами -->
<div class="flex items-center gap-2 bg-gray-100 dark:bg-gray-800 p-1 rounded-lg">
  <button onclick="ThemeManager.setTheme('light')" class="px-3 py-1 rounded hover:bg-white dark:hover:bg-gray-700">
    ☀️ Светлая
  </button>
  <button onclick="ThemeManager.setTheme('dark')" class="px-3 py-1 rounded hover:bg-white dark:hover:bg-gray-700">
    🌙 Тёмная
  </button>
  <button onclick="ThemeManager.setTheme('system')" class="px-3 py-1 rounded hover:bg-white dark:hover:bg-gray-700">
    💻 Системная
  </button>
</div>
```

## 🖼️ Изображения в dark mode

### Разные изображения для разных тем

```html
<picture>
  <source srcset="logo-dark.svg" media="(prefers-color-scheme: dark)">
  <img src="logo-light.svg" alt="Логотип">
</picture>
```

### Инверсия SVG

```html
<!-- Светлая тема: чёрная иконка -->
<!-- Тёмная тема: белая иконка -->
<svg class="w-6 h-6 text-gray-900 dark:text-gray-100" fill="currentColor" viewBox="0 0 24 24">
  <path d="..."/>
</svg>
```

### Корректировка яркости изображений

```html
<!-- Фото в светлой теме: обычная яркость -->
<!-- Фото в тёмной теме: чуть темнее -->
<img
  src="photo.jpg"
  class="brightness-100 dark:brightness-75 rounded-lg"
  alt="Фото"
>
```

### Инверсия для иконок

```html
<!-- Специальный класс для инверсии чёрно-белых изображений -->
<img
  src="icon.png"
  class="dark:invert"
  alt="Иконка"
>
```

## 🎯 Практические паттерны

### 1. 🎴 Карточка с полной поддержкой dark mode

```html
<div class="bg-white dark:bg-gray-800 rounded-xl shadow-md dark:shadow-gray-900/50 overflow-hidden max-w-sm">
  <img
    src="product.jpg"
    class="w-full h-48 object-cover brightness-100 dark:brightness-90"
    alt="Товар"
  >
  <div class="p-6">
    <div class="flex items-center gap-2 mb-2">
      <span class="bg-blue-100 dark:bg-blue-900/30 text-blue-800 dark:text-blue-300 text-xs font-medium px-2 py-1 rounded">
        Новинка
      </span>
    </div>
    <h3 class="text-xl font-bold text-gray-900 dark:text-gray-100 mb-2">
      Название товара
    </h3>
    <p class="text-gray-600 dark:text-gray-400 text-sm mb-4">
      Описание товара с поддержкой тёмной темы.
    </p>
    <div class="flex items-center justify-between">
      <div>
        <span class="text-2xl font-bold text-gray-900 dark:text-gray-100">2 990 ₽</span>
        <span class="text-sm text-gray-400 dark:text-gray-500 line-through ml-2">3 990 ₽</span>
      </div>
      <button class="bg-blue-600 dark:bg-blue-500 hover:bg-blue-700 dark:hover:bg-blue-600 text-white px-4 py-2 rounded-lg transition">
        Купить
      </button>
    </div>
  </div>
</div>
```

### 2. 📝 Форма с dark mode

```html
<form class="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 max-w-md space-y-4">
  <h2 class="text-2xl font-bold text-gray-900 dark:text-gray-100">Вход</h2>

  <div>
    <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
      Email
    </label>
    <input
      type="email"
      class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100 placeholder-gray-400 dark:placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 dark:focus:ring-blue-400"
      placeholder="you@example.com"
    >
  </div>

  <div>
    <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
      Пароль
    </label>
    <input
      type="password"
      class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100 placeholder-gray-400 dark:placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 dark:focus:ring-blue-400"
      placeholder="••••••••"
    >
  </div>

  <div class="flex items-center justify-between">
    <label class="flex items-center gap-2">
      <input type="checkbox" class="rounded border-gray-300 dark:border-gray-600 text-blue-600 dark:text-blue-500 focus:ring-blue-500 dark:focus:ring-blue-400">
      <span class="text-sm text-gray-700 dark:text-gray-300">Запомнить меня</span>
    </label>
    <a href="#" class="text-sm text-blue-600 dark:text-blue-400 hover:underline">
      Забыли пароль?
    </a>
  </div>

  <button
    type="submit"
    class="w-full bg-blue-600 dark:bg-blue-500 hover:bg-blue-700 dark:hover:bg-blue-600 text-white font-medium py-2 rounded-lg transition"
  >
    Войти
  </button>
</form>
```

### 3. 📊 Таблица с dark mode

```html
<div class="overflow-x-auto">
  <table class="w-full bg-white dark:bg-gray-800 rounded-lg shadow-md">
    <thead class="bg-gray-50 dark:bg-gray-700 border-b border-gray-200 dark:border-gray-600">
      <tr>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Имя</th>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Email</th>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Роль</th>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Статус</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-gray-200 dark:divide-gray-700">
      <tr class="hover:bg-gray-50 dark:hover:bg-gray-700/50 transition">
        <td class="px-6 py-4 font-medium text-gray-900 dark:text-gray-100">Иван Иванов</td>
        <td class="px-6 py-4 text-gray-600 dark:text-gray-400">ivan@example.com</td>
        <td class="px-6 py-4 text-gray-600 dark:text-gray-400">Администратор</td>
        <td class="px-6 py-4">
          <span class="bg-green-100 dark:bg-green-900/30 text-green-800 dark:text-green-300 text-xs px-2 py-1 rounded">
            Активен
          </span>
        </td>
      </tr>
      <tr class="hover:bg-gray-50 dark:hover:bg-gray-700/50 transition">
        <td class="px-6 py-4 font-medium text-gray-900 dark:text-gray-100">Мария Петрова</td>
        <td class="px-6 py-4 text-gray-600 dark:text-gray-400">maria@example.com</td>
        <td class="px-6 py-4 text-gray-600 dark:text-gray-400">Пользователь</td>
        <td class="px-6 py-4">
          <span class="bg-yellow-100 dark:bg-yellow-900/30 text-yellow-800 dark:text-yellow-300 text-xs px-2 py-1 rounded">
            Ожидает
          </span>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

### 4. 🎨 Градиенты с dark mode

```html
<!-- Светлая тема: яркий градиент -->
<!-- Тёмная тема: более приглушённый -->
<div class="bg-gradient-to-br from-blue-500 to-purple-600 dark:from-blue-700 dark:to-purple-900 p-8 rounded-xl text-white">
  <h2 class="text-3xl font-bold mb-2">Градиентный блок</h2>
  <p class="text-blue-100 dark:text-purple-200">
    Цвета градиента адаптируются под тему
  </p>
</div>
```

### 5. 🌫️ Glassmorphism с dark mode

```html
<div class="relative h-96 bg-gradient-to-br from-purple-500 via-pink-500 to-orange-500 dark:from-purple-900 dark:via-pink-900 dark:to-orange-900">
  <!-- Декоративные круги -->
  <div class="absolute top-10 left-10 w-32 h-32 bg-yellow-300 dark:bg-yellow-700 rounded-full blur-2xl"></div>
  <div class="absolute bottom-10 right-10 w-40 h-40 bg-blue-400 dark:bg-blue-800 rounded-full blur-2xl"></div>

  <!-- Стеклянная карточка -->
  <div class="absolute inset-0 flex items-center justify-center">
    <div class="bg-white/20 dark:bg-black/30 backdrop-blur-lg border border-white/30 dark:border-white/10 rounded-2xl p-8 shadow-2xl max-w-md">
      <h2 class="text-2xl font-bold text-white mb-4">Glassmorphism</h2>
      <p class="text-white/90 dark:text-white/80">
        Стеклянный эффект работает в обеих темах
      </p>
    </div>
  </div>
</div>
```

## ⚙️ Кастомные цвета для dark mode

### Через CSS-переменные (рекомендуется)

```js
// tailwind.config.js
module.exports = {
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        'surface': {
          DEFAULT: 'rgb(var(--surface) / <alpha-value>)',
          secondary: 'rgb(var(--surface-secondary) / <alpha-value>)',
        },
        'content': {
          DEFAULT: 'rgb(var(--content) / <alpha-value>)',
          secondary: 'rgb(var(--content-secondary) / <alpha-value>)',
        },
      },
    },
  },
}
```

```css
/* styles.css */
:root {
  --surface: 255 255 255;           /* white */
  --surface-secondary: 249 250 251; /* gray-50 */
  --content: 17 24 39;              /* gray-900 */
  --content-secondary: 75 85 99;    /* gray-600 */
}

.dark {
  --surface: 17 24 39;              /* gray-900 */
  --surface-secondary: 31 41 55;    /* gray-800 */
  --content: 243 244 246;           /* gray-100 */
  --content-secondary: 156 163 175; /* gray-400 */
}
```

```html
<!-- Автоматически адаптируется -->
<div class="bg-surface text-content">
  <p class="text-content-secondary">Вторичный текст</p>
</div>
```

### Преимущества подхода

- ✅ **Один класс** вместо `bg-white dark:bg-gray-900`
- ✅ **Централизованное управление** цветами
- ✅ **Легко менять палитру** — правим только CSS-переменные
- ✅ **Поддержка прозрачности** — `bg-surface/50`

## 📊 Шпаргалка: что когда использовать

| Задача | Классы |
| :-- | :-- |
| Фон | `bg-white dark:bg-gray-900` |
| Текст | `text-gray-900 dark:text-gray-100` |
| Вторичный текст | `text-gray-600 dark:text-gray-400` |
| Граница | `border-gray-200 dark:border-gray-700` |
| Hover фон | `hover:bg-gray-100 dark:hover:bg-gray-800` |
| Input фон | `bg-white dark:bg-gray-700` |
| Input граница | `border-gray-300 dark:border-gray-600` |
| Placeholder | `placeholder-gray-400 dark:placeholder-gray-500` |
| Бейдж | `bg-blue-100 dark:bg-blue-900/30 text-blue-800 dark:text-blue-300` |
| Тень | `shadow-md dark:shadow-gray-900/50` |
| Разделитель | `divide-gray-200 dark:divide-gray-700` |
| Инверсия SVG | `dark:invert` |
| Затемнение фото | `brightness-100 dark:brightness-75` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Забывают настроить `darkMode: 'class'`

```js
// ❌ Плохо: по умолчанию используется media
module.exports = {
  // darkMode не указан
}

// ✅ Хорошо: явно указываем class
module.exports = {
  darkMode: 'class',
}
```

### ❌ Ошибка 2: `dark:` без парного светлого класса

```html
<!-- ❌ Плохо: в светлой теме фон не задан -->
<div class="dark:bg-gray-900">Нет светлого фона</div>

<!-- ✅ Хорошо: оба варианта -->
<div class="bg-white dark:bg-gray-900">Оба варианта</div>
```

### ❌ Ошибка 3: Мигание темы при загрузке

```html
<!-- ❌ Плохо: скрипт в конце body -->
<body>
  <!-- Контент -->
  <script>
    // Применяем тему
  </script>
</body>

<!-- ✅ Хорошо: скрипт в <head> до рендеринга -->
<head>
  <script>
    // Применяем тему ДО рендеринга
  </script>
</head>
<body>
  <!-- Контент -->
</body>
```

### ❌ Ошибка 4: Игнорируют системные настройки

```js
// ❌ Плохо: только localStorage
const theme = localStorage.getItem('theme');

// ✅ Хорошо: localStorage + системные настройки
const theme = localStorage.getItem('theme') ||
  (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
```

### ❌ Ошибка 5: Используют `dark:` для акцентных цветов

```html
<!-- ❌ Плохо: акцентный синий не должен меняться -->
<button class="bg-blue-600 dark:bg-blue-400">
  Акцент меняется — плохо
</button>

<!-- ✅ Хорошо: акцент остаётся, меняется только фон/текст -->
<button class="bg-blue-600 hover:bg-blue-700 text-white">
  Акцент стабилен
</button>
```

### ❌ Ошибка 6: Забывают про тени в dark mode

```html
<!-- ❌ Плохо: чёрная тень на тёмном фоне не видна -->
<div class="bg-gray-900 shadow-lg">Тень не видна</div>

<!-- ✅ Хорошо: настраиваем цвет тени -->
<div class="bg-gray-900 shadow-lg shadow-gray-900/50 dark:shadow-black/50">
  Тень видна
</div>
```

### ❌ Ошибка 7: Чистый белый в dark mode

```html
<!-- ❌ Плохо: слишком яркий контраст -->
<div class="bg-white dark:bg-white">Белый в dark mode</div>

<!-- ✅ Хорошо: используем оттенки серого -->
<div class="bg-white dark:bg-gray-900">Комфортный контраст</div>
```

### ❌ Ошибка 8: Забывают про focus-состояния

```html
<!-- ❌ Плохо: focus ring не виден в dark mode -->
<input class="focus:ring-2 focus:ring-blue-500">

<!-- ✅ Хорошо: настраиваем ring для dark mode -->
<input class="focus:ring-2 focus:ring-blue-500 dark:focus:ring-blue-400">
```

## 🎯 Что дальше?

Теперь вы полностью владеете тёмной темой! Но интерактивность — это не только темы. Следующий важный аспект — **состояния элементов**: hover, focus, active, disabled.

**Следующий шаг:** [🎯 Состояния элементов в Tailwind CSS](states.md) — изучим все модификаторы состояний и научимся создавать отзывчивые интерфейсы.

---

---




<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: responsive\states.md -->
<!-- ═══════════════════════════════════════════════════════════ -->

# 🎯 Состояния элементов в Tailwind CSS

> **Полное руководство по интерактивным состояниям:** от hover и focus до group-hover, peer и кастомных модификаторов

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Освоите все основные модификаторы состояний: hover, focus, active, disabled
- ✅ Поймёте разницу между focus, focus-within и focus-visible
- ✅ Научитесь использовать group-hover и peer для сложных взаимодействий
- ✅ Освоите модификаторы для форм: checked, indeterminate, required, invalid
- ✅ Поймёте порядок применения состояний (specificity)
- ✅ Создадите отзывчивые интерфейсы с богатой интерактивностью
- ✅ Избежите типичных ошибок при работе с состояниями

## 🎨 Основные модификаторы состояний

Tailwind предоставляет **модификаторы состояний**, которые применяются **перед утилитарным классом** через двоеточие:

```
hover:bg-blue-600
focus:ring-2
active:scale-95
disabled:opacity-50
```

### Порядок имеет значение

```html
<!-- ✅ Правильно: hover перед focus -->
<button class="hover:bg-blue-600 focus:ring-2">...</button>

<!-- ❌ Неправильно: focus перед hover (может не работать) -->
<button class="focus:ring-2 hover:bg-blue-600">...</button>
```

## 🔥 Hover: `hover:`

Применяется при наведении курсора мыши:

```html
<!-- Изменение фона -->
<button class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded">
  Наведи на меня
</button>

<!-- Изменение текста -->
<a href="#" class="text-gray-600 hover:text-blue-600 hover:underline">
  Ссылка
</a>

<!-- Изменение тени -->
<div class="shadow-md hover:shadow-xl transition-shadow">
  Карточка с усилением тени
</div>

<!-- Изменение масштаба -->
<button class="hover:scale-105 transition-transform">
  Увеличение при hover
</button>
```

### Hover с transition

Всегда добавляйте `transition` для плавных изменений:

```html
<!-- ❌ Плохо: резкое изменение -->
<button class="bg-blue-500 hover:bg-blue-600">Резко</button>

<!-- ✅ Хорошо: плавное изменение -->
<button class="bg-blue-500 hover:bg-blue-600 transition-colors duration-200">
  Плавно
</button>

<!-- ✅ Отлично: плавное изменение всех свойств -->
<button class="bg-blue-500 hover:bg-blue-600 hover:scale-105 hover:shadow-lg transition-all duration-300">
  Все свойства плавно
</button>
```

### Доступные transition-утилиты

| Класс | CSS |
| :-- | :-- |
| `transition-none` | `transition-property: none` |
| `transition-all` | `transition-property: all` |
| `transition` | `transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter` |
| `transition-colors` | `transition-property: color, background-color, border-color, text-decoration-color, fill, stroke` |
| `transition-opacity` | `transition-property: opacity` |
| `transition-shadow` | `transition-property: box-shadow` |
| `transition-transform` | `transition-property: transform` |

### Длительность transition

| Класс | CSS |
| :-- | :-- |
| `duration-75` | `transition-duration: 75ms` |
| `duration-100` | `transition-duration: 100ms` |
| `duration-150` | `transition-duration: 150ms` |
| `duration-200` | `transition-duration: 200ms` |
| `duration-300` | `transition-duration: 300ms` |
| `duration-500` | `transition-duration: 500ms` |
| `duration-700` | `transition-duration: 700ms` |
| `duration-1000` | `transition-duration: 1000ms` |

### Функции easing

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `ease-linear` | `transition-timing-function: linear` | Линейная |
| `ease-in` | `transition-timing-function: cubic-bezier(0.4, 0, 1, 1)` | Ускорение |
| `ease-out` | `transition-timing-function: cubic-bezier(0, 0, 0.2, 1)` | Замедление |
| `ease-in-out` | `transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1)` | Ускорение и замедление |

## 🎯 Focus: `focus:`

Применяется когда элемент получает фокус (клавиатурой или мышью):

```html
<!-- Focus ring для input -->
<input
  type="text"
  class="border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
  placeholder="Фокус с ring"
>

<!-- Focus для кнопки -->
<button class="focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
  Кнопка с focus ring
</button>

<!-- Focus для ссылки -->
<a href="#" class="focus:outline-none focus:underline focus:text-blue-600">
  Ссылка с focus
</a>
```

### Focus-within: `focus-within:`

Применяется когда **любой дочерний элемент** получает фокус:

```html
<!-- Подсветка контейнера при фокусе на input -->
<div class="border border-gray-300 focus-within:border-blue-500 focus-within:ring-2 focus-within:ring-blue-500/20 rounded-lg p-2">
  <input
    type="text"
    class="w-full focus:outline-none"
    placeholder="Фокус подсветит контейнер"
  >
</div>
```

### Focus-visible: `focus-visible:`

Применяется только при **клавиатурной навигации** (Tab), но не при клике мышью:

```html
<!-- Focus ring только при клавиатурной навигации -->
<button class="focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2">
  Кнопка с focus-visible
</button>
```

> 💡 **Когда использовать:** `focus-visible` — современный подход для accessibility. Пользователи мыши не видят ring, но клавиатурные пользователи видят.

### Разница между focus, focus-within, focus-visible

| Модификатор | Когда применяется |
| :-- | :-- |
| `focus:` | Элемент получил фокус (мышь или клавиатура) |
| `focus-within:` | Любой дочерний элемент получил фокус |
| `focus-visible:` | Элемент получил фокус через клавиатуру |

## 🔘 Active: `active:`

Применяется в момент **нажатия** (между mousedown и mouseup):

```html
<!-- Кнопка "вдавливается" при клике -->
<button class="bg-blue-500 hover:bg-blue-600 active:bg-blue-700 active:scale-95 transition-all">
  Нажми меня
</button>

<!-- Ссылка меняет цвет при клике -->
<a href="#" class="text-blue-600 hover:text-blue-700 active:text-blue-800">
  Ссылка
</a>
```

## 🚫 Disabled: `disabled:`

Применяется к элементам с атрибутом `disabled`:

```html
<!-- Недоступная кнопка -->
<button
  disabled
  class="bg-blue-500 hover:bg-blue-600 disabled:bg-gray-300 disabled:cursor-not-allowed disabled:opacity-50 text-white px-4 py-2 rounded"
>
  Недоступна
</button>

<!-- Недоступный input -->
<input
  type="text"
  disabled
  class="border border-gray-300 disabled:bg-gray-100 disabled:cursor-not-allowed"
  placeholder="Недоступно"
>
```

## 👥 Group-hover: `group-hover:`

Применяется к **дочерним элементам** при hover на **родительском** элементе с классом `group`:

```html
<!-- Карточка: при hover на карточке меняется стрелка -->
<div class="group bg-white p-6 rounded-lg shadow hover:shadow-lg transition-shadow">
  <h3 class="text-xl font-bold mb-2">Заголовок</h3>
  <p class="text-gray-600 mb-4">Описание</p>
  <div class="flex items-center gap-2 text-blue-600">
    <span>Подробнее</span>
    <svg class="w-4 h-4 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
    </svg>
  </div>
</div>
```

### Group-focus, group-active

```html
<!-- Group-focus -->
<div class="group">
  <input type="text" class="border focus:outline-none">
  <span class="text-gray-400 group-focus-within:text-blue-600">
    Подсказка
  </span>
</div>

<!-- Group-active -->
<div class="group">
  <button class="bg-blue-500 active:bg-blue-700">Кнопка</button>
  <span class="text-gray-600 group-active:text-blue-600">
    Активно
  </span>
</div>
```

## 🤝 Peer: `peer-*:`

Применяется к **соседним элементам** на основе состояния **предыдущего** элемента с классом `peer`:

```html
<!-- Input с валидацией: при фокусе на input меняется label -->
<div class="relative">
  <input
    type="email"
    id="email"
    class="peer border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20 px-4 py-2 rounded w-full"
    placeholder=" "
  >
  <label
    for="email"
    class="absolute left-4 top-2 text-gray-500 peer-focus:top-0 peer-focus:text-xs peer-focus:text-blue-600 peer-[:not(:placeholder-shown)]:top-0 peer-[:not(:placeholder-shown)]:text-xs transition-all"
  >
    Email
  </label>
</div>
```

### Peer-checked для чекбоксов и радиокнопок

```html
<!-- Кастомный чекбокс -->
<label class="flex items-center gap-3 cursor-pointer">
  <input type="checkbox" class="peer sr-only">
  <div class="w-5 h-5 border-2 border-gray-300 rounded peer-checked:bg-blue-500 peer-checked:border-blue-500 flex items-center justify-center transition-colors">
    <svg class="w-3 h-3 text-white opacity-0 peer-checked:opacity-100 transition-opacity" fill="currentColor" viewBox="0 0 20 20">
      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
    </svg>
  </div>
  <span class="text-gray-700">Согласен с условиями</span>
</label>
```

### Peer-disabled

```html
<!-- Label меняется при disabled input -->
<div class="flex items-center gap-2">
  <input type="checkbox" id="option" disabled class="peer">
  <label for="option" class="peer-disabled:text-gray-400 peer-disabled:cursor-not-allowed">
    Опция (недоступна)
  </label>
</div>
```

## ✅ Состояния форм

### Checked: `checked:`

```html
<!-- Кастомный чекбокс -->
<label class="flex items-center gap-2 cursor-pointer">
  <input type="checkbox" class="peer sr-only">
  <div class="w-5 h-5 border-2 border-gray-300 rounded peer-checked:bg-blue-500 peer-checked:border-blue-500"></div>
  <span>Выбрать</span>
</label>
```

### Indeterminate: `indeterminate:`

```html
<!-- Чекбокс в неопределённом состоянии -->
<input type="checkbox" class="indeterminate:bg-gray-400" id="select-all">
```

### Required: `required:`

```html
<!-- Звёздочка для обязательных полей -->
<label>
  Email <span class="required:text-red-500">*</span>
</label>
<input type="email" required class="required:border-red-500">
```

### Invalid: `invalid:`

```html
<!-- Красная граница при невалидном email -->
<input
  type="email"
  class="border border-gray-300 invalid:border-red-500 invalid:text-red-600 focus:outline-none focus:ring-2 focus:ring-blue-500 invalid:focus:ring-red-500"
  placeholder="you@example.com"
>
```

### Placeholder-shown: `placeholder-shown:`

```html
<!-- Label поднимается при вводе текста -->
<div class="relative">
  <input
    type="text"
    class="peer pt-5 pb-2 px-4 border rounded w-full"
    placeholder=" "
  >
  <label class="absolute left-4 top-2 text-sm text-gray-500 peer-placeholder-shown:top-4 peer-placeholder-shown:text-base transition-all">
    Имя
  </label>
</div>
```

### Autofill: `autofill:`

```html
<!-- Стилизация автозаполнения браузера -->
<input
  type="text"
  class="autofill:bg-yellow-100 autofill:text-yellow-900"
>
```

## 🎯 Комбинирование состояний

### Несколько состояний одновременно

```html
<!-- Hover + focus + active -->
<button class="
  bg-blue-500
  hover:bg-blue-600
  focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2
  active:bg-blue-700 active:scale-95
  transition-all duration-200
">
  Кнопка
</button>
```

### Состояния + responsive

```html
<!-- Hover только на десктопе -->
<button class="hover:bg-blue-600 md:hover:bg-blue-700 lg:hover:bg-blue-800">
  Адаптивный hover
</button>
```

### Состояния + dark mode

```html
<!-- Hover в обеих темах -->
<button class="
  bg-blue-500 dark:bg-blue-600
  hover:bg-blue-600 dark:hover:bg-blue-700
  focus:ring-blue-500 dark:focus:ring-blue-400
">
  Кнопка
</button>
```

### Состояния + group-hover + peer

```html
<!-- Сложное взаимодействие -->
<div class="group">
  <input type="checkbox" class="peer sr-only">
  <div class="peer-checked:bg-green-500 group-hover:scale-110 transition-all">
    Чекбокс
  </div>
  <span class="group-hover:text-blue-600 peer-checked:text-green-600">
    Текст
  </span>
</div>
```

## 🎨 Практические паттерны

### 1. 🔘 Кнопка с полным набором состояний

```html
<button class="
  bg-blue-600
  hover:bg-blue-700
  focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2
  active:bg-blue-800 active:scale-95
  disabled:bg-gray-300 disabled:cursor-not-allowed disabled:opacity-50
  text-white font-medium px-6 py-3 rounded-lg
  transition-all duration-200
">
  Нажми меня
</button>
```

### 2. 🎴 Карточка с hover-эффектами

```html
<div class="group bg-white rounded-xl shadow-md hover:shadow-xl transition-shadow duration-300 overflow-hidden max-w-sm">
  <div class="relative overflow-hidden">
    <img
      src="product.jpg"
      class="w-full h-48 object-cover group-hover:scale-110 transition-transform duration-500"
      alt="Товар"
    >
    <div class="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-colors duration-300"></div>
    <button class="absolute bottom-4 left-1/2 -translate-x-1/2 bg-white text-gray-900 px-4 py-2 rounded-lg opacity-0 group-hover:opacity-100 transition-opacity duration-300">
      Быстрый просмотр
    </button>
  </div>
  <div class="p-6">
    <h3 class="text-xl font-bold text-gray-900 group-hover:text-blue-600 transition-colors">
      Название товара
    </h3>
    <p class="text-gray-600 mt-2">Описание товара</p>
    <div class="mt-4 flex items-center justify-between">
      <span class="text-2xl font-bold text-gray-900">2 990 ₽</span>
      <button class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg transition-colors">
        В корзину
      </button>
    </div>
  </div>
</div>
```

### 3. 📝 Input с floating label

```html
<div class="relative">
  <input
    type="email"
    id="email"
    class="peer w-full px-4 pt-6 pb-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
    placeholder=" "
  >
  <label
    for="email"
    class="absolute left-4 top-4 text-gray-500 pointer-events-none transition-all
           peer-focus:top-2 peer-focus:text-xs peer-focus:text-blue-600
           peer-[:not(:placeholder-shown)]:top-2 peer-[:not(:placeholder-shown)]:text-xs"
  >
    Email адрес
  </label>
</div>
```

### 4. ✅ Кастомный чекбокс

```html
<label class="flex items-center gap-3 cursor-pointer group">
  <input type="checkbox" class="peer sr-only">
  <div class="
    w-5 h-5 border-2 border-gray-300 rounded
    peer-checked:bg-blue-500 peer-checked:border-blue-500
    group-hover:border-blue-400
    flex items-center justify-center
    transition-colors duration-200
  ">
    <svg
      class="w-3 h-3 text-white opacity-0 peer-checked:opacity-100 transition-opacity duration-200"
      fill="currentColor"
      viewBox="0 0 20 20"
    >
      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
    </svg>
  </div>
  <span class="text-gray-700 group-hover:text-gray-900 transition-colors">
    Согласен с условиями использования
  </span>
</label>
```

### 5. 🎚️ Toggle switch

```html
<label class="relative inline-flex items-center cursor-pointer">
  <input type="checkbox" class="sr-only peer">
  <div class="
    w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300
    rounded-full peer
    peer-checked:after:translate-x-full peer-checked:after:border-white
    after:content-[''] after:absolute after:top-[2px] after:left-[2px]
    after:bg-white after:border-gray-300 after:border after:rounded-full
    after:h-5 after:w-5 after:transition-all
    peer-checked:bg-blue-600
  "></div>
  <span class="ml-3 text-sm font-medium text-gray-900">Уведомления</span>
</label>
```

### 6. 📋 Выпадающее меню

```html
<div class="relative group">
  <button class="bg-gray-100 hover:bg-gray-200 px-4 py-2 rounded-lg transition-colors">
    Меню
  </button>
  <div class="
    absolute top-full left-0 mt-2 w-48 bg-white rounded-lg shadow-lg
    opacity-0 invisible group-hover:opacity-100 group-hover:visible
    transition-all duration-200
  ">
    <a href="#" class="block px-4 py-2 hover:bg-gray-100 transition-colors">Пункт 1</a>
    <a href="#" class="block px-4 py-2 hover:bg-gray-100 transition-colors">Пункт 2</a>
    <a href="#" class="block px-4 py-2 hover:bg-gray-100 transition-colors">Пункт 3</a>
  </div>
</div>
```

### 7. 🎨 Галерея с hover-эффектами

```html
<div class="grid grid-cols-3 gap-4">
  <div class="relative overflow-hidden rounded-lg group cursor-pointer">
    <img
      src="photo1.jpg"
      class="w-full h-48 object-cover group-hover:scale-110 group-hover:brightness-75 transition-all duration-300"
      alt="Фото 1"
    >
    <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
      <span class="text-white text-lg font-bold bg-black/50 px-4 py-2 rounded">
        Просмотр
      </span>
    </div>
  </div>
  <!-- Повторить для других фото -->
</div>
```

## 📊 Шпаргалка: что когда использовать

| Задача | Модификатор |
| :-- | :-- |
| Hover эффект | `hover:` |
| Focus ring | `focus:ring-2 focus:ring-blue-500` |
| Focus только клавиатура | `focus-visible:` |
| Focus на дочерних | `focus-within:` |
| Активное состояние (клик) | `active:` |
| Disabled состояние | `disabled:` |
| Hover на родителе | `group` + `group-hover:` |
| Состояние предыдущего элемента | `peer` + `peer-checked:`, `peer-focus:` |
| Checked чекбокс | `peer-checked:` |
| Invalid input | `invalid:` |
| Required поле | `required:` |
| Placeholder показан | `placeholder-shown:` |
| Autofill браузера | `autofill:` |
| Плавный переход | `transition-all duration-200` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Забывают `transition` для hover-эффектов

```html
<!-- ❌ Плохо: резкое изменение -->
<button class="bg-blue-500 hover:bg-blue-600">Резко</button>

<!-- ✅ Хорошо: плавное изменение -->
<button class="bg-blue-500 hover:bg-blue-600 transition-colors duration-200">Плавно</button>
```

### ❌ Ошибка 2: `focus:` без `focus:outline-none`

```html
<!-- ❌ Плохо: двойная обводка (стандартная + ring) -->
<input class="focus:ring-2 focus:ring-blue-500">

<!-- ✅ Хорошо: убираем стандартный outline -->
<input class="focus:outline-none focus:ring-2 focus:ring-blue-500">
```

### ❌ Ошибка 3: `group-hover:` без класса `group` на родителе

```html
<!-- ❌ Плохо: group-hover не работает -->
<div>
  <span class="group-hover:text-blue-600">Не работает</span>
</div>

<!-- ✅ Хорошо: добавляем group -->
<div class="group">
  <span class="group-hover:text-blue-600">Работает</span>
</div>
```

### ❌ Ошибка 4: `peer:` без класса `peer` на предыдущем элементе

```html
<!-- ❌ Плохо: peer не работает -->
<input type="checkbox">
<span class="peer-checked:text-blue-600">Не работает</span>

<!-- ✅ Хорошо: добавляем peer -->
<input type="checkbox" class="peer">
<span class="peer-checked:text-blue-600">Работает</span>
```

### ❌ Ошибка 5: Неправильный порядок состояний

```html
<!-- ❌ Плохо: focus перед hover -->
<button class="focus:ring-2 hover:bg-blue-600">Неправильный порядок</button>

<!-- ✅ Хорошо: hover перед focus -->
<button class="hover:bg-blue-600 focus:ring-2">Правильный порядок</button>
```

### ❌ Ошибка 6: Забывают про accessibility

```html
<!-- ❌ Плохо: нет focus-состояния для клавиатурных пользователей -->
<button class="hover:bg-blue-600">Нет focus</button>

<!-- ✅ Хорошо: есть focus-состояние -->
<button class="hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500">
  Есть focus
</button>
```

### ❌ Ошибка 7: `hover:` на мобильных устройствах

```html
<!-- ❌ Плохо: hover "залипает" на мобильных -->
<button class="hover:bg-blue-600">Hover на мобильных</button>

<!-- ✅ Хорошо: используем hover только на десктопе -->
<button class="md:hover:bg-blue-600">Hover только на десктопе</button>
```

### ❌ Ошибка 8: Слишком много transition-свойств

```html
<!-- ❌ Плохо: transition-all может тормозить -->
<div class="transition-all duration-500">Тяжёлая анимация</div>

<!-- ✅ Хорошо: transition только для нужных свойств -->
<div class="transition-colors duration-200">Лёгкая анимация</div>
```

## 🎯 Что дальше?

Теперь вы полностью владеете состояниями элементов! Но это только часть responsive-дизайна. Следующий уровень — **продвинутые техники Tailwind CSS**: кастомизация, плагины, директивы.

**Следующий шаг:** [⚙️ Кастомизация Tailwind CSS](../advanced/customization.md) — изучим, как расширять конфигурацию и создавать собственные утилиты.

---

> 💬 **Упражнение:** создайте форму регистрации с floating labels, кастомными чекбоксами, toggle switch для уведомлений, и кнопкой с полным набором состояний (hover, focus, active, disabled). Все элементы должны иметь плавные transition-эффекты.

---




---

# 🔴 Раздел: Advanced

---



<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: advanced\customization.md -->
<!-- ═══════════════════════════════════════════════════════════ -->

# ⚙️ Кастомизация Tailwind CSS

> **Полное руководство по настройке Tailwind под ваш проект:** от базовой конфигурации до создания собственных утилит и плагинов

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Поймёте структуру `tailwind.config.js`
- ✅ Научитесь расширять тему: цвета, шрифты, отступы, breakpoints
- ✅ Освоите полную замену темы (когда нужно переопределить всё)
- ✅ Создадите собственные утилитарные классы
- ✅ Научитесь создавать компоненты через `addComponents`
- ✅ Поймёте, как работают плагины
- ✅ Освоите presets для переиспользования конфигурации
- ✅ Избежите типичных ошибок при кастомизации

## 📁 Структура `tailwind.config.js`

Полный конфиг выглядит так:

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  // 1. Какие файлы сканировать
  content: [
    './src/**/*.{html,js,jsx,ts,tsx,vue,svelte}',
    './public/**/*.html',
  ],

  // 2. Темы (дизайн-система)
  theme: {
    // Расширение стандартной темы
    extend: {
      colors: {},
      spacing: {},
      fontSize: {},
      fontFamily: {},
      screens: {},
      // ... другие свойства
    },
    // Или полная замена (без extend)
    // colors: {},
  },

  // 3. Плагины
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],

  // 4. Пресеты (базовая конфигурация)
  presets: [],

  // 5. Dark mode
  darkMode: 'class', // или 'media'

  // 6. Важность селекторов
  important: false, // или true, или '#app'

  // 7. Префикс для всех классов
  prefix: '', // например, 'tw-'

  // 8. Вариации (какие состояния генерировать)
  variants: {},
}
```

## 🎨 Расширение темы: `theme.extend`

### Добавление своих цветов

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        // Простой цвет
        'brand': '#ff5722',

        // Палитра с оттенками
        'brand': {
          50:  '#fff3ed',
          100: '#ffe4d6',
          200: '#ffc5ac',
          300: '#ffa082',
          400: '#ff7a58',
          500: '#ff5722', // основной
          600: '#e64a19',
          700: '#c43e14',
          800: '#a33310',
          900: '#7a260c',
          950: '#4d1808',
        },

        // Семантические цвета
        'success': '#10b981',
        'warning': '#f59e0b',
        'error':   '#ef4444',
        'info':    '#3b82f6',
      },
    },
  },
}
```

```html
<!-- Использование -->
<div class="bg-brand-500 text-white">Брендовый цвет</div>
<button class="bg-success hover:bg-success/90 text-white">Успех</button>
```

### Добавление своих отступов

```js
module.exports = {
  theme: {
    extend: {
      spacing: {
        '18': '4.5rem',    // 72px (между 16 и 20)
        '88': '22rem',     // 352px
        '128': '32rem',    // 512px
        'screen/2': '50vw',
        'screen/3': '33.33vw',
      },
    },
  },
}
```

```html
<div class="p-18">Кастомный padding 72px</div>
<div class="h-screen/2">Половина экрана</div>
```

### Добавление своих размеров шрифтов

```js
module.exports = {
  theme: {
    extend: {
      fontSize: {
        '2xs': ['0.625rem', { lineHeight: '0.875rem' }], // 10px
        'display': ['4rem', { lineHeight: '1', letterSpacing: '-0.02em' }], // 64px
      },
    },
  },
}
```

```html
<p class="text-2xs">Микро-текст</p>
<h1 class="text-display">Огромный заголовок</h1>
```

### Добавление своих breakpoints

```js
module.exports = {
  theme: {
    extend: {
      screens: {
        'xs': '480px',        // Очень маленькие мобильные
        '3xl': '1920px',      // Очень большие экраны
        'tablet': '640px',    // Семантические имена
        'laptop': '1024px',
        'desktop': '1280px',
        'portrait': { 'raw': '(orientation: portrait)' },
        'landscape': { 'raw': '(orientation: landscape)' },
      },
    },
  },
}
```

```html
<!-- Использование -->
<div class="text-sm xs:text-base md:text-lg laptop:text-xl">
  Адаптивный текст
</div>

<!-- Только для портретной ориентации -->
<div class="portrait:hidden">Скрыть в портрете</div>
```

### Добавление своих шрифтов

```js
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Inter', 'system-ui', 'sans-serif'],
        'display': ['"Playfair Display"', 'serif'],
        'mono': ['"JetBrains Mono"', 'monospace'],
        'handwriting': ['"Caveat"', 'cursive'],
      },
    },
  },
}
```

### Добавление своих теней

```js
module.exports = {
  theme: {
    extend: {
      boxShadow: {
        'inner-lg': 'inset 0 2px 4px 0 rgb(0 0 0 / 0.1)',
        'glow-blue': '0 0 20px rgb(59 130 246 / 0.5)',
        'glow-red': '0 0 20px rgb(239 68 68 / 0.5)',
        '3d': '0 10px 0 -2px #3b82f6, 0 15px 20px -5px rgb(0 0 0 / 0.3)',
      },
    },
  },
}
```

```html
<div class="shadow-glow-blue">Светящаяся синяя тень</div>
<button class="shadow-3d">3D кнопка</button>
```

### Добавление своих анимаций

```js
module.exports = {
  theme: {
    extend: {
      animation: {
        'fade-in': 'fadeIn 0.5s ease-in',
        'fade-out': 'fadeOut 0.5s ease-out',
        'slide-up': 'slideUp 0.3s ease-out',
        'slide-down': 'slideDown 0.3s ease-out',
        'bounce-slow': 'bounce 2s infinite',
        'pulse-slow': 'pulse 3s infinite',
        'spin-slow': 'spin 3s linear infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        fadeOut: {
          '0%': { opacity: '1' },
          '100%': { opacity: '0' },
        },
        slideUp: {
          '0%': { transform: 'translateY(20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        slideDown: {
          '0%': { transform: 'translateY(-20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
      },
    },
  },
}
```

```html
<div class="animate-fade-in">Плавное появление</div>
<div class="animate-slide-up">Скольжение вверх</div>
```

## 🔄 Полная замена темы

Если вам нужно **полностью заменить** стандартную тему (а не расширять), используйте `theme` без `extend`:

```js
module.exports = {
  theme: {
    // Полностью заменяет стандартные цвета
    colors: {
      'primary': '#3b82f6',
      'secondary': '#8b5cf6',
      'neutral': '#6b7280',
      'background': '#ffffff',
      'text': '#111827',
    },

    // Полностью заменяет стандартные отступы
    spacing: {
      '0': '0',
      '1': '0.25rem',
      '2': '0.5rem',
      '3': '0.75rem',
      '4': '1rem',
      '5': '1.25rem',
      '6': '1.5rem',
      '8': '2rem',
      '10': '2.5rem',
      '12': '3rem',
      '16': '4rem',
      '20': '5rem',
    },

    // Полностью заменяет breakpoints
    screens: {
      'mobile': '320px',
      'tablet': '768px',
      'desktop': '1024px',
      'wide': '1440px',
    },
  },
}
```

> ⚠️ **Важно:** при полной замене вы **теряете все стандартные значения**. Используйте только если действительно нужно переопределить всё.

### Комбинирование: extend + полная замена

```js
module.exports = {
  theme: {
    // Полная замена для colors
    colors: {
      'primary': '#3b82f6',
      'secondary': '#8b5cf6',
    },

    // Расширение для spacing (стандартные + свои)
    extend: {
      spacing: {
        '18': '4.5rem',
      },
    },
  },
}
```

## 🛠 Создание кастомных утилит

### Через `addUtilities` в плагине

```js
// tailwind.config.js
const plugin = require('tailwindcss/plugin')

module.exports = {
  plugins: [
    plugin(function({ addUtilities }) {
      const newUtilities = {
        '.text-shadow': {
          textShadow: '2px 2px 4px rgb(0 0 0 / 0.5)',
        },
        '.text-shadow-sm': {
          textShadow: '1px 1px 2px rgb(0 0 0 / 0.3)',
        },
        '.text-shadow-lg': {
          textShadow: '4px 4px 8px rgb(0 0 0 / 0.7)',
        },
        '.text-shadow-none': {
          textShadow: 'none',
        },
        '.scrollbar-hide': {
          /* IE and Edge */
          '-ms-overflow-style': 'none',
          /* Firefox */
          'scrollbar-width': 'none',
          /* Safari and Chrome */
          '&::-webkit-scrollbar': {
            display: 'none',
          },
        },
      }

      addUtilities(newUtilities)
    }),
  ],
}
```

```html
<h1 class="text-shadow-lg text-white">Текст с тенью</h1>
<div class="scrollbar-hide overflow-x-auto">...</div>
```

### Динамические утилиты

```js
const plugin = require('tailwindcss/plugin')

module.exports = {
  plugins: [
    plugin(function({ matchUtilities, theme }) {
      matchUtilities(
        {
          // Генерирует .text-shadow-{color}
          'text-shadow': (value) => ({
            textShadow: `2px 2px 4px ${value}`,
          }),
        },
        { values: theme('colors') }
      )
    }),
  ],
}
```

```html
<h1 class="text-shadow-blue-500">Синяя тень</h1>
<h1 class="text-shadow-red-500">Красная тень</h1>
```

## 🧩 Создание компонентов

Компоненты — это **переиспользуемые группы утилит**, которые применяются через один класс:

```js
const plugin = require('tailwindcss/plugin')

module.exports = {
  plugins: [
    plugin(function({ addComponents }) {
      const buttons = {
        '.btn': {
          padding: '0.5rem 1rem',
          borderRadius: '0.375rem',
          fontWeight: '500',
          transition: 'all 0.2s',
        },
        '.btn-primary': {
          backgroundColor: '#3b82f6',
          color: '#ffffff',
          '&:hover': {
            backgroundColor: '#2563eb',
          },
          '&:focus': {
            outline: 'none',
            boxShadow: '0 0 0 3px rgb(59 130 246 / 0.5)',
          },
        },
        '.btn-secondary': {
          backgroundColor: '#6b7280',
          color: '#ffffff',
          '&:hover': {
            backgroundColor: '#4b5563',
          },
        },
        '.btn-danger': {
          backgroundColor: '#ef4444',
          color: '#ffffff',
          '&:hover': {
            backgroundColor: '#dc2626',
          },
        },
        '.btn-lg': {
          padding: '0.75rem 1.5rem',
          fontSize: '1.125rem',
        },
        '.btn-sm': {
          padding: '0.25rem 0.75rem',
          fontSize: '0.875rem',
        },
      }

      addComponents(buttons)
    }),
  ],
}
```

```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-danger btn-lg">Danger Large</button>
```

### Компоненты с responsive-вариантами

```js
const plugin = require('tailwindcss/plugin')

module.exports = {
  plugins: [
    plugin(function({ addComponents, theme }) {
      addComponents({
        '.container': {
          width: '100%',
          marginRight: 'auto',
          marginLeft: 'auto',
          paddingLeft: '1rem',
          paddingRight: '1rem',
        },
      })

      // Responsive варианты
      const screens = theme('screens')
      const containerSizes = {
        'sm': '640px',
        'md': '768px',
        'lg': '1024px',
        'xl': '1280px',
        '2xl': '1536px',
      }

      Object.entries(screens).forEach(([breakpoint, value]) => {
        addComponents({
          [`@media (min-width: ${value})`]: {
            '.container': {
              maxWidth: containerSizes[breakpoint] || value,
            },
          },
        })
      })
    }),
  ],
}
```

## 🔌 Плагины

### Подключение готовых плагинов

```bash
npm install -D @tailwindcss/forms @tailwindcss/typography @tailwindcss/aspect-ratio @tailwindcss/container-queries
```

```js
// tailwind.config.js
module.exports = {
  plugins: [
    require('@tailwindcss/forms'),           // Улучшенные формы
    require('@tailwindcss/typography'),      // Типографика для статей
    require('@tailwindcss/aspect-ratio'),    // Aspect ratio (для старых браузеров)
    require('@tailwindcss/container-queries'), // Container queries
  ],
}
```

### Пример: @tailwindcss/forms

```html
<!-- Без плагина: нужно стилизовать каждое поле -->
<input type="text" class="border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500">

<!-- С плагином: базовые стили применяются автоматически -->
<input type="text" class="form-input rounded border-gray-300 focus:border-blue-500 focus:ring-blue-500">
<select class="form-select rounded border-gray-300">...</select>
<input type="checkbox" class="form-checkbox rounded border-gray-300 text-blue-600">
```

### Пример: @tailwindcss/typography

```html
<article class="prose prose-lg prose-blue max-w-none">
  <h1>Заголовок статьи</h1>
  <p>
    Плагин <code>typography</code> автоматически стилизует весь HTML-контент:
    заголовки, параграфы, списки, цитаты, код и таблицы.
  </p>
  <h2>Подзаголовок</h2>
  <ul>
    <li>Пункт 1</li>
    <li>Пункт 2</li>
  </ul>
  <blockquote>
    Цитата с автоматическим стилем.
  </blockquote>
  <pre><code>const x = 42;</code></pre>
</article>
```

Варианты:
- `prose` — базовый
- `prose-sm`, `prose-base`, `prose-lg`, `prose-xl`, `prose-2xl` — размеры
- `prose-slate`, `prose-gray`, `prose-zinc`, `prose-neutral`, `prose-stone` — цвета
- `prose-invert` — для тёмной темы

### Создание собственного плагина

```js
// plugins/text-shadow.js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ addUtilities, theme }) {
  const textShadows = {
    '.text-shadow': {
      textShadow: '2px 2px 4px rgb(0 0 0 / 0.5)',
    },
    '.text-shadow-sm': {
      textShadow: '1px 1px 2px rgb(0 0 0 / 0.3)',
    },
    '.text-shadow-lg': {
      textShadow: '4px 4px 8px rgb(0 0 0 / 0.7)',
    },
  }

  addUtilities(textShadows, ['responsive', 'hover'])
})
```

```js
// tailwind.config.js
module.exports = {
  plugins: [
    require('./plugins/text-shadow.js'),
  ],
}
```

### Плагин с конфигурацией

```js
// plugins/badges.js
const plugin = require('tailwindcss/plugin')

module.exports = plugin.withOptions(
  function(options = {}) {
    return function({ addComponents, theme }) {
      const variants = options.variants || ['primary', 'secondary', 'success', 'warning', 'danger']

      const badges = {}

      variants.forEach(variant => {
        const color = theme(`colors.${variant}`, theme(`colors.blue`))

        badges[`.badge-${variant}`] = {
          display: 'inline-flex',
          alignItems: 'center',
          padding: '0.25rem 0.75rem',
          borderRadius: '9999px',
          fontSize: '0.75rem',
          fontWeight: '500',
          backgroundColor: color[100],
          color: color[800],
        }
      })

      addComponents(badges)
    }
  },
  function(options = {}) {
    return {
      variants: options.variants || ['primary', 'secondary', 'success', 'warning', 'danger'],
    }
  }
)
```

```js
// tailwind.config.js
module.exports = {
  plugins: [
    require('./plugins/badges')({
      variants: ['primary', 'secondary', 'success', 'warning', 'danger', 'info'],
    }),
  ],
}
```

```html
<span class="badge-primary">Primary</span>
<span class="badge-success">Success</span>
<span class="badge-danger">Danger</span>
```

## 📦 Presets

Presets позволяют **переиспользовать конфигурацию** между проектами:

```js
// presets/company-preset.js
module.exports = {
  theme: {
    extend: {
      colors: {
        'brand': {
          50:  '#f0f9ff',
          500: '#0ea5e9',
          900: '#0c4a6e',
        },
      },
      fontFamily: {
        'sans': ['Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
```

```js
// tailwind.config.js
module.exports = {
  presets: [
    require('./presets/company-preset.js'),
  ],

  // Можно расширить preset
  theme: {
    extend: {
      colors: {
        'accent': '#ec4899',
      },
    },
  },
}
```

## 🎯 Практические паттерны

### 1. 🎨 Полная дизайн-система

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        // Брендовые цвета
        'brand': {
          50:  '#f0f9ff',
          100: '#e0f2fe',
          500: '#0ea5e9',
          600: '#0284c7',
          700: '#0369a1',
          900: '#0c4a6e',
        },

        // Семантические цвета
        'success': {
          50: '#f0fdf4',
          500: '#22c55e',
          700: '#15803d',
        },
        'warning': {
          50: '#fffbeb',
          500: '#f59e0b',
          700: '#b45309',
        },
        'error': {
          50: '#fef2f2',
          500: '#ef4444',
          700: '#b91c1c',
        },
      },

      fontFamily: {
        'sans': ['Inter', 'system-ui', 'sans-serif'],
        'display': ['"Playfair Display"', 'serif'],
        'mono': ['"JetBrains Mono"', 'monospace'],
      },

      spacing: {
        '18': '4.5rem',
        '88': '22rem',
        '128': '32rem',
      },

      borderRadius: {
        '4xl': '2rem',
      },

      boxShadow: {
        'glow': '0 0 20px rgb(14 165 233 / 0.5)',
        'glow-lg': '0 0 40px rgb(14 165 233 / 0.6)',
      },

      animation: {
        'fade-in': 'fadeIn 0.3s ease-out',
        'slide-up': 'slideUp 0.3s ease-out',
      },

      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
      },
    },
  },

  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('./plugins/text-shadow.js'),
  ],
}
```

### 2. 🎨 CSS-переменные для динамической темизации

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        'primary': 'rgb(var(--color-primary) / <alpha-value>)',
        'secondary': 'rgb(var(--color-secondary) / <alpha-value>)',
        'background': 'rgb(var(--color-background) / <alpha-value>)',
        'surface': 'rgb(var(--color-surface) / <alpha-value>)',
        'content': 'rgb(var(--color-content) / <alpha-value>)',
        'content-secondary': 'rgb(var(--color-content-secondary) / <alpha-value>)',
      },
    },
  },
}
```

```css
/* styles.css */
:root {
  --color-primary: 14 165 233;        /* #0ea5e9 */
  --color-secondary: 139 92 246;      /* #8b5cf6 */
  --color-background: 255 255 255;
  --color-surface: 249 250 251;       /* gray-50 */
  --color-content: 17 24 39;          /* gray-900 */
  --color-content-secondary: 75 85 99; /* gray-600 */
}

.dark {
  --color-primary: 56 189 248;        /* #38bdf8 */
  --color-secondary: 167 139 250;     /* #a78bfa */
  --color-background: 17 24 39;       /* gray-900 */
  --color-surface: 31 41 55;          /* gray-800 */
  --color-content: 243 244 246;       /* gray-100 */
  --color-content-secondary: 156 163 175; /* gray-400 */
}
```

```html
<!-- Автоматически адаптируется -->
<div class="bg-background text-content">
  <div class="bg-surface p-4">
    <h2 class="text-primary">Заголовок</h2>
    <p class="text-content-secondary">Описание</p>
  </div>
</div>

<!-- Работает с прозрачностью -->
<div class="bg-primary/10 border border-primary/20">
  Полупрозрачный фон
</div>
```

### 3. 🔌 Плагин для кастомных кнопок

```js
// plugins/buttons.js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ addComponents, theme }) {
  const baseButton = {
    display: 'inline-flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontWeight: '500',
    borderRadius: '0.5rem',
    transition: 'all 0.2s',
    '&:focus': {
      outline: 'none',
      ring: '2px',
    },
    '&:disabled': {
      opacity: '0.5',
      cursor: 'not-allowed',
    },
  }

  addComponents([
    {
      '.btn': baseButton,
      '.btn-sm': { padding: '0.375rem 0.75rem', fontSize: '0.875rem' },
      '.btn-md': { padding: '0.5rem 1rem', fontSize: '1rem' },
      '.btn-lg': { padding: '0.75rem 1.5rem', fontSize: '1.125rem' },
    },
    {
      '.btn-primary': {
        backgroundColor: theme('colors.blue.600'),
        color: '#ffffff',
        '&:hover': { backgroundColor: theme('colors.blue.700') },
        '&:focus': { boxShadow: `0 0 0 3px ${theme('colors.blue.500')}50` },
      },
      '.btn-secondary': {
        backgroundColor: theme('colors.gray.600'),
        color: '#ffffff',
        '&:hover': { backgroundColor: theme('colors.gray.700') },
      },
      '.btn-outline': {
        backgroundColor: 'transparent',
        border: `1px solid ${theme('colors.gray.300')}`,
        color: theme('colors.gray.700'),
        '&:hover': { backgroundColor: theme('colors.gray.50') },
      },
      '.btn-ghost': {
        backgroundColor: 'transparent',
        color: theme('colors.gray.700'),
        '&:hover': { backgroundColor: theme('colors.gray.100') },
      },
    },
  ])
})
```

```html
<button class="btn btn-md btn-primary">Primary</button>
<button class="btn btn-lg btn-secondary">Secondary</button>
<button class="btn btn-sm btn-outline">Outline</button>
<button class="btn btn-md btn-ghost">Ghost</button>
<button class="btn btn-md btn-primary" disabled>Disabled</button>
```

## 📊 Шпаргалка: что когда использовать

| Задача | Решение |
| :-- | :-- |
| Добавить свой цвет | `theme.extend.colors` |
| Заменить все цвета | `theme.colors` (без extend) |
| Добавить свой отступ | `theme.extend.spacing` |
| Добавить свой шрифт | `theme.extend.fontFamily` |
| Добавить свой breakpoint | `theme.extend.screens` |
| Добавить свою тень | `theme.extend.boxShadow` |
| Добавить свою анимацию | `theme.extend.animation` + `keyframes` |
| Создать утилиту | `addUtilities` в плагине |
| Создать компонент | `addComponents` в плагине |
| Переиспользовать конфиг | `presets` |
| Динамическая темизация | CSS-переменные + `theme.extend.colors` |
| Подключить готовый плагин | `plugins: [require('@tailwindcss/forms')]` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Забывают `content` в конфиге

```js
// ❌ Плохо: Tailwind не найдёт классы
module.exports = {
  theme: {
    extend: {
      colors: {
        'brand': '#ff5722',
      },
    },
  },
}

// ✅ Хорошо: указываем, где искать классы
module.exports = {
  content: [
    './src/**/*.{html,js,jsx,ts,tsx,vue}',
  ],
  theme: {
    extend: {
      colors: {
        'brand': '#ff5722',
      },
    },
  },
}
```

### ❌ Ошибка 2: Полная замена вместо расширения

```js
// ❌ Плохо: теряем все стандартные цвета
module.exports = {
  theme: {
    colors: {
      'brand': '#ff5722',
    },
  },
}

// ✅ Хорошо: расширяем стандартные цвета
module.exports = {
  theme: {
    extend: {
      colors: {
        'brand': '#ff5722',
      },
    },
  },
}
```

### ❌ Ошибка 3: Конфликт имён со стандартными утилитами

```js
// ❌ Плохо: конфликт с .text-red-500
module.exports = {
  theme: {
    extend: {
      colors: {
        'red': '#ff0000', // Перезаписывает стандартный red
      },
    },
  },
}

// ✅ Хорошо: используем уникальное имя
module.exports = {
  theme: {
    extend: {
      colors: {
        'brand-red': '#ff0000',
      },
    },
  },
}
```

### ❌ Ошибка 4: Забывают про `<alpha-value>` для CSS-переменных

```js
// ❌ Плохо: bg-primary/50 не будет работать
module.exports = {
  theme: {
    extend: {
      colors: {
        'primary': 'rgb(var(--color-primary))',
      },
    },
  },
}

// ✅ Хорошо: добавляем <alpha-value>
module.exports = {
  theme: {
    extend: {
      colors: {
        'primary': 'rgb(var(--color-primary) / <alpha-value>)',
      },
    },
  },
}
```

### ❌ Ошибка 5: Изменяют конфиг без перезапуска

```bash
# ❌ Плохо: изменения не применятся
# Просто редактируем tailwind.config.js

# ✅ Хорошо: перезапускаем dev-сервер
npm run dev
# или
npx tailwindcss -i ./src/input.css -o ./src/output.css --watch
```

### ❌ Ошибка 6: Слишком много кастомных утилит

```js
// ❌ Плохо: раздуваем CSS
const plugin = require('tailwindcss/plugin')

module.exports = {
  plugins: [
    plugin(function({ addUtilities }) {
      addUtilities({
        '.my-custom-text-red': { color: 'red' },
        '.my-custom-bg-blue': { backgroundColor: 'blue' },
        '.my-custom-p-4': { padding: '1rem' },
        // ... сотни таких утилит
      })
    }),
  ],
}

// ✅ Хорошо: используем стандартные утилиты или arbitrary values
<div class="text-red-500 bg-blue-500 p-4">...</div>
<div class="text-[#ff0000] bg-[#0000ff]">...</div>
```

## 🎯 Что дальше?

Теперь вы полностью владеете кастомизацией Tailwind CSS! Но это только начало продвинутого уровня. Следующие важные темы:

- **[Плагины](plugins.md)** — углублённое создание плагинов
- **[Директивы](directives.md)** — `@apply`, `@layer`, `theme()`
- **[Оптимизация](optimization.md)** — PurgeCSS, production build

**Следующий шаг:** [🔌 Плагины в Tailwind CSS](plugins.md) — изучим создание мощных плагинов для расширения функциональности.

---

---




<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: advanced\directives.md -->
<!-- ═══════════════════════════════════════════════════════════ -->

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

---




<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: advanced\optimization.md -->
<!-- ═══════════════════════════════════════════════════════════ -->

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

---




<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: advanced\plugins.md -->
<!-- ═══════════════════════════════════════════════════════════ -->

# 🔌 Плагины в Tailwind CSS

> **Полное руководство по плагинам:** от подключения готовых плагинов до создания собственных расширений функциональности

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Поймёте, что такое плагины и зачем они нужны
- ✅ Научитесь подключать официальные плагины Tailwind
- ✅ Освоите создание собственных плагинов
- ✅ Поймёте разницу между `addUtilities`, `addComponents`, `addBase`
- ✅ Научитесь создавать динамические утилиты через `matchUtilities`
- ✅ Освоите работу с темой через `theme()`
- ✅ Создадите плагины с конфигурацией
- ✅ Избежите типичных ошибок при работе с плагинами

## 🧩 Что такое плагины?

**Плагины** — это способ расширять функциональность Tailwind CSS. Они позволяют:

- Добавлять **новые утилиты** (например, `text-shadow`, `scrollbar-hide`)
- Создавать **компоненты** (например, `.btn`, `.card`)
- Добавлять **базовые стили** (например, сброс CSS, типографика)
- Расширять **тему** (цвета, шрифты, отступы)
- Добавлять **варианты** (модификаторы состояний)

## 📦 Официальные плагины

### @tailwindcss/forms

Автоматически стилизует формы для консистентного вида:

```bash
npm install -D @tailwindcss/forms
```

```js
// tailwind.config.js
module.exports = {
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
```

```html
<!-- Без плагина: нужно стилизовать каждое поле -->
<input type="text" class="border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500">

<!-- С плагином: базовые стили применяются автоматически -->
<input type="text" class="form-input rounded border-gray-300 focus:border-blue-500 focus:ring-blue-500">
<select class="form-select rounded border-gray-300">...</select>
<input type="checkbox" class="form-checkbox rounded border-gray-300 text-blue-600">
<input type="radio" class="form-radio border-gray-300 text-blue-600">
```

#### Стратегии стилизации

```js
// tailwind.config.js
module.exports = {
  plugins: [
    require('@tailwindcss/forms')({
      strategy: 'base', // или 'class'
    }),
  ],
}
```

- `strategy: 'base'` (по умолчанию) — стили применяются ко всем формам
- `strategy: 'class'` — стили только к элементам с классом `form-*`

### @tailwindcss/typography

Добавляет класс `prose` для стилизации HTML-контента:

```bash
npm install -D @tailwindcss/typography
```

```js
// tailwind.config.js
module.exports = {
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
```

```html
<article class="prose prose-lg prose-blue max-w-none">
  <h1>Заголовок статьи</h1>
  <p>
    Плагин <code>typography</code> автоматически стилизует весь HTML-контент:
    заголовки, параграфы, списки, цитаты, код и таблицы.
  </p>
  <h2>Подзаголовок</h2>
  <ul>
    <li>Пункт 1</li>
    <li>Пункт 2</li>
  </ul>
  <blockquote>
    Цитата с автоматическим стилем.
  </blockquote>
  <pre><code>const x = 42;</code></pre>
</article>
```

#### Варианты `prose`

- **Размеры:** `prose-sm`, `prose-base`, `prose-lg`, `prose-xl`, `prose-2xl`
- **Цвета:** `prose-slate`, `prose-gray`, `prose-zinc`, `prose-neutral`, `prose-stone`
- **Тёмная тема:** `prose-invert`

```html
<!-- Большая типографика в синих тонах -->
<article class="prose prose-lg prose-blue">...</article>

<!-- Тёмная тема -->
<article class="prose prose-invert">...</article>
```

### @tailwindcss/aspect-ratio

Полезно для старых браузеров, которые не поддерживают `aspect-ratio`:

```bash
npm install -D @tailwindcss/aspect-ratio
```

```js
// tailwind.config.js
module.exports = {
  plugins: [
    require('@tailwindcss/aspect-ratio'),
  ],
}
```

```html
<!-- 16:9 видео -->
<div class="aspect-w-16 aspect-h-9">
  <iframe src="..."></iframe>
</div>

<!-- 1:1 квадрат -->
<div class="aspect-w-1 aspect-h-1">
  <img src="..." class="object-cover">
</div>
```

### @tailwindcss/container-queries

Добавляет поддержку container queries:

```bash
npm install -D @tailwindcss/container-queries
```

```js
// tailwind.config.js
module.exports = {
  plugins: [
    require('@tailwindcss/container-queries'),
  ],
}
```

```html
<div class="@container">
  <div class="@md:flex @lg:grid @lg:grid-cols-3">
    <!-- Меняет layout в зависимости от ширины контейнера -->
  </div>
</div>
```

## 🛠 Создание собственных плагинов

### Базовая структура

```js
// plugins/my-plugin.js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ addUtilities, addComponents, addBase, theme }) {
  // Ваш код здесь
})
```

### Подключение плагина

```js
// tailwind.config.js
module.exports = {
  plugins: [
    require('./plugins/my-plugin.js'),
  ],
}
```

## 🎨 Добавление утилит: `addUtilities`

`addUtilities` добавляет **новые утилитарные классы**:

```js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ addUtilities }) {
  const newUtilities = {
    // Text shadow
    '.text-shadow': {
      textShadow: '2px 2px 4px rgb(0 0 0 / 0.5)',
    },
    '.text-shadow-sm': {
      textShadow: '1px 1px 2px rgb(0 0 0 / 0.3)',
    },
    '.text-shadow-lg': {
      textShadow: '4px 4px 8px rgb(0 0 0 / 0.7)',
    },
    '.text-shadow-none': {
      textShadow: 'none',
    },

    // Scrollbar hide
    '.scrollbar-hide': {
      /* IE and Edge */
      '-ms-overflow-style': 'none',
      /* Firefox */
      'scrollbar-width': 'none',
      /* Safari and Chrome */
      '&::-webkit-scrollbar': {
        display: 'none',
      },
    },

    // Content visibility
    '.content-auto': {
      contentVisibility: 'auto',
    },
    '.content-hidden': {
      contentVisibility: 'hidden',
    },
  }

  addUtilities(newUtilities)
})
```

```html
<h1 class="text-shadow-lg text-white">Текст с тенью</h1>
<div class="scrollbar-hide overflow-x-auto">...</div>
```

### Динамические утилиты: `matchUtilities`

`matchUtilities` создаёт **динамические утилиты** на основе темы:

```js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ matchUtilities, theme }) {
  matchUtilities(
    {
      // Генерирует .text-shadow-{color}
      'text-shadow': (value) => ({
        textShadow: `2px 2px 4px ${value}`,
      }),
    },
    { values: theme('colors') }
  )
})
```

```html
<h1 class="text-shadow-blue-500">Синяя тень</h1>
<h1 class="text-shadow-red-500">Красная тень</h1>
<h1 class="text-shadow-green-500">Зелёная тень</h1>
```

### Утилиты с вариантами

```js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ addUtilities }) {
  addUtilities({
    '.text-shadow': {
      textShadow: '2px 2px 4px rgb(0 0 0 / 0.5)',
    },
  }, {
    variants: ['responsive', 'hover', 'focus', 'dark'],
  })
})
```

```html
<!-- Работает с модификаторами -->
<h1 class="text-shadow hover:text-shadow-lg dark:text-shadow-sm">
  Адаптивная тень
</h1>
```

## 🧩 Добавление компонентов: `addComponents`

`addComponents` добавляет **переиспользуемые компоненты**:

```js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ addComponents }) {
  const buttons = {
    '.btn': {
      padding: '0.5rem 1rem',
      borderRadius: '0.375rem',
      fontWeight: '500',
      transition: 'all 0.2s',
      '&:focus': {
        outline: 'none',
        boxShadow: '0 0 0 3px rgb(59 130 246 / 0.5)',
      },
      '&:disabled': {
        opacity: '0.5',
        cursor: 'not-allowed',
      },
    },
    '.btn-primary': {
      backgroundColor: '#3b82f6',
      color: '#ffffff',
      '&:hover': {
        backgroundColor: '#2563eb',
      },
    },
    '.btn-secondary': {
      backgroundColor: '#6b7280',
      color: '#ffffff',
      '&:hover': {
        backgroundColor: '#4b5563',
      },
    },
    '.btn-outline': {
      backgroundColor: 'transparent',
      border: '1px solid #d1d5db',
      color: '#374151',
      '&:hover': {
        backgroundColor: '#f9fafb',
      },
    },
    '.btn-lg': {
      padding: '0.75rem 1.5rem',
      fontSize: '1.125rem',
    },
    '.btn-sm': {
      padding: '0.25rem 0.75rem',
      fontSize: '0.875rem',
    },
  }

  addComponents(buttons)
})
```

```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary btn-lg">Secondary Large</button>
<button class="btn btn-outline btn-sm">Outline Small</button>
```

### Компоненты с темой

```js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ addComponents, theme }) {
  addComponents({
    '.card': {
      backgroundColor: theme('colors.white'),
      borderRadius: theme('borderRadius.lg'),
      boxShadow: theme('boxShadow.md'),
      padding: theme('spacing.6'),
      '&:hover': {
        boxShadow: theme('boxShadow.lg'),
      },
    },
  })
})
```

## 🎨 Добавление базовых стилей: `addBase`

`addBase` добавляет **глобальные стили** (как в `@layer base`):

```js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ addBase, theme }) {
  addBase({
    'html': {
      fontFamily: theme('fontFamily.sans'),
      lineHeight: theme('lineHeight.normal'),
    },
    'body': {
      backgroundColor: theme('colors.gray.50'),
      color: theme('colors.gray.900'),
    },
    'h1': {
      fontSize: theme('fontSize.4xl'),
      fontWeight: theme('fontWeight.bold'),
    },
    'h2': {
      fontSize: theme('fontSize.3xl'),
      fontWeight: theme('fontWeight.semibold'),
    },
    'a': {
      color: theme('colors.blue.600'),
      '&:hover': {
        color: theme('colors.blue.800'),
      },
    },
  })
})
```

## 🎯 Работа с темой: `theme()`

Функция `theme()` позволяет **получать значения из конфигурации**:

```js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ addUtilities, theme }) {
  // Получаем цвета из темы
  const colors = theme('colors')

  // Получаем конкретный цвет
  const primaryColor = theme('colors.blue.500')

  // Получаем отступы
  const spacing = theme('spacing')

  // Получаем breakpoints
  const screens = theme('screens')

  addUtilities({
    '.custom-shadow': {
      boxShadow: `0 4px 6px -1px ${primaryColor}40`,
    },
  })
})
```

### Fallback значения

```js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ theme }) {
  // С fallback значением
  const customColor = theme('colors.brand', '#ff5722')

  // Без fallback (undefined, если не найдено)
  const maybeColor = theme('colors.maybe')
})
```

## 🔧 Плагины с конфигурацией

### `plugin.withOptions`

Позволяет создавать плагины **с параметрами**:

```js
// plugins/badges.js
const plugin = require('tailwindcss/plugin')

module.exports = plugin.withOptions(
  function(options = {}) {
    return function({ addComponents, theme }) {
      const variants = options.variants || ['primary', 'secondary', 'success', 'warning', 'danger']

      const badges = {}

      variants.forEach(variant => {
        const color = theme(`colors.${variant}`, theme('colors.blue'))

        badges[`.badge-${variant}`] = {
          display: 'inline-flex',
          alignItems: 'center',
          padding: '0.25rem 0.75rem',
          borderRadius: '9999px',
          fontSize: '0.75rem',
          fontWeight: '500',
          backgroundColor: color[100] || color,
          color: color[800] || color,
        }
      })

      addComponents(badges)
    }
  },
  function(options = {}) {
    return {
      variants: options.variants || ['primary', 'secondary', 'success', 'warning', 'danger'],
    }
  }
)
```

```js
// tailwind.config.js
module.exports = {
  plugins: [
    require('./plugins/badges')({
      variants: ['primary', 'secondary', 'success', 'warning', 'danger', 'info'],
    }),
  ],
}
```

```html
<span class="badge-primary">Primary</span>
<span class="badge-success">Success</span>
<span class="badge-danger">Danger</span>
<span class="badge-info">Info</span>
```

## 🎨 Практические паттерны

### 1. 🔤 Плагин для text-shadow

```js
// plugins/text-shadow.js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ matchUtilities, theme }) {
  matchUtilities(
    {
      'text-shadow': (value) => ({
        textShadow: `2px 2px 4px ${value}`,
      }),
      'text-shadow-sm': (value) => ({
        textShadow: `1px 1px 2px ${value}`,
      }),
      'text-shadow-lg': (value) => ({
        textShadow: `4px 4px 8px ${value}`,
      }),
    },
    { values: theme('colors') }
  )
})
```

```html
<h1 class="text-shadow-blue-500 text-4xl font-bold">
  Синяя тень
</h1>
<h1 class="text-shadow-lg-red-500 text-4xl font-bold">
  Большая красная тень
</h1>
```

### 2. 🎴 Плагин для карточек

```js
// plugins/cards.js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ addComponents, theme }) {
  addComponents({
    '.card': {
      backgroundColor: theme('colors.white'),
      borderRadius: theme('borderRadius.lg'),
      boxShadow: theme('boxShadow.md'),
      overflow: 'hidden',
      transition: 'box-shadow 0.2s',
      '&:hover': {
        boxShadow: theme('boxShadow.lg'),
      },
    },
    '.card-header': {
      padding: `${theme('spacing.4')} ${theme('spacing.6')}`,
      borderBottom: `1px solid ${theme('colors.gray.200')}`,
    },
    '.card-body': {
      padding: theme('spacing.6'),
    },
    '.card-footer': {
      padding: `${theme('spacing.4')} ${theme('spacing.6')}`,
      borderTop: `1px solid ${theme('colors.gray.200')}`,
      backgroundColor: theme('colors.gray.50'),
    },
  })
})
```

```html
<div class="card max-w-sm">
  <div class="card-header">
    <h3 class="text-lg font-bold">Заголовок</h3>
  </div>
  <div class="card-body">
    <p>Содержимое карточки</p>
  </div>
  <div class="card-footer">
    <button class="btn btn-primary">Действие</button>
  </div>
</div>
```

### 3. 🎨 Плагин для градиентных текстов

```js
// plugins/gradient-text.js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ matchUtilities, theme }) {
  matchUtilities(
    {
      'gradient-text': (value) => ({
        background: `linear-gradient(to right, ${value.from}, ${value.to})`,
        '-webkit-background-clip': 'text',
        '-webkit-text-fill-color': 'transparent',
        'background-clip': 'text',
      }),
    },
    {
      values: {
        'blue-purple': { from: theme('colors.blue.500'), to: theme('colors.purple.500') },
        'pink-red': { from: theme('colors.pink.500'), to: theme('colors.red.500') },
        'green-blue': { from: theme('colors.green.500'), to: theme('colors.blue.500') },
        'yellow-orange': { from: theme('colors.yellow.500'), to: theme('colors.orange.500') },
      },
    }
  )
})
```

```html
<h1 class="gradient-text-blue-purple text-5xl font-bold">
  Градиентный текст
</h1>
<h1 class="gradient-text-pink-red text-5xl font-bold">
  Розово-красный градиент
</h1>
```

### 4. 📏 Плагин для кастомных контейнеров

```js
// plugins/container.js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ addComponents, theme }) {
  const screens = theme('screens')

  const containerStyles = {
    '.container': {
      width: '100%',
      marginRight: 'auto',
      marginLeft: 'auto',
      paddingLeft: theme('spacing.4'),
      paddingRight: theme('spacing.4'),
    },
  }

  // Добавляем max-width для каждого breakpoint
  Object.entries(screens).forEach(([breakpoint, value]) => {
    containerStyles[`@media (min-width: ${value})`] = {
      '.container': {
        maxWidth: value,
      },
    }
  })

  addComponents(containerStyles)
})
```

```html
<div class="container">
  <!-- Контент с автоматической шириной для каждого breakpoint -->
</div>
```

### 5. 🎯 Плагин для aspect-ratio

```js
// plugins/aspect-ratio.js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ addUtilities }) {
  addUtilities({
    '.aspect-square': {
      aspectRatio: '1 / 1',
    },
    '.aspect-video': {
      aspectRatio: '16 / 9',
    },
    '.aspect-portrait': {
      aspectRatio: '3 / 4',
    },
    '.aspect-landscape': {
      aspectRatio: '4 / 3',
    },
    '.aspect-ultrawide': {
      aspectRatio: '21 / 9',
    },
  })
})
```

```html
<div class="aspect-video bg-gray-200">
  <img src="video-thumbnail.jpg" class="w-full h-full object-cover">
</div>
```

## 📊 Шпаргалка: что когда использовать

| Задача | Метод |
| :-- | :-- |
| Добавить новую утилиту | `addUtilities` |
| Динамическая утилита на основе темы | `matchUtilities` |
| Создать переиспользуемый компонент | `addComponents` |
| Добавить глобальные стили | `addBase` |
| Получить значение из темы | `theme('colors.blue.500')` |
| Плагин с параметрами | `plugin.withOptions` |
| Подключить официальный плагин | `require('@tailwindcss/forms')` |
| Подключить свой плагин | `require('./plugins/my-plugin.js')` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Забывают `require('tailwindcss/plugin')`

```js
// ❌ Плохо: plugin не определён
module.exports = function({ addUtilities }) {
  // ...
}

// ✅ Хорошо: импортируем plugin
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ addUtilities }) {
  // ...
})
```

### ❌ Ошибка 2: Забывают подключить плагин в конфиге

```js
// ❌ Плохо: плагин создан, но не подключён
// plugins/my-plugin.js создан, но tailwind.config.js не обновлён

// ✅ Хорошо: подключаем в tailwind.config.js
module.exports = {
  plugins: [
    require('./plugins/my-plugin.js'),
  ],
}
```

### ❌ Ошибка 3: Конфликт имён со стандартными утилитами

```js
// ❌ Плохо: конфликт с .text-blue-500
addUtilities({
  '.text-blue-500': {
    color: '#0000ff',
  },
})

// ✅ Хорошо: используем уникальное имя
addUtilities({
  '.custom-text-blue': {
    color: '#0000ff',
  },
})
```

### ❌ Ошибка 4: Забывают про `&` для pseudo-классов

```js
// ❌ Плохо: :hover не работает
addComponents({
  '.btn': {
    backgroundColor: 'blue',
    ':hover': {
      backgroundColor: 'darkblue',
    },
  },
})

// ✅ Хорошо: используем &
addComponents({
  '.btn': {
    backgroundColor: 'blue',
    '&:hover': {
      backgroundColor: 'darkblue',
    },
  },
})
```

### ❌ Ошибка 5: Забывают про `theme()` для консистентности

```js
// ❌ Плохо: жёстко закодированные значения
addComponents({
  '.card': {
    padding: '24px',
    borderRadius: '8px',
  },
})

// ✅ Хорошо: используем значения из темы
addComponents({
  '.card': {
    padding: theme('spacing.6'),
    borderRadius: theme('borderRadius.lg'),
  },
})
```

### ❌ Ошибка 6: Слишком сложные плагины

```js
// ❌ Плохо: плагин делает слишком много
module.exports = plugin(function({ addUtilities, addComponents, addBase }) {
  // 500 строк кода...
})

// ✅ Хорошо: разбиваем на несколько плагинов
module.exports = {
  plugins: [
    require('./plugins/text-shadow.js'),
    require('./plugins/cards.js'),
    require('./plugins/buttons.js'),
  ],
}
```

## 🎯 Что дальше?

Теперь вы полностью владеете плагинами Tailwind CSS! Но это только часть продвинутого уровня. Следующие важные темы:

- **[Директивы](directives.md)** — `@apply`, `@layer`, `theme()`
- **[Оптимизация](optimization.md)** — PurgeCSS, production build

**Следующий шаг:** [📝 Директивы в Tailwind CSS](directives.md) — изучим работу с `@apply`, `@layer` и другими директивами.

---


---




---

# 🔌 Раздел: Integrations

---



<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: integrations\nextjs.md -->
<!-- ═══════════════════════════════════════════════════════════ -->

# 🚀 Next.js + Tailwind CSS

> **Полное руководство по интеграции Tailwind CSS с Next.js:** от базовой настройки до Server Components, оптимизации шрифтов, изображений и production-деплоя

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Настроите Tailwind CSS в Next.js (App Router и Pages Router)
- ✅ Поймёте особенности работы с Server и Client Components
- ✅ Освоите `next/font` для оптимизации шрифтов
- ✅ Научитесь использовать `next/image` с Tailwind
- ✅ Настроите dark mode через `next-themes` без мигания
- ✅ Интегрируете Metadata API с Tailwind
- ✅ Освоите паттерны для App Router
- ✅ Избежите типичных ошибок при работе с Next.js + Tailwind

## 🚀 Установка и настройка

### Вариант 1: App Router (Next.js 13+, рекомендуется)

```bash
# Создание проекта
npx create-next-app@latest my-app
cd my-app

# Tailwind уже установлен по умолчанию!
# Если нужно установить вручную:
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

```js
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx}',
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
    './src/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

```css
/* app/globals.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

```tsx
// app/layout.tsx
import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'My App',
  description: 'Generated by create next app',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="ru" className={inter.className}>
      <body className="min-h-screen bg-white dark:bg-gray-900">
        {children}
      </body>
    </html>
  )
}
```

### Вариант 2: Pages Router (legacy)

```js
// tailwind.config.js
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
  ],
}
```

```css
/* styles/globals.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

```tsx
// pages/_app.tsx
import type { AppProps } from 'next/app'
import '@/styles/globals.css'

export default function App({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />
}
```

```tsx
// pages/_document.tsx
import { Html, Head, Main, NextScript } from 'next/document'

export default function Document() {
  return (
    <Html lang="ru">
      <Head />
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}
```

## 🎨 Server Components vs Client Components

В Next.js App Router есть **два типа компонентов**, и это влияет на использование Tailwind:

### Server Components (по умолчанию)

```tsx
// app/page.tsx — это Server Component
export default function HomePage() {
  return (
    <main className="min-h-screen bg-gray-50">
      <h1 className="text-4xl font-bold text-gray-900">
        Привет, Next.js!
      </h1>
      <p className="mt-4 text-gray-600">
        Этот компонент рендерится на сервере
      </p>
    </main>
  )
}
```

> 💡 **Правило:** все стили Tailwind работают одинаково в обоих типах компонентов. Разница только в том, где компонент рендерится.

### Client Components

```tsx
'use client'

import { useState } from 'react'

export default function Counter() {
  const [count, setCount] = useState(0)
  
  return (
    <div className="p-6 bg-white rounded-lg shadow-md">
      <p className="text-2xl font-bold text-gray-900">{count}</p>
      <button
        onClick={() => setCount(count + 1)}
        className="mt-4 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
      >
        Увеличить
      </button>
    </div>
  )
}
```

### Комбинирование

```tsx
// app/page.tsx — Server Component
import ClientCounter from '@/components/ClientCounter'

export default async function Page() {
  // Данные можно получать на сервере
  const data = await fetch('https://api.example.com/data').then(r => r.json())
  
  return (
    <main className="min-h-screen bg-gray-50 p-8">
      <h1 className="text-4xl font-bold text-gray-900 mb-8">
        Dashboard
      </h1>
      
      {/* Клиентский компонент */}
      <ClientCounter initialValue={data.count} />
    </main>
  )
}
```

## 🔤 next/font — оптимизация шрифтов

Next.js автоматически оптимизирует шрифты — это **лучше**, чем Google Fonts через CDN.

### Google Fonts

```tsx
// app/layout.tsx
import { Inter, Playfair_Display } from 'next/font/google'

// Один шрифт
const inter = Inter({
  subsets: ['latin', 'cyrillic'],
  weight: ['400', '500', '600', '700'],
  display: 'swap',
})

// Несколько шрифтов
const playfair = Playfair_Display({
  subsets: ['latin'],
  weight: ['700'],
  variable: '--font-playfair',
})

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="ru" className={`${inter.className} ${playfair.variable}`}>
      <body>{children}</body>
    </html>
  )
}
```

```tsx
// Использование
<h1 className="font-sans text-4xl">Обычный текст с Inter</h1>
<h2 className="font-[var(--font-playfair)] text-3xl">Заголовок с Playfair</h2>
```

### Локальные шрифты

```tsx
// app/layout.tsx
import localFont from 'next/font/local'

const myFont = localFont({
  src: [
    {
      path: '../public/fonts/MyFont-Regular.woff2',
      weight: '400',
      style: 'normal',
    },
    {
      path: '../public/fonts/MyFont-Bold.woff2',
      weight: '700',
      style: 'normal',
    },
  ],
  display: 'swap',
})

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ru" className={myFont.className}>
      <body>{children}</body>
    </html>
  )
}
```

### Конфигурация Tailwind для next/font

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        sans: ['var(--font-inter)'],
        display: ['var(--font-playfair)'],
        mono: ['var(--font-jetbrains)'],
      },
    },
  },
}
```

```tsx
// app/layout.tsx
const inter = Inter({
  subsets: ['latin'],
  variable: '--font-inter',
})

const playfair = Playfair_Display({
  subsets: ['latin'],
  variable: '--font-playfair',
})

const jetbrains = JetBrains_Mono({
  subsets: ['latin'],
  variable: '--font-jetbrains',
})

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ru" className={`${inter.variable} ${playfair.variable} ${jetbrains.variable}`}>
      <body>{children}</body>
    </html>
  )
}
```

```tsx
// Использование
<h1 className="font-display text-5xl">Заголовок</h1>
<p className="font-sans">Обычный текст</p>
<code className="font-mono">const x = 42;</code>
```

## 🖼️ next/image + Tailwind

`next/image` автоматически оптимизирует изображения — используйте его вместо `<img>`.

### Базовое использование

```tsx
import Image from 'next/image'

export default function ProductCard() {
  return (
    <div className="relative h-64 w-full">
      <Image
        src="/product.jpg"
        alt="Товар"
        fill
        className="object-cover rounded-lg"
        sizes="(max-width: 768px) 100vw, 50vw"
      />
    </div>
  )
}
```

### С фиксированными размерами

```tsx
<Image
  src="/avatar.jpg"
  alt="Аватар"
  width={96}
  height={96}
  className="rounded-full border-2 border-white shadow-md"
/>
```

### С приоритетной загрузкой

```tsx
<Image
  src="/hero.jpg"
  alt="Hero"
  fill
  priority
  className="object-cover"
/>
```

### Практический паттерн: карточка товара

```tsx
import Image from 'next/image'

interface ProductCardProps {
  title: string
  price: number
  image: string
  badge?: string
}

export function ProductCard({ title, price, image, badge }: ProductCardProps) {
  return (
    <div className="group bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-lg transition-shadow">
      <div className="relative aspect-square overflow-hidden">
        <Image
          src={image}
          alt={title}
          fill
          className="object-cover group-hover:scale-110 transition-transform duration-500"
          sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 25vw"
        />
        
        {badge && (
          <span className="absolute top-3 left-3 bg-red-500 text-white text-xs font-bold px-2 py-1 rounded">
            {badge}
          </span>
        )}
      </div>
      
      <div className="p-4">
        <h3 className="font-medium text-gray-900 line-clamp-2">{title}</h3>
        <div className="mt-2 flex items-baseline gap-2">
          <span className="text-xl font-bold text-gray-900">
            {price.toLocaleString('ru-RU')} ₽
          </span>
        </div>
        <button className="mt-3 w-full bg-blue-600 hover:bg-blue-700 text-white py-2 rounded-lg font-medium transition-colors">
          В корзину
        </button>
      </div>
    </div>
  )
}
```

## 🌙 Dark Mode через next-themes

`next-themes` — лучший способ добавить dark mode в Next.js **без мигания**.

### Установка

```bash
npm install next-themes
```

### Провайдер темы

```tsx
// app/providers.tsx
'use client'

import { ThemeProvider } from 'next-themes'
import { ReactNode } from 'react'

export function Providers({ children }: { children: ReactNode }) {
  return (
    <ThemeProvider
      attribute="class"
      defaultTheme="system"
      enableSystem
      disableTransitionOnChange
    >
      {children}
    </ThemeProvider>
  )
}
```

```tsx
// app/layout.tsx
import { Providers } from './providers'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="ru" suppressHydrationWarning>
      <body>
        <Providers>{children}</Providers>
      </body>
    </html>
  )
}
```

> 💡 **Важно:** `suppressHydrationWarning` нужен, чтобы избежать предупреждений о несоответствии HTML между сервером и клиентом.

### Компонент переключателя

```tsx
// components/ThemeToggle.tsx
'use client'

import { useTheme } from 'next-themes'
import { useEffect, useState } from 'react'
import { Sun, Moon, Monitor } from 'lucide-react'
import { cn } from '@/lib/utils'

export function ThemeToggle() {
  const { theme, setTheme } = useTheme()
  const [mounted, setMounted] = useState(false)

  // Избегаем гидратационных несоответствий
  useEffect(() => {
    setMounted(true)
  }, [])

  if (!mounted) {
    return <div className="w-9 h-9" /> // Placeholder
  }

  return (
    <div className="inline-flex items-center gap-1 bg-gray-100 dark:bg-gray-800 p-1 rounded-lg">
      <button
        onClick={() => setTheme('light')}
        className={cn(
          'p-2 rounded-md transition-colors',
          theme === 'light' && 'bg-white dark:bg-gray-700 shadow-sm'
        )}
        aria-label="Светлая тема"
      >
        <Sun className="w-4 h-4" />
      </button>
      <button
        onClick={() => setTheme('dark')}
        className={cn(
          'p-2 rounded-md transition-colors',
          theme === 'dark' && 'bg-white dark:bg-gray-700 shadow-sm'
        )}
        aria-label="Тёмная тема"
      >
        <Moon className="w-4 h-4" />
      </button>
      <button
        onClick={() => setTheme('system')}
        className={cn(
          'p-2 rounded-md transition-colors',
          theme === 'system' && 'bg-white dark:bg-gray-700 shadow-sm'
        )}
        aria-label="Системная тема"
      >
        <Monitor className="w-4 h-4" />
      </button>
    </div>
  )
}
```

### Хук useTheme

```tsx
'use client'

import { useTheme } from 'next-themes'

export function ThemedCard() {
  const { theme, resolvedTheme } = useTheme()
  
  return (
    <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
      <p className="text-gray-900 dark:text-gray-100">
        Текущая тема: {theme}
      </p>
      <p className="text-gray-600 dark:text-gray-400">
        Разрешённая тема: {resolvedTheme}
      </p>
    </div>
  )
}
```

## 📝 Metadata API

### Статические метаданные

```tsx
// app/page.tsx
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Главная страница',
  description: 'Описание главной страницы',
  openGraph: {
    title: 'Главная страница',
    description: 'Описание для соцсетей',
    images: ['/og-image.png'],
  },
}

export default function HomePage() {
  return <h1 className="text-4xl font-bold">Главная</h1>
}
```

### Динамические метаданные

```tsx
// app/blog/[slug]/page.tsx
import type { Metadata, ResolvingMetadata } from 'next'

type Props = {
  params: { slug: string }
}

export async function generateMetadata(
  { params }: Props,
  parent: ResolvingMetadata
): Promise<Metadata> {
  const post = await fetch(`https://api.example.com/posts/${params.slug}`).then(r => r.json())
  
  return {
    title: post.title,
    description: post.excerpt,
    openGraph: {
      images: [post.coverImage],
    },
  }
}

export default async function BlogPost({ params }: Props) {
  const post = await fetch(`https://api.example.com/posts/${params.slug}`).then(r => r.json())
  
  return (
    <article className="max-w-3xl mx-auto px-4 py-8">
      <h1 className="text-4xl font-bold text-gray-900 dark:text-gray-100 mb-4">
        {post.title}
      </h1>
      <div className="prose dark:prose-invert max-w-none">
        <div dangerouslySetInnerHTML={{ __html: post.content }} />
      </div>
    </article>
  )
}
```

## 🎨 Практические паттерны

### 1. 📱 Responsive Sidebar с next/link

```tsx
// components/Sidebar.tsx
'use client'

import Link from 'next/link'
import { usePathname } from 'next/navigation'
import { useState } from 'react'
import { Menu, X, Home, User, Settings } from 'lucide-react'
import { cn } from '@/lib/utils'

const menuItems = [
  { href: '/', label: 'Главная', icon: Home },
  { href: '/profile', label: 'Профиль', icon: User },
  { href: '/settings', label: 'Настройки', icon: Settings },
]

export function Sidebar() {
  const pathname = usePathname()
  const [isOpen, setIsOpen] = useState(false)

  return (
    <>
      {/* Mobile header */}
      <div className="lg:hidden flex items-center justify-between p-4 bg-white dark:bg-gray-900 border-b dark:border-gray-800">
        <span className="font-bold text-xl">Logo</span>
        <button
          onClick={() => setIsOpen(!isOpen)}
          className="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800"
        >
          {isOpen ? <X /> : <Menu />}
        </button>
      </div>

      <div className="flex">
        {/* Sidebar */}
        <aside
          className={cn(
            'fixed inset-y-0 left-0 z-50 w-64 bg-white dark:bg-gray-900 border-r dark:border-gray-800 transform transition-transform lg:translate-x-0 lg:static lg:inset-0',
            isOpen ? 'translate-x-0' : '-translate-x-full'
          )}
        >
          <nav className="p-4 space-y-1">
            {menuItems.map((item) => {
              const Icon = item.icon
              const isActive = pathname === item.href
              
              return (
                <Link
                  key={item.href}
                  href={item.href}
                  onClick={() => setIsOpen(false)}
                  className={cn(
                    'flex items-center gap-3 px-4 py-2 rounded-lg transition-colors',
                    isActive
                      ? 'bg-blue-50 dark:bg-blue-900/30 text-blue-600 dark:text-blue-400'
                      : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800'
                  )}
                >
                  <Icon className="w-5 h-5" />
                  {item.label}
                </Link>
              )
            })}
          </nav>
        </aside>

        {/* Overlay */}
        {isOpen && (
          <div
            className="fixed inset-0 bg-black/50 z-40 lg:hidden"
            onClick={() => setIsOpen(false)}
          />
        )}
      </div>
    </>
  )
}
```

### 2. 🎴 Карточка с next/image и next/link

```tsx
import Image from 'next/image'
import Link from 'next/link'

interface ArticleCardProps {
  slug: string
  title: string
  excerpt: string
  coverImage: string
  author: string
  date: string
}

export function ArticleCard({ slug, title, excerpt, coverImage, author, date }: ArticleCardProps) {
  return (
    <article className="group bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-200 dark:border-gray-700 overflow-hidden hover:shadow-lg transition-shadow">
      <Link href={`/blog/${slug}`} className="block">
        <div className="relative aspect-video overflow-hidden">
          <Image
            src={coverImage}
            alt={title}
            fill
            className="object-cover group-hover:scale-105 transition-transform duration-500"
            sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
          />
        </div>
      </Link>
      
      <div className="p-6">
        <div className="flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400 mb-2">
          <span>{author}</span>
          <span>·</span>
          <time>{date}</time>
        </div>
        
        <Link href={`/blog/${slug}`}>
          <h3 className="text-xl font-bold text-gray-900 dark:text-gray-100 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors">
            {title}
          </h3>
        </Link>
        
        <p className="mt-2 text-gray-600 dark:text-gray-400 line-clamp-2">
          {excerpt}
        </p>
        
        <Link
          href={`/blog/${slug}`}
          className="mt-4 inline-flex items-center text-blue-600 dark:text-blue-400 font-medium hover:underline"
        >
          Читать далее →
        </Link>
      </div>
    </article>
  )
}
```

### 3. 📊 Страница с данными с сервера

```tsx
// app/dashboard/page.tsx
import { Suspense } from 'react'
import Image from 'next/image'

async function getStats() {
  const res = await fetch('https://api.example.com/stats', {
    next: { revalidate: 60 }, // ISR: ревалидация каждые 60 секунд
  })
  return res.json()
}

async function StatsGrid() {
  const stats = await getStats()
  
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
      <div className="bg-gradient-to-br from-blue-500 to-blue-600 rounded-xl p-6 text-white">
        <h3 className="text-sm font-medium opacity-90">Пользователи</h3>
        <p className="text-3xl font-bold mt-2">{stats.users.toLocaleString()}</p>
        <p className="text-sm opacity-75 mt-1">+12% за месяц</p>
      </div>
      
      <div className="bg-gradient-to-br from-green-500 to-green-600 rounded-xl p-6 text-white">
        <h3 className="text-sm font-medium opacity-90">Доход</h3>
        <p className="text-3xl font-bold mt-2">{stats.revenue.toLocaleString()} ₽</p>
        <p className="text-sm opacity-75 mt-1">+8% за месяц</p>
      </div>
      
      <div className="bg-gradient-to-br from-purple-500 to-purple-600 rounded-xl p-6 text-white">
        <h3 className="text-sm font-medium opacity-90">Заказы</h3>
        <p className="text-3xl font-bold mt-2">{stats.orders.toLocaleString()}</p>
        <p className="text-sm opacity-75 mt-1">+15% за месяц</p>
      </div>
      
      <div className="bg-gradient-to-br from-orange-500 to-orange-600 rounded-xl p-6 text-white">
        <h3 className="text-sm font-medium opacity-90">Конверсия</h3>
        <p className="text-3xl font-bold mt-2">{stats.conversion}%</p>
        <p className="text-sm opacity-75 mt-1">+2% за месяц</p>
      </div>
    </div>
  )
}

function StatsSkeleton() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
      {[...Array(4)].map((_, i) => (
        <div key={i} className="bg-gray-200 dark:bg-gray-700 rounded-xl p-6 animate-pulse">
          <div className="h-4 bg-gray-300 dark:bg-gray-600 rounded w-1/2 mb-2" />
          <div className="h-8 bg-gray-300 dark:bg-gray-600 rounded w-3/4 mb-2" />
          <div className="h-3 bg-gray-300 dark:bg-gray-600 rounded w-1/3" />
        </div>
      ))}
    </div>
  )
}

export default function DashboardPage() {
  return (
    <main className="min-h-screen bg-gray-50 dark:bg-gray-900 p-8">
      <h1 className="text-3xl font-bold text-gray-900 dark:text-gray-100 mb-8">
        Дашборд
      </h1>
      
      <Suspense fallback={<StatsSkeleton />}>
        <StatsGrid />
      </Suspense>
    </main>
  )
}
```

### 4. 🎨 Блог с типографикой

```tsx
// app/blog/[slug]/page.tsx
import Image from 'next/image'
import { notFound } from 'next/navigation'

export default async function BlogPost({ params }: { params: { slug: string } }) {
  const post = await getPost(params.slug)
  
  if (!post) notFound()
  
  return (
    <article className="max-w-4xl mx-auto px-4 py-12">
      {/* Header */}
      <header className="mb-8">
        <div className="text-sm text-blue-600 dark:text-blue-400 font-medium uppercase tracking-wider mb-2">
          {post.category}
        </div>
        <h1 className="text-4xl md:text-5xl font-bold text-gray-900 dark:text-gray-100 leading-tight mb-4">
          {post.title}
        </h1>
        <div className="flex items-center gap-4 text-gray-500 dark:text-gray-400">
          <div className="flex items-center gap-2">
            <Image
              src={post.author.avatar}
              alt={post.author.name}
              width={32}
              height={32}
              className="rounded-full"
            />
            <span className="font-medium text-gray-900 dark:text-gray-100">
              {post.author.name}
            </span>
          </div>
          <span>·</span>
          <time>{post.date}</time>
          <span>·</span>
          <span>{post.readingTime} мин чтения</span>
        </div>
      </header>
      
      {/* Cover image */}
      <div className="relative aspect-video rounded-xl overflow-hidden mb-8">
        <Image
          src={post.coverImage}
          alt={post.title}
          fill
          priority
          className="object-cover"
        />
      </div>
      
      {/* Content */}
      <div className="prose prose-lg dark:prose-invert max-w-none prose-headings:font-bold prose-a:text-blue-600 dark:prose-a:text-blue-400">
        <div dangerouslySetInnerHTML={{ __html: post.content }} />
      </div>
    </article>
  )
}
```

### 5. 🔍 Страница поиска с useSearchParams

```tsx
// app/search/page.tsx
'use client'

import { useSearchParams, useRouter } from 'next/navigation'
import { useState, useEffect } from 'react'
import { Search } from 'lucide-react'

export default function SearchPage() {
  const searchParams = useSearchParams()
  const router = useRouter()
  const [query, setQuery] = useState(searchParams.get('q') || '')
  
  useEffect(() => {
    const timer = setTimeout(() => {
      if (query) {
        router.push(`/search?q=${encodeURIComponent(query)}`)
      }
    }, 300)
    
    return () => clearTimeout(timer)
  }, [query, router])
  
  return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      <div className="relative">
        <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Поиск..."
          className="w-full pl-12 pr-4 py-3 border border-gray-300 dark:border-gray-700 rounded-lg bg-white dark:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>
      
      {/* Результаты */}
      <div className="mt-8 space-y-4">
        {/* ... */}
      </div>
    </div>
  )
}
```

### 6. 🎯 Loading states с Suspense

```tsx
// app/loading.tsx
export default function Loading() {
  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 flex items-center justify-center">
      <div className="text-center">
        <div className="w-16 h-16 border-4 border-blue-500 border-t-transparent rounded-full animate-spin mx-auto" />
        <p className="mt-4 text-gray-600 dark:text-gray-400">Загрузка...</p>
      </div>
    </div>
  )
}
```

```tsx
// app/error.tsx
'use client'

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 flex items-center justify-center p-4">
      <div className="max-w-md w-full bg-white dark:bg-gray-800 rounded-xl shadow-lg p-8 text-center">
        <div className="w-16 h-16 bg-red-100 dark:bg-red-900/30 rounded-full flex items-center justify-center mx-auto mb-4">
          <span className="text-3xl">⚠️</span>
        </div>
        <h2 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-2">
          Что-то пошло не так
        </h2>
        <p className="text-gray-600 dark:text-gray-400 mb-6">
          {error.message || 'Произошла ошибка при загрузке страницы'}
        </p>
        <button
          onClick={reset}
          className="px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg font-medium transition-colors"
        >
          Попробовать снова
        </button>
      </div>
    </div>
  )
}
```

### 7. 📝 Форма с Server Actions

```tsx
// app/contact/page.tsx
import { contactFormAction } from './actions'

export default function ContactPage() {
  return (
    <form
      action={contactFormAction}
      className="max-w-md mx-auto bg-white dark:bg-gray-800 rounded-xl shadow-md p-6 space-y-4"
    >
      <h2 className="text-2xl font-bold text-gray-900 dark:text-gray-100">
        Связаться с нами
      </h2>
      
      <div>
        <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
          Имя
        </label>
        <input
          type="text"
          name="name"
          required
          className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>
      
      <div>
        <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
          Email
        </label>
        <input
          type="email"
          name="email"
          required
          className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>
      
      <div>
        <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
          Сообщение
        </label>
        <textarea
          name="message"
          required
          rows={4}
          className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>
      
      <button
        type="submit"
        className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 rounded-lg transition-colors"
      >
        Отправить
      </button>
    </form>
  )
}
```

```tsx
// app/contact/actions.ts
'use server'

export async function contactFormAction(formData: FormData) {
  const name = formData.get('name') as string
  const email = formData.get('email') as string
  const message = formData.get('message') as string
  
  // Валидация
  if (!name || !email || !message) {
    throw new Error('Все поля обязательны')
  }
  
  // Отправка данных
  await fetch('https://api.example.com/contact', {
    method: 'POST',
    body: JSON.stringify({ name, email, message }),
  })
  
  // Редирект после успешной отправки
  // redirect('/contact/success')
}
```

## 📦 Оптимизация для production

### tailwind.config.js

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx}',
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
    './src/**/*.{js,ts,jsx,tsx}',
    // Важно: включаем ВСЕ директории с компонентами
  ],
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        sans: ['var(--font-inter)'],
        display: ['var(--font-playfair)'],
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
  ],
}
```

### next.config.js

```js
/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    formats: ['image/avif', 'image/webp'],
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'images.example.com',
      },
    ],
  },
}

module.exports = nextConfig
```

### Анализ бандла

```bash
# Анализ размера бандла
ANALYZE=true npm run build

# Или через @next/bundle-analyzer
npm install -D @next/bundle-analyzer
```

```js
// next.config.js
const withBundleAnalyzer = require('@next/bundle-analyzer')({
  enabled: process.env.ANALYZE === 'true',
})

module.exports = withBundleAnalyzer({
  // ...
})
```

## 📊 Шпаргалка: что когда использовать

| Задача | Решение |
| :-- | :-- |
| Настройка Tailwind в Next.js | `npx create-next-app` + `tailwindcss init -p` |
| Оптимизация шрифтов | `next/font` + CSS-переменные |
| Оптимизация изображений | `next/image` + Tailwind-классы |
| Dark mode без мигания | `next-themes` + `ThemeProvider` |
| Server Component | По умолчанию в App Router |
| Client Component | `'use client'` в начале файла |
| Metadata | `export const metadata` или `generateMetadata` |
| Навигация | `next/link` вместо `<a>` |
| Редирект | `redirect()` из `next/navigation` |
| Server Actions | `'use server'` + `action={fn}` |
| Loading states | `loading.tsx` + `Suspense` |
| Error handling | `error.tsx` + `global-error.tsx` |
| ISR (ревалидация) | `next: { revalidate: 60 }` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Забывают `'use client'` для интерактивных компонентов

```tsx
// ❌ Плохо: useState без 'use client'
import { useState } from 'react'

export default function Counter() {
  const [count, setCount] = useState(0)
  // Ошибка!
}

// ✅ Хорошо: добавляем 'use client'
'use client'

import { useState } from 'react'

export default function Counter() {
  const [count, setCount] = useState(0)
  // Работает!
}
```

### ❌ Ошибка 2: Используют `<img>` вместо `next/image`

```tsx
// ❌ Плохо: нет оптимизации
<img src="/photo.jpg" className="w-full h-64 object-cover" />

// ✅ Хорошо: автоматическая оптимизация
import Image from 'next/image'

<Image
  src="/photo.jpg"
  alt="Фото"
  width={800}
  height={400}
  className="w-full h-64 object-cover"
/>
```

### ❌ Ошибка 3: Забывают `suppressHydrationWarning` для ThemeProvider

```tsx
// ❌ Плохо: warning о гидратации
<html lang="ru">
  <body>
    <ThemeProvider>{children}</ThemeProvider>
  </body>
</html>

// ✅ Хорошо: подавляем warning
<html lang="ru" suppressHydrationWarning>
  <body>
    <ThemeProvider>{children}</ThemeProvider>
  </body>
</html>
```

### ❌ Ошибка 4: Используют `useSearchParams` без Suspense

```tsx
// ❌ Плохо: ошибка при статической генерации
'use client'

import { useSearchParams } from 'next/navigation'

export default function SearchPage() {
  const searchParams = useSearchParams()
  // Ошибка!
}

// ✅ Хорошо: оборачиваем в Suspense
import { Suspense } from 'react'
import SearchPageClient from './SearchPageClient'

export default function SearchPage() {
  return (
    <Suspense fallback={<div>Загрузка...</div>}>
      <SearchPageClient />
    </Suspense>
  )
}
```

### ❌ Ошибка 5: Забывают про `content` в tailwind.config.js

```js
// ❌ Плохо: Tailwind не найдёт классы
module.exports = {
  content: ['./pages/**/*.{js,tsx}'],
  // Пропущены app/ и components/
}

// ✅ Хорошо: указываем все директории
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx}',
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
  ],
}
```

### ❌ Ошибка 6: Используют `router.push` в Server Components

```tsx
// ❌ Плохо: useRouter работает только в Client Components
export default function Page() {
  const router = useRouter()
  // Ошибка!
}

// ✅ Хорошо: используем redirect из next/navigation
import { redirect } from 'next/navigation'

export default async function Page() {
  const user = await getUser()
  if (!user) redirect('/login')
  // Работает!
}
```

### ❌ Ошибка 7: Забывают про `mounted` в ThemeToggle

```tsx
// ❌ Плохо: несоответствие между сервером и клиентом
export function ThemeToggle() {
  const { theme } = useTheme()
  return <div>{theme}</div>
  // На сервере theme = undefined, на клиенте = 'light'
}

// ✅ Хорошо: ждём монтирования
'use client'

import { useEffect, useState } from 'react'
import { useTheme } from 'next-themes'

export function ThemeToggle() {
  const { theme } = useTheme()
  const [mounted, setMounted] = useState(false)
  
  useEffect(() => setMounted(true), [])
  
  if (!mounted) return <div />
  return <div>{theme}</div>
}
```

### ❌ Ошибка 8: Используют `<a>` вместо `next/link`

```tsx
// ❌ Плохо: полная перезагрузка страницы
<a href="/about" className="text-blue-600">О нас</a>

// ✅ Хорошо: клиентская навигация
import Link from 'next/link'

<Link href="/about" className="text-blue-600 hover:underline">
  О нас
</Link>
```

### ❌ Ошибка 9: Забывают про `fill` в next/image для relative sizing

```tsx
// ❌ Плохо: Image не заполняет контейнер
<div className="relative h-64">
  <Image src="/photo.jpg" alt="Фото" className="object-cover" />
</div>

// ✅ Хорошо: используем fill
<div className="relative h-64">
  <Image src="/photo.jpg" alt="Фото" fill className="object-cover" />
</div>
```

### ❌ Ошибка 10: Не оптимизируют шрифты через next/font

```tsx
// ❌ Плохо: загрузка шрифта через CDN
<link href="https://fonts.googleapis.com/css2?family=Inter" rel="stylesheet" />

// ✅ Хорошо: next/font оптимизирует загрузку
import { Inter } from 'next/font/google'
const inter = Inter({ subsets: ['latin'] })

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ru" className={inter.className}>
      <body>{children}</body>
    </html>
  )
}
```

## 🎯 Что дальше?

Теперь вы полностью владеете интеграцией Next.js + Tailwind CSS! Вы изучили все три основные интеграции:

- ⚛️ **[React](react.md)** — базовая интеграция
- 🔌 **[Vue](vue.md)** — интеграция с Vue.js
- 🚀 **[Next.js](nextjs.md)** — fullstack-фреймворк

### Что изучить дальше

1. **Деплой** — Vercel, Netlify, self-hosted
2. **Middleware** — аутентификация, редиректы, i18n
3. **API Routes** — создание backend на Next.js
4. **Edge Functions** — serverless на edge
5. **Incremental Static Regeneration** — ISR для динамических страниц

---

---




<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: integrations\react.md -->
<!-- ═══════════════════════════════════════════════════════════ -->

# ⚛️ React + Tailwind CSS

> **Полное руководство по интеграции Tailwind CSS с React:** от базовой настройки до продвинутых паттернов с TypeScript, динамическими классами и компонентными библиотеками

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Настроите Tailwind CSS в React-проекте (Vite, CRA, Next.js)
- ✅ Освоите работу с `className` и динамическими классами
- ✅ Научитесь использовать `clsx`, `classnames`, `tailwind-merge`
- ✅ Создадите компонентные библиотеки с `cva` (class-variance-authority)
- ✅ Интегрируете TypeScript с типизацией классов
- ✅ Освоите паттерны для Button, Card, Input и других компонентов
- ✅ Настроите dark mode в React-приложении
- ✅ Избежите типичных ошибок при работе с React + Tailwind

## 🚀 Установка и настройка

### Вариант 1: Vite + React (рекомендуется)

```bash
# Создание проекта
npm create vite@latest my-app -- --template react
cd my-app

# Установка Tailwind
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

```js
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

```css
/* src/index.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

```jsx
// src/main.jsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
```

### Вариант 2: Create React App (legacy)

```bash
npx create-react-app my-app
cd my-app
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

### Вариант 3: Next.js

```bash
npx create-next-app@latest my-app
cd my-app
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

Next.js автоматически настраивает PostCSS, поэтому конфиг проще:

```js
// tailwind.config.js
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
    './app/**/*.{js,ts,jsx,tsx}',
  ],
}
```

## 🎨 Базовое использование в JSX

### `className` вместо `class`

В React используется `className` вместо `class` (так как `class` — зарезервированное слово в JS):

```jsx
// ❌ Неправильно
<div class="bg-blue-500 text-white">...</div>

// ✅ Правильно
<div className="bg-blue-500 text-white">...</div>
```

### Динамические стили через JavaScript

```jsx
function Card({ title, description, variant = 'default' }) {
  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <h3 className="text-xl font-bold text-gray-900">{title}</h3>
      <p className="text-gray-600 mt-2">{description}</p>
    </div>
  )
}
```

## 🔄 Динамические классы

### Условные классы через template literals

```jsx
function Button({ variant = 'primary', size = 'md', children }) {
  return (
    <button
      className={`
        rounded-lg font-medium transition-colors
        ${variant === 'primary' ? 'bg-blue-600 text-white hover:bg-blue-700' : ''}
        ${variant === 'secondary' ? 'bg-gray-200 text-gray-900 hover:bg-gray-300' : ''}
        ${variant === 'danger' ? 'bg-red-600 text-white hover:bg-red-700' : ''}
        ${size === 'sm' ? 'px-3 py-1.5 text-sm' : ''}
        ${size === 'md' ? 'px-4 py-2' : ''}
        ${size === 'lg' ? 'px-6 py-3 text-lg' : ''}
      `}
    >
      {children}
    </button>
  )
}
```

### Условные классы через тернарный оператор

```jsx
function Badge({ status }) {
  return (
    <span
      className={`
        px-2 py-1 rounded-full text-xs font-medium
        ${status === 'active' ? 'bg-green-100 text-green-800' : ''}
        ${status === 'pending' ? 'bg-yellow-100 text-yellow-800' : ''}
        ${status === 'error' ? 'bg-red-100 text-red-800' : ''}
      `}
    >
      {status}
    </span>
  )
}
```

### Условные классы через объект

```jsx
function Button({ isActive, isDisabled, children }) {
  return (
    <button
      className={{
        'bg-blue-600 text-white': isActive,
        'bg-gray-200 text-gray-500': !isActive,
        'opacity-50 cursor-not-allowed': isDisabled,
        'px-4 py-2 rounded-lg': true,
      }}
    >
      {children}
    </button>
  )
}
```

> ⚠️ **Важно:** объект в `className` не работает нативно в React! Нужна библиотека `classnames` или `clsx`.

## 🛠 Библиотеки для работы с классами

### clsx (рекомендуется)

Лёгкая утилита для условных классов:

```bash
npm install clsx
```

```jsx
import clsx from 'clsx'

function Button({ variant = 'primary', size = 'md', isActive, children }) {
  return (
    <button
      className={clsx(
        // Базовые классы
        'rounded-lg font-medium transition-colors',
        
        // Варианты
        {
          'bg-blue-600 text-white hover:bg-blue-700': variant === 'primary',
          'bg-gray-200 text-gray-900 hover:bg-gray-300': variant === 'secondary',
          'bg-red-600 text-white hover:bg-red-700': variant === 'danger',
        },
        
        // Размеры
        {
          'px-3 py-1.5 text-sm': size === 'sm',
          'px-4 py-2': size === 'md',
          'px-6 py-3 text-lg': size === 'lg',
        },
        
        // Состояния
        isActive && 'ring-2 ring-blue-500'
      )}
    >
      {children}
    </button>
  )
}
```

### classnames

Альтернатива `clsx` с тем же API:

```bash
npm install classnames
```

```jsx
import classNames from 'classnames'

const buttonClass = classNames(
  'px-4 py-2 rounded-lg',
  {
    'bg-blue-600': isPrimary,
    'bg-red-600': isDanger,
  }
)
```

### tailwind-merge

Решает проблему **конфликта классов** при их объединении:

```bash
npm install tailwind-merge
```

```jsx
import { twMerge } from 'tailwind-merge'

// ❌ Без twMerge: p-4 перезаписывается p-8, но оба остаются в строке
const className = twMerge('p-4 bg-blue-500', 'p-8')
// Результат: "bg-blue-500 p-8" (p-4 удалён!)

// ✅ С twMerge: корректное разрешение конфликтов
const className = twMerge('px-4 py-2', 'px-8')
// Результат: "py-2 px-8" (px-4 заменён на px-8)
```

### clsx + tailwind-merge (идеальная комбинация)

```bash
npm install clsx tailwind-merge
```

```jsx
// lib/utils.js
import { clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'

export function cn(...inputs) {
  return twMerge(clsx(inputs))
}
```

```jsx
// Использование
import { cn } from '@/lib/utils'

function Button({ className, variant = 'primary', children }) {
  return (
    <button
      className={cn(
        'px-4 py-2 rounded-lg font-medium',
        {
          'bg-blue-600 text-white hover:bg-blue-700': variant === 'primary',
          'bg-red-600 text-white hover:bg-red-700': variant === 'danger',
        },
        className // пользовательские классы корректно перезапишут базовые
      )}
    >
      {children}
    </button>
  )
}
```

> 💡 **Паттерн `cn()`** — это стандарт в современных React-проектах (используется в shadcn/ui).

## 🧩 class-variance-authority (cva)

Мощная библиотека для создания **вариативных компонентов**:

```bash
npm install class-variance-authority
```

```jsx
// components/button.tsx
import { cva } from 'class-variance-authority'
import { cn } from '@/lib/utils'

const buttonVariants = cva(
  // Базовые классы
  'inline-flex items-center justify-center rounded-lg font-medium transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2',
  {
    variants: {
      variant: {
        primary: 'bg-blue-600 text-white hover:bg-blue-700 focus:ring-blue-500',
        secondary: 'bg-gray-200 text-gray-900 hover:bg-gray-300 focus:ring-gray-500',
        danger: 'bg-red-600 text-white hover:bg-red-700 focus:ring-red-500',
        outline: 'border border-gray-300 bg-transparent hover:bg-gray-50',
        ghost: 'bg-transparent hover:bg-gray-100',
      },
      size: {
        sm: 'px-3 py-1.5 text-sm',
        md: 'px-4 py-2',
        lg: 'px-6 py-3 text-lg',
        icon: 'p-2',
      },
    },
    defaultVariants: {
      variant: 'primary',
      size: 'md',
    },
  }
)

function Button({ variant, size, className, children, ...props }) {
  return (
    <button
      className={cn(buttonVariants({ variant, size }), className)}
      {...props}
    >
      {children}
    </button>
  )
}

export { Button, buttonVariants }
```

```jsx
// Использование
<Button variant="primary" size="md">Сохранить</Button>
<Button variant="danger" size="lg">Удалить</Button>
<Button variant="outline" size="sm">Отмена</Button>
<Button variant="ghost" size="icon">
  <Icon />
</Button>
```

## 📘 TypeScript + Tailwind

### Типизация пропсов компонентов

```tsx
import { cva, type VariantProps } from 'class-variance-authority'
import { cn } from '@/lib/utils'

const buttonVariants = cva(
  'inline-flex items-center justify-center rounded-lg font-medium',
  {
    variants: {
      variant: {
        primary: 'bg-blue-600 text-white hover:bg-blue-700',
        secondary: 'bg-gray-200 text-gray-900 hover:bg-gray-300',
      },
      size: {
        sm: 'px-3 py-1.5 text-sm',
        md: 'px-4 py-2',
        lg: 'px-6 py-3 text-lg',
      },
    },
    defaultVariants: {
      variant: 'primary',
      size: 'md',
    },
  }
)

// Извлекаем типы вариантов
type ButtonVariants = VariantProps<typeof buttonVariants>

interface ButtonProps extends ButtonVariants, React.ButtonHTMLAttributes<HTMLButtonElement> {
  className?: string
}

function Button({ variant, size, className, children, ...props }: ButtonProps) {
  return (
    <button
      className={cn(buttonVariants({ variant, size }), className)}
      {...props}
    >
      {children}
    </button>
  )
}

export { Button }
```

### Типизация className

```tsx
import type { ClassNameValue } from 'clsx'

interface CardProps {
  className?: ClassNameValue
  title: string
  children: React.ReactNode
}

function Card({ className, title, children }: CardProps) {
  return (
    <div className={cn('bg-white rounded-lg shadow-md p-6', className)}>
      <h3 className="text-xl font-bold">{title}</h3>
      {children}
    </div>
  )
}
```

## 🎨 Практические паттерны компонентов

### 1. 🔘 Button (полноценный)

```tsx
import { cva, type VariantProps } from 'class-variance-authority'
import { cn } from '@/lib/utils'
import { Loader2 } from 'lucide-react'

const buttonVariants = cva(
  'inline-flex items-center justify-center rounded-lg font-medium transition-all focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:pointer-events-none disabled:opacity-50',
  {
    variants: {
      variant: {
        primary: 'bg-blue-600 text-white hover:bg-blue-700 focus:ring-blue-500',
        secondary: 'bg-gray-100 text-gray-900 hover:bg-gray-200 focus:ring-gray-500',
        danger: 'bg-red-600 text-white hover:bg-red-700 focus:ring-red-500',
        outline: 'border border-gray-300 bg-transparent hover:bg-gray-50',
        ghost: 'hover:bg-gray-100',
        link: 'text-blue-600 underline-offset-4 hover:underline',
      },
      size: {
        sm: 'h-8 px-3 text-sm',
        md: 'h-10 px-4',
        lg: 'h-12 px-6 text-lg',
        icon: 'h-10 w-10',
      },
    },
    defaultVariants: {
      variant: 'primary',
      size: 'md',
    },
  }
)

interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  isLoading?: boolean
}

function Button({
  variant,
  size,
  className,
  isLoading,
  children,
  disabled,
  ...props
}: ButtonProps) {
  return (
    <button
      className={cn(buttonVariants({ variant, size }), className)}
      disabled={disabled || isLoading}
      {...props}
    >
      {isLoading && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
      {children}
    </button>
  )
}

export { Button, buttonVariants }
```

### 2. 🎴 Card

```tsx
import { cn } from '@/lib/utils'

interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  hover?: boolean
}

function Card({ className, hover, children, ...props }: CardProps) {
  return (
    <div
      className={cn(
        'bg-white rounded-xl shadow-sm border border-gray-200',
        hover && 'transition-shadow hover:shadow-md',
        className
      )}
      {...props}
    >
      {children}
    </div>
  )
}

function CardHeader({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) {
  return (
    <div
      className={cn('flex flex-col space-y-1.5 p-6 border-b', className)}
      {...props}
    />
  )
}

function CardTitle({ className, ...props }: React.HTMLAttributes<HTMLHeadingElement>) {
  return (
    <h3
      className={cn('text-xl font-semibold leading-none tracking-tight', className)}
      {...props}
    />
  )
}

function CardDescription({ className, ...props }: React.HTMLAttributes<HTMLParagraphElement>) {
  return (
    <p
      className={cn('text-sm text-gray-500', className)}
      {...props}
    />
  )
}

function CardContent({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) {
  return <div className={cn('p-6', className)} {...props} />
}

function CardFooter({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) {
  return (
    <div
      className={cn('flex items-center p-6 pt-0', className)}
      {...props}
    />
  )
}

export { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter }
```

```jsx
// Использование
<Card hover>
  <CardHeader>
    <CardTitle>Заголовок</CardTitle>
    <CardDescription>Описание карточки</CardDescription>
  </CardHeader>
  <CardContent>
    <p>Содержимое карточки</p>
  </CardContent>
  <CardFooter>
    <Button>Действие</Button>
  </CardFooter>
</Card>
```

### 3. 📝 Input с floating label

```tsx
import { cn } from '@/lib/utils'
import { forwardRef } from 'react'

interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string
  error?: string
  hint?: string
}

const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ className, label, error, hint, id, ...props }, ref) => {
    const inputId = id || `input-${Math.random().toString(36).slice(2)}`

    return (
      <div className="w-full">
        {label && (
          <label
            htmlFor={inputId}
            className="block text-sm font-medium text-gray-700 mb-1"
          >
            {label}
          </label>
        )}
        <input
          id={inputId}
          ref={ref}
          className={cn(
            'flex h-10 w-full rounded-lg border bg-white px-3 py-2 text-sm',
            'placeholder:text-gray-400',
            'focus:outline-none focus:ring-2 focus:ring-offset-1',
            'disabled:cursor-not-allowed disabled:opacity-50',
            error
              ? 'border-red-500 focus:border-red-500 focus:ring-red-500'
              : 'border-gray-300 focus:border-blue-500 focus:ring-blue-500',
            className
          )}
          {...props}
        />
        {error && (
          <p className="mt-1 text-sm text-red-500">{error}</p>
        )}
        {hint && !error && (
          <p className="mt-1 text-sm text-gray-500">{hint}</p>
        )}
      </div>
    )
  }
)

Input.displayName = 'Input'

export { Input }
```

```jsx
// Использование
<Input
  label="Email"
  type="email"
  placeholder="you@example.com"
  error="Неверный email"
  hint="Введите рабочий email"
/>
```

### 4. 🏷️ Badge

```tsx
import { cva, type VariantProps } from 'class-variance-authority'
import { cn } from '@/lib/utils'

const badgeVariants = cva(
  'inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-semibold transition-colors',
  {
    variants: {
      variant: {
        default: 'bg-blue-100 text-blue-800',
        secondary: 'bg-gray-100 text-gray-800',
        success: 'bg-green-100 text-green-800',
        warning: 'bg-yellow-100 text-yellow-800',
        danger: 'bg-red-100 text-red-800',
        outline: 'border border-gray-300 text-gray-700',
      },
    },
    defaultVariants: {
      variant: 'default',
    },
  }
)

interface BadgeProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof badgeVariants> {}

function Badge({ className, variant, ...props }: BadgeProps) {
  return (
    <div
      className={cn(badgeVariants({ variant }), className)}
      {...props}
    />
  )
}

export { Badge, badgeVariants }
```

### 5. 🎚️ Toggle / Switch

```tsx
import { cn } from '@/lib/utils'

interface ToggleProps {
  checked: boolean
  onChange: (checked: boolean) => void
  label?: string
  disabled?: boolean
}

function Toggle({ checked, onChange, label, disabled }: ToggleProps) {
  return (
    <label className={cn(
      'inline-flex items-center cursor-pointer',
      disabled && 'opacity-50 cursor-not-allowed'
    )}>
      <input
        type="checkbox"
        className="sr-only peer"
        checked={checked}
        onChange={(e) => onChange(e.target.checked)}
        disabled={disabled}
      />
      <div className={cn(
        'relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300',
        'rounded-full peer',
        'peer-checked:after:translate-x-full peer-checked:after:border-white',
        'after:content-[""] after:absolute after:top-[2px] after:left-[2px]',
        'after:bg-white after:border-gray-300 after:border after:rounded-full',
        'after:h-5 after:w-5 after:transition-all',
        'dark:bg-gray-700 dark:peer-focus:ring-blue-800',
        checked && 'bg-blue-600'
      )} />
      {label && (
        <span className="ml-3 text-sm font-medium text-gray-900 dark:text-gray-300">
          {label}
        </span>
      )}
    </label>
  )
}
```

### 6. 📋 Select

```tsx
import { cn } from '@/lib/utils'
import { forwardRef } from 'react'

interface SelectProps extends React.SelectHTMLAttributes<HTMLSelectElement> {
  label?: string
  error?: string
  options: Array<{ value: string; label: string }>
}

const Select = forwardRef<HTMLSelectElement, SelectProps>(
  ({ className, label, error, options, id, ...props }, ref) => {
    const selectId = id || `select-${Math.random().toString(36).slice(2)}`

    return (
      <div className="w-full">
        {label && (
          <label htmlFor={selectId} className="block text-sm font-medium text-gray-700 mb-1">
            {label}
          </label>
        )}
        <select
          id={selectId}
          ref={ref}
          className={cn(
            'flex h-10 w-full rounded-lg border bg-white px-3 py-2 text-sm',
            'focus:outline-none focus:ring-2 focus:ring-offset-1',
            'disabled:cursor-not-allowed disabled:opacity-50',
            error
              ? 'border-red-500 focus:border-red-500 focus:ring-red-500'
              : 'border-gray-300 focus:border-blue-500 focus:ring-blue-500',
            className
          )}
          {...props}
        >
          {options.map((option) => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
        </select>
        {error && <p className="mt-1 text-sm text-red-500">{error}</p>}
      </div>
    )
  }
)

Select.displayName = 'Select'

export { Select }
```

## 🌙 Dark Mode в React

### Через контекст (рекомендуется)

```tsx
// contexts/theme.tsx
import { createContext, useContext, useEffect, useState } from 'react'

type Theme = 'dark' | 'light' | 'system'

interface ThemeContextType {
  theme: Theme
  setTheme: (theme: Theme) => void
}

const ThemeContext = createContext<ThemeContextType | undefined>(undefined)

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useState<Theme>(() => {
    if (typeof window === 'undefined') return 'light'
    return (localStorage.getItem('theme') as Theme) || 'system'
  })

  useEffect(() => {
    const root = window.document.documentElement
    root.classList.remove('light', 'dark')

    if (theme === 'system') {
      const systemTheme = window.matchMedia('(prefers-color-scheme: dark)').matches
        ? 'dark'
        : 'light'
      root.classList.add(systemTheme)
    } else {
      root.classList.add(theme)
    }

    localStorage.setItem('theme', theme)
  }, [theme])

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  )
}

export function useTheme() {
  const context = useContext(ThemeContext)
  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider')
  }
  return context
}
```

```tsx
// App.tsx
import { ThemeProvider } from './contexts/theme'

function App() {
  return (
    <ThemeProvider>
      <YourApp />
    </ThemeProvider>
  )
}
```

```tsx
// components/ThemeToggle.tsx
import { useTheme } from '@/contexts/theme'
import { Moon, Sun, Monitor } from 'lucide-react'
import { cn } from '@/lib/utils'

export function ThemeToggle() {
  const { theme, setTheme } = useTheme()

  return (
    <div className="inline-flex items-center gap-1 bg-gray-100 dark:bg-gray-800 p-1 rounded-lg">
      <button
        onClick={() => setTheme('light')}
        className={cn(
          'p-2 rounded-md transition-colors',
          theme === 'light' && 'bg-white dark:bg-gray-700 shadow-sm'
        )}
        aria-label="Светлая тема"
      >
        <Sun className="h-4 w-4" />
      </button>
      <button
        onClick={() => setTheme('dark')}
        className={cn(
          'p-2 rounded-md transition-colors',
          theme === 'dark' && 'bg-white dark:bg-gray-700 shadow-sm'
        )}
        aria-label="Тёмная тема"
      >
        <Moon className="h-4 w-4" />
      </button>
      <button
        onClick={() => setTheme('system')}
        className={cn(
          'p-2 rounded-md transition-colors',
          theme === 'system' && 'bg-white dark:bg-gray-700 shadow-sm'
        )}
        aria-label="Системная тема"
      >
        <Monitor className="h-4 w-4" />
      </button>
    </div>
  )
}
```

### Инициализация до рендера (без мигания)

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="ru">
  <head>
    <script>
      // Применяем тему ДО рендеринга React
      ;(function() {
        const theme = localStorage.getItem('theme') || 'system'
        const root = document.documentElement
        
        if (theme === 'system') {
          const systemTheme = window.matchMedia('(prefers-color-scheme: dark)').matches
            ? 'dark'
            : 'light'
          root.classList.add(systemTheme)
        } else {
          root.classList.add(theme)
        }
      })()
    </script>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

## 📦 Интеграция с популярными библиотеками

### React Hook Form + Tailwind

```tsx
import { useForm } from 'react-hook-form'
import { cn } from '@/lib/utils'

interface FormData {
  email: string
  password: string
}

function LoginForm() {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<FormData>()

  const onSubmit = async (data: FormData) => {
    // Отправка данных
    await new Promise((resolve) => setTimeout(resolve, 1000))
    console.log(data)
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4 max-w-md mx-auto p-6">
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">
          Email
        </label>
        <input
          type="email"
          {...register('email', {
            required: 'Email обязателен',
            pattern: {
              value: /^\S+@\S+$/i,
              message: 'Неверный формат email',
            },
          })}
          className={cn(
            'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2',
            errors.email
              ? 'border-red-500 focus:ring-red-500'
              : 'border-gray-300 focus:ring-blue-500'
          )}
        />
        {errors.email && (
          <p className="mt-1 text-sm text-red-500">{errors.email.message}</p>
        )}
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">
          Пароль
        </label>
        <input
          type="password"
          {...register('password', {
            required: 'Пароль обязателен',
            minLength: {
              value: 8,
              message: 'Минимум 8 символов',
            },
          })}
          className={cn(
            'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2',
            errors.password
              ? 'border-red-500 focus:ring-red-500'
              : 'border-gray-300 focus:ring-blue-500'
          )}
        />
        {errors.password && (
          <p className="mt-1 text-sm text-red-500">{errors.password.message}</p>
        )}
      </div>

      <button
        type="submit"
        disabled={isSubmitting}
        className="w-full bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 disabled:opacity-50 transition-colors"
      >
        {isSubmitting ? 'Вход...' : 'Войти'}
      </button>
    </form>
  )
}
```

### React Router + Tailwind

```tsx
import { Link, NavLink } from 'react-router-dom'
import { cn } from '@/lib/utils'

function Navigation() {
  return (
    <nav className="bg-white border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex">
            <Link to="/" className="flex items-center font-bold text-xl text-gray-900">
              Logo
            </Link>
            <div className="hidden sm:ml-6 sm:flex sm:space-x-8">
              <NavLink
                to="/"
                className={({ isActive }) =>
                  cn(
                    'inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium',
                    isActive
                      ? 'border-blue-500 text-gray-900'
                      : 'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700'
                  )
                }
              >
                Главная
              </NavLink>
              <NavLink
                to="/about"
                className={({ isActive }) =>
                  cn(
                    'inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium',
                    isActive
                      ? 'border-blue-500 text-gray-900'
                      : 'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700'
                  )
                }
              >
                О нас
              </NavLink>
            </div>
          </div>
        </div>
      </div>
    </nav>
  )
}
```

## 🎯 Практические паттерны

### 1. 📱 Responsive Sidebar

```tsx
import { useState } from 'react'
import { cn } from '@/lib/utils'
import { Menu, X } from 'lucide-react'

function Dashboard() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false)

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Mobile header */}
      <div className="lg:hidden flex items-center justify-between p-4 bg-white border-b">
        <span className="font-bold text-xl">Logo</span>
        <button
          onClick={() => setIsSidebarOpen(!isSidebarOpen)}
          className="p-2 rounded-lg hover:bg-gray-100"
        >
          {isSidebarOpen ? <X /> : <Menu />}
        </button>
      </div>

      <div className="flex">
        {/* Sidebar */}
        <aside
          className={cn(
            'fixed inset-y-0 left-0 z-50 w-64 bg-white border-r transform transition-transform lg:translate-x-0 lg:static lg:inset-0',
            isSidebarOpen ? 'translate-x-0' : '-translate-x-full'
          )}
        >
          <div className="p-4">
            <h2 className="font-bold text-xl mb-4 hidden lg:block">Logo</h2>
            <nav className="space-y-1">
              {['Главная', 'Профиль', 'Настройки', 'Выход'].map((item) => (
                <a
                  key={item}
                  href="#"
                  className="block px-4 py-2 rounded-lg text-gray-700 hover:bg-gray-100"
                >
                  {item}
                </a>
              ))}
            </nav>
          </div>
        </aside>

        {/* Overlay */}
        {isSidebarOpen && (
          <div
            className="fixed inset-0 bg-black/50 z-40 lg:hidden"
            onClick={() => setIsSidebarOpen(false)}
          />
        )}

        {/* Main content */}
        <main className="flex-1 p-4 lg:p-8">
          <h1 className="text-2xl font-bold mb-6">Дашборд</h1>
          {/* Контент */}
        </main>
      </div>
    </div>
  )
}
```

### 2. 🎴 Карточка товара с hover-эффектами

```tsx
import { cn } from '@/lib/utils'
import { ShoppingCart, Heart } from 'lucide-react'
import { useState } from 'react'

interface ProductCardProps {
  title: string
  price: number
  oldPrice?: number
  image: string
  badge?: string
}

function ProductCard({ title, price, oldPrice, image, badge }: ProductCardProps) {
  const [isFavorite, setIsFavorite] = useState(false)

  return (
    <div className="group bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-lg transition-shadow">
      {/* Изображение */}
      <div className="relative aspect-square overflow-hidden">
        <img
          src={image}
          alt={title}
          className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
        />
        
        {/* Бейдж */}
        {badge && (
          <span className="absolute top-3 left-3 bg-red-500 text-white text-xs font-bold px-2 py-1 rounded">
            {badge}
          </span>
        )}

        {/* Кнопка избранного */}
        <button
          onClick={() => setIsFavorite(!isFavorite)}
          className={cn(
            'absolute top-3 right-3 p-2 rounded-full transition-all',
            isFavorite
              ? 'bg-red-500 text-white'
              : 'bg-white/80 text-gray-700 hover:bg-white'
          )}
        >
          <Heart className={cn('w-5 h-5', isFavorite && 'fill-current')} />
        </button>

        {/* Overlay с кнопкой */}
        <div className="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-colors flex items-center justify-center opacity-0 group-hover:opacity-100">
          <button className="bg-white text-gray-900 px-4 py-2 rounded-lg font-medium hover:bg-gray-100 transition">
            Быстрый просмотр
          </button>
        </div>
      </div>

      {/* Контент */}
      <div className="p-4">
        <h3 className="font-medium text-gray-900 line-clamp-2">{title}</h3>
        <div className="mt-2 flex items-baseline gap-2">
          <span className="text-xl font-bold text-gray-900">
            {price.toLocaleString('ru-RU')} ₽
          </span>
          {oldPrice && (
            <span className="text-sm text-gray-400 line-through">
              {oldPrice.toLocaleString('ru-RU')} ₽
            </span>
          )}
        </div>
        <button className="mt-3 w-full bg-blue-600 hover:bg-blue-700 text-white py-2 rounded-lg font-medium transition-colors flex items-center justify-center gap-2">
          <ShoppingCart className="w-4 h-4" />
          В корзину
        </button>
      </div>
    </div>
  )
}
```

### 3. 📊 Таблица с сортировкой

```tsx
import { useState } from 'react'
import { cn } from '@/lib/utils'
import { ArrowUpDown } from 'lucide-react'

interface User {
  id: number
  name: string
  email: string
  role: string
  status: 'active' | 'pending' | 'inactive'
}

function UsersTable({ users }: { users: User[] }) {
  const [sortField, setSortField] = useState<keyof User>('name')
  const [sortDirection, setSortDirection] = useState<'asc' | 'desc'>('asc')

  const handleSort = (field: keyof User) => {
    if (sortField === field) {
      setSortDirection(sortDirection === 'asc' ? 'desc' : 'asc')
    } else {
      setSortField(field)
      setSortDirection('asc')
    }
  }

  const sortedUsers = [...users].sort((a, b) => {
    const aValue = a[sortField]
    const bValue = b[sortField]
    if (aValue < bValue) return sortDirection === 'asc' ? -1 : 1
    if (aValue > bValue) return sortDirection === 'asc' ? 1 : -1
    return 0
  })

  return (
    <div className="bg-white rounded-xl shadow-sm border overflow-hidden">
      <div className="overflow-x-auto">
        <table className="w-full">
          <thead className="bg-gray-50 border-b">
            <tr>
              {(['name', 'email', 'role', 'status'] as const).map((field) => (
                <th
                  key={field}
                  onClick={() => handleSort(field)}
                  className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100"
                >
                  <div className="flex items-center gap-1">
                    {field}
                    <ArrowUpDown className={cn(
                      'w-3 h-3',
                      sortField === field ? 'text-blue-600' : 'text-gray-400'
                    )} />
                  </div>
                </th>
              ))}
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-200">
            {sortedUsers.map((user) => (
              <tr key={user.id} className="hover:bg-gray-50 transition-colors">
                <td className="px-6 py-4 font-medium text-gray-900">{user.name}</td>
                <td className="px-6 py-4 text-gray-600">{user.email}</td>
                <td className="px-6 py-4 text-gray-600">{user.role}</td>
                <td className="px-6 py-4">
                  <span
                    className={cn(
                      'px-2 py-1 rounded-full text-xs font-medium',
                      {
                        'bg-green-100 text-green-800': user.status === 'active',
                        'bg-yellow-100 text-yellow-800': user.status === 'pending',
                        'bg-gray-100 text-gray-800': user.status === 'inactive',
                      }
                    )}
                  >
                    {user.status}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}
```

## 📊 Шпаргалка: что когда использовать

| Задача | Решение |
| :-- | :-- |
| Условные классы | `clsx` или `classnames` |
| Разрешение конфликтов классов | `tailwind-merge` |
| Идеальная комбинация | `cn()` = `twMerge(clsx(...))` |
| Вариативные компоненты | `cva` (class-variance-authority) |
| TypeScript + варианты | `VariantProps<typeof cva>` |
| Динамические классы | `cn()` с объектом или массивом |
| Dark mode | Контекст + `localStorage` + `useEffect` |
| Без мигания темы | Скрипт в `<head>` до рендера |
| Переиспользование паттернов | Компоненты Button, Card, Input |
| Формы | React Hook Form + `cn()` для ошибок |
| Навигация | React Router `NavLink` + `cn()` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: `class` вместо `className`

```jsx
// ❌ Плохо: class не работает в React
<div class="bg-blue-500">...</div>

// ✅ Хорошо: используем className
<div className="bg-blue-500">...</div>
```

### ❌ Ошибка 2: Динамическая конкатенация классов

```jsx
// ❌ Плохо: Tailwind не увидит эти классы
const variant = 'primary'
<button className={`btn-${variant}`}>Кнопка</button>

// ✅ Хорошо: полные имена классов
const variants = {
  primary: 'bg-blue-600 text-white',
  secondary: 'bg-gray-200 text-gray-900',
}
<button className={variants[variant]}>Кнопка</button>
```

### ❌ Ошибка 3: Конфликт классов без `tailwind-merge`

```jsx
// ❌ Плохо: p-4 и p-8 оба остаются, последний выигрывает непредсказуемо
<div className={`p-4 bg-blue-500 ${customClass}`}>
  {/* customClass = "p-8" — результат непредсказуем */}
</div>

// ✅ Хорошо: twMerge корректно разрешает конфликты
<div className={twMerge('p-4 bg-blue-500', customClass)}>
  {/* customClass = "p-8" — результат: "bg-blue-500 p-8" */}
</div>
```

### ❌ Ошибка 4: Мигание темы при загрузке

```jsx
// ❌ Плохо: тема применяется после рендера React
function App() {
  useEffect(() => {
    document.documentElement.classList.add('dark')
  }, [])
}

// ✅ Хорошо: тема применяется до рендера
// В index.html:
<script>
  ;(function() {
    const theme = localStorage.getItem('theme')
    if (theme === 'dark') document.documentElement.classList.add('dark')
  })()
</script>
```

### ❌ Ошибка 5: Забывают про `forwardRef` в компонентах

```tsx
// ❌ Плохо: ref не работает
function Input({ className, ...props }) {
  return <input className={className} {...props} />
}

// ✅ Хорошо: используем forwardRef
const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ className, ...props }, ref) => {
    return <input ref={ref} className={className} {...props} />
  }
)
Input.displayName = 'Input'
```

### ❌ Ошибка 6: Избыточные `div`-обёртки

```jsx
// ❌ Плохо: лишний div
<div>
  <div className="bg-white p-4 rounded-lg">
    <p>Контент</p>
  </div>
</div>

// ✅ Хорошо: применяем классы к существующему элементу
<div className="bg-white p-4 rounded-lg">
  <p>Контент</p>
</div>
```

### ❌ Ошибка 7: Забывают про `displayName` для `forwardRef`

```tsx
// ❌ Плохо: в DevTools будет "ForwardRef"
const Input = forwardRef<HTMLInputElement, InputProps>((props, ref) => {
  return <input ref={ref} {...props} />
})

// ✅ Хорошо: добавляем displayName
const Input = forwardRef<HTMLInputElement, InputProps>((props, ref) => {
  return <input ref={ref} {...props} />
})
Input.displayName = 'Input'
```

### ❌ Ошибка 8: Не типизируют варианты cva

```tsx
// ❌ Плохо: нет типов для variant и size
function Button({ variant, size, children }) {
  // ...
}

// ✅ Хорошо: типизируем через VariantProps
const buttonVariants = cva('...', { variants: { ... } })
type ButtonProps = VariantProps<typeof buttonVariants>
function Button({ variant, size, children }: ButtonProps) {
  // ...
}
```

### ❌ Ошибка 9: Забывают про `content` в `tailwind.config.js`

```js
// ❌ Плохо: Tailwind не найдёт классы в компонентах
module.exports = {
  // content отсутствует
}

// ✅ Хорошо: указываем все пути
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
}
```

### ❌ Ошибка 10: Дублирование классов вместо компонентов

```jsx
// ❌ Плохо: дублирование
<button className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
  Сохранить
</button>
<button className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
  Отмена
</button>

// ✅ Хорошо: переиспользуем компонент
<Button variant="primary">Сохранить</Button>
<Button variant="primary">Отмена</Button>
```

## 🎯 Что дальше?

Теперь вы полностью владеете интеграцией React + Tailwind CSS! Но это только одна из популярных связок.

**Следующий шаг:** [🔌 Vue + Tailwind CSS](vue.md) — изучим интеграцию с Vue.js, Composition API и SFC.

---

---




<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: integrations\vue.md -->
<!-- ═══════════════════════════════════════════════════════════ -->

# 🔌 Vue + Tailwind CSS

> **Полное руководство по интеграции Tailwind CSS с Vue 3:** от базовой настройки до Composition API, composables и компонентных библиотек

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Настроите Tailwind CSS в Vue 3 проекте (Vite, Nuxt 3)
- ✅ Освоите `:class` binding — объекты, массивы, computed
- ✅ Научитесь создавать переиспользуемые компоненты
- ✅ Освоите composables для логики стилей
- ✅ Интегрируете TypeScript с `defineProps`
- ✅ Поймёте паттерны для Button, Card, Input и других компонентов
- ✅ Настроите dark mode через composable
- ✅ Избежите типичных ошибок при работе с Vue + Tailwind

## 🚀 Установка и настройка

### Вариант 1: Vite + Vue 3 (рекомендуется)

```bash
# Создание проекта
npm create vite@latest my-app -- --template vue-ts
cd my-app

# Установка Tailwind
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

```js
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

```css
/* src/style.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

```ts
// src/main.ts
import { createApp } from 'vue'
import App from './App.vue'
import './style.css'

createApp(App).mount('#app')
```

### Вариант 2: Nuxt 3

```bash
npx nuxi@latest init my-app
cd my-app
npm install -D @nuxtjs/tailwindcss
```

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  modules: ['@nuxtjs/tailwindcss'],
  tailwindcss: {
    configPath: 'tailwind.config.js',
  },
})
```

```js
// tailwind.config.js
module.exports = {
  content: [
    './components/**/*.{vue,js,ts}',
    './layouts/**/*.vue',
    './pages/**/*.vue',
    './plugins/**/*.{js,ts}',
    './app.vue',
  ],
}
```

## 🎨 Базовое использование `:class`

В Vue используется **`:class` binding** (сокращение от `v-bind:class`) для динамических классов:

### Статические классы

```vue
<template>
  <div class="bg-white rounded-lg shadow-md p-6">
    <h3 class="text-xl font-bold text-gray-900">Заголовок</h3>
    <p class="text-gray-600 mt-2">Описание</p>
  </div>
</template>
```

### Динамические классы через объект

```vue
<template>
  <button
    :class="{
      'bg-blue-600 text-white': isPrimary,
      'bg-gray-200 text-gray-900': !isPrimary,
      'opacity-50 cursor-not-allowed': disabled,
      'px-4 py-2 rounded-lg': true,
    }"
    :disabled="disabled"
  >
    <slot />
  </button>
</template>

<script setup lang="ts">
defineProps<{
  isPrimary?: boolean
  disabled?: boolean
}>()
</script>
```

### Динамические классы через массив

```vue
<template>
  <div :class="[baseClass, sizeClass, variantClass]">
    <slot />
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  size?: 'sm' | 'md' | 'lg'
  variant?: 'primary' | 'secondary' | 'danger'
}>(), {
  size: 'md',
  variant: 'primary',
})

const baseClass = 'px-4 py-2 rounded-lg font-medium transition-colors'

const sizeClass = computed(() => ({
  sm: 'text-sm px-3 py-1.5',
  md: 'text-base px-4 py-2',
  lg: 'text-lg px-6 py-3',
}[props.size]))

const variantClass = computed(() => ({
  primary: 'bg-blue-600 text-white hover:bg-blue-700',
  secondary: 'bg-gray-200 text-gray-900 hover:bg-gray-300',
  danger: 'bg-red-600 text-white hover:bg-red-700',
}[props.variant]))
</script>
```

### Тернарный оператор

```vue
<template>
  <div
    :class="isActive
      ? 'bg-blue-600 text-white'
      : 'bg-gray-100 text-gray-900'"
  >
    Контент
  </div>
</template>
```

## 🛠 Библиотеки для работы с классами

### clsx + tailwind-merge (рекомендуется)

```bash
npm install clsx tailwind-merge
```

```ts
// lib/utils.ts
import { type ClassValue, clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
```

```vue
<template>
  <button :class="cn(
    'px-4 py-2 rounded-lg font-medium',
    variant === 'primary' && 'bg-blue-600 text-white hover:bg-blue-700',
    variant === 'secondary' && 'bg-gray-200 text-gray-900 hover:bg-gray-300',
    size === 'lg' && 'px-6 py-3 text-lg',
    className
  )">
    <slot />
  </button>
</template>

<script setup lang="ts">
import { cn } from '@/lib/utils'

withDefaults(defineProps<{
  variant?: 'primary' | 'secondary' | 'danger'
  size?: 'sm' | 'md' | 'lg'
  className?: string
}>(), {
  variant: 'primary',
  size: 'md',
})
</script>
```

### class-variance-authority (cva)

```bash
npm install class-variance-authority
```

```ts
// components/ui/button.ts
import { cva, type VariantProps } from 'class-variance-authority'
import { cn } from '@/lib/utils'

export const buttonVariants = cva(
  'inline-flex items-center justify-center rounded-lg font-medium transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:pointer-events-none disabled:opacity-50',
  {
    variants: {
      variant: {
        primary: 'bg-blue-600 text-white hover:bg-blue-700 focus:ring-blue-500',
        secondary: 'bg-gray-100 text-gray-900 hover:bg-gray-200 focus:ring-gray-500',
        danger: 'bg-red-600 text-white hover:bg-red-700 focus:ring-red-500',
        outline: 'border border-gray-300 bg-transparent hover:bg-gray-50',
        ghost: 'bg-transparent hover:bg-gray-100',
      },
      size: {
        sm: 'h-8 px-3 text-sm',
        md: 'h-10 px-4',
        lg: 'h-12 px-6 text-lg',
        icon: 'h-10 w-10',
      },
    },
    defaultVariants: {
      variant: 'primary',
      size: 'md',
    },
  }
)

export type ButtonVariants = VariantProps<typeof buttonVariants>
```

```vue
<!-- components/ui/Button.vue -->
<template>
  <button
    :class="cn(buttonVariants({ variant, size }), $attrs.class)"
    v-bind="$attrs"
  >
    <slot />
  </button>
</template>

<script setup lang="ts">
import { buttonVariants, type ButtonVariants } from './button'
import { cn } from '@/lib/utils'

defineProps<ButtonVariants>()
</script>
```

```vue
<!-- Использование -->
<template>
  <Button variant="primary" size="md">Сохранить</Button>
  <Button variant="danger" size="lg">Удалить</Button>
  <Button variant="outline" size="sm">Отмена</Button>
</template>
```

## 🧩 Composables для переиспользования

### useTheme — управление темой

```ts
// composables/useTheme.ts
import { ref, watchEffect, computed } from 'vue'

type Theme = 'light' | 'dark' | 'system'

const theme = ref<Theme>(
  (localStorage.getItem('theme') as Theme) || 'system'
)

export function useTheme() {
  const resolvedTheme = computed<'light' | 'dark'>(() => {
    if (theme.value === 'system') {
      return window.matchMedia('(prefers-color-scheme: dark)').matches
        ? 'dark'
        : 'light'
    }
    return theme.value
  })

  const isDark = computed(() => resolvedTheme.value === 'dark')

  function setTheme(newTheme: Theme) {
    theme.value = newTheme
    localStorage.setItem('theme', newTheme)
  }

  function toggleTheme() {
    setTheme(isDark.value ? 'light' : 'dark')
  }

  watchEffect(() => {
    const root = document.documentElement
    root.classList.remove('light', 'dark')
    root.classList.add(resolvedTheme.value)
  })

  return {
    theme,
    resolvedTheme,
    isDark,
    setTheme,
    toggleTheme,
  }
}
```

```vue
<!-- components/ThemeToggle.vue -->
<template>
  <div class="inline-flex items-center gap-1 bg-gray-100 dark:bg-gray-800 p-1 rounded-lg">
    <button
      v-for="mode in (['light', 'dark', 'system'] as const)"
      :key="mode"
      @click="setTheme(mode)"
      :class="cn(
        'p-2 rounded-md transition-colors',
        theme === mode && 'bg-white dark:bg-gray-700 shadow-sm'
      )"
      :aria-label="`Тема: ${mode}`"
    >
      <Sun v-if="mode === 'light'" class="w-4 h-4" />
      <Moon v-else-if="mode === 'dark'" class="w-4 h-4" />
      <Monitor v-else class="w-4 h-4" />
    </button>
  </div>
</template>

<script setup lang="ts">
import { useTheme } from '@/composables/useTheme'
import { cn } from '@/lib/utils'
import { Sun, Moon, Monitor } from 'lucide-vue-next'

const { theme, setTheme } = useTheme()
</script>
```

### useClassMerge — объединение классов

```ts
// composables/useClassMerge.ts
import { computed, type MaybeRefOrGetter } from 'vue'
import { cn } from '@/lib/utils'

export function useClassMerge(
  ...classes: MaybeRefOrGetter<string | undefined | null | false>[]
) {
  return computed(() => {
    const resolved = classes.map(cls => {
      if (typeof cls === 'function') return cls()
      return cls
    })
    return cn(...resolved)
  })
}
```

```vue
<template>
  <div :class="mergedClass">
    <slot />
  </div>
</template>

<script setup lang="ts">
import { useClassMerge } from '@/composables/useClassMerge'

const props = defineProps<{
  variant?: 'primary' | 'secondary'
  class?: string
}>()

const mergedClass = useClassMerge(
  'base-classes',
  () => props.variant === 'primary' ? 'bg-blue-500' : 'bg-gray-500',
  () => props.class
)
</script>
```

## 📘 TypeScript + Vue

### Типизация пропсов

```vue
<template>
  <button
    :class="cn(buttonVariants({ variant, size }), $attrs.class)"
    :disabled="disabled || isLoading"
    v-bind="$attrs"
  >
    <Loader2 v-if="isLoading" class="mr-2 h-4 w-4 animate-spin" />
    <slot />
  </button>
</template>

<script setup lang="ts">
import { buttonVariants, type ButtonVariants } from './button'
import { cn } from '@/lib/utils'
import { Loader2 } from 'lucide-vue-next'

interface Props extends ButtonVariants {
  isLoading?: boolean
  disabled?: boolean
}

withDefaults(defineProps<Props>(), {
  variant: 'primary',
  size: 'md',
  isLoading: false,
  disabled: false,
})
</script>
```

### Типизация emits

```vue
<template>
  <input
    :value="modelValue"
    @input="$emit('update:modelValue', ($event.target as HTMLInputElement).value)"
    :class="cn(
      'w-full px-4 py-2 border rounded-lg',
      error ? 'border-red-500' : 'border-gray-300'
    )"
  >
</template>

<script setup lang="ts">
import { cn } from '@/lib/utils'

defineProps<{
  modelValue: string
  error?: string
}>()

defineEmits<{
  'update:modelValue': [value: string]
}>()
</script>
```

### defineModel (Vue 3.4+)

```vue
<template>
  <input
    v-model="model"
    :class="cn(
      'w-full px-4 py-2 border rounded-lg',
      error ? 'border-red-500 focus:ring-red-500' : 'border-gray-300 focus:ring-blue-500'
    )"
  >
</template>

<script setup lang="ts">
import { cn } from '@/lib/utils'

const model = defineModel<string>({ required: true })

defineProps<{
  error?: string
}>()
</script>
```

## 🎨 Практические паттерны компонентов

### 1. 🔘 Button (полноценный)

```vue
<!-- components/ui/Button.vue -->
<template>
  <component
    :is="as"
    :class="cn(buttonVariants({ variant, size }), $attrs.class)"
    :disabled="disabled || isLoading"
    v-bind="$attrs"
  >
    <Loader2 v-if="isLoading" class="mr-2 h-4 w-4 animate-spin" />
    <slot />
  </component>
</template>

<script setup lang="ts">
import { cn } from '@/lib/utils'
import { buttonVariants, type ButtonVariants } from './button'
import { Loader2 } from 'lucide-vue-next'

interface Props extends ButtonVariants {
  as?: string | Component
  isLoading?: boolean
  disabled?: boolean
}

withDefaults(defineProps<Props>(), {
  as: 'button',
  variant: 'primary',
  size: 'md',
  isLoading: false,
  disabled: false,
})
</script>
```

### 2. 🎴 Card

```vue
<!-- components/ui/Card.vue -->
<template>
  <div :class="cn(
    'bg-white rounded-xl shadow-sm border border-gray-200',
    hover && 'transition-shadow hover:shadow-md',
    $attrs.class
  )">
    <slot />
  </div>
</template>

<script setup lang="ts">
import { cn } from '@/lib/utils'

defineProps<{
  hover?: boolean
}>()
</script>
```

```vue
<!-- components/ui/CardHeader.vue -->
<template>
  <div :class="cn('flex flex-col space-y-1.5 p-6 border-b', $attrs.class)">
    <slot />
  </div>
</template>

<script setup lang="ts">
import { cn } from '@/lib/utils'
</script>
```

```vue
<!-- Использование -->
<Card hover>
  <CardHeader>
    <h3 class="text-xl font-bold">Заголовок</h3>
    <p class="text-sm text-gray-500">Описание</p>
  </CardHeader>
  <div class="p-6">
    <p>Содержимое карточки</p>
  </div>
  <div class="p-6 pt-0">
    <Button>Действие</Button>
  </div>
</Card>
```

### 3. 📝 Input с v-model

```vue
<!-- components/ui/Input.vue -->
<template>
  <div class="w-full">
    <label
      v-if="label"
      :for="inputId"
      class="block text-sm font-medium text-gray-700 mb-1"
    >
      {{ label }}
    </label>
    <input
      :id="inputId"
      :value="modelValue"
      @input="$emit('update:modelValue', ($event.target as HTMLInputElement).value)"
      :type="type"
      :placeholder="placeholder"
      :class="cn(
        'flex h-10 w-full rounded-lg border bg-white px-3 py-2 text-sm',
        'placeholder:text-gray-400',
        'focus:outline-none focus:ring-2 focus:ring-offset-1',
        'disabled:cursor-not-allowed disabled:opacity-50',
        error
          ? 'border-red-500 focus:border-red-500 focus:ring-red-500'
          : 'border-gray-300 focus:border-blue-500 focus:ring-blue-500',
        $attrs.class
      )"
    >
    <p v-if="error" class="mt-1 text-sm text-red-500">{{ error }}</p>
    <p v-else-if="hint" class="mt-1 text-sm text-gray-500">{{ hint }}</p>
  </div>
</template>

<script setup lang="ts">
import { cn } from '@/lib/utils'

defineProps<{
  modelValue: string
  label?: string
  type?: string
  placeholder?: string
  error?: string
  hint?: string
}>()

defineEmits<{
  'update:modelValue': [value: string]
}>()

const inputId = `input-${Math.random().toString(36).slice(2)}`
</script>
```

```vue
<!-- Использование -->
<Input
  v-model="email"
  label="Email"
  type="email"
  placeholder="you@example.com"
  :error="errors.email"
/>
```

### 4. 🏷️ Badge

```vue
<!-- components/ui/Badge.vue -->
<template>
  <div :class="cn(badgeVariants({ variant }), $attrs.class)">
    <slot />
  </div>
</template>

<script setup lang="ts">
import { cn } from '@/lib/utils'
import { cva, type VariantProps } from 'class-variance-authority'

const badgeVariants = cva(
  'inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-semibold transition-colors',
  {
    variants: {
      variant: {
        default: 'bg-blue-100 text-blue-800',
        secondary: 'bg-gray-100 text-gray-800',
        success: 'bg-green-100 text-green-800',
        warning: 'bg-yellow-100 text-yellow-800',
        danger: 'bg-red-100 text-red-800',
        outline: 'border border-gray-300 text-gray-700',
      },
    },
    defaultVariants: {
      variant: 'default',
    },
  }
)

defineProps<VariantProps<typeof badgeVariants>>()
</script>
```

### 5. 🎚️ Toggle / Switch

```vue
<!-- components/ui/Toggle.vue -->
<template>
  <label :class="cn(
    'inline-flex items-center cursor-pointer',
    disabled && 'opacity-50 cursor-not-allowed'
  )">
    <input
      type="checkbox"
      class="sr-only peer"
      :checked="modelValue"
      @change="$emit('update:modelValue', ($event.target as HTMLInputElement).checked)"
      :disabled="disabled"
    >
    <div :class="cn(
      'relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300',
      'rounded-full peer',
      'peer-checked:after:translate-x-full peer-checked:after:border-white',
      'after:content-[\'\'] after:absolute after:top-[2px] after:left-[2px]',
      'after:bg-white after:border-gray-300 after:border after:rounded-full',
      'after:h-5 after:w-5 after:transition-all',
      'dark:bg-gray-700 dark:peer-focus:ring-blue-800',
      modelValue && 'bg-blue-600'
    )" />
    <span v-if="label" class="ml-3 text-sm font-medium text-gray-900 dark:text-gray-300">
      {{ label }}
    </span>
  </label>
</template>

<script setup lang="ts">
import { cn } from '@/lib/utils'

defineProps<{
  modelValue: boolean
  label?: string
  disabled?: boolean
}>()

defineEmits<{
  'update:modelValue': [value: boolean]
}>()
</script>
```

### 6. 📋 Select

```vue
<!-- components/ui/Select.vue -->
<template>
  <div class="w-full">
    <label
      v-if="label"
      :for="selectId"
      class="block text-sm font-medium text-gray-700 mb-1"
    >
      {{ label }}
    </label>
    <select
      :id="selectId"
      :value="modelValue"
      @change="$emit('update:modelValue', ($event.target as HTMLSelectElement).value)"
      :class="cn(
        'flex h-10 w-full rounded-lg border bg-white px-3 py-2 text-sm',
        'focus:outline-none focus:ring-2 focus:ring-offset-1',
        'disabled:cursor-not-allowed disabled:opacity-50',
        error
          ? 'border-red-500 focus:border-red-500 focus:ring-red-500'
          : 'border-gray-300 focus:border-blue-500 focus:ring-blue-500',
        $attrs.class
      )"
    >
      <option v-if="placeholder" value="" disabled>{{ placeholder }}</option>
      <option
        v-for="option in options"
        :key="option.value"
        :value="option.value"
      >
        {{ option.label }}
      </option>
    </select>
    <p v-if="error" class="mt-1 text-sm text-red-500">{{ error }}</p>
  </div>
</template>

<script setup lang="ts">
import { cn } from '@/lib/utils'

defineProps<{
  modelValue: string
  options: Array<{ value: string; label: string }>
  label?: string
  placeholder?: string
  error?: string
}>()

defineEmits<{
  'update:modelValue': [value: string]
}>()

const selectId = `select-${Math.random().toString(36).slice(2)}`
</script>
```

## 🎯 Практические паттерны

### 1. 📱 Responsive Sidebar с composables

```vue
<!-- composables/useSidebar.ts -->
import { ref } from 'vue'

const isOpen = ref(false)

export function useSidebar() {
  function toggle() {
    isOpen.value = !isOpen.value
  }

  function close() {
    isOpen.value = false
  }

  return { isOpen, toggle, close }
}
```

```vue
<!-- components/Dashboard.vue -->
<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Mobile header -->
    <div class="lg:hidden flex items-center justify-between p-4 bg-white border-b">
      <span class="font-bold text-xl">Logo</span>
      <button
        @click="toggle"
        class="p-2 rounded-lg hover:bg-gray-100"
      >
        <Menu v-if="!isOpen" class="w-6 h-6" />
        <X v-else class="w-6 h-6" />
      </button>
    </div>

    <div class="flex">
      <!-- Sidebar -->
      <aside
        :class="cn(
          'fixed inset-y-0 left-0 z-50 w-64 bg-white border-r transform transition-transform lg:translate-x-0 lg:static lg:inset-0',
          isOpen ? 'translate-x-0' : '-translate-x-full'
        )"
      >
        <div class="p-4">
          <h2 class="font-bold text-xl mb-4 hidden lg:block">Logo</h2>
          <nav class="space-y-1">
            <RouterLink
              v-for="item in menuItems"
              :key="item.path"
              :to="item.path"
              class="block px-4 py-2 rounded-lg text-gray-700 hover:bg-gray-100"
              active-class="bg-blue-50 text-blue-600"
            >
              {{ item.label }}
            </RouterLink>
          </nav>
        </div>
      </aside>

      <!-- Overlay -->
      <div
        v-if="isOpen"
        class="fixed inset-0 bg-black/50 z-40 lg:hidden"
        @click="close"
      />

      <!-- Main content -->
      <main class="flex-1 p-4 lg:p-8">
        <RouterView />
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useSidebar } from '@/composables/useSidebar'
import { cn } from '@/lib/utils'
import { Menu, X } from 'lucide-vue-next'
import { RouterLink, RouterView } from 'vue-router'

const { isOpen, toggle, close } = useSidebar()

const menuItems = [
  { path: '/', label: 'Главная' },
  { path: '/profile', label: 'Профиль' },
  { path: '/settings', label: 'Настройки' },
]
</script>
```

### 2. 🎴 Карточка товара с hover-эффектами

```vue
<!-- components/ProductCard.vue -->
<template>
  <div class="group bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-lg transition-shadow">
    <!-- Изображение -->
    <div class="relative aspect-square overflow-hidden">
      <img
        :src="image"
        :alt="title"
        class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
      >
      
      <!-- Бейдж -->
      <Badge
        v-if="badge"
        variant="danger"
        class="absolute top-3 left-4"
      >
        {{ badge }}
      </Badge>

      <!-- Кнопка избранного -->
      <button
        @click="isFavorite = !isFavorite"
        :class="cn(
          'absolute top-3 right-3 p-2 rounded-full transition-all',
          isFavorite
            ? 'bg-red-500 text-white'
            : 'bg-white/80 text-gray-700 hover:bg-white'
        )"
      >
        <Heart :class="cn('w-5 h-5', isFavorite && 'fill-current')" />
      </button>

      <!-- Overlay с кнопкой -->
      <div class="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-colors flex items-center justify-center opacity-0 group-hover:opacity-100">
        <Button variant="outline" class="bg-white">
          Быстрый просмотр
        </Button>
      </div>
    </div>

    <!-- Контент -->
    <div class="p-4">
      <h3 class="font-medium text-gray-900 line-clamp-2">{{ title }}</h3>
      <div class="mt-2 flex items-baseline gap-2">
        <span class="text-xl font-bold text-gray-900">
          {{ price.toLocaleString('ru-RU') }} ₽
        </span>
        <span v-if="oldPrice" class="text-sm text-gray-400 line-through">
          {{ oldPrice.toLocaleString('ru-RU') }} ₽
        </span>
      </div>
      <Button class="mt-3 w-full" @click="$emit('addToCart')">
        <ShoppingCart class="w-4 h-4 mr-2" />
        В корзину
      </Button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { cn } from '@/lib/utils'
import { Heart, ShoppingCart } from 'lucide-vue-next'
import Badge from './ui/Badge.vue'
import Button from './ui/Button.vue'

defineProps<{
  title: string
  price: number
  oldPrice?: number
  image: string
  badge?: string
}>()

defineEmits<{
  addToCart: []
}>()

const isFavorite = ref(false)
</script>
```

### 3. 📊 Таблица с сортировкой

```vue
<!-- components/UsersTable.vue -->
<template>
  <div class="bg-white rounded-xl shadow-sm border overflow-hidden">
    <div class="overflow-x-auto">
      <table class="w-full">
        <thead class="bg-gray-50 border-b">
          <tr>
            <th
              v-for="column in columns"
              :key="column.key"
              @click="handleSort(column.key)"
              class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100"
            >
              <div class="flex items-center gap-1">
                {{ column.label }}
                <ArrowUpDown :class="cn(
                  'w-3 h-3',
                  sortField === column.key ? 'text-blue-600' : 'text-gray-400'
                )" />
              </div>
            </th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-200">
          <tr
            v-for="user in sortedUsers"
            :key="user.id"
            class="hover:bg-gray-50 transition-colors"
          >
            <td class="px-6 py-4 font-medium text-gray-900">{{ user.name }}</td>
            <td class="px-6 py-4 text-gray-600">{{ user.email }}</td>
            <td class="px-6 py-4 text-gray-600">{{ user.role }}</td>
            <td class="px-6 py-4">
              <Badge :variant="statusVariant(user.status)">
                {{ user.status }}
              </Badge>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { cn } from '@/lib/utils'
import { ArrowUpDown } from 'lucide-vue-next'
import Badge from './ui/Badge.vue'

interface User {
  id: number
  name: string
  email: string
  role: string
  status: 'active' | 'pending' | 'inactive'
}

const props = defineProps<{
  users: User[]
}>()

const columns = [
  { key: 'name', label: 'Имя' },
  { key: 'email', label: 'Email' },
  { key: 'role', label: 'Роль' },
  { key: 'status', label: 'Статус' },
]

const sortField = ref<keyof User>('name')
const sortDirection = ref<'asc' | 'desc'>('asc')

function handleSort(field: keyof User) {
  if (sortField.value === field) {
    sortDirection.value = sortDirection.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortField.value = field
    sortDirection.value = 'asc'
  }
}

const sortedUsers = computed(() => {
  return [...props.users].sort((a, b) => {
    const aValue = a[sortField.value]
    const bValue = b[sortField.value]
    if (aValue < bValue) return sortDirection.value === 'asc' ? -1 : 1
    if (aValue > bValue) return sortDirection.value === 'asc' ? 1 : -1
    return 0
  })
})

function statusVariant(status: User['status']) {
  return {
    active: 'success',
    pending: 'warning',
    inactive: 'secondary',
  }[status] as 'success' | 'warning' | 'secondary'
}
</script>
```

### 4. 📝 Форма с валидацией

```vue
<!-- components/RegisterForm.vue -->
<template>
  <form @submit.prevent="handleSubmit" class="space-y-4 max-w-md mx-auto p-6 bg-white rounded-xl shadow-md">
    <h2 class="text-2xl font-bold text-gray-900">Регистрация</h2>

    <Input
      v-model="form.name"
      label="Имя"
      placeholder="Иван Иванов"
      :error="errors.name"
    />

    <Input
      v-model="form.email"
      label="Email"
      type="email"
      placeholder="you@example.com"
      :error="errors.email"
    />

    <Input
      v-model="form.password"
      label="Пароль"
      type="password"
      placeholder="••••••••"
      :error="errors.password"
    />

    <Toggle
      v-model="form.newsletter"
      label="Получать новости"
    />

    <Button
      type="submit"
      class="w-full"
      :is-loading="isSubmitting"
    >
      Зарегистрироваться
    </Button>
  </form>
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue'
import Input from './ui/Input.vue'
import Button from './ui/Button.vue'
import Toggle from './ui/Toggle.vue'

const form = reactive({
  name: '',
  email: '',
  password: '',
  newsletter: false,
})

const errors = reactive({
  name: '',
  email: '',
  password: '',
})

const isSubmitting = ref(false)

function validate() {
  errors.name = form.name.length < 2 ? 'Минимум 2 символа' : ''
  errors.email = /^\S+@\S+$/.test(form.email) ? '' : 'Неверный email'
  errors.password = form.password.length < 8 ? 'Минимум 8 символов' : ''
  return !errors.name && !errors.email && !errors.password
}

async function handleSubmit() {
  if (!validate()) return

  isSubmitting.value = true
  try {
    await new Promise(resolve => setTimeout(resolve, 1000))
    console.log('Form submitted:', form)
  } finally {
    isSubmitting.value = false
  }
}
</script>
```

## 🛣️ Vue Router + Tailwind

### Активные ссылки

```vue
<!-- components/Navigation.vue -->
<template>
  <nav class="bg-white border-b border-gray-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16">
        <div class="flex">
          <RouterLink to="/" class="flex items-center font-bold text-xl text-gray-900">
            Logo
          </RouterLink>
          <div class="hidden sm:ml-6 sm:flex sm:space-x-8">
            <RouterLink
              v-for="item in links"
              :key="item.path"
              :to="item.path"
              :class="cn(
                'inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium transition-colors',
                $route.path === item.path
                  ? 'border-blue-500 text-gray-900'
                  : 'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700'
              )"
            >
              {{ item.label }}
            </RouterLink>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { RouterLink, useRoute } from 'vue-router'
import { cn } from '@/lib/utils'

const route = useRoute()

const links = [
  { path: '/', label: 'Главная' },
  { path: '/about', label: 'О нас' },
  { path: '/contact', label: 'Контакты' },
]
</script>
```

### useRoute в composables

```ts
// composables/useActiveLink.ts
import { computed } from 'vue'
import { useRoute } from 'vue-router'

export function useActiveLink(path: string) {
  const route = useRoute()
  
  const isActive = computed(() => route.path === path)
  const isExactActive = computed(() => route.path === path)
  
  return {
    isActive,
    isExactActive,
    activeClass: computed(() => isActive.value ? 'text-blue-600 font-medium' : 'text-gray-600'),
  }
}
```

## 📊 Шпаргалка: что когда использовать

| Задача | Решение |
| :-- | :-- |
| Статические классы | `class="..."` |
| Динамические классы (объект) | `:class="{ active: isActive }"` |
| Динамические классы (массив) | `:class="[base, condition && 'active']"` |
| Объединение классов | `cn()` = `twMerge(clsx(...))` |
| Вариативные компоненты | `cva` (class-variance-authority) |
| Передача классов в дочерний | `$attrs.class` |
| v-model для классов | `defineModel()` |
| Переиспользование логики | Composables |
| Dark mode | `useTheme()` composable |
| Активные ссылки | `useRoute()` + `cn()` |
| Формы | `reactive()` + валидация |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Забывают `:` перед `class`

```vue
<!-- ❌ Плохо: статическая строка, не будет работать -->
<button class="{ 'bg-blue-500': isPrimary }">Кнопка</button>

<!-- ✅ Хорошо: v-bind для динамических классов -->
<button :class="{ 'bg-blue-500': isPrimary }">Кнопка</button>
```

### ❌ Ошибка 2: Динамическая конкатенация классов

```vue
<!-- ❌ Плохо: Tailwind не увидит эти классы -->
<button :class="`btn-${variant}`">Кнопка</button>

<!-- ✅ Хорошо: полные имена классов -->
<button :class="variants[variant]">Кнопка</button>
```

### ❌ Ошибка 3: Забывают про `$attrs.class`

```vue
<!-- ❌ Плохо: пользовательские классы игнорируются -->
<template>
  <button class="btn">
    <slot />
  </button>
</template>

<!-- ✅ Хорошо: передаём пользовательские классы -->
<template>
  <button :class="cn('btn', $attrs.class)">
    <slot />
  </button>
</template>
```

### ❌ Ошибка 4: Мутация пропсов

```vue
<!-- ❌ Плохо: нельзя мутировать пропсы -->
<script setup>
const props = defineProps<{ class: string }>()
props.class = 'new-class' // Ошибка!
</script>

<!-- ✅ Хорошо: используем локальную переменную или computed -->
<script setup>
const props = defineProps<{ class?: string }>()
const mergedClass = computed(() => cn('base', props.class))
</script>
```

### ❌ Ошибка 5: Забывают про `inheritAttrs: false`

```vue
<!-- ❌ Плохо: атрибуты дублируются -->
<template>
  <div class="wrapper">
    <input :class="$attrs.class" />
  </div>
</template>

<!-- ✅ Хорошо: отключаем автоматическое наследование -->
<template>
  <div class="wrapper">
    <input :class="$attrs.class" v-bind="$attrs" />
  </div>
</template>

<script setup>
defineOptions({ inheritAttrs: false })
</script>
```

### ❌ Ошибка 6: `watchEffect` без cleanup

```ts
// ❌ Плохо: подписка не очищается
watchEffect(() => {
  window.addEventListener('resize', handleResize)
})

// ✅ Хорошо: возвращаем cleanup функцию
watchEffect((onCleanup) => {
  window.addEventListener('resize', handleResize)
  onCleanup(() => {
    window.removeEventListener('resize', handleResize)
  })
})
```

### ❌ Ошибка 7: Забывают про `content` в конфиге

```js
// ❌ Плохо: Tailwind не найдёт классы в .vue файлах
module.exports = {
  content: ['./src/**/*.js'],
}

// ✅ Хорошо: указываем .vue файлы
module.exports = {
  content: ['./src/**/*.{vue,js,ts}'],
}
```

### ❌ Ошибка 8: Избыточные `<div>` обёртки

```vue
<!-- ❌ Плохо: лишний div -->
<template>
  <div>
    <div class="card">
      <p>Контент</p>
    </div>
  </div>
</template>

<!-- ✅ Хорошо: применяем классы напрямую -->
<template>
  <div class="card">
    <p>Контент</p>
  </div>
</template>
```

### ❌ Ошибка 9: Не типизируют emits

```vue
<!-- ❌ Плохо: нет типов для событий -->
<script setup>
defineEmits(['update:modelValue'])
</script>

<!-- ✅ Хорошо: типизированные emits -->
<script setup lang="ts">
defineEmits<{
  'update:modelValue': [value: string]
  'submit': []
}>()
</script>
```

### ❌ Ошибка 10: Забывают про `defineModel` (Vue 3.4+)

```vue
<!-- ❌ Плохо: много кода для v-model -->
<script setup>
const props = defineProps<{ modelValue: string }>()
const emit = defineEmits(['update:modelValue'])
</script>
<template>
  <input
    :value="props.modelValue"
    @input="emit('update:modelValue', $event.target.value)"
  >
</template>

<!-- ✅ Хорошо: defineModel упрощает код -->
<script setup>
const model = defineModel<string>()
</script>
<template>
  <input v-model="model">
</template>
```

## 🎯 Что дальше?

Теперь вы полностью владеете интеграцией Vue + Tailwind CSS! Но это только одна из популярных связок.

**Следующий шаг:** [🚀 Next.js + Tailwind CSS](nextjs.md) — изучим интеграцию с Next.js, Server Components и App Router.

---

---



---

# 📁 Структура проекта

```
tailwind-css-guide/
├── collector/ [1 файлов]
│   └── collect-app.ps1 (12 541 байт)
├── docs/ [24 файлов, 6 подпапок]
│   ├── advanced/ [4 файлов]
│   │   ├── customization.md (29 334 байт)
│   │   ├── directives.md (27 018 байт)
│   │   ├── optimization.md (19 249 байт)
│   │   └── plugins.md (23 068 байт)
│   ├── basics/ [4 файлов]
│   │   ├── configuration.md (23 045 байт)
│   │   ├── installation.md (29 158 байт)
│   │   ├── introduction.md (13 301 байт)
│   │   └── utility-classes.md (27 907 байт)
│   ├── integrations/ [3 файлов]
│   │   ├── nextjs.md (39 434 байт)
│   │   ├── react.md (43 579 байт)
│   │   └── vue.md (36 987 байт)
│   ├── layout/ [4 файлов]
│   │   ├── flexbox.md (19 126 байт)
│   │   ├── grid.md (30 592 байт)
│   │   ├── sizing.md (26 758 байт)
│   │   └── spacing.md (22 397 байт)
│   ├── responsive/ [3 файлов]
│   │   ├── breakpoints.md (26 342 байт)
│   │   ├── dark-mode.md (29 265 байт)
│   │   └── states.md (25 354 байт)
│   ├── styling/ [5 файлов]
│   │   ├── backgrounds.md (24 695 байт)
│   │   ├── borders.md (25 280 байт)
│   │   ├── colors.md (20 733 байт)
│   │   ├── effects.md (25 503 байт)
│   │   └── typography.md (25 311 байт)
│   └── index.md (7 112 байт)
├── output/ [2 файлов]
│   ├── tailwind-css-guide-full.md (631 521 байт)
│   └── tailwind-css-guide-full.pdf (14 195 882 байт)
├── LICENSE.md (0 байт)
├── mkdocs.yml (1 617 байт)
└── README.md (4 899 байт)
```



---

## 📊 Статистика экспорта

| Параметр | Значение |
| :-- | :-- |
| **Обработано файлов** | 24 |
| **Пропущено файлов** | 0 |
| **Общий объём контента** | 517 307 символов |
| **Размер итогового файла** | 633 602 байт |
| **Дата генерации** | 29.06.2026 01:11:05 |

---

_Сгенерировано автоматически скриптом `collector/export-docs.ps1`_