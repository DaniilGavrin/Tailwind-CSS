# 🖼️ Фоны в Tailwind CSS

> **Полное руководство по работе с фонами:** от простых цветов до фоновых изображений, градиентов, паттернов и эффектов размытия

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Освоите все способы задания фона: цвета, изображения, градиенты
- ✅ Научитесь управлять размером, позицией и повторением фоновых изображений
- ✅ Поймёте разницу между `bg-cover` и `bg-contain`
- ✅ Создадите красивые hero-секции с изображениями
- ✅ Освоите эффекты размытия и затемнения
- ✅ Настроите кастомные фоновые изображения через конфиг
- ✅ Избежите типичных ошибок при работе с фонами

## 🎨 Цвет фона: `bg-{color}`

Базовый способ — использовать цвета из палитры Tailwind (подробнее в разделе [Цвета](../styling/colors.md)):

```html
<div class="bg-white">Белый фон</div>
<div class="bg-gray-50">Очень светлый серый</div>
<div class="bg-gray-100">Светло-серый</div>
<div class="bg-gray-900">Почти чёрный</div>
<div class="bg-blue-500">Синий</div>
<div class="bg-red-50">Светло-красный (для алертов)</div>
```

### Прозрачный фон

```html
<div class="bg-transparent">Прозрачный (по умолчанию)</div>
<div class="bg-white/50">Белый с 50% прозрачности</div>
<div class="bg-black/80">Чёрный с 80% непрозрачности</div>
```

## 🖼️ Фоновые изображения

### Подключение через arbitrary values

```html
<div class="bg-[url('/images/hero.jpg')]">
  Фон с изображением
</div>

<!-- С кавычками внутри URL -->
<div class="bg-[url('https://example.com/image.png')]">
  Внешнее изображение
</div>

<!-- SVG inline -->
<div class="bg-[url('data:image/svg+xml,...')]">
  SVG фон
</div>
```

### Через конфигурацию (рекомендуется)

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      backgroundImage: {
        'hero-pattern': "url('/images/hero-pattern.svg')",
        'footer-texture': "url('/images/footer-texture.png')",
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'gradient-conic': 'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',
      },
    },
  },
}
```

```html
<div class="bg-hero-pattern">Использование кастомного фона</div>
<div class="bg-footer-texture">Текстура в футере</div>
```

## 📐 Размер фона: `bg-{size}`

Управляет тем, как изображение масштабируется внутри контейнера:

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `bg-auto` | `background-size: auto` | Оригинальный размер |
| `bg-cover` | `background-size: cover` | Заполняет контейнер, обрезая края |
| `bg-contain` | `background-size: contain` | Вписывается целиком, может оставить пустоты |

```html
<!-- Cover: изображение заполняет весь блок, часть может быть обрезана -->
<div class="bg-[url('/photo.jpg')] bg-cover h-64">
  Идеально для hero-секций
</div>

<!-- Contain: изображение видно целиком, могут быть пустые полосы -->
<div class="bg-[url('/logo.svg')] bg-contain bg-no-repeat h-64">
  Логотип целиком виден
</div>

<!-- Auto: оригинальный размер (может не поместиться) -->
<div class="bg-[url('/pattern.png')] bg-auto bg-repeat">
  Паттерн в оригинальном размере
</div>
```

### Arbitrary значения

```html
<!-- Точные размеры -->
<div class="bg-[url('/icon.svg')] bg-[length:32px_32px] bg-no-repeat">
  Иконка 32×32
</div>

<!-- Процентные значения -->
<div class="bg-[url('/photo.jpg')] bg-[length:150%_auto]">
  Увеличенное изображение
</div>
```

> 💡 **Когда что использовать:**
> - `bg-cover` — для фотографий, hero-секций, карточек
> - `bg-contain` — для логотипов, иконок, когда важно видеть изображение целиком
> - `bg-auto` — для паттернов и текстур

## 🎯 Позиционирование: `bg-{position}`

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `bg-bottom` | `background-position: bottom` | Снизу |
| `bg-center` | `background-position: center` | По центру |
| `bg-left` | `background-position: left` | Слева |
| `bg-left-bottom` | `background-position: left bottom` | Слева снизу |
| `bg-left-top` | `background-position: left top` | Слева сверху |
| `bg-right` | `background-position: right` | Справа |
| `bg-right-bottom` | `background-position: right bottom` | Справа снизу |
| `bg-right-top` | `background-position: right top` | Справа сверху |
| `bg-top` | `background-position: top` | Сверху |

```html
<!-- Фото с фокусом на лице (сверху) -->
<div class="bg-[url('/portrait.jpg')] bg-cover bg-top h-64">
  Портрет
