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