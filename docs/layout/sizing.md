# 📐 Размеры в Tailwind CSS

> **Полное руководство по управлению размерами:** от ширины и высоты до aspect-ratio и адаптивных размеров

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Освоите все утилиты для управления шириной и высотой
- ✅ Научитесь использовать min/max значения для гибких размеров
- ✅ Поймёте разницу между фиксированными, процентными и viewport-размерами
- ✅ Освоите `aspect-ratio` для пропорциональных элементов
- ✅ Научитесь создавать адаптивные размеры
- ✅ Поймёте, когда использовать `size-*` вместо `w-*` + `h-*`
- ✅ Избежите типичных ошибок при работе с размерами

## 📏 Ширина: `w-{size}`

Tailwind использует **единую шкалу** для размеров (как и для отступов):

### Фиксированные размеры

| Класс | CSS | Визуально |
| :-- | :-- | :-- |
| `w-0` | `width: 0px` | Нет ширины |
| `w-px` | `width: 1px` | 1 пиксель |
| `w-0.5` | `width: 0.125rem` (2px) | Очень узкий |
| `w-1` | `width: 0.25rem` (4px) | Узкий |
| `w-4` | `width: 1rem` (16px) | Средний |
| `w-8` | `width: 2rem` (32px) | Широкий |
| `w-16` | `width: 4rem` (64px) | Очень широкий |
| `w-32` | `width: 8rem` (128px) | Огромный |
| `w-64` | `width: 16rem` (256px) | Максимальный фиксированный |

### Дробные размеры (проценты)

| Класс | CSS | Применение |
| :-- | :-- | :-- |
| `w-1/2` | `width: 50%` | Половина родителя |
| `w-1/3` | `width: 33.333%` | Треть родителя |
| `w-2/3` | `width: 66.667%` | Две трети |
| `w-1/4` | `width: 25%` | Четверть |
| `w-3/4` | `width: 75%` | Три четверти |
| `w-1/5` | `width: 20%` | Пятая часть |
| `w-2/5` | `width: 40%` | Две пятых |
| `w-3/5` | `width: 60%` | Три пятых |
| `w-4/5` | `width: 80%` | Четыре пятых |
| `w-full` | `width: 100%` | Вся ширина родителя |
| `w-screen` | `width: 100vw` | Вся ширина viewport |
| `w-min` | `width: min-content` | По содержимому (мин) |
| `w-max` | `width: max-content` | По содержимому (макс) |
| `w-fit` | `width: fit-content` | Автоматически по содержимому |

```html
<!-- Фиксированная ширина -->
<div class="w-64 bg-blue-500">Ширина 256px</div>

<!-- Процентная ширина -->
<div class="w-1/2 bg-green-500">Половина родителя</div>

<!-- На всю ширину -->
<div class="w-full bg-purple-500">На всю ширину</div>

<!-- По содержимому -->
<div class="w-fit bg-orange-500">Подстроится под текст</div>
```

### Viewport-размеры

```html
<!-- На всю ширину экрана -->
<section class="w-screen bg-gray-900 text-white p-8">
  Hero на всю ширину экрана
</section>
```

## 📐 Минимальная ширина: `min-w-{size}`

| Класс | CSS | Применение |
| :-- | :-- | :-- |
| `min-w-0` | `min-width: 0px` | Сброс минимальной ширины |
| `min-w-full` | `min-width: 100%` | Минимум — вся ширина родителя |
| `min-w-min` | `min-width: min-content` | По минимальному содержимому |
| `min-w-max` | `min-width: max-content` | По максимальному содержимому |
| `min-w-fit` | `min-width: fit-content` | Автоматически |
| `min-w-{size}` | `min-width: {size}` | Фиксированное значение |

```html
<!-- Элемент не может быть уже 200px -->
<div class="min-w-[200px] w-1/2 bg-blue-500">
  Минимум 200px, но может растянуться
</div>

<!-- Кнопка не сжимается -->
<button class="min-w-max bg-blue-600 text-white px-4 py-2 rounded">
  Текст кнопки не переносится
</button>
```

> 💡 **Важно:** `min-w-0` критически важен в flex-контейнерах для работы `truncate` и переполнения текста.

## 📏 Максимальная ширина: `max-w-{size}`

