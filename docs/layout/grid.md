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