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