### Предустановленные значения

| Класс | CSS | Применение |
| :-- | :-- | :-- |
| `max-w-0` | `max-width: 0rem` | Нет ширины |
| `max-w-none` | `max-width: none` | Без ограничений |
| `max-w-xs` | `max-width: 20rem` (320px) | Очень узкий |
| `max-w-sm` | `max-width: 24rem` (384px) | Узкий |
| `max-w-md` | `max-width: 28rem` (448px) | Средний |
| `max-w-lg` | `max-width: 32rem` (512px) | Широкий |
| `max-w-xl` | `max-width: 36rem` (576px) | Очень широкий |
| `max-w-2xl` | `max-width: 42rem` (672px) | Широкий контент |
| `max-w-3xl` | `max-width: 48rem` (768px) | Контент статей |
| `max-w-4xl` | `max-width: 56rem` (896px) | Широкие статьи |
| `max-w-5xl` | `max-width: 64rem` (1024px) | Очень широкий |
| `max-w-6xl` | `max-width: 72rem` (1152px) | Огромный |
| `max-w-7xl` | `max-width: 80rem` (1280px) | Максимальный |
| `max-w-full` | `max-width: 100%` | 100% родителя |
| `max-w-min` | `max-width: min-content` | По минимальному содержимому |
| `max-w-max` | `max-width: max-content` | По максимальному содержимому |
| `max-w-fit` | `max-width: fit-content` | Автоматически |
| `max-w-prose` | `max-width: 65ch` | Оптимально для чтения |
| `max-w-screen-sm` | `max-width: 640px` | Breakpoint sm |
| `max-w-screen-md` | `max-width: 768px` | Breakpoint md |
| `max-w-screen-lg` | `max-width: 1024px` | Breakpoint lg |
| `max-w-screen-xl` | `max-width: 1280px` | Breakpoint xl |
| `max-w-screen-2xl` | `max-width: 1536px` | Breakpoint 2xl |

```html
<!-- Контейнер с максимальной шириной -->
<div class="max-w-7xl mx-auto px-4">
  Контент не шире 1280px, центрирован
</div>

<!-- Статья с оптимальной шириной для чтения -->
<article class="max-w-prose mx-auto">
  Длинный текст статьи, комфортный для чтения
</article>

<!-- Модальное окно -->
<div class="max-w-md mx-auto bg-white p-6 rounded-lg shadow-lg">
  Модальное окно шириной до 448px
</div>
```

> 💡 **max-w-prose** — это **65ch** (65 символов), оптимальная ширина для чтения длинного текста по исследованиям читаемости.

## 📐 Высота: `h-{size}`

Синтаксис идентичен ширине:

### Фиксированные размеры

```html
<div class="h-16 bg-blue-500">Высота 64px</div>
<div class="h-32 bg-green-500">Высота 128px</div>
<div class="h-64 bg-purple-500">Высота 256px</div>
```

### Дробные и viewport

| Класс | CSS | Применение |
| :-- | :-- | :-- |
| `h-1/2` | `height: 50%` | Половина родителя |
| `h-1/3` | `height: 33.333%` | Треть |
| `h-2/3` | `height: 66.667%` | Две трети |
| `h-1/4` | `height: 25%` | Четверть |
| `h-3/4` | `height: 75%` | Три четверти |
| `h-1/5` | `height: 20%` | Пятая часть |
| `h-full` | `height: 100%` | Вся высота родителя |
| `h-screen` | `height: 100vh` | Вся высота viewport |
| `h-svh` | `height: 100svh` | Small viewport height (мобильные) |
| `h-lvh` | `height: 100lvh` | Large viewport height |
| `h-dvh` | `height: 100dvh` | Dynamic viewport height |
| `h-min` | `height: min-content` | По содержимому (мин) |
| `h-max` | `height: max-content` | По содержимому (макс) |
| `h-fit` | `height: fit-content` | Автоматически |

```html
<!-- Hero на всю высоту экрана -->
<section class="h-screen bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center">
  <h1 class="text-5xl font-bold text-white">Добро пожаловать!</h1>
</section>

<!-- Половина высоты родителя -->
<div class="h-64 relative">
  <div class="h-1/2 bg-blue-500">Половина высоты</div>
</div>
```

