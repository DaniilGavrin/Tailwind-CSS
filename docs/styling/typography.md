# 🔤 Типографика в Tailwind CSS

> **Полное руководство по работе с текстом:** от размеров шрифтов до кастомных гарнитур, межстрочных интервалов и адаптивной типографики

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Освоите всю шкалу размеров шрифтов Tailwind
- ✅ Научитесь управлять жирностью, межстрочным интервалом и трекингом
- ✅ Сможете правильно выравнивать и декорировать текст
- ✅ Настроите кастомные шрифты (Google Fonts, локальные)
- ✅ Поймёте принципы иерархии и читаемости
- ✅ Освоите responsive-типографику
- ✅ Избежите типичных ошибок в работе с текстом

## 📏 Размеры шрифтов: `text-{size}`

Tailwind предоставляет **10 предустановленных размеров**, основанных на рем-единицах:

| Класс | Размер | Строка | Когда использовать |
| :-- | :-- | :-- | :-- |
| `text-xs` | 0.75rem (12px) | 1rem | Подписи, метки, бейджи |
| `text-sm` | 0.875rem (14px) | 1.25rem | Второстепенный текст, хелперы |
| `text-base` | 1rem (16px) | 1.5rem | Основной текст (по умолчанию) |
| `text-lg` | 1.125rem (18px) | 1.75rem | Вводные абзацы, подзаголовки |
| `text-xl` | 1.25rem (20px) | 1.75rem | Заголовки разделов |
| `text-2xl` | 1.5rem (24px) | 2rem | Подзаголовки страниц |
| `text-3xl` | 1.875rem (30px) | 2.25rem | Заголовки страниц |
| `text-4xl` | 2.25rem (36px) | 2.5rem | Большие заголовки |
| `text-5xl` | 3rem (48px) | 1 | Hero-секции |
| `text-6xl` | 3.75rem (60px) | 1 | Огромные заголовки |
| `text-7xl` | 4.5rem (72px) | 1 | Дисплейные заголовки |
| `text-8xl` | 6rem (96px) | 1 | Очень крупные акценты |
| `text-9xl` | 8rem (128px) | 1 | Экстремальные размеры |

```html
<!-- Типовая иерархия страницы -->
<h1 class="text-4xl font-bold">Главный заголовок</h1>
<h2 class="text-2xl font-semibold">Подзаголовок</h2>
<h3 class="text-xl font-medium">Заголовок раздела</h3>
<p class="text-base">Обычный текст параграфа.</p>
<small class="text-sm text-gray-500">Подпись или метка времени</small>
```

### Arbitrary значения для размеров

```html
<!-- Точный размер в пикселях -->
<h1 class="text-[42px]">Кастомный размер</h1>

<!-- В rem -->
<p class="text-[1.375rem]">Точный rem</p>
```

## 💪 Жирность шрифта: `font-{weight}`

| Класс | CSS | Визуально |
| :-- | :-- | :-- |
| `font-thin` | `font-weight: 100` | Очень тонкий |
| `font-extralight` | `font-weight: 200` | Extra light |
| `font-light` | `font-weight: 300` | Тонкий |
| `font-normal` | `font-weight: 400` | Обычный (по умолчанию) |
| `font-medium` | `font-weight: 500` | Средний |
| `font-semibold` | `font-weight: 600` | Полужирный |
| `font-bold` | `font-weight: 700` | Жирный |
| `font-extrabold` | `font-weight: 800` | Очень жирный |
| `font-black` | `font-weight: 900` | Чёрный (максимум) |

```html
<p class="font-light">Тонкий текст — для элегантности</p>
<p class="font-normal">Обычный текст — для читаемости</p>
<p class="font-medium">Средний — для акцентов</p>
<p class="font-semibold">Полужирный — для подзаголовков</p>
<p class="font-bold">Жирный — для заголовков</p>
```

> 💡 **Совет:** не все шрифты имеют все начертания. Google Fonts часто ограничивается 4–5 вариантами. Проверяйте доступность перед использованием.

## 📐 Межстрочный интервал: `leading-{value}`

`leading` управляет `line-height` — расстоянием между строками.

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `leading-none` | `line-height: 1` | Без отступов (для заголовков) |
| `leading-tight` | `line-height: 1.25` | Плотный (заголовки) |
| `leading-snug` | `line-height: 1.375` | Умеренно плотный |
| `leading-normal` | `line-height: 1.5` | Нормальный (по умолчанию) |
| `leading-relaxed` | `line-height: 1.625` | Свободный (для длинных текстов) |
| `leading-loose` | `line-height: 2` | Очень свободный |
| `leading-3` ... `leading-10` | Фиксированные rem | Точный контроль |

