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