> 💡 **svh/lvh/dvh** — современные viewport-единицы, которые корректно работают на мобильных с адресной строкой. Используйте `dvh` для мобильных приложений.

## 📏 Минимальная высота: `min-h-{size}`

| Класс | CSS | Применение |
| :-- | :-- | :-- |
| `min-h-0` | `min-height: 0px` | Сброс |
| `min-h-full` | `min-height: 100%` | 100% родителя |
| `min-h-screen` | `min-height: 100vh` | 100vh |
| `min-h-svh` | `min-height: 100svh` | Small viewport |
| `min-h-lvh` | `min-height: 100lvh` | Large viewport |
| `min-h-dvh` | `min-height: 100dvh` | Dynamic viewport |
| `min-h-min` | `min-height: min-content` | По содержимому |
| `min-h-max` | `min-height: max-content` | По содержимому |
| `min-h-fit` | `min-height: fit-content` | Автоматически |

```html
<!-- Страница минимум на весь экран, но может расти -->
<main class="min-h-screen bg-gray-50">
  <!-- Контент может быть длиннее экрана -->
</main>

<!-- Input не сжимается -->
<input class="min-h-[44px] w-full border rounded-lg px-4">
```

## 📐 Максимальная высота: `max-h-{size}`

| Класс | CSS |
| :-- | :-- |
| `max-h-full` | `max-height: 100%` |
| `max-h-screen` | `max-height: 100vh` |
| `max-h-svh` | `max-height: 100svh` |
| `max-h-lvh` | `max-height: 100lvh` |
| `max-h-dvh` | `max-height: 100dvh` |
| `max-h-min` | `max-height: min-content` |
| `max-h-max` | `max-height: max-content` |
| `max-h-fit` | `max-height: fit-content` |
| `max-h-{size}` | Фиксированные значения |

```html
<!-- Контейнер со скроллом -->
<div class="max-h-64 overflow-y-auto border rounded-lg p-4">
  <!-- Длинный список, который будет скроллиться -->
  <ul class="space-y-2">
    <li>Пункт 1</li>
    <li>Пункт 2</li>
    <!-- ... много пунктов -->
  </ul>
</div>

<!-- Модальное окно не выше экрана -->
<div class="max-h-[90vh] overflow-y-auto bg-white rounded-lg p-6">
  <!-- Длинный контент -->
</div>
```

## 📦 Size: `size-{size}`

`size-*` — это **сокращение** для одновременной установки `width` и `height`:

```html
<!-- ❌ Длинная запись -->
<div class="w-16 h-16 bg-blue-500">Квадрат</div>

<!-- ✅ Короткая запись -->
<div class="size-16 bg-blue-500">Квадрат</div>
```

### Доступные значения

Аналогичны `w-*` и `h-*`:

```html
<!-- Фиксированные размеры -->
<div class="size-8 bg-blue-500">32×32</div>
<div class="size-16 bg-blue-500">64×64</div>
<div class="size-32 bg-blue-500">128×128</div>

<!-- Full -->
<div class="size-full bg-blue-500">100%×100%</div>
```

> 💡 **Когда использовать:** для квадратных элементов (иконки, аватары, кнопки-иконки). Для прямоугольников используйте `w-*` и `h-*` отдельно.

## 🖼️ Aspect Ratio: `aspect-{ratio}`

Управляет **соотношением сторон** элемента:

| Класс | CSS | Применение |
| :-- | :-- | :-- |
| `aspect-auto` | `aspect-ratio: auto` | По содержимому (по умолчанию) |
| `aspect-square` | `aspect-ratio: 1 / 1` | Квадрат |
| `aspect-video` | `aspect-ratio: 16 / 9` | Видео |

```html
<!-- Квадратное изображение -->
<div class="aspect-square w-64 bg-blue-500">
  <img src="photo.jpg" class="w-full h-full object-cover" alt="">
</div>

<!-- Видео 16:9 -->
<div class="aspect-video w-full bg-gray-900">
  <iframe src="..." class="w-full h-full" frameborder="0"></iframe>
</div>
```

### Кастомные соотношения