```html
<!-- Заголовок: плотный интервал -->
<h1 class="text-4xl font-bold leading-tight">
  Заголовок с плотным межстрочным интервалом
</h1>

<!-- Параграф: свободный интервал для читаемости -->
<p class="text-base leading-relaxed max-w-prose">
  Длинный текст с комфортным межстрочным интервалом.
  Чем длиннее абзац, тем важнее свободный leading.
  Это улучшает читаемость и снижает усталость глаз.
</p>
```

> 💡 **Правило:** для заголовков — `leading-tight` или `leading-none`. Для параграфов — `leading-relaxed` или `leading-loose`.

## 🔠 Трекинг (межбуквенный интервал): `tracking-{value}`

| Класс | CSS | Когда использовать |
| :-- | :-- | :-- |
| `tracking-tighter` | `-0.05em` | Крупные заголовки |
| `tracking-tight` | `-0.025em` | Заголовки |
| `tracking-normal` | `0em` | Обычный текст |
| `tracking-wide` | `0.025em` | Подзаголовки |
| `tracking-wider` | `0.05em` | UPPERCASE-подписи |
| `tracking-widest` | `0.1em` | Декоративные элементы |

```html
<!-- Заголовок с узким трекингом — выглядит компактнее -->
<h1 class="text-5xl font-bold tracking-tight">
  Заголовок
</h1>

<!-- Подпись капсом с широким трекингом -->
<span class="text-xs font-semibold uppercase tracking-widest text-gray-500">
  Категория статьи
</span>
```

## 🎯 Выравнивание текста: `text-{align}`

| Класс | CSS |
| :-- | :-- |
| `text-left` | `text-align: left` |
| `text-center` | `text-align: center` |
| `text-right` | `text-align: right` |
| `text-justify` | `text-align: justify` |
| `text-start` | `text-align: start` (с учётом RTL) |
| `text-end` | `text-align: end` (с учётом RTL) |

```html
<p class="text-left">По левому краю (по умолчанию)</p>
<p class="text-center">По центру</p>
<p class="text-right">По правому краю</p>
<p class="text-justify">
  По ширине — текст растягивается на всю строку.
  Используется в книжной вёрстке, но в вебе с осторожностью.
</p>
```

## ✏️ Декорирование текста: `underline`, `line-through`

| Класс | CSS |
| :-- | :-- |
| `underline` | `text-decoration-line: underline` |
| `overline` | `text-decoration-line: overline` |
| `line-through` | `text-decoration-line: line-through` |
| `no-underline` | `text-decoration-line: none` |

### Стиль подчёркивания

| Класс | CSS |
| :-- | :-- |
| `decoration-solid` | Сплошная линия |
| `decoration-double` | Двойная линия |
| `decoration-dotted` | Точечная |
| `decoration-dashed` | Пунктирная |
| `decoration-wavy` | Волнистая (для ошибок) |

### Толщина и отступ

```html
<!-- Толщина -->
<a href="#" class="underline decoration-1">Тонкое подчёркивание</a>
<a href="#" class="underline decoration-2">Среднее</a>
<a href="#" class="underline decoration-4">Толстое</a>

<!-- Отступ от текста -->
<a href="#" class="underline underline-offset-2">С отступом 2px</a>
<a href="#" class="underline underline-offset-4">С отступом 4px</a>
<a href="#" class="underline underline-offset-8">С большим отступом</a>

<!-- Цвет подчёркивания -->
<a href="#" class="underline decoration-blue-500">Синее подчёркивание</a>
```

```html
<!-- Зачёркнутая цена (скидка) -->
<div class="flex items-center gap-2">
  <span class="text-gray-400 line-through">2 990 ₽</span>
  <span class="text-red-500 font-bold">1 990 ₽</span>
</div>
```

## 🔄 Трансформация текста: `uppercase`, `lowercase`, `capitalize`

| Класс | Результат |
| :-- | :-- |
| `uppercase` | `ВСЕ БУКВЫ ЗАГЛАВНЫЕ` |
| `lowercase` | `все буквы строчные` |
| `capitalize` | `Каждое Слово С Заглавной` |
| `normal-case` | `Как в оригинале` |

