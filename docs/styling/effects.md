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