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