```html
<!-- Бейдж категории -->
<span class="text-xs font-semibold uppercase tracking-wider text-blue-600">
  Новинка
</span>

<!-- Заголовок с капитализацией -->
<h2 class="text-2xl capitalize">заголовок статьи</h2>
```

> ⚠️ **Важно:** `capitalize` работает только с латиницей. Для кириллицы и других языков используйте CSS `text-transform` с осторожностью или преобразуйте текст на стороне сервера/клиента.

## 📦 Перенос слов и обрезка: `truncate`, `break-*`

### Обрезка с многоточием

```html
<!-- Однострочная обрезка -->
<p class="truncate max-w-xs">
  Очень длинный заголовок, который не помещается в одну строку и будет обрезан с многоточием
</p>
```

`truncate` = `overflow-hidden` + `text-ellipsis` + `whitespace-nowrap`

### Перенос слов

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `break-normal` | `overflow-wrap: normal` | Без переноса |
| `break-words` | `overflow-wrap: break-word` | Перенос по словам |
| `break-all` | `word-break: break-all` | Перенос в любом месте |
| `break-keep` | `word-break: keep-all` | Сохранять слова |

```html
<!-- Длинная ссылка переносится -->
<a href="#" class="break-words text-blue-500">
  https://example.com/very/long/url/that/needs/to/break/properly
</a>

<!-- Код или хеши — перенос в любом месте -->
<code class="break-all text-sm">
  550e8400e29b41d4a716446655440000
</code>
```

### Многострочная обрезка (line-clamp)

```html
<!-- Обрезать после 2 строк -->
<p class="line-clamp-2">
  Очень длинный текст, который будет обрезан после второй строки.
  Остальной текст не будет виден, а в конце появится многоточие.
  Это полезно для карточек с превью контента.
</p>

<!-- 3 строки -->
<p class="line-clamp-3">...</p>

<!-- Без ограничений -->
<p class="line-clamp-none">...</p>
```

## 🔤 Шрифты: `font-{family}`

По умолчанию Tailwind предоставляет три семейства:

| Класс | CSS | Применение |
| :-- | :-- | :-- |
| `font-sans` | `ui-sans-serif, system-ui, ...` | Основной текст, UI |
| `font-serif` | `ui-serif, Georgia, ...` | Статьи, блоги, книги |
| `font-mono` | `ui-monospace, SFMono-Regular, ...` | Код, технические данные |

```html
<p class="font-sans">Основной текст без засечек</p>
<p class="font-serif">Текст с засечками для статей</p>
<code class="font-mono bg-gray-100 px-1">const x = 42;</code>
```

### Подключение кастомных шрифтов

#### Вариант 1: Google Fonts через CDN

```html
<!-- В <head> -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
```

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Inter', 'system-ui', 'sans-serif'],
        'display': ['"Playfair Display"', 'serif'],
      },
    },
  },
}
```

```html
<h1 class="font-display text-5xl">Заголовок с засечками</h1>
<p class="font-sans">Обычный текст с Inter</p>
```

#### Вариант 2: Локальные шрифты

```css
/* styles.css */
@font-face {
  font-family: 'CustomFont';
  src: url('/fonts/custom.woff2') format('woff2');
  font-weight: 400;
  font-display: swap;
}
```

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        'custom': ['CustomFont', 'sans-serif'],
      },
    },
  },
}
```

## 📝 Отступ первой строки: `indent-{size}`

```html
<!-- Красная строка -->
<p class="indent-8">
  Первая строка этого абзаца будет иметь отступ.
  Это классический приём книжной вёрстки.
  Остальные строки начинаются с левого края.
</p>
```

## 📏 Вертикальное выравнивание: `align-{value}`

Работает для инлайновых и inline-block элементов:

| Класс | CSS |
| :-- | :-- |
| `align-baseline` | `vertical-align: baseline` |
| `align-top` | `vertical-align: top` |
| `align-middle` | `vertical-align: middle` |
| `align-bottom` | `vertical-align: bottom` |
| `align-text-top` | `vertical-align: text-top` |
| `align-text-bottom` | `vertical-align: text-bottom` |
| `align-sub` | `vertical-align: sub` |
| `align-super` | `vertical-align: super` |

```html
<!-- Иконка по центру текста -->
<p>
  Текст
  <svg class="inline w-4 h-4 align-middle" viewBox="0 0 24 24">...</svg>
  и иконка
</p>

<!-- Верхний индекс -->
<p>E = mc<sup class="align-super text-xs">2</sup></p>
```