</div>

<!-- Логотип по центру -->
<div class="bg-[url('/logo.svg')] bg-contain bg-center bg-no-repeat h-32">
  Логотип
</div>

<!-- Декоративный элемент в правом верхнем углу -->
<div class="bg-[url('/decoration.svg')] bg-right-top bg-no-repeat">
  Контент
</div>
```

### Arbitrary позиционирование

```html
<!-- Точные проценты -->
<div class="bg-[url('/photo.jpg')] bg-cover bg-[position:20%_30%]">
  Смещение к конкретному месту фото
</div>

<!-- В пикселях -->
<div class="bg-[url('/icon.svg')] bg-[position:16px_16px] bg-no-repeat">
  Отступ 16px от левого верхнего угла
</div>
```

## 🔁 Повторение: `bg-repeat`

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `bg-repeat` | `background-repeat: repeat` | По обеим осям (по умолчанию) |
| `bg-no-repeat` | `background-repeat: no-repeat` | Без повторения |
| `bg-repeat-x` | `background-repeat: repeat-x` | Только по горизонтали |
| `bg-repeat-y` | `background-repeat: repeat-y` | Только по вертикали |
| `bg-repeat-round` | `background-repeat: round` | Масштабируется для заполнения |
| `bg-repeat-space` | `background-repeat: space` | Равные промежутки без обрезки |

```html
<!-- Паттерн на весь экран -->
<div class="bg-[url('/pattern.png')] bg-repeat min-h-screen">
  Фоновый паттерн
</div>

<!-- Горизонтальная полоса декоративных элементов -->
<div class="bg-[url('/dots.svg')] bg-repeat-x bg-center h-8">
  Декоративная полоса
</div>

<!-- Одно изображение без повторения -->
<div class="bg-[url('/hero.jpg')] bg-no-repeat bg-cover">
  Hero-секция
</div>
```

## 📌 Прикрепление: `bg-{attachment}`

Управляет тем, как фон ведёт себя при прокрутке:

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `bg-fixed` | `background-attachment: fixed` | Фиксирован относительно viewport |
| `bg-local` | `background-attachment: local` | Фиксирован относительно содержимого |
| `bg-scroll` | `background-attachment: scroll` | Прокручивается с элементом (по умолчанию) |

```html
<!-- Параллакс-эффект: фон остаётся на месте при прокрутке -->
<div class="bg-[url('/landscape.jpg')] bg-fixed bg-cover bg-center h-screen">
  <div class="flex items-center justify-center h-full text-white text-4xl font-bold">
    Параллакс
  </div>
</div>

<!-- Прокручивается вместе с контентом -->
<div class="bg-[url('/pattern.png')] bg-scroll">
  Обычный фон
</div>
```

> ⚠️ **Важно:** `bg-fixed` может вызывать проблемы с производительностью на мобильных устройствах и часто отключается в iOS Safari. Используйте с осторожностью.

## 🎭 Background origin и clip

### Origin: откуда считается фон

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `bg-origin-border` | `background-origin: border-box` | От края границы |
| `bg-origin-padding` | `background-origin: padding-box` | От края padding (по умолчанию) |
| `bg-origin-content` | `background-origin: content-box` | От края контента |

### Clip: где обрезается фон

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `bg-clip-border` | `background-clip: border-box` | Включая границу |
| `bg-clip-padding` | `background-clip: padding-box` | До padding |
| `bg-clip-content` | `background-clip: content-box` | Только контент |
| `bg-clip-text` | `background-clip: text` | Только внутри текста |

```html
<!-- Градиентный текст -->
<h1 class="text-6xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-purple-600">
  Градиентный текст
</h1>
```

## 🌫️ Эффекты размытия и затемнения

### Backdrop blur (размытие заднего плана)

```html
<!-- Стеклянный эффект (glassmorphism) -->
<div class="relative h-96 bg-[url('/photo.jpg')] bg-cover">
  <div class="absolute inset-0 bg-white/30 backdrop-blur-md">
    <div class="p-8">
      <h2 class="text-2xl font-bold">Стеклянная карточка</h2>
      <p>Контент поверх размытого фона</p>
    </div>
  </div>