```html
<!-- 4:3 (старое ТВ) -->
<div class="aspect-[4/3] w-full bg-gray-200">
  Контент в формате 4:3
</div>

<!-- 21:9 (ультраширокий) -->
<div class="aspect-[21/9] w-full bg-gray-200">
  Ультраширокий формат
</div>

<!-- 2:3 (портрет) -->
<div class="aspect-[2/3] w-64 bg-gray-200">
  Портретная ориентация
</div>

<!-- 3:2 (фото) -->
<div class="aspect-[3/2] w-full bg-gray-200">
  Фотографический формат
</div>
```

## 🎯 Практические паттерны

### 1. 🎴 Карточка товара с квадратным изображением

```html
<div class="bg-white rounded-xl shadow-md overflow-hidden max-w-sm">
  <!-- Квадратное изображение -->
  <div class="aspect-square bg-gray-100">
    <img
      src="product.jpg"
      alt="Товар"
      class="w-full h-full object-cover"
    >
  </div>

  <div class="p-4">
    <h3 class="font-bold text-lg">Название товара</h3>
    <p class="text-gray-600 text-sm mt-1">Описание</p>
    <div class="mt-3 flex items-center justify-between">
      <span class="text-xl font-bold">2 990 ₽</span>
      <button class="bg-blue-600 text-white px-4 py-2 rounded-lg">
        Купить
      </button>
    </div>
  </div>
</div>
```

### 2. 🎬 Hero-секция на весь экран

```html
<section class="min-h-screen bg-gradient-to-br from-blue-600 to-purple-700 flex items-center justify-center p-4">
  <div class="max-w-4xl text-center">
    <h1 class="text-4xl sm:text-5xl md:text-6xl font-bold text-white mb-6">
      Создавайте красивые интерфейсы
    </h1>
    <p class="text-lg sm:text-xl text-blue-100 mb-8 max-w-2xl mx-auto">
      Utility-first CSS фреймворк для быстрой разработки
    </p>
    <div class="flex flex-col sm:flex-row gap-4 justify-center">
      <button class="bg-white text-blue-600 font-semibold px-8 py-3 rounded-lg">
        Начать
      </button>
      <button class="border-2 border-white text-white font-semibold px-8 py-3 rounded-lg">
        Документация
      </button>
    </div>
  </div>
</section>
```

### 3. 🖼️ Галерея с aspect-ratio

```html
<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
  <div class="aspect-square overflow-hidden rounded-lg">
    <img src="photo1.jpg" class="w-full h-full object-cover hover:scale-110 transition-transform" alt="">
  </div>
  <div class="aspect-square overflow-hidden rounded-lg">
    <img src="photo2.jpg" class="w-full h-full object-cover hover:scale-110 transition-transform" alt="">
  </div>
  <div class="aspect-square overflow-hidden rounded-lg">
    <img src="photo3.jpg" class="w-full h-full object-cover hover:scale-110 transition-transform" alt="">
  </div>
  <div class="aspect-square overflow-hidden rounded-lg">
    <img src="photo4.jpg" class="w-full h-full object-cover hover:scale-110 transition-transform" alt="">
  </div>
</div>
```

### 4. 📊 Dashboard с виджетами

```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
  <!-- Виджет статистики -->
  <div class="bg-white rounded-xl shadow-sm border p-6 min-h-[140px]">
    <div class="flex items-center justify-between">
      <div>
        <p class="text-sm text-gray-500">Пользователи</p>
        <p class="text-3xl font-bold mt-1">12 345</p>
      </div>
      <div class="size-12 bg-blue-100 rounded-full flex items-center justify-center">
        <svg class="size-6 text-blue-600" fill="currentColor" viewBox="0 0 24 24">
          <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>
        </svg>
      </div>
    </div>
    <p class="text-sm text-green-600 mt-2">+12% за месяц</p>
  </div>

  <!-- Повторить для других виджетов -->
</div>
```

### 5. 🎥 Видео-плеер с aspect-ratio

```html
<div class="max-w-4xl mx-auto">
  <div class="aspect-video bg-black rounded-xl overflow-hidden shadow-2xl">
    <video
      class="w-full h-full object-cover"
      controls
      poster="poster.jpg"
    >
      <source src="video.mp4" type="video/mp4">
    </video>
  </div>
  <div class="mt-4">
    <h2 class="text-2xl font-bold">Название видео</h2>
    <p class="text-gray-600 mt-1">Описание видео</p>
  </div>
</div>
```