## 🌫️ Белый пробел: `whitespace-{value}`

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `whitespace-normal` | `white-space: normal` | Переносы работают |
| `whitespace-nowrap` | `white-space: nowrap` | Без переносов |
| `whitespace-pre` | `white-space: pre` | Как `<pre>` |
| `whitespace-pre-line` | `white-space: pre-line` | Сохраняет переносы строк |
| `whitespace-pre-wrap` | `white-space: pre-wrap` | Сохраняет всё + переносы |
| `whitespace-break-spaces` | `white-space: break-spaces` | Как pre-wrap + перенос по пробелам |

```html
<!-- Код с сохранением форматирования -->
<pre class="whitespace-pre-wrap bg-gray-100 p-4 rounded">
function hello() {
  console.log("Привет!");
}
</pre>

<!-- Однострочный текст без переносов -->
<div class="whitespace-nowrap overflow-hidden">
  Очень длинная строка, которая не будет переноситься на новую строку
</div>
```

## 📱 Responsive типограграфика

Меняйте размеры и параметры на разных экранах:

```html
<!-- Mobile-first подход -->
<h1 class="text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-bold">
  Адаптивный заголовок
</h1>

<p class="text-sm sm:text-base md:text-lg leading-relaxed">
  Адаптивный параграф с комфортной читаемостью на всех устройствах.
</p>
```

### Clamp для плавной типографики

```html
<!-- Плавное изменение размера от 1.5rem до 3rem -->
<h1 class="text-[clamp(1.5rem,5vw,3rem)] font-bold">
  Плавный заголовок
</h1>
```

## 🎨 Практические паттерны

### 1. 📰 Типовая иерархия статьи

```html
<article class="max-w-prose mx-auto px-4">
  <!-- Категория -->
  <span class="text-xs font-semibold uppercase tracking-wider text-blue-600">
    Технологии
  </span>

  <!-- Заголовок -->
  <h1 class="mt-2 text-4xl font-bold tracking-tight text-gray-900">
    Как правильно использовать типографику в вебе
  </h1>

  <!-- Метаданные -->
  <div class="mt-4 flex items-center gap-2 text-sm text-gray-500">
    <span>Иван Иванов</span>
    <span>·</span>
    <time>5 июня 2026</time>
    <span>·</span>
    <span>7 мин чтения</span>
  </div>

  <!-- Вводный абзац -->
  <p class="mt-6 text-lg text-gray-600 leading-relaxed">
    Типографика — это основа любого интерфейса. Правильно подобранные
    шрифты, размеры и интервалы делают контент читаемым и приятным.
  </p>

  <!-- Подзаголовок -->
  <h2 class="mt-8 text-2xl font-semibold text-gray-900">
    Размеры шрифтов
  </h2>

  <!-- Параграф -->
  <p class="mt-4 text-base text-gray-700 leading-relaxed">
    Tailwind предлагает удобную шкалу размеров от <code class="font-mono text-sm bg-gray-100 px-1">text-xs</code>
    до <code class="font-mono text-sm bg-gray-100 px-1">text-9xl</code>.
  </p>

  <!-- Цитата -->
  <blockquote class="mt-6 border-l-4 border-blue-500 pl-4 italic text-gray-600">
    «Типографика — это одежда языка.»
    <footer class="mt-2 text-sm not-italic text-gray-500">— Эрик Шпикерман</footer>
  </blockquote>
</article>
```

### 2. 🏷️ Карточка с иерархией

```html
<div class="bg-white rounded-xl shadow-md p-6 max-w-sm">
  <span class="text-xs font-semibold uppercase tracking-wider text-purple-600">
    Премиум
  </span>
  <h3 class="mt-2 text-xl font-bold text-gray-900">
    Название продукта
  </h3>
  <p class="mt-2 text-sm text-gray-600 leading-relaxed line-clamp-3">
    Краткое описание продукта, которое может быть длинным и занимать несколько строк.
  </p>
  <div class="mt-4 flex items-baseline gap-2">
    <span class="text-2xl font-bold text-gray-900">2 990 ₽</span>
    <span class="text-sm text-gray-400 line-through">3 990 ₽</span>
  </div>
  <button class="mt-4 w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 rounded-lg">
    Купить
  </button>
</div>
```

### 3. 💻 Блок кода