</div>
```

Размеры размытия:

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

### Затемнение через overlay

```html
<!-- Затемнение для читаемости текста поверх фото -->
<div class="relative h-96 bg-[url('/photo.jpg')] bg-cover">
  <!-- Overlay -->
  <div class="absolute inset-0 bg-black/50"></div>

  <!-- Контент -->
  <div class="relative z-10 flex items-center justify-center h-full text-white">
    <h2 class="text-4xl font-bold">Читаемый заголовок</h2>
  </div>
</div>
```

### Градиентный overlay

```html
<!-- Градиент от прозрачного к чёрному снизу -->
<div class="relative h-96 bg-[url('/photo.jpg')] bg-cover">
  <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent"></div>

  <div class="relative z-10 flex items-end h-full p-6">
    <h2 class="text-3xl font-bold text-white">Заголовок поверх фото</h2>
  </div>
</div>
```

## 🌈 Градиенты как фон

Подробно про градиенты — в разделе [Цвета](../styling/colors.md#градиенты). Краткая сводка:

```html
<!-- Линейный градиент -->
<div class="bg-gradient-to-r from-blue-500 to-purple-600 h-32">
  Линейный
</div>

<!-- Трёхцветный градиент -->
<div class="bg-gradient-to-br from-pink-500 via-red-500 to-yellow-500 h-32">
  Трёхцветный
</div>

<!-- Радиальный градиент -->
<div class="bg-radial from-blue-500 to-purple-600 h-32">
  Радиальный
</div>

<!-- Конический градиент -->
<div class="bg-conic from-red-500 via-yellow-500 to-green-500 h-32">
  Конический
</div>
```

### Градиент + изображение

```html
<!-- Градиент поверх изображения -->
<div class="bg-[url('/photo.jpg')] bg-cover">
  <div class="bg-gradient-to-r from-blue-600/80 to-purple-600/80 h-64">
    <div class="flex items-center justify-center h-full text-white text-2xl font-bold">
      Градиент поверх фото
    </div>
  </div>
</div>
```

## 🎨 SVG-паттерны и текстуры

### Inline SVG в CSS

```html
<div class="bg-[url('data:image/svg+xml,%3Csvg%20...')] bg-repeat">
  SVG паттерн
</div>
```

### Через конфиг

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      backgroundImage: {
        'dots': "url(\"data:image/svg+xml,%3Csvg width='20' height='20' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='2' cy='2' r='1' fill='%23cbd5e1'/%3E%3C/svg%3E\")",
        'grid': "url(\"data:image/svg+xml,%3Csvg width='40' height='40' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 0h40v40H0z' fill='none' stroke='%23e5e7eb'/%3E%3C/svg%3E\")",
      },
    },
  },
}
```

```html
<div class="bg-dots bg-repeat min-h-screen">
  Фон с точками
</div>

<div class="bg-grid bg-repeat min-h-screen">
  Фон с сеткой
</div>
```

### Готовые ресурсы для паттернов

