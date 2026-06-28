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