```html
<div class="bg-gray-900 rounded-lg p-4 overflow-x-auto">
  <div class="flex items-center justify-between mb-3">
    <span class="text-xs font-mono text-gray-400">script.js</span>
    <button class="text-xs text-gray-400 hover:text-white">Копировать</button>
  </div>
  <pre class="text-sm font-mono text-gray-100 leading-relaxed"><code>function greet(name) {
  console.log(`Hello, ${name}!`);
}

greet('World');</code></pre>
</div>
```

### 4. 📊 Статистика с крупной цифрой

```html
<div class="text-center">
  <div class="text-5xl font-bold tracking-tight text-blue-600">
    80K+
  </div>
  <div class="mt-2 text-sm font-medium uppercase tracking-wider text-gray-500">
    Звёзд на GitHub
  </div>
</div>
```

## 📊 Шпаргалка: что когда использовать

| Задача | Классы |
| :-- | :-- |
| Заголовок H1 | `text-4xl font-bold tracking-tight` |
| Заголовок H2 | `text-2xl font-semibold` |
| Заголовок H3 | `text-xl font-medium` |
| Основной текст | `text-base leading-relaxed` |
| Мелкий текст | `text-sm text-gray-600` |
| Подпись | `text-xs uppercase tracking-wider` |
| Ссылка | `text-blue-600 underline underline-offset-2` |
| Код inline | `font-mono text-sm bg-gray-100 px-1` |
| Блок кода | `font-mono text-sm bg-gray-900 text-gray-100` |
| Зачёркнутая цена | `line-through text-gray-400` |
| Обрезка 1 строка | `truncate` |
| Обрезка N строк | `line-clamp-2`, `line-clamp-3` |
| Красная строка | `indent-8` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Слишком много размеров шрифтов на странице

```html
<!-- ❌ Плохо: 8 разных размеров — хаос -->
<h1 class="text-5xl">...</h1>
<h2 class="text-[28px]">...</h2>
<h3 class="text-[19px]">...</h3>
<p class="text-[15px]">...</p>

<!-- ✅ Хорошо: 4-5 размеров из шкалы -->
<h1 class="text-4xl">...</h1>
<h2 class="text-2xl">...</h2>
<h3 class="text-xl">...</h3>
<p class="text-base">...</p>
<small class="text-sm">...</small>
```

### ❌ Ошибка 2: Забывают про `max-w-prose` для длинных текстов

```html
<!-- ❌ Плохо: строка на весь экран — тяжело читать -->
<p class="text-base">Очень длинный текст на всю ширину экрана...</p>

<!-- ✅ Хорошо: комфортная ширина 65-75 символов -->
<p class="text-base leading-relaxed max-w-prose">
  Длинный текст с комфортной шириной строки.
</p>
```

### ❌ Ошибка 3: `text-justify` без hyphens

```html
<!-- ❌ Плохо: большие пробелы между словами -->
<p class="text-justify">Длинный текст...</p>

<!-- ✅ Хорошо: добавить переносы -->
<p class="text-justify hyphens-auto">Длинный текст...</p>
```

### ❌ Ошибка 4: Неподходящий leading для заголовков

```html
<!-- ❌ Плохо: заголовок с обычным leading выглядит рыхло -->
<h1 class="text-5xl leading-relaxed">Заголовок</h1>

<!-- ✅ Хорошо: плотный leading для крупных заголовков -->
<h1 class="text-5xl leading-tight">Заголовок</h1>
```

### ❌ Ошибка 5: Игнорируют `font-display: swap`

```css
/* ❌ Плохо: текст не виден, пока шрифт грузится */
@font-face {
  font-family: 'Custom';
  src: url('custom.woff2');
}

/* ✅ Хорошо: сразу показываем fallback */
@font-face {
  font-family: 'Custom';
  src: url('custom.woff2');
  font-display: swap;
}
```

## 🎯 Что дальше?

Теперь вы мастерски владеете типографикой! Но визуальный стиль — это не только текст. Следующий важный аспект — **фоны и фоновые изображения**.

**Следующий шаг:** [🖼️ Фоны в Tailwind CSS](backgrounds.md) — изучим работу с фонами, изображениями, градиентами и эффектами размытия.

---

> 💬 **Упражнение:** сверстайте карточку блога с категорией, заголовком, мета-данными (автор, дата), вводным абзацем (обрезанным до 3 строк) и кнопкой «Читать далее». Используйте только типографические утилиты Tailwind!