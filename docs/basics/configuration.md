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