### 6. 👤 Аватары разных размеров

```html
<div class="flex items-center gap-4">
  <!-- XS -->
  <div class="size-8 rounded-full bg-blue-500 flex items-center justify-center text-white text-xs font-bold">
    A
  </div>

  <!-- SM -->
  <div class="size-10 rounded-full bg-green-500 flex items-center justify-center text-white text-sm font-bold">
    B
  </div>

  <!-- MD -->
  <div class="size-12 rounded-full bg-purple-500 flex items-center justify-center text-white font-bold">
    C
  </div>

  <!-- LG -->
  <div class="size-16 rounded-full bg-orange-500 flex items-center justify-center text-white text-xl font-bold">
    D
  </div>

  <!-- XL -->
  <div class="size-20 rounded-full bg-red-500 flex items-center justify-center text-white text-2xl font-bold">
    E
  </div>
</div>
```

### 7. 📋 Таблица с max-height и скроллом

```html
<div class="bg-white rounded-xl shadow-sm border overflow-hidden">
  <div class="px-6 py-4 border-b">
    <h3 class="font-bold text-lg">Последние действия</h3>
  </div>

  <div class="max-h-96 overflow-y-auto">
    <ul class="divide-y divide-gray-200">
      <li class="px-6 py-3 hover:bg-gray-50">
        <p class="font-medium">Новый заказ #1234</p>
        <p class="text-sm text-gray-500">2 минуты назад</p>
      </li>
      <li class="px-6 py-3 hover:bg-gray-50">
        <p class="font-medium">Регистрация пользователя</p>
        <p class="text-sm text-gray-500">5 минут назад</p>
      </li>
      <!-- Много пунктов -->
    </ul>
  </div>
</div>
```

### 8. 📱 Адаптивный контейнер

```html
<!-- Контейнер с разной шириной на разных экранах -->
<div class="w-full max-w-sm sm:max-w-md md:max-w-lg lg:max-w-xl xl:max-w-2xl mx-auto px-4">
  <h2 class="text-2xl font-bold mb-4">Адаптивный контейнер</h2>
  <p class="text-gray-600">
    Ширина контейнера меняется в зависимости от размера экрана
  </p>
</div>
```

## 📊 Шпаргалка: что когда использовать

| Задача | Классы |
| :-- | :-- |
| Фиксированная ширина | `w-64`, `w-32` |
| Процентная ширина | `w-1/2`, `w-1/3`, `w-full` |
| Ширина viewport | `w-screen` |
| Максимальная ширина | `max-w-7xl`, `max-w-prose` |
| Минимальная ширина | `min-w-[200px]`, `min-w-max` |
| Фиксированная высота | `h-64`, `h-32` |
| Высота viewport | `h-screen`, `h-dvh` |
| Минимальная высота | `min-h-screen` |
| Максимальная высота | `max-h-64`, `max-h-screen` |
| Квадратный элемент | `size-16`, `size-full` |
| Соотношение сторон | `aspect-square`, `aspect-video` |
| Кастомное соотношение | `aspect-[4/3]`, `aspect-[21/9]` |
| По содержимому | `w-fit`, `h-fit`, `w-max`, `h-max` |
| Центрирование контейнера | `max-w-7xl mx-auto` |
| Оптимальная ширина текста | `max-w-prose` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: `h-full` без высоты у родителя

```html
<!-- ❌ Плохо: h-full не работает, если у родителя нет высоты -->
<div>
  <div class="h-full bg-blue-500">Не работает</div>
</div>

<!-- ✅ Хорошо: у родителя указана высота -->
<div class="h-64 relative">
  <div class="h-full bg-blue-500">Работает</div>
</div>
```

### ❌ Ошибка 2: Забывают `min-w-0` в flex для truncate

```html
<!-- ❌ Плохо: truncate не работает -->
<div class="flex">
  <div class="flex-1 truncate">
    Очень-очень-длинный-текст
  </div>
</div>

<!-- ✅ Хорошо: min-w-0 позволяет сжиматься -->
<div class="flex">
  <div class="flex-1 min-w-0 truncate">
    Очень-очень-длинный-текст
  </div>
</div>
```

