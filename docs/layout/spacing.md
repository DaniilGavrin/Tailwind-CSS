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