- 🌐 [Hero Patterns](https://heropatterns.com/) — коллекция SVG-паттернов
- 🌐 [Transparent Textures](https://www.transparenttextures.com/) — текстуры
- 🌐 [Patternico](https://patternico.com/) — генератор паттернов
- 🌐 [Haikei](https://haikei.app/) — генератор SVG-фонов

## 📱 Responsive фоны

Меняйте фоны на разных экранах:

```html
<!-- Мобильные: одно фото -->
<!-- Десктоп: другое фото -->
<div class="bg-[url('/mobile-hero.jpg')] md:bg-[url('/desktop-hero.jpg')] bg-cover bg-center h-96">
  Адаптивный фон
</div>

<!-- Мобильные: паттерн -->
<!-- Десктоп: сплошной цвет -->
<div class="bg-[url('/pattern.png')] md:bg-blue-500 min-h-screen">
  Адаптивный фон
</div>
```

## 🎨 Практические паттерны

### 1. 🎬 Hero-секция с фото и затемнением

```html
<section class="relative h-[600px] bg-[url('/hero.jpg')] bg-cover bg-center">
  <!-- Затемнение -->
  <div class="absolute inset-0 bg-gradient-to-b from-black/60 to-black/30"></div>

  <!-- Контент -->
  <div class="relative z-10 flex flex-col items-center justify-center h-full text-center text-white px-4">
    <h1 class="text-5xl md:text-6xl font-bold mb-4">
      Добро пожаловать
    </h1>
    <p class="text-xl md:text-2xl text-gray-200 max-w-2xl">
      Создавайте красивые интерфейсы с Tailwind CSS
    </p>
    <button class="mt-8 bg-white text-gray-900 font-semibold px-8 py-3 rounded-lg hover:bg-gray-100 transition">
      Начать
    </button>
  </div>
</section>
```

### 2. 🪟 Glassmorphism карточка

```html
<div class="relative h-96 bg-gradient-to-br from-purple-500 via-pink-500 to-orange-500">
  <!-- Декоративные круги -->
  <div class="absolute top-10 left-10 w-32 h-32 bg-yellow-300 rounded-full blur-2xl"></div>
  <div class="absolute bottom-10 right-10 w-40 h-40 bg-blue-400 rounded-full blur-2xl"></div>

  <!-- Стеклянная карточка -->
  <div class="absolute inset-0 flex items-center justify-center">
    <div class="bg-white/20 backdrop-blur-lg border border-white/30 rounded-2xl p-8 shadow-2xl max-w-md">
      <h2 class="text-2xl font-bold text-white mb-4">Glassmorphism</h2>
      <p class="text-white/90">
        Современный эффект матового стекла с размытием заднего плана.
      </p>
    </div>
  </div>
</div>
```

### 3. 📄 Страница с декоративным фоном

```html
<div class="min-h-screen bg-gray-50">
  <!-- Декоративные элементы -->
  <div class="fixed top-0 left-0 w-96 h-96 bg-purple-300 rounded-full mix-blend-multiply filter blur-3xl opacity-30 -translate-x-1/2 -translate-y-1/2"></div>
  <div class="fixed top-0 right-0 w-96 h-96 bg-yellow-300 rounded-full mix-blend-multiply filter blur-3xl opacity-30 translate-x-1/2 -translate-y-1/2"></div>
  <div class="fixed bottom-0 left-1/2 w-96 h-96 bg-pink-300 rounded-full mix-blend-multiply filter blur-3xl opacity-30 translate-x-1/2 translate-y-1/2"></div>

  <!-- Контент -->
  <div class="relative z-10 max-w-4xl mx-auto py-16 px-4">
    <h1 class="text-4xl font-bold text-gray-900 mb-8">
      Страница с декоративным фоном
    </h1>
    <div class="bg-white/80 backdrop-blur-sm rounded-xl shadow-xl p-8">
      <p>Контент на полупрозрачной карточке</p>
    </div>
  </div>
</div>
```

### 4. 🎴 Карточка товара с изображением

```html
<div class="bg-white rounded-xl shadow-lg overflow-hidden max-w-sm">
  <!-- Изображение -->
  <div class="relative h-64 bg-[url('/product.jpg')] bg-cover bg-center">
    <!-- Бейдж -->
    <span class="absolute top-4 left-4 bg-red-500 text-white text-xs font-bold px-2 py-1 rounded">
      -30%
    </span>
    <!-- Градиент снизу для плавного перехода -->
    <div class="absolute inset-x-0 bottom-0 h-20 bg-gradient-to-t from-white to-transparent"></div>
  </div>

  <!-- Контент -->
  <div class="p-6">
    <h3 class="text-xl font-bold text-gray-900">Название товара</h3>
    <p class="mt-2 text-gray-600 text-sm">Краткое описание товара</p>
    <div class="mt-4 flex items-baseline gap-2">
      <span class="text-2xl font-bold text-gray-900">2 990 ₽</span>
      <span class="text-sm text-gray-400 line-through">4 270 ₽</span>
    </div>
    <button class="mt-4 w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 rounded-lg transition">
      В корзину
    </button>
  </div>
</div>
```

### 5. 🎨 Секция с паттерном

```html
<section class="relative py-20 bg-blue-600 overflow-hidden">
  <!-- SVG паттерн поверх цвета -->
  <div class="absolute inset-0 opacity-10 bg-[url('data:image/svg+xml,...')] bg-repeat"></div>

  <!-- Контент -->
  <div class="relative z-10 max-w-4xl mx-auto px-4 text-center text-white">
    <h2 class="text-4xl font-bold mb-4">Секция с паттерном</h2>
    <p class="text-xl text-blue-100">
      Паттерн добавляет текстуру и глубину фону
    </p>
  </div>
</section>
```

## 📊 Шпаргалка: что когда использовать

| Задача | Классы |
| :-- | :-- |
| Цвет фона | `bg-blue-500` |
| Прозрачный цвет | `bg-blue-500/50` |
| Фоновое изображение | `bg-[url('/img.jpg')]` |
| Изображение на весь блок | `bg-cover bg-center` |
| Изображение целиком | `bg-contain bg-center bg-no-repeat` |
| Паттерн | `bg-repeat` |
| Параллакс | `bg-fixed` |
| Градиент | `bg-gradient-to-r from-... to-...` |
| Стеклянный эффект | `bg-white/30 backdrop-blur-md` |
| Затемнение поверх фото | `bg-black/50` |
| Градиентный текст | `bg-clip-text text-transparent bg-gradient-to-r` |
| Позиция фона | `bg-top`, `bg-center`, `bg-[position:20%_30%]` |
| Размер фона | `bg-[length:32px_32px]` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: `bg-cover` без `bg-center`

```html
<!-- ❌ Плохо: изображение может быть обрезано некрасиво -->
<div class="bg-[url('/photo.jpg')] bg-cover h-64">...</div>

<!-- ✅ Хорошо: центрирование даёт предсказуемый результат -->
<div class="bg-[url('/photo.jpg')] bg-cover bg-center h-64">...</div>
```

### ❌ Ошибка 2: Фоновое изображение без высоты

```html
<!-- ❌ Плохо: блок схлопнется, фона не будет видно -->
<div class="bg-[url('/photo.jpg')] bg-cover">...</div>

<!-- ✅ Хорошо: указана высота -->
<div class="bg-[url('/photo.jpg')] bg-cover h-64">...</div>
```

### ❌ Ошибка 3: `bg-fixed` на мобильных

```html
<!-- ❌ Плохо: на iOS может не работать или тормозить -->
<div class="bg-[url('/photo.jpg')] bg-fixed bg-cover h-screen">...</div>

<!-- ✅ Хорошо: используем только на десктопе -->
<div class="bg-[url('/photo.jpg')] md:bg-fixed bg-cover bg-scroll h-screen">...</div>
```

### ❌ Ошибка 4: Текст на фото без overlay

```html
<!-- ❌ Плохо: текст может сливаться с фото -->
<div class="bg-[url('/photo.jpg')] bg-cover h-64">
  <h2 class="text-white text-4xl">Заголовок</h2>
</div>

<!-- ✅ Хорошо: overlay для читаемости -->
<div class="relative bg-[url('/photo.jpg')] bg-cover h-64">
  <div class="absolute inset-0 bg-black/50"></div>
  <h2 class="relative z-10 text-white text-4xl">Заголовок</h2>
</div>
```

### ❌ Ошибка 5: Забывают `bg-no-repeat` для одиночных изображений

```html
<!-- ❌ Плохо: изображение может повториться -->
<div class="bg-[url('/logo.svg')] bg-contain h-32">...</div>

<!-- ✅ Хорошо: явно запрещаем повторение -->
<div class="bg-[url('/logo.svg')] bg-contain bg-no-repeat h-32">...</div>
```

### ❌ Ошибка 6: Тяжёлые изображения без оптимизации

```html
<!-- ❌ Плохо: 5MB JPEG на фон -->
<div class="bg-[url('/huge-photo.jpg')] bg-cover h-96">...</div>

<!-- ✅ Хорошо: оптимизированное изображение (WebP, сжатие, ресайз) -->
<div class="bg-[url('/optimized-photo.webp')] bg-cover h-96">...</div>
```

> 💡 **Совет:** используйте WebP/AVIF, сжимайте через [Squoosh](https://squoosh.app/) или [TinyPNG](https://tinypng.com/), ресайзьте до нужного размера.

## 🎯 Что дальше?

Теперь вы полностью владеете фонами! Следующий важный аспект визуального стиля — **границы и обводки**.

**Следующий шаг:** [🔲 Границы в Tailwind CSS](borders.md) — изучим работу с границами, радиусами скругления, ring-эффектами и разделителями.

---

> 💬 **Упражнение:** создайте hero-секцию с фоновым изображением, градиентным overlay, заголовком, подзаголовком и кнопкой. Добавьте glassmorphism-карточку поверх с размытием фона. Убедитесь, что всё читаемо и красиво!