### ❌ Ошибка 3: `w-screen` с горизонтальным скроллом

```html
<!-- ❌ Плохо: может появиться горизонтальный скролл из-за scrollbar -->
<div class="w-screen bg-blue-500">
  На всю ширину экрана
</div>

<!-- ✅ Хорошо: используйте w-full для контейнеров внутри body -->
<div class="w-full bg-blue-500">
  На всю ширину родителя
</div>
```

### ❌ Ошибка 4: `h-screen` на мобильных с адресной строкой

```html
<!-- ❌ Плохо: на мобильных адресная строка "съедает" часть высоты -->
<section class="h-screen">
  Hero-секция
</section>

<!-- ✅ Хорошо: используйте dvh для мобильных -->
<section class="h-dvh">
  Hero-секция корректно работает на мобильных
</section>
```

### ❌ Ошибка 5: `aspect-ratio` без ширины

```html
<!-- ❌ Плохо: aspect-ratio не работает без ширины -->
<div class="aspect-video bg-blue-500">
  Не работает
</div>

<!-- ✅ Хорошо: указываем ширину -->
<div class="aspect-video w-full bg-blue-500">
  Работает
</div>
```

### ❌ Ошибка 6: Фиксированная ширина для адаптивного контента

```html
<!-- ❌ Плохо: на мобильных не влезет -->
<div class="w-[800px]">
  Контент
</div>

<!-- ✅ Хорошо: адаптивная ширина с максимумом -->
<div class="w-full max-w-4xl mx-auto px-4">
  Контент
</div>
```

### ❌ Ошибка 7: Забывают `overflow` с `max-h`

```html
<!-- ❌ Плохо: контент выйдет за пределы, но не будет скролла -->
<div class="max-h-64">
  <!-- Длинный контент -->
</div>

<!-- ✅ Хорошо: добавляем overflow -->
<div class="max-h-64 overflow-y-auto">
  <!-- Длинный контент со скроллом -->
</div>
```

### ❌ Ошибка 8: `size-*` для прямоугольников

```html
<!-- ❌ Плохо: size устанавливает одинаковые width и height -->
<div class="size-64 bg-blue-500">
  Получится квадрат, а не прямоугольник
</div>

<!-- ✅ Хорошо: для прямоугольников используйте w-* и h-* -->
<div class="w-64 h-32 bg-blue-500">
  Прямоугольник 256×128
</div>
```

### ❌ Ошибка 9: `max-w-prose` для UI-элементов

```html
<!-- ❌ Плохо: max-w-prose (65ch) слишком узкий для UI -->
<div class="max-w-prose bg-white p-6 rounded-lg shadow">
  <!-- Карточка с UI-элементами -->
</div>

<!-- ✅ Хорошо: max-w-prose для текста, max-w-{size} для UI -->
<article class="max-w-prose">
  <!-- Статья с длинным текстом -->
</article>

<div class="max-w-md bg-white p-6 rounded-lg shadow">
  <!-- Карточка с UI -->
</div>
```

### ❌ Ошибка 10: Забывают про responsive размеры

```html
<!-- ❌ Плохо: одинаковый размер на всех экранах -->
<div class="w-64 h-64 bg-blue-500">
  Фиксированный размер
</div>

<!-- ✅ Хорошо: адаптивные размеры -->
<div class="w-full sm:w-1/2 lg:w-1/3 h-64 md:h-96 bg-blue-500">
  Адаптивный размер
</div>
```

## 🎯 Что дальше?

Поздравляем! Вы полностью освоили секцию **Layout** — от flexbox и grid до отступов и размеров. Теперь вы можете создавать любые макеты.

### Что вы изучили в секции Layout

- 📐 **Flexbox** — одномерная раскладка
- 🔲 **Grid** — двумерная раскладка
- 📏 **Отступы** — padding, margin, space, gap
- 📐 **Размеры** — width, height, min/max, aspect-ratio

### Следующий шаг

Теперь переходим к основам — установка и конфигурация Tailwind CSS.

**Следующий раздел:** [📦 Установка Tailwind CSS](../basics/installation.md) — научимся подключать Tailwind в различные проекты.

---