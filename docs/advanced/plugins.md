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
