# 📘 Tailwind CSS Guide — Полная версия

> Автоматически сгенерированная версия всей документации
> Дата генерации: 29.06.2026 01:11:04
> Источник: https://github.com/DaniilGavrin/tailwind-css-guide

# 📘 Tailwind CSS Guide

> **Utility-first CSS фреймворк для быстрого создания современных интерфейсов**

## 🎯 Что такое Tailwind CSS?

### 💡 Ключевые преимущества

- ⚡ **Быстрая разработка** — не нужно переключаться между HTML и CSS файлами

- 🎨 **Консистентный дизайн** — встроенная система цветов, отступов и типографики

- 📱 **Адаптивность из коробки** — мобильная адаптация через префиксы (`sm:`, `md:`, `lg:`)

- 🌙 **Dark mode** — поддержка тёмной темы одной директивой

- 📦 **Маленький размер** — PurgeCSS удаляет неиспользуемые классы

- 🔧 **Полная кастомизация** — настройте всё под свой дизайн-систему

## 🚀 Пример использования

Посмотрите, как легко создать карточку на Tailwind:

```html
<div class="max-w-sm rounded-xl overflow-hidden shadow-lg bg-white p-6">
  <img class="w-full h-48 object-cover rounded-lg" src="image.jpg" alt="Превью">
  <h2 class="text-xl font-bold text-gray-800 mt-4 mb-2">Заголовок карточки</h2>
# ... (ещё 4 строк) ...
    Подробнее
  </button>
</div>
```

**Результат:** готовая карточка с изображением, текстом и кнопкой — без единой строки кастомного CSS!

### 🟢 Новички

- Изучите основы Tailwind CSS за 1-2 часа

- Поймёте философию utility-first подхода

- Начнёте верстать адаптивные макеты без боли

### 🟡 Уверенные пользователи

- Освоите продвинутые техники: Flexbox, Grid, анимации

- Настроите dark mode и кастомные темы

- Интегрируете Tailwind в React, Vue, Next.js

### 🔴 Профи

- Создадите собственные плагины и утилиты

- Оптимизируете production build

- Настроите дизайн-систему для команды

## 📚 Структура документации

| Раздел | Что внутри | Уровень |
| :-- | :-- | :-- |
| **[Основы](basics/introduction.md)** | Установка, конфигурация, первые шаги | 🟢 Новичок |
| **[Макет](layout/flexbox.md)** | Flexbox, Grid, отступы, размеры | 🟢 Новичок |
| **[Стили](styling/colors.md)** | Цвета, типографика, фоны, границы | 🟡 Уверенный |
| **[Адаптивность](responsive/breakpoints.md)** | Breakpoints, dark mode, состояния | 🟡 Уверенный |
| **[Продвинутое](advanced/customization.md)** | Кастомизация, плагины, директивы | 🔴 Профи |
| **[Интеграции](integrations/react.md)** | React, Vue, Next.js | 🔴 Профи |

## 🚀 Быстрый старт

### Вариант 1: Через CDN (для тестов)

### Вариант 2: Через npm (для продакшена)

```bash
# Установка
npm install -D tailwindcss
npx tailwindcss init

# Создайте tailwind.config.js
```

Затем в вашем CSS файле:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### Вариант 3: Через Play CDN (для экспериментов)

```html
<script src="https://cdn.tailwindcss.com?plugins=forms,typography"></script>
```

## 🎓 Что вы изучите

После прохождения этого гайда вы сможете:

- ✅ Создавать адаптивные макеты за минуты

- ✅ Настраивать дизайн-систему под проект

- ✅ Работать с тёмной темой и состояниями

- ✅ Интегрировать Tailwind в любой фреймворк

- ✅ Оптимизировать CSS для продакшена

- ✅ Создавать собственные плагины

# 🟢 Раздел: Basics

# ⚙️ Конфигурация Tailwind CSS

## 📁 Что такое `tailwind.config.js`

Это **главный конфигурационный файл** Tailwind CSS. Он говорит Tailwind:

- **Какие файлы сканировать** (чтобы генерировать только нужные классы)

- **Какую тему использовать** (цвета, шрифты, отступы)

- **Какие плагины подключить** (формы, типографика и т.д.)

- **Как себя вести** (dark mode, префиксы, важность)

### Где находится файл

```
my-project/
├── src/
├── tailwind.config.js   ← Вот он!
├── postcss.config.js
├── package.json
└── ...
```

### Как создать файл

Если вы забыли создать его при установке:

```bash
npx tailwindcss init
```

Или с PostCSS конфигом:

```bash
npx tailwindcss init -p
```

## 📋 Структура конфигурации

Полный конфиг выглядит так:

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  // 1. Какие файлы сканировать
# ... (ещё 22 строк) ...
  // 8. Встроенные утилиты
  corePlugins: {},
}
```

Разберём каждую секцию подробно.

## 📂 Секция `content` — САМАЯ ВАЖНАЯ

**Это самая важная секция!** От неё зависит, будет ли Tailwind вообще работать.

### Что делает `content`

Tailwind сканирует файлы, указанные в `content`, и генерирует CSS **только для тех классов, которые реально используются** в вашем коде.

```
1. Вы указали: content: ['./src/**/*.html']
2. Tailwind сканирует все HTML файлы в src/
3. Находит классы: bg-blue-500, p-4, rounded
4. Генерирует CSS только для этих классов
5. Итоговый CSS весит 5-15 KB вместо 3-4 MB
```

### Базовая настройка

```js
// tailwind.config.js
module.exports = {
  content: [
    './src/**/*.{html,js,jsx,ts,tsx,vue,svelte}',
  ],
}
```

### Для разных фреймворков

#### HTML / Vanilla JS

```js
module.exports = {
  content: [
    './*.html',
    './src/**/*.{html,js}',
  ],
}
```

#### React / Vite

```js
module.exports = {
  content: [
    './index.html',
    './src/**/*.{js,ts,jsx,tsx}',
  ],
}
```

#### Vue / Vite

```js
module.exports = {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts}',
  ],
}
```

#### Next.js (App Router)

```js
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx}',
# ... (ещё 1 строк) ...
    './components/**/*.{js,ts,jsx,tsx}',
  ],
}
```

#### Next.js (Pages Router)

```js
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
  ],
}
```

#### Nuxt 3

```js
module.exports = {
  content: [
    './components/**/*.{vue,js,ts}',
# ... (ещё 3 строк) ...
    './app.vue',
  ],
}
```

#### Svelte / SvelteKit

```js
module.exports = {
  content: [
    './src/**/*.{html,js,svelte,ts}',
  ],
}
```

#### Laravel / Blade

```js
module.exports = {
  content: [
    './resources/**/*.blade.php',
# ... (ещё 1 строк) ...
    './resources/**/*.vue',
  ],
}
```

#### WordPress

```js
module.exports = {
  content: [
    './**/*.php',
    './src/**/*.{js,jsx,ts,tsx}',
  ],
}
```

#### Astro

```js
module.exports = {
  content: [
    './src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}',
  ],
}
```

### Исключения

Можно исключить файлы из сканирования с помощью `!`:

```js
module.exports = {
  content: {
    files: [
# ... (ещё 3 строк) ...
    ],
  },
}
```

### ⚠️ Что будет, если не настроить `content`

**Вариант 1:** CSS будет пустым — Tailwind не найдёт ни одного класса.

**Вариант 2:** CSS будет содержать все 50 000+ классов — размер 3-4 MB.

**Оба варианта — плохо!** Всегда настраивайте `content`.

## 🎨 Секция `theme` — базовое расширение

Тема определяет вашу дизайн-систему: цвета, шрифты, отступы и т.д.

### Расширение темы (рекомендуется)

Добавляет свои значения **к стандартным**:

```js
module.exports = {
  theme: {
    extend: {
# ... (ещё 6 строк) ...
    },
  },
}
```

Теперь можно использовать:

```html
<div class="bg-brand text-white">Брендовый цвет</div>
<h1 class="font-display">Заголовок</h1>
```

### Полная замена темы

Заменяет стандартные значения **полностью**:

```js
module.exports = {
  theme: {
    // Без extend — полная замена
# ... (ещё 3 строк) ...
    },
  },
}
```

> ⚠️ **Важно:** при полной замене вы теряете все стандартные цвета (blue, red, green и т.д.). Используйте только если действительно нужно.

### Что можно настроить в теме

| Свойство | Что определяет |
| :-- | :-- |
| `colors` | Цветовая палитра |
| `spacing` | Отступы (padding, margin, gap) |
| `fontSize` | Размеры шрифтов |
| `fontFamily` | Шрифты |
| `screens` | Breakpoints для responsive |
| `borderRadius` | Радиусы скругления |
| `boxShadow` | Тени |
| `animation` | Анимации |
| `transitionDuration` | Длительность transition |

> 💡 **Подробнее:** продвинутая работа с темой разбирается в разделе [Кастомизация](../advanced/customization.md).

## 🌙 Секция `darkMode` — тёмная тема

Управляет тем, как работает dark mode:

### Режим `class` (рекомендуется)

Тема переключается добавлением класса `dark` к `<html>`:

```js
module.exports = {
  darkMode: 'class',
}
```

### Режим `media`

Тема переключается автоматически по системным настройкам:

```js
module.exports = {
  darkMode: 'media', // по умолчанию
}
```

```html
<!-- Автоматически следует системным настройкам -->
<div class="bg-white dark:bg-gray-900">...</div>
```

### Сравнение режимов

| Режим | Плюсы | Минусы |
| :-- | :-- | :-- |
| `class` | Полный контроль, можно сохранить выбор | Нужен JavaScript |
| `media` | Работает из коробки | Нельзя переключить вручную |

> 💡 **Подробнее:** работа с dark mode разбирается в разделе [Dark Mode](../responsive/dark-mode.md).

## 🔌 Секция `plugins` — подключение плагинов

Плагины добавляют новую функциональность в Tailwind:

```js
module.exports = {
  plugins: [
    require('@tailwindcss/forms'),           // Улучшенные формы
# ... (ещё 2 строк) ...
    require('@tailwindcss/container-queries'), // Container queries
  ],
}
```

### Установка плагинов

```bash
npm install -D @tailwindcss/forms @tailwindcss/typography
```

### Что дают плагины

| Плагин | Что добавляет |
| :-- | :-- |
| `@tailwindcss/forms` | Красивые стили для input, select, checkbox |
| `@tailwindcss/typography` | Класс `prose` для стилизации HTML-контента |
| `@tailwindcss/aspect-ratio` | Утилиты для aspect ratio |
| `@tailwindcss/container-queries` | Container queries |

> 💡 **Подробнее:** создание собственных плагинов разбирается в разделе [Плагины](../advanced/plugins.md).

## ⚡ Секция `important` — важность селекторов

Добавляет `!important` ко всем утилитам Tailwind:

```js
module.exports = {
  important: true,
}
```

### Когда использовать

**Хорошие случаи:**

- Интеграция Tailwind в существующий проект с конфликтующими стилями

- Работа с CSS-фреймворками (Bootstrap, Foundation)

**Плохие случаи:**

- Новые проекты (лучше решить конфликты правильно)

- Когда можно использовать специфичные селекторы

### Альтернатива: ID-селектор

Можно указать ID, к которому будут привязаны стили:

```js
module.exports = {
  important: '#app',
}
```

Все утилиты будут сгенерированы как `#app .bg-blue-500`, что повышает их специфичность без `!important`.

## 🔤 Секция `prefix` — префиксы классов

Добавляет префикс ко всем классам Tailwind:

```js
module.exports = {
  prefix: 'tw-',
}
```

```html
<!-- Было -->
<div class="bg-blue-500 p-4 rounded">

<!-- Стало -->
<div class="tw-bg-blue-500 tw-p-4 tw-rounded">
```

### Когда использовать

- Интеграция Tailwind в проект с существующими CSS-классами

- Избежание конфликтов имён

> ⚠️ **Не рекомендуется** для новых проектов — это усложняет код.

## 🎛 Секция `corePlugins` — управление утилитами

Позволяет **отключить** встроенные утилиты:

### Отключение всех утилит

```js
module.exports = {
  corePlugins: {
    // Пустой объект — все утилиты отключены
  },
}
```

### Отключение конкретных утилит

```js
module.exports = {
  corePlugins: {
    float: false,           // Отключаем float
# ... (ещё 1 строк) ...
    visibility: false,      // Отключаем visibility
  },
}
```

### Отключение Preflight (CSS Reset)

```js
module.exports = {
  corePlugins: {
    preflight: false,
  },
}
```

> ⚠️ **Осторожно:** Preflight сбрасывает стандартные стили браузера. Без него могут сломаться существующие стили.

### Когда отключать утилиты

- **Preflight** — при интеграции в существующий проект

- **Конкретные утилиты** — если они конфликтуют с вашим CSS

- **Все утилиты** — если используете только кастомные утилиты

## 📦 Секция `presets` — базовая конфигурация

Позволяет переиспользовать конфигурацию между проектами:

```js
// presets/company-preset.js
module.exports = {
  theme: {
# ... (ещё 7 строк) ...
    require('@tailwindcss/forms'),
  ],
}
```

```js
// tailwind.config.js
module.exports = {
  presets: [
# ... (ещё 8 строк) ...
    },
  },
}
```

> 💡 **Подробнее:** presets разбираются в разделе [Кастомизация](../advanced/customization.md).

## 🎯 Типовые конфигурации

### Минимальная конфигурация

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js}'],
# ... (ещё 2 строк) ...
  },
  plugins: [],
}
```

### React + Vite + TypeScript

```js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
# ... (ещё 19 строк) ...
    require('@tailwindcss/forms'),
  ],
}
```

### Next.js (App Router)

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
# ... (ещё 15 строк) ...
    require('@tailwindcss/forms'),
  ],
}
```

### Vue + Vite + TypeScript

```js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
# ... (ещё 12 строк) ...
    require('@tailwindcss/forms'),
  ],
}
```

### Laravel + Blade

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
# ... (ещё 13 строк) ...
    require('@tailwindcss/forms'),
  ],
}
```

### WordPress

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
# ... (ещё 9 строк) ...
    require('@tailwindcss/typography'),
  ],
}
```

## 📊 Шпаргалка: что когда использовать

| Задача | Решение |
| :-- | :-- |
| Настроить сканирование файлов | `content: ['./src/**/*.{html,js}']` |
| Добавить свой цвет | `theme.extend.colors` |
| Добавить свой шрифт | `theme.extend.fontFamily` |
| Добавить свой breakpoint | `theme.extend.screens` |
| Включить dark mode | `darkMode: 'class'` |
| Подключить плагин форм | `plugins: [require('@tailwindcss/forms')]` |
| Подключить плагин типографики | `plugins: [require('@tailwindcss/typography')]` |
| Повысить специфичность | `important: true` или `important: '#app'` |
| Добавить префикс | `prefix: 'tw-'` |
| Отключить Preflight | `corePlugins: { preflight: false }` |
| Отключить конкретные утилиты | `corePlugins: { float: false }` |
| Переиспользовать конфиг | `presets: [require('./preset.js')]` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Забывают настроить `content`

```js
// ❌ Плохо: content отсутствует
module.exports = {
  theme: {
# ... (ещё 16 строк) ...
    },
  },
}
```

**Результат:** CSS будет пустым или содержать все классы.

### ❌ Ошибка 2: Неправильные пути в `content`

```js
// ❌ Плохо: пути не существуют
module.exports = {
  content: ['./app/**/*.html'], // папки app нет
# ... (ещё 3 строк) ...
module.exports = {
  content: ['./src/**/*.html'],
}
```

### ❌ Ошибка 3: Забывают расширения файлов

```js
// ❌ Плохо: Vue-файлы не сканируются
module.exports = {
  content: ['./src/**/*.js'],
# ... (ещё 3 строк) ...
module.exports = {
  content: ['./src/**/*.{js,ts,vue}'],
}
```

### ❌ Ошибка 4: Полная замена вместо расширения

```js
// ❌ Плохо: теряем все стандартные цвета
module.exports = {
  theme: {
# ... (ещё 13 строк) ...
    },
  },
}
```

### ❌ Ошибка 5: Забывают JSDoc тип

```js
// ❌ Плохо: нет автодополнения в IDE
module.exports = {
  content: ['./src/**/*.html'],
# ... (ещё 4 строк) ...
module.exports = {
  content: ['./src/**/*.html'],
}
```

### ❌ Ошибка 6: Изменяют конфиг без перезапуска

```bash
# ❌ Плохо: изменения не применятся
# Просто редактируем tailwind.config.js

# ... (ещё 1 строк) ...
npm run dev
# или
npx tailwindcss -i ./src/input.css -o ./src/output.css --watch
```

### ❌ Ошибка 7: `important: true` без необходимости

```js
// ❌ Плохо: !important везде — сложно переопределить
module.exports = {
  important: true,
# ... (ещё 1 строк) ...

// ✅ Хорошо: решаем конфликты правильно
// Используем специфичные селекторы или @layer
```

### ❌ Ошибка 8: Префикс для нового проекта

```js
// ❌ Плохо: усложняет код без необходимости
module.exports = {
  prefix: 'tw-',
# ... (ещё 1 строк) ...

// ✅ Хорошо: префикс только при интеграции
// Для новых проектов префикс не нужен
```

### ❌ Ошибка 9: Отключают Preflight без причины

```js
// ❌ Плохо: Preflight отключён, стили сломаны
module.exports = {
  corePlugins: {
# ... (ещё 3 строк) ...

// ✅ Хорошо: Preflight включён (по умолчанию)
// Отключаем только при интеграции в существующий проект
```

### ❌ Ошибка 10: Забывают про `darkMode: 'class'`

```js
// ❌ Плохо: по умолчанию используется media
module.exports = {
  // darkMode не указан
# ... (ещё 3 строк) ...
module.exports = {
  darkMode: 'class',
}
```

# 📦 Установка Tailwind CSS

## 🎯 Какой способ установки выбрать?

Tailwind CSS можно установить несколькими способами. Выбор зависит от ваших целей:

| Способ | Когда использовать | Production-ready |
| :-- | :-- | :-- |
| **Play CDN** | Быстрые эксперименты, прототипы, CodePen | ❌ Нет |
| **Tailwind CLI** | Простые статические сайты без сборщика | ✅ Да |
| **PostCSS** (рекомендуется) | Production-проекты с фреймворками | ✅ Да |
| **Vite / Next.js / Nuxt** | Современные фронтенд-проекты | ✅ Да |
| **CDN (полный)** | Legacy-проекты, email-вёрстка | ⚠️ С ограничениями |

> 💡 **Рекомендация:** для новых проектов используйте **PostCSS** или **Vite**. Для экспериментов — **Play CDN**.

## 🚀 Вариант 1: Play CDN (для экспериментов)

Самый быстрый способ попробовать Tailwind — подключить его через CDN прямо в HTML:

### Шаг 1: Создайте HTML-файл

### Шаг 2: Откройте в браузере

Просто откройте файл в браузере — Tailwind уже работает!

### ⚙️ Кастомизация Play CDN

Можно настроить Tailwind прямо в HTML:

### 📦 Подключение плагинов через CDN

```html
<script src="https://cdn.tailwindcss.com?plugins=forms,typography,aspect-ratio"></script>
```

### ⚠️ Ограничения Play CDN

- ❌ **Не для production** — нет оптимизации, большой размер

- ❌ **Нет JIT-компиляции** в полной мере

- ❌ **Нет кастомных плагинов** (только официальные)

- ❌ **Зависимость от CDN** — если CDN упадёт, сайт сломается

> 💡 **Используйте Play CDN только для:** прототипов, CodePen, быстрых экспериментов, email-вёрстки.

## 🛠️ Вариант 2: Tailwind CLI (для простых проектов)

Tailwind CLI — это standalone-инструмент, который не требует Node.js или PostCSS.

### Шаг 1: Установите Tailwind

```bash
# Через npm (нужен Node.js)
npm install -D tailwindcss

# Или скачайте standalone binary с GitHub
# https://github.com/tailwindlabs/tailwindcss/releases
```

### Шаг 2: Инициализируйте конфигурацию

```bash
npx tailwindcss init
```

Это создаст файл `tailwind.config.js`:

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
# ... (ещё 2 строк) ...
  },
  plugins: [],
}
```

### Шаг 3: Создайте CSS-файл

Создайте `src/input.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### Шаг 4: Запустите CLI

```bash
# Однократная сборка
npx tailwindcss -i ./src/input.css -o ./src/output.css

# ... (ещё 2 строк) ...

# С минификацией (для production)
npx tailwindcss -i ./src/input.css -o ./src/output.css --minify
```

### Шаг 5: Подключите CSS в HTML

```html
<!DOCTYPE html>
<html lang="ru">
<head>
# ... (ещё 4 строк) ...
  <h1 class="text-3xl font-bold text-blue-600">Tailwind CLI</h1>
</body>
</html>
```

### 📁 Структура проекта

```
my-project/
├── src/
│   ├── input.css       ← Исходный CSS с директивами
# ... (ещё 1 строк) ...
│   └── index.html      ← Ваш HTML
├── tailwind.config.js  ← Конфигурация Tailwind
└── package.json
```

### ⚙️ Добавление в package.json

```json
{
  "scripts": {
    "dev": "npx tailwindcss -i ./src/input.css -o ./src/output.css --watch",
    "build": "npx tailwindcss -i ./src/input.css -o ./src/output.css --minify"
  }
}
```

```bash
# Разработка
npm run dev

# Production
npm run build
```

## ⚙️ Вариант 3: PostCSS (рекомендуется)

PostCSS — **официально рекомендуемый** способ установки Tailwind для production-проектов.

### Шаг 1: Установите зависимости

```bash
npm install -D tailwindcss postcss autoprefixer
```

### Шаг 2: Инициализируйте конфигурации

```bash
npx tailwindcss init -p
```

Флаг `-p` создаст оба файла: `tailwind.config.js` и `postcss.config.js`.

```js
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
# ... (ещё 3 строк) ...
  },
  plugins: [],
}
```

```js
// postcss.config.js
module.exports = {
  plugins: {
# ... (ещё 1 строк) ...
    autoprefixer: {},
  },
}
```

### Шаг 3: Настройте `content`

**Критически важный шаг!** Tailwind должен знать, какие файлы сканировать для генерации CSS:

```js
// tailwind.config.js
module.exports = {
  content: [
# ... (ещё 11 строк) ...
  ],
  // ...
}
```

> ⚠️ **Важно:** если не настроить `content`, Tailwind сгенерирует **пустой CSS** или **весь CSS** (3+ MB).

### Шаг 4: Добавьте директивы в CSS

Создайте `src/input.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### Шаг 5: Интегрируйте с вашим сборщиком

#### Vite

```js
// vite.config.js
import { defineConfig } from 'vite'

# ... (ещё 2 строк) ...
    postcss: './postcss.config.js',
  },
})
```

```js
// src/main.js
import './input.css'
```

#### Webpack

```js
// webpack.config.js
module.exports = {
  // ...
# ... (ещё 20 строк) ...
    ],
  },
}
```

#### Parcel

Parcel автоматически подхватывает PostCSS — просто создайте `postcss.config.js`.

#### Create React App

```bash
# CRA уже поддерживает PostCSS
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

### 📁 Структура проекта

```
my-project/
├── src/
│   ├── input.css        ← Директивы Tailwind
# ... (ещё 2 строк) ...
├── tailwind.config.js   ← Конфигурация Tailwind
├── postcss.config.js    ← Конфигурация PostCSS
└── package.json
```

## 🎨 Вариант 4: Vite + React / Vue

Самый популярный современный стек.

### React + Vite

```bash
# Создание проекта
npm create vite@latest my-app -- --template react
cd my-app
# ... (ещё 1 строк) ...
# Установка Tailwind
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

```js
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
export default {
# ... (ещё 6 строк) ...
  },
  plugins: [],
}
```

```css
/* src/index.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

```bash
# Запуск
npm run dev
```

### Vue 3 + Vite

```bash
# Создание проекта
npm create vite@latest my-app -- --template vue
cd my-app
# ... (ещё 1 строк) ...
# Установка Tailwind
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

```js
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
export default {
# ... (ещё 6 строк) ...
  },
  plugins: [],
}
```

```css
/* src/style.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

> 📚 **Подробнее:** см. разделы [React + Tailwind](../integrations/react.md) и [Vue + Tailwind](../integrations/vue.md).

## 🚀 Вариант 5: Next.js

Next.js имеет **встроенную поддержку** Tailwind CSS.

### Шаг 1: Создание проекта

```bash
npx create-next-app@latest my-app
cd my-app

# ... (ещё 1 строк) ...
# Если нет:
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

### Шаг 2: Настройка конфигурации

```js
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
# ... (ещё 8 строк) ...
  },
  plugins: [],
}
```

### Шаг 3: Добавление директив

```css
/* app/globals.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### Шаг 4: Подключение в layout

### Шаг 5: Использование

```bash
npm run dev
```

> 📚 **Подробнее:** см. раздел [Next.js + Tailwind](../integrations/nextjs.md).

## 🎭 Вариант 6: Nuxt 3

### Шаг 1: Установка модуля

```bash
npx nuxi@latest init my-app
cd my-app
npm install -D @nuxtjs/tailwindcss
```

### Шаг 2: Настройка

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  modules: ['@nuxtjs/tailwindcss'],
# ... (ещё 1 строк) ...
    configPath: 'tailwind.config.js',
  },
})
```

### Шаг 3: Конфигурация

```js
// tailwind.config.js
module.exports = {
  content: [
# ... (ещё 4 строк) ...
    './app.vue',
  ],
}
```

### Шаг 4: Использование

```vue
<!-- pages/index.vue -->
<template>
  <div class="min-h-screen bg-gray-100 flex items-center justify-center">
# ... (ещё 4 строк) ...
    </div>
  </div>
</template>
```

## 🐘 Вариант 7: Laravel

Laravel имеет **отличную интеграцию** с Tailwind через Vite.

### Шаг 1: Создание проекта

```bash
laravel new my-app
cd my-app
```

### Шаг 2: Установка зависимостей

```bash
npm install
```

### Шаг 3: Настройка Tailwind

```js
// tailwind.config.js
const defaultTheme = require('tailwindcss/defaultTheme')

# ... (ещё 13 строк) ...
  },
  plugins: [require('@tailwindcss/forms')],
}
```

### Шаг 4: CSS-файл

```css
/* resources/css/app.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### Шаг 5: Подключение в шаблоне

### Шаг 6: Запуск

```bash
# В одном терминале — Laravel
php artisan serve

# В другом — Vite
npm run dev
```

## 🎨 Вариант 8: Ruby on Rails

### Шаг 1: Установка

```bash
# Через importmap (Rails 7+)
./bin/importmap pin tailwindcss

# Или через npm
npm install -D tailwindcss postcss autoprefixer
```

### Шаг 2: Использование с gem

```bash
# Добавьте в Gemfile
gem 'tailwindcss-rails'

bundle install
rails tailwindcss:install
```

### Шаг 3: Запуск

```bash
# В одном терминале — Rails
bin/rails server

# В другом — Tailwind
bin/rails tailwindcss:watch
```

## 🎨 Вариант 9: Django

### Шаг 1: Установка

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

### Шаг 2: Настройка

```js
// tailwind.config.js
module.exports = {
  content: [
# ... (ещё 1 строк) ...
    './**/templates/**/*.html',
  ],
}
```

### Шаг 3: Сборка CSS

```json
// package.json
{
  "scripts": {
# ... (ещё 1 строк) ...
    "build": "npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --minify"
  }
}
```

### Шаг 4: Подключение в шаблоне

## ✅ Проверка установки

После установки убедитесь, что всё работает:

### Тестовая страница

### Чеклист проверки

- [ ] CSS-файл сгенерирован и подключён

- [ ] Стили применяются (карточка имеет белый фон, тени, скругления)

- [ ] Hover-эффекты работают

- [ ] Responsive работает (уменьшите окно браузера)

- [ ] Консоль браузера не показывает ошибок 404

## 🔄 Tailwind v3 vs v4

В 2025 году вышел **Tailwind CSS v4** с новым движком Oxide. Вот основные отличия:

### Что нового в v4

- ⚡ **Новый движок Oxide** — в 10 раз быстрее

- 🎨 **CSS-first конфигурация** — настройка прямо в CSS

- 📦 **Zero-config установка** — `@import "tailwindcss"`

- 🚀 **Нативная поддержка cascade layers**

- 🎯 **Улучшенная производительность**

### Установка v4

```bash
npm install tailwindcss @tailwindcss/postcss postcss
```

```css
/* input.css */
@import "tailwindcss";
```

### Установка v3 (стабильная)

```bash
npm install -D tailwindcss postcss autoprefixer
```

```css
/* input.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

> 💡 **Рекомендация:** для новых проектов используйте **v4**. Для существующих — оставайтесь на **v3** до момента миграции.

## 📊 Сравнение способов установки

| Способ | Скорость настройки | Production | Сложность | Рекомендация |
| :-- | :--: | :--: | :--: | :-- |
| **Play CDN** | ⚡ 1 мин | ❌ | 🟢 Очень просто | Только для экспериментов |
| **Tailwind CLI** | ⚡ 5 мин | ✅ | 🟢 Просто | Для статических сайтов |
| **PostCSS** | ⏱ 10 мин | ✅ | 🟡 Средне | ✅ **Рекомендуется** |
| **Vite** | ⏱ 10 мин | ✅ | 🟡 Средне | ✅ **Для React/Vue** |
| **Next.js** | ⏱ 5 мин | ✅ | 🟢 Просто | ✅ **Для Next.js** |
| **Laravel** | ⏱ 10 мин | ✅ | 🟡 Средне | ✅ **Для Laravel** |

### 1. 📁 Базовая структура проекта

```
my-project/
├── src/
│   ├── input.css          ← Директивы Tailwind
# ... (ещё 4 строк) ...
├── postcss.config.js      ← Конфигурация PostCSS
├── package.json
└── .gitignore
```

### 2. 📝 package.json scripts

```json
{
  "scripts": {
    "dev": "npx tailwindcss -i ./src/input.css -o ./src/output.css --watch",
# ... (ещё 1 строк) ...
    "analyze": "npx tailwindcss -i ./src/input.css -o ./src/output.css --minify && gzip -c ./src/output.css | wc -c"
  }
}
```

### 3. 🎨 .gitignore для Tailwind

```gitignore
# Зависимости
node_modules/

# ... (ещё 8 строк) ...
# OS
.DS_Store
Thumbs.db
```

### 4. 🔧 TypeScript + Tailwind

```bash
npm install -D tailwindcss @types/node
```

```js
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
# ... (ещё 3 строк) ...
  },
  plugins: [],
}
```

## 📊 Шпаргалка: что когда использовать

| Задача | Команда |
| :-- | :-- |
| Быстрый эксперимент | `<script src="https://cdn.tailwindcss.com"></script>` |
| Установка через npm | `npm install -D tailwindcss postcss autoprefixer` |
| Инициализация конфига | `npx tailwindcss init -p` |
| Однократная сборка | `npx tailwindcss -i input.css -o output.css` |
| Watch-режим | `npx tailwindcss -i input.css -o output.css --watch` |
| Production build | `npx tailwindcss -i input.css -o output.css --minify` |
| Обновление Tailwind | `npm update tailwindcss` |
| Проверка версии | `npx tailwindcss --help` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Забывают настроить `content`

```js
// ❌ Плохо: Tailwind не знает, что сканировать
module.exports = {
  // content отсутствует
# ... (ещё 5 строк) ...
  content: ["./src/**/*.{html,js,jsx,ts,tsx,vue}"],
  theme: { extend: {} },
}
```

**Результат:** CSS будет пустым или содержать все классы (3+ MB).

### ❌ Ошибка 2: Путают `input.css` и `output.css`

```html
<!-- ❌ Плохо: подключаем исходный файл -->
<link href="./input.css" rel="stylesheet">

<!-- ✅ Хорошо: подключаем сгенерированный -->
<link href="./output.css" rel="stylesheet">
```

### ❌ Ошибка 3: Забывают директивы в CSS

```css
/* ❌ Плохо: нет директив */
body {
  background: blue;
# ... (ещё 3 строк) ...
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### ❌ Ошибка 4: Используют Play CDN в production

```html
<!-- ❌ Плохо: CDN не для production -->
<script src="https://cdn.tailwindcss.com"></script>

<!-- ✅ Хорошо: локальный CSS -->
<link href="./output.css" rel="stylesheet">
```

### ❌ Ошибка 5: Не перезапускают dev-сервер после изменения конфига

```bash
# ❌ Плохо: изменения в tailwind.config.js не применятся
# Просто редактируем файл

# ... (ещё 1 строк) ...
npm run dev
# или
npx tailwindcss -i input.css -o output.css --watch
```

### ❌ Ошибка 6: Неправильные пути в `content`

```js
// ❌ Плохо: пути не существуют
module.exports = {
  content: ["./app/**/*.html"], // папки app нет
# ... (ещё 3 строк) ...
module.exports = {
  content: ["./src/**/*.html"],
}
```

### ❌ Ошибка 7: Забывают установить PostCSS и Autoprefixer

```bash
# ❌ Плохо: только Tailwind
npm install -D tailwindcss

# ✅ Хорошо: полный набор
npm install -D tailwindcss postcss autoprefixer
```

### ❌ Ошибка 8: Не используют `--watch` при разработке

```bash
# ❌ Плохо: нужно вручную пересобирать
npx tailwindcss -i input.css -o output.css

# ✅ Хорошо: автоматическая пересборка
npx tailwindcss -i input.css -o output.css --watch
```

### ❌ Ошибка 9: Забывают `--minify` в production

```bash
# ❌ Плохо: неминифицированный CSS
npx tailwindcss -i input.css -o output.css

# ✅ Хорошо: минифицированный CSS
npx tailwindcss -i input.css -o output.css --minify
```

### ❌ Ошибка 10: Конфликт версий Tailwind

```bash
# Проверка версии
npx tailwindcss --help

# ... (ещё 3 строк) ...
# Или переустановить
rm -rf node_modules package-lock.json
npm install
```

# 📘 Введение в Tailwind CSS

## 🧠 Философия utility-first

### Что такое utility-first?

**Utility-first** — это подход, при котором вы стилизуете элементы, комбинируя **мелкие, одноцелевые классы** прямо в HTML.

#### ❌ Традиционный подход

**Проблемы:**

- Нужно придумать имена классов (`alert`, `alert-message`)

- CSS разбросан по отдельному файлу

- При изменении дизайна нужно править два места

- Класс `.alert` может конфликтовать с другим `.alert`

#### ✅ Utility-first подход

```html
<div class="bg-red-100 border border-red-200 rounded-lg p-4 text-red-800">
  <p class="font-medium">Ошибка!</p>
</div>
```

**Преимущества:**

- 🎯 Всё видно сразу в HTML

- 🚫 Нет проблем с именами классов

- 🔄 Легко изменить стили — просто поменяйте классы

- 📦 Нет каскадных конфликтов

## 🏛 Основные принципы Tailwind

### 1. 🎨 Ограниченная дизайн-система

Tailwind предоставляет **заранее определённые значения** для большинства свойств:

```html
<!-- Отступы: 0, 1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20... -->
<div class="p-4">...</div>

# ... (ещё 2 строк) ...

<!-- Размеры шрифтов: xs, sm, base, lg, xl, 2xl, 3xl... -->
<h1 class="text-2xl">...</h1>
```

**Зачем?** Это заставляет вас использовать **консистентные значения** вместо случайных чисел (`padding: 13px` — такое больше не пройдёт).

### 2. 📱 Mobile-first адаптивность

Все responsive-классы работают через **префиксы breakpoints**:

```html
<div class="w-full md:w-1/2 lg:w-1/3">
  <!-- На мобильных: 100% ширины -->
  <!-- На планшетах (md:): 50% ширины -->
  <!-- На десктопах (lg:): 33% ширины -->
</div>
```

### 3. 🌙 Состояния через префиксы

```html
<button class="bg-blue-500 hover:bg-blue-600 focus:ring-2 active:scale-95">
  Нажми меня
</button>
```

### 4. ⚡ JIT-компиляция (Just-In-Time)

### 🟢 Идеально подходит для:

- **SaaS-продуктов** — где важен уникальный дизайн

- **Дашбордов и админок** — много повторяющихся UI-паттернов

- **Лендингов** — быстрая вёрстка с кастомным дизайном

- **Дизайн-систем** — Tailwind как основа для компонентов

- **Прототипов** — когда нужно быстро и красиво

- **Командной разработки** — консистентность без code review стилей

### 🟡 Подходит с оговорками:

- **Контентные сайты** (блоги, новости) — можно, но избыточно

- **Email-вёрстка** — нужны инлайновые стили (есть плагин)

- **Legacy-проекты** — интеграция может быть сложной

### 🔴 Не подходит для:

- **Микро-проектов на 1 страницу** — проще написать CSS вручную

- **Проектов с очень сложными анимациями** — GSAP/Framer Motion удобнее

- **Когда команда категорически против** — навязывать технологии бессмысленно

### 🟢 Основы

- **Установка и настройка** — как подключить Tailwind в проект

- **Конфигурация** — `tailwind.config.js` и кастомные значения

- **Утилитарные классы** — основные классы для стилизации

### 🟡 Средний уровень

- **Flexbox и Grid** — создание сложных макетов

- **Responsive дизайн** — адаптация под разные устройства

- **Состояния** — hover, focus, active, group-hover

- **Dark mode** — тёмная тема из коробки

### 🔴 Продвинутый уровень

- **Кастомизация** — создание собственных утилит

- **Директивы** — `@apply`, `@layer`, `theme()`

- **Плагины** — расширение функциональности

- **Оптимизация** — PurgeCSS и production build

### 1. 📏 Используйте значения из дизайн-системы

```html
<!-- ❌ Плохо -->
<div class="p-[13px] text-[15px]">

<!-- ✅ Хорошо -->
<div class="p-3 text-sm">
```

### 2. 🧹 Группируйте классы логически

### 3. 📦 Выносите повторяющиеся паттерны в компоненты

```html
<!-- ❌ Плохо: дублирование -->
<button class="bg-blue-500 text-white px-4 py-2 rounded">Сохранить</button>
<button class="bg-blue-500 text-white px-4 py-2 rounded">Отмена</button>
# ... (ещё 1 строк) ...
<!-- ✅ Хорошо: React-компонент -->
<Button variant="primary">Сохранить</Button>
<Button variant="primary">Отмена</Button>
```

### 4. 🎨 Используйте arbitrary values только при необходимости

```html
<!-- ✅ Хорошо: из дизайн-системы -->
<div class="w-64 h-48">

<!-- 🟡 Допустимо: если реально нужно кастомное значение -->
<div class="w-[267px] h-[183px]">
```

> 💬 **Вопрос для размышления:** какой из подходов (BEM, CSS Modules, Tailwind) вам ближе и почему? Попробуйте переписать один из своих старых компонентов на Tailwind и сравните ощущения.

# 🎨 Утилитарные классы

> **Обзор всех категорий утилитарных классов Tailwind CSS:** от макета и типографики до эффектов и интерактивности. Этот раздел — карта, которая поможет ориентироваться в 50 000+ классах Tailwind.

## 🧠 Что такое утилитарный класс?

**Утилитарный класс** — это маленький CSS-класс, который делает **одну конкретную вещь**:

```html
<!-- Каждый класс = одно CSS-свойство -->
<div class="bg-blue-500 p-4 rounded-lg text-white font-bold">
  <!-- bg-blue-500 → background-color: #3b82f6 -->
# ... (ещё 2 строк) ...
  <!-- text-white → color: #ffffff -->
  <!-- font-bold → font-weight: 700 -->
</div>
```

### Анатомия утилитарного класса

```
[модификатор:]утилита-значение

Примеры:
# ... (ещё 2 строк) ...
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

Каждый имеет 11 оттенков: `50`, `100`, `200`, `300`, `400`, `500`, `600`, `700`, `800`, `900`, `950`

#### Прозрачность

```html
<div class="bg-blue-500/50">50% прозрачности</div>
<p class="text-gray-900/80">80% непрозрачности</p>
```

> 📚 **Подробнее:** [Цвета](../styling/colors.md)

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

## 🎨 Пример: сборка компонента из утилит

Посмотрим, как из отдельных утилит собирается реальный UI-элемент:

### Карточка товара

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
# ... (ещё 1 строк) ...
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
# ... (ещё 3 строк) ...
<button class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded transition-colors">
  Плавный hover-эффект
</button>
```

### Что вы изучили в секции Basics

- 📘 **Введение** — философия utility-first

- 📦 **Установка** — как подключить Tailwind

- ⚙️ **Конфигурация** — как настроить `tailwind.config.js`

- 🎨 **Утилитарные классы** — обзор всех категорий

# 📐 Раздел: Layout

# 📐 Flexbox в Tailwind CSS

## 🧠 Краткое напоминание: что такое Flexbox?

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

> 💡 **Правило:** в 95% случаев используйте `flex`. `inline-flex` нужен только когда контейнер должен вести себя как инлайновый элемент (например, кнопка с иконкой).

## 🧭 Направление: `flex-direction`

По умолчанию flex-элементы располагаются **в строку** (слева направо). Tailwind позволяет менять направление:

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `flex-row` | `flex-direction: row` | → По горизонтали (по умолчанию) |
| `flex-row-reverse` | `flex-direction: row-reverse` | ← Справа налево |
| `flex-col` | `flex-direction: column` | ↓ По вертикали |
| `flex-col-reverse` | `flex-direction: column-reverse` | ↑ Снизу вверх |

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
# ... (ещё 3 строк) ...
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

## 📐 Выравнивание по поперечной оси: `align-items`

Поперечная ось — перпендикулярна главной (по умолчанию — вертикаль).

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `items-start` | `align-items: flex-start` | К верху |
| `items-end` | `align-items: flex-end` | К низу |
| `items-center` | `align-items: center` | По центру |
| `items-baseline` | `align-items: baseline` | По базовой линии текста |
| `items-stretch` | `align-items: stretch` | Растянуть (по умолчанию) |

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
# ... (ещё 3 строк) ...
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
# ... (ещё 1 строк) ...
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

| Критерий | `gap` | `space-x/y` |
| :-- | :-- | :-- |
| **Работа с `flex-wrap`** | ✅ Корректно | ❌ Лишние отступы на краях |
| **Производительность** | 🟢 Нативный CSS | 🟡 Через `> * + *` |
| **Поддержка браузеров** | 🟢 Все современные | 🟢 Все |
| **Рекомендация** | ✅ Использовать всегда | 🟡 Только для legacy |

> 💡 **Правило:** всегда используйте `gap`. `space-x/y` оставьте для случаев, когда нужно поддерживать IE11 (хотя Tailwind v3 его уже не поддерживает).

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
# ... (ещё 2 строк) ...
    <a href="#" class="hover:text-blue-500">Контакты</a>
  </div>
</nav>
```

### 3. 💬 Чат-сообщения

### 4. 🏆 Holy Grail Layout

### 5. 🏷️ Список с иконкой и бейджем

## 📱 Responsive Flexbox

Одна из самых мощных фишек — менять направление и выравнивание на разных экранах:

```html
<!-- Мобильные: колонка -->
<!-- Планшеты: 2 в ряд -->
<!-- Десктоп: 4 в ряд -->
# ... (ещё 3 строк) ...
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

> 💡 **Почему:** flex-элементы по умолчанию имеют `min-width: auto`, что мешает `truncate` работать.

### ❌ Ошибка 2: `flex-1` без `min-w-0` в карточках

```html
<!-- ❌ Карточки могут не сжиматься -->
<div class="flex gap-4">
  <div class="flex-1">Длинный контент...</div>
# ... (ещё 3 строк) ...
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

# 🔲 Grid в Tailwind CSS

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
# ... (ещё 3 строк) ...
  <div class="bg-blue-500 p-4 text-white">5</div>
  <div class="bg-blue-500 p-4 text-white">6</div>
</div>
```

### Адаптивные сетки

```html
<!-- Мобильные: 1 колонка -->
<!-- Планшеты: 2 колонки -->
<!-- Десктопы: 4 колонки -->
# ... (ещё 3 строк) ...
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

### Row start/end

Аналогично для строк:

## 🌊 Auto-flow: `grid-flow-{direction}`

Управляет тем, как элементы автоматически размещаются в сетке:

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `grid-flow-row` | `grid-auto-flow: row` | Заполнение по строкам (по умолчанию) |
| `grid-flow-col` | `grid-auto-flow: column` | Заполнение по колонкам |
| `grid-flow-dense` | `grid-auto-flow: dense` | Заполнение пустых мест |
| `grid-flow-row-dense` | `grid-auto-flow: row dense` | По строкам + заполнение пустот |
| `grid-flow-col-dense` | `grid-auto-flow: column dense` | По колонкам + заполнение пустот |

### Dense: заполнение пустот

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
# ... (ещё 1 строк) ...
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
# ... (ещё 3 строк) ...
  <div class="bg-purple-500 p-4 text-white self-end">5 (вниз)</div>
  <div class="bg-blue-500 p-4 text-white">6</div>
</div>
```

## 🎨 Arbitrary values

Если стандартных значений недостаточно:

### 1. 🏆 Holy Grail Layout

### 2. 🖼️ Masonry-подобная галерея

### 3. 📊 Dashboard с виджетами

### 4. 📝 Форма с grid

### 5. 🎴 Карточка с наложением

### 6. 📱 Адаптивная сетка с auto-fit

```html
<!-- Автоматическая адаптивная сетка -->
<div class="grid gap-4" style="grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));">
  <div class="bg-white p-6 rounded-lg shadow">Карточка 1</div>
# ... (ещё 2 строк) ...
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

### ❌ Ошибка 2: `col-span` больше, чем колонок в сетке

```html
<!-- ❌ Плохо: col-span-4 в сетке из 3 колонок -->
<div class="grid grid-cols-3 gap-4">
  <div class="col-span-4">Не работает как ожидается</div>
# ... (ещё 3 строк) ...
<div class="grid grid-cols-3 gap-4">
  <div class="col-span-3">На всю ширину</div>
</div>
```

### ❌ Ошибка 3: Grid для простых компонентов

### ❌ Ошибка 4: Забывают про `min-h` для grid с `h-` у родителя

```html
<!-- ❌ Плохо: grid может схлопнуться -->
<div class="grid grid-cols-3 gap-4">
  <div class="bg-blue-500">1</div>
# ... (ещё 3 строк) ...
<div class="grid grid-cols-3 gap-4 min-h-64">
  <div class="bg-blue-500">1</div>
</div>
```

### ❌ Ошибка 5: `gap` вместо `padding` для внешних отступов

```html
<!-- ❌ Плохо: gap не создаёт отступов по краям -->
<div class="grid grid-cols-3 gap-4">
  <div class="bg-blue-500">1</div>
# ... (ещё 3 строк) ...
<div class="grid grid-cols-3 gap-4 p-4">
  <div class="bg-blue-500">1</div>
</div>
```

### ❌ Ошибка 6: Забывают про responsive

### ❌ Ошибка 7: `grid-flow-col` без явных строк

# 📐 Размеры в Tailwind CSS

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
# ... (ещё 3 строк) ...
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
# ... (ещё 3 строк) ...
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
# ... (ещё 1 строк) ...

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
# ... (ещё 1 строк) ...

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
# ... (ещё 3 строк) ...
<div class="aspect-video w-full bg-gray-900">
  <iframe src="..." class="w-full h-full" frameborder="0"></iframe>
</div>
```

### Кастомные соотношения

### 1. 🎴 Карточка товара с квадратным изображением

### 2. 🎬 Hero-секция на весь экран

### 3. 🖼️ Галерея с aspect-ratio

### 4. 📊 Dashboard с виджетами

### 5. 🎥 Видео-плеер с aspect-ratio

### 6. 👤 Аватары разных размеров

### 7. 📋 Таблица с max-height и скроллом

### 8. 📱 Адаптивный контейнер

```html
<!-- Контейнер с разной шириной на разных экранах -->
<div class="w-full max-w-sm sm:max-w-md md:max-w-lg lg:max-w-xl xl:max-w-2xl mx-auto px-4">
  <h2 class="text-2xl font-bold mb-4">Адаптивный контейнер</h2>
# ... (ещё 1 строк) ...
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
# ... (ещё 3 строк) ...
<div class="h-64 relative">
  <div class="h-full bg-blue-500">Работает</div>
</div>
```

### ❌ Ошибка 2: Забывают `min-w-0` в flex для truncate

### ❌ Ошибка 3: `w-screen` с горизонтальным скроллом

```html
<!-- ❌ Плохо: может появиться горизонтальный скролл из-за scrollbar -->
<div class="w-screen bg-blue-500">
  На всю ширину экрана
# ... (ещё 3 строк) ...
<div class="w-full bg-blue-500">
  На всю ширину родителя
</div>
```

### ❌ Ошибка 4: `h-screen` на мобильных с адресной строкой

```html
<!-- ❌ Плохо: на мобильных адресная строка "съедает" часть высоты -->
<section class="h-screen">
  Hero-секция
# ... (ещё 3 строк) ...
<section class="h-dvh">
  Hero-секция корректно работает на мобильных
</section>
```

### ❌ Ошибка 5: `aspect-ratio` без ширины

```html
<!-- ❌ Плохо: aspect-ratio не работает без ширины -->
<div class="aspect-video bg-blue-500">
  Не работает
# ... (ещё 3 строк) ...
<div class="aspect-video w-full bg-blue-500">
  Работает
</div>
```

### ❌ Ошибка 6: Фиксированная ширина для адаптивного контента

```html
<!-- ❌ Плохо: на мобильных не влезет -->
<div class="w-[800px]">
  Контент
# ... (ещё 3 строк) ...
<div class="w-full max-w-4xl mx-auto px-4">
  Контент
</div>
```

### ❌ Ошибка 7: Забывают `overflow` с `max-h`

```html
<!-- ❌ Плохо: контент выйдет за пределы, но не будет скролла -->
<div class="max-h-64">
  <!-- Длинный контент -->
# ... (ещё 3 строк) ...
<div class="max-h-64 overflow-y-auto">
  <!-- Длинный контент со скроллом -->
</div>
```

### ❌ Ошибка 8: `size-*` для прямоугольников

```html
<!-- ❌ Плохо: size устанавливает одинаковые width и height -->
<div class="size-64 bg-blue-500">
  Получится квадрат, а не прямоугольник
# ... (ещё 3 строк) ...
<div class="w-64 h-32 bg-blue-500">
  Прямоугольник 256×128
</div>
```

### ❌ Ошибка 9: `max-w-prose` для UI-элементов

### ❌ Ошибка 10: Забывают про responsive размеры

```html
<!-- ❌ Плохо: одинаковый размер на всех экранах -->
<div class="w-64 h-64 bg-blue-500">
  Фиксированный размер
# ... (ещё 3 строк) ...
<div class="w-full sm:w-1/2 lg:w-1/3 h-64 md:h-96 bg-blue-500">
  Адаптивный размер
</div>
```

### Что вы изучили в секции Layout

- 📐 **Flexbox** — одномерная раскладка

- 🔲 **Grid** — двумерная раскладка

- 📏 **Отступы** — padding, margin, space, gap

- 📐 **Размеры** — width, height, min/max, aspect-ratio

# 📏 Отступы в Tailwind CSS

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
# ... (ещё 3 строк) ...
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
# ... (ещё 3 строк) ...
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
# ... (ещё 3 строк) ...
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

> 💡 **Правило:** используйте `gap` для flex и grid. `space-x/y` оставьте для случаев, когда нельзя использовать gap (старые браузеры).

## 🎯 Arbitrary значения

Если стандартной шкалы недостаточно:

## 📱 Responsive отступы

```html
<!-- Mobile-first: маленькие → большие -->
<div class="p-4 sm:p-6 md:p-8 lg:p-12">
  Адаптивные отступы
# ... (ещё 3 строк) ...
<div class="px-4 py-8 md:px-8 md:py-12 lg:px-16">
  Адаптивные отступы по осям
</div>
```

### 1. 🎴 Стандартная карточка

### 2. 📝 Форма с консистентными отступами

### 3. 🧭 Навигация с отступами

### 4. 🎨 Секция с адаптивными отступами

### 5. 🎯 Вложенные списки с разными отступами

### 6. 🖼️ Галерея с отрицательными margin

### 7. 📊 Статистика с отступами

### 8. 💬 Чат с отступами

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

### ❌ Ошибка 2: `space-x` с `flex-wrap`

### ❌ Ошибка 3: Margin вместо padding для внутренних отступов

```html
<!-- ❌ Плохо: margin создаёт отступ снаружи -->
<div class="bg-blue-500">
  <p class="m-4 text-white">Текст</p>
# ... (ещё 3 строк) ...
<div class="bg-blue-500 p-4">
  <p class="text-white">Текст</p>
</div>
```

### ❌ Ошибка 4: Забывают про responsive отступы

```html
<!-- ❌ Плохо: одинаковые отступы на всех экранах -->
<div class="p-4">
  Контент
# ... (ещё 3 строк) ...
<div class="p-4 md:p-8 lg:p-12">
  Контент
</div>
```

### ❌ Ошибка 5: `mx-auto` без ширины

```html
<!-- ❌ Плохо: блок на всю ширину, центрирование не работает -->
<div class="mx-auto bg-blue-500">
  Не центрируется
# ... (ещё 3 строк) ...
<div class="mx-auto max-w-4xl bg-blue-500">
  Центрируется
</div>
```

### ❌ Ошибка 6: Использование `space-y` для grid

### ❌ Ошибка 7: Противоречивые отступы

```html
<!-- ❌ Плохо: p-4 и pt-8 конфликтуют -->
<div class="p-4 pt-8">
  Непонятный результат
# ... (ещё 3 строк) ...
<div class="px-4 pt-8 pb-4">
  Понятный результат
</div>
```

### ❌ Ошибка 8: Чрезмерное использование отрицательных margin

```html
<!-- ❌ Плохо: слишком много отрицательных margin -->
<div class="-mt-4 -mb-4 -mx-8">
  Сложно поддерживать
# ... (ещё 3 строк) ...
<div class="relative">
  <div class="absolute -top-4">Элемент</div>
</div>
```

# 🎨 Раздел: Styling

# 🖼️ Фоны в Tailwind CSS

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

### Через конфигурацию (рекомендуется)

```js
// tailwind.config.js
module.exports = {
  theme: {
# ... (ещё 7 строк) ...
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

### Arbitrary значения

```html
<!-- Точные размеры -->
<div class="bg-[url('/icon.svg')] bg-[length:32px_32px] bg-no-repeat">
  Иконка 32×32
# ... (ещё 3 строк) ...
<div class="bg-[url('/photo.jpg')] bg-[length:150%_auto]">
  Увеличенное изображение
</div>
```

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

### Arbitrary позиционирование

```html
<!-- Точные проценты -->
<div class="bg-[url('/photo.jpg')] bg-cover bg-[position:20%_30%]">
  Смещение к конкретному месту фото
# ... (ещё 3 строк) ...
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

## 📌 Прикрепление: `bg-{attachment}`

Управляет тем, как фон ведёт себя при прокрутке:

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `bg-fixed` | `background-attachment: fixed` | Фиксирован относительно viewport |
| `bg-local` | `background-attachment: local` | Фиксирован относительно содержимого |
| `bg-scroll` | `background-attachment: scroll` | Прокручивается с элементом (по умолчанию) |

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
# ... (ещё 3 строк) ...
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
# ... (ещё 4 строк) ...
    <h2 class="text-4xl font-bold">Читаемый заголовок</h2>
  </div>
</div>
```

### Градиентный overlay

```html
<!-- Градиент от прозрачного к чёрному снизу -->
<div class="relative h-96 bg-[url('/photo.jpg')] bg-cover">
  <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent"></div>
# ... (ещё 2 строк) ...
    <h2 class="text-3xl font-bold text-white">Заголовок поверх фото</h2>
  </div>
</div>
```

## 🌈 Градиенты как фон

Подробно про градиенты — в разделе [Цвета](../styling/colors.md#градиенты). Краткая сводка:

### Градиент + изображение

```html
<!-- Градиент поверх изображения -->
<div class="bg-[url('/photo.jpg')] bg-cover">
  <div class="bg-gradient-to-r from-blue-600/80 to-purple-600/80 h-64">
# ... (ещё 2 строк) ...
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
# ... (ещё 5 строк) ...
    },
  },
}
```

```html
<div class="bg-dots bg-repeat min-h-screen">
  Фон с точками
</div>
# ... (ещё 1 строк) ...
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

### 1. 🎬 Hero-секция с фото и затемнением

### 2. 🪟 Glassmorphism карточка

### 3. 📄 Страница с декоративным фоном

### 4. 🎴 Карточка товара с изображением

### 5. 🎨 Секция с паттерном

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
# ... (ещё 4 строк) ...
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

# 🔲 Границы в Tailwind CSS

## 📏 Ширина границы: `border-{width}`

Tailwind предоставляет **5 предустановленных ширин** границ:

| Класс | CSS | Визуально |
| :-- | :-- | :-- |
| `border` | `border-width: 1px` | Тонкая граница (по умолчанию) |
| `border-0` | `border-width: 0` | Без границы |
| `border-2` | `border-width: 2px` | Средняя граница |
| `border-4` | `border-width: 4px` | Толстая граница |
| `border-8` | `border-width: 8px` | Очень толстая граница |

```html
<div class="border border-gray-300 p-4">Тонкая граница (1px)</div>
<div class="border-2 border-gray-300 p-4">Средняя граница (2px)</div>
<div class="border-4 border-gray-300 p-4">Толстая граница (4px)</div>
<div class="border-8 border-gray-300 p-4">Очень толстая граница (8px)</div>
```

### Отдельные стороны

Если нужна граница только с определённой стороны:

| Класс | CSS |
| :-- | :-- |
| `border-t` | `border-top-width: 1px` |
| `border-r` | `border-right-width: 1px` |
| `border-b` | `border-bottom-width: 1px` |
| `border-l` | `border-left-width: 1px` |
| `border-x` | `border-left-width: 1px; border-right-width: 1px` |
| `border-y` | `border-top-width: 1px; border-bottom-width: 1px` |

### Arbitrary значения

```html
<!-- Точная ширина в пикселях -->
<div class="border-[3px] border-gray-300 p-4">Граница 3px</div>
```

## 🎨 Цвет границы: `border-{color}`

Используйте цвета из палитры Tailwind (подробнее в разделе [Цвета](../styling/colors.md)):

```html
<div class="border-2 border-gray-300 p-4">Серая граница</div>
<div class="border-2 border-blue-500 p-4">Синяя граница</div>
<div class="border-2 border-red-500 p-4">Красная граница</div>
<div class="border-2 border-green-500 p-4">Зелёная граница</div>
<div class="border-2 border-transparent p-4">Прозрачная граница</div>
```

### Прозрачность

```html
<div class="border-2 border-blue-500/50 p-4">Синяя с 50% прозрачности</div>
<div class="border-2 border-white/20 p-4 bg-gray-900">Белая с 20% прозрачности</div>
```

### Отдельные стороны с цветом

```html
<!-- Разные цвета для разных сторон -->
<div class="border-t-2 border-t-red-500 border-b-2 border-b-blue-500 p-4">
  Красная сверху, синяя снизу
</div>
```

## 🎭 Стиль границы: `border-{style}`

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `border-solid` | `border-style: solid` | Сплошная линия (по умолчанию) |
| `border-dashed` | `border-style: dashed` | Пунктирная |
| `border-dotted` | `border-style: dotted` | Точечная |
| `border-double` | `border-style: double` | Двойная линия |
| `border-hidden` | `border-style: hidden` | Скрытая (как none, но для таблиц) |
| `border-none` | `border-style: none` | Без границы |

```html
<div class="border-2 border-dashed border-gray-400 p-4">Пунктирная граница</div>
<div class="border-2 border-dotted border-gray-400 p-4">Точечная граница</div>
<div class="border-4 border-double border-gray-400 p-4">Двойная граница</div>
```

> 💡 **Совет:** `border-dashed` часто используется для drag-and-drop зон и placeholder-элементов.

## 🔄 Скругление углов: `rounded-{size}`

Tailwind предоставляет **8 предустановленных радиусов**:

| Класс | CSS | Визуально |
| :-- | :-- | :-- |
| `rounded-none` | `border-radius: 0` | Без скругления (острые углы) |
| `rounded-sm` | `border-radius: 0.125rem` (2px) | Очень маленькое скругление |
| `rounded` | `border-radius: 0.25rem` (4px) | Маленькое скругление |
| `rounded-md` | `border-radius: 0.375rem` (6px) | Среднее скругление |
| `rounded-lg` | `border-radius: 0.5rem` (8px) | Большое скругление |
| `rounded-xl` | `border-radius: 0.75rem` (12px) | Очень большое скругление |
| `rounded-2xl` | `border-radius: 1rem` (16px) | Огромное скругление |
| `rounded-3xl` | `border-radius: 1.5rem` (24px) | Максимальное скругление |
| `rounded-full` | `border-radius: 9999px` | Полное скругление (круг/пилюля) |

### Отдельные углы

Если нужно скруглить только определённые углы:

| Класс | CSS |
| :-- | :-- |
| `rounded-t` | `border-top-left-radius` + `border-top-right-radius` |
| `rounded-r` | `border-top-right-radius` + `border-bottom-right-radius` |
| `rounded-b` | `border-bottom-left-radius` + `border-bottom-right-radius` |
| `rounded-l` | `border-top-left-radius` + `border-bottom-left-radius` |
| `rounded-tl` | `border-top-left-radius` |
| `rounded-tr` | `border-top-right-radius` |
| `rounded-br` | `border-bottom-right-radius` |
| `rounded-bl` | `border-bottom-left-radius` |

### Arbitrary значения

```html
<!-- Точный радиус в пикселях -->
<div class="border-2 border-gray-300 p-4 rounded-[10px]">Радиус 10px</div>

<!-- Процентный радиус -->
<div class="border-2 border-gray-300 p-4 rounded-[50%]">Радиус 50%</div>
```

## 💍 Ring-эффекты: `ring-{width}`

`ring` — это **внешняя обводка**, которая не занимает места (в отличие от `border`). Идеально для focus-состояний.

| Класс | CSS |
| :-- | :-- |
| `ring-0` | `box-shadow: 0 0 0 0px` |
| `ring-1` | `box-shadow: 0 0 0 1px` |
| `ring-2` | `box-shadow: 0 0 0 2px` |
| `ring` | `box-shadow: 0 0 0 3px` (по умолчанию) |
| `ring-4` | `box-shadow: 0 0 0 4px` |
| `ring-8` | `box-shadow: 0 0 0 8px` |
| `ring-inset` | `box-shadow: inset 0 0 0 3px` |

### Цвет ring

```html
<input
  type="text"
  class="border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
  placeholder="Фокус с синим ring"
>
```

### Ring offset (отступ от элемента)

```html
<input
  type="text"
  class="border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
  placeholder="Ring с отступом"
>
```

| Класс | CSS |
| :-- | :-- |
| `ring-offset-0` | `--tw-ring-offset-width: 0px` |
| `ring-offset-1` | `--tw-ring-offset-width: 1px` |
| `ring-offset-2` | `--tw-ring-offset-width: 2px` |
| `ring-offset-4` | `--tw-ring-offset-width: 4px` |
| `ring-offset-8` | `--tw-ring-offset-width: 8px` |

### Цвет ring offset

```html
<input
  type="text"
  class="bg-gray-100 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 focus:ring-offset-gray-100"
  placeholder="Ring offset того же цвета, что и фон"
>
```

> 💡 **Важно:** `ring` использует `box-shadow`, поэтому не влияет на layout. `border` занимает место.

## 📏 Outline: `outline-{width}`

`outline` — это **внешняя обводка** (как `ring`), но с другим синтаксисом и поведением:

| Класс | CSS |
| :-- | :-- |
| `outline-none` | `outline: 2px solid transparent; outline-offset: 2px` |
| `outline` | `outline-style: solid` |
| `outline-dashed` | `outline-style: dashed` |
| `outline-dotted` | `outline-style: dotted` |
| `outline-double` | `outline-style: double` |

```html
<!-- Focus с outline -->
<button class="focus:outline-none focus:outline-2 focus:outline-blue-500">
  Кнопка с outline при фокусе
# ... (ещё 3 строк) ...
<button class="focus:outline-2 focus:outline-blue-500 focus:outline-offset-2">
  Кнопка с отступом outline
</button>
```

### Разница между `ring` и `outline`

| Критерий | `ring` | `outline` |
| :-- | :-- | :-- |
| **Реализация** | `box-shadow` | `outline` CSS property |
| **Скругление** | Следует `border-radius` | Не следует `border-radius` |
| **Отступ** | `ring-offset-{size}` | `outline-offset-{size}` |
| **Рекомендация** | ✅ Для focus-состояний | 🟡 Для accessibility |

> 💡 **Правило:** используйте `ring` для focus-состояний в UI. `outline` оставьте для случаев, когда нужно следовать нативному поведению браузера.

## 🔗 Разделители: `divide-{width}` и `divide-{color}`

`divide` добавляет границы **между дочерними элементами**:

### Ширина

| Класс | CSS |
| :-- | :-- |
| `divide-x` | `border-left-width: 1px` между элементами |
| `divide-x-0` | Без горизонтальных разделителей |
| `divide-x-2` | `border-left-width: 2px` |
| `divide-x-4` | `border-left-width: 4px` |
| `divide-x-8` | `border-left-width: 8px` |
| `divide-y` | `border-top-width: 1px` между элементами |
| `divide-y-0` | Без вертикальных разделителей |
| `divide-y-2` | `border-top-width: 2px` |
| `divide-y-4` | `border-top-width: 4px` |
| `divide-y-8` | `border-top-width: 8px` |

### Цвет

### Стиль разделителей

```html
<!-- Пунктирные разделители -->
<div class="divide-y divide-dashed divide-gray-300">
  <div class="py-2">Пункт 1</div>
  <div class="py-2">Пункт 2</div>
</div>
```

### Reverse (для RTL)

```html
<!-- Разделители справа (для RTL языков) -->
<div class="divide-x divide-x-reverse divide-gray-200 flex">
  <div class="px-4">Элемент 1</div>
  <div class="px-4">Элемент 2</div>
</div>
```

### 1. 🎴 Карточка с границей

```html
<div class="bg-white border border-gray-200 rounded-xl shadow-sm p-6 max-w-sm">
  <h3 class="text-xl font-bold text-gray-900 mb-2">Название карточки</h3>
  <p class="text-gray-600 text-sm">
# ... (ещё 3 строк) ...
    Действие
  </button>
</div>
```

### 2. 🎯 Input с focus ring

### 3. 📊 Список с разделителями

### 4. 🏷️ Бейдж с границей

### 5. 🎨 Карточка с акцентной границей слева

```html
<div class="bg-white border-l-4 border-blue-500 rounded-r-lg shadow-sm p-6 max-w-md">
  <h3 class="text-lg font-bold text-gray-900 mb-2">Важная информация</h3>
  <p class="text-gray-600 text-sm">
    Этот блок выделен акцентной границей слева для привлечения внимания.
  </p>
</div>
```

### 6. 🔘 Группа кнопок с разделителями

### 7. 🖼️ Аватар с границей

### 8. 🎯 Drag-and-drop зона

```html
<div class="border-2 border-dashed border-gray-300 rounded-lg p-12 text-center hover:border-blue-500 transition-colors">
  <svg class="mx-auto w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"/>
# ... (ещё 4 строк) ...
  </p>
  <p class="mt-1 text-xs text-gray-500">PNG, JPG до 10MB</p>
</div>
```

## 📊 Шпаргалка: что когда использовать

| Задача | Классы |
| :-- | :-- |
| Тонкая граница | `border border-gray-300` |
| Толстая граница | `border-4 border-gray-300` |
| Только снизу | `border-b border-gray-200` |
| Только слева (акцент) | `border-l-4 border-blue-500` |
| Пунктирная граница | `border-2 border-dashed border-gray-400` |
| Скругление углов | `rounded-lg`, `rounded-xl`, `rounded-full` |
| Только верхние углы | `rounded-t-lg` |
| Focus ring | `focus:ring-2 focus:ring-blue-500` |
| Ring с отступом | `focus:ring-2 focus:ring-blue-500 focus:ring-offset-2` |
| Разделители между элементами | `divide-y divide-gray-200` |
| Горизонтальные разделители | `divide-x divide-gray-200` |
| Аватар | `rounded-full border-2 border-white` |
| Кнопка-пилюля | `rounded-full` |
| Drag-and-drop зона | `border-2 border-dashed` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Забывают `border` при указании цвета

```html
<!-- ❌ Плохо: цвет границы не применится без width -->
<div class="border-gray-300 p-4">Нет границы</div>

<!-- ✅ Хорошо: указываем ширину -->
<div class="border border-gray-300 p-4">Есть граница</div>
```

### ❌ Ошибка 2: `ring` вместо `border` для постоянной границы

```html
<!-- ❌ Плохо: ring занимает место и может обрезаться -->
<div class="ring-2 ring-gray-300 p-4">Кольцо</div>

<!-- ✅ Хорошо: border для постоянной границы -->
<div class="border-2 border-gray-300 p-4">Граница</div>
```

### ❌ Ошибка 3: Забывают `focus:outline-none` при использовании `focus:ring`

### ❌ Ошибка 4: `rounded-full` для неквадратных элементов

```html
<!-- ❌ Плохо: получится овал, не круг -->
<div class="w-32 h-16 rounded-full bg-blue-500">Овал</div>

# ... (ещё 2 строк) ...

<!-- ✅ Или используйте rounded-{size} для прямоугольников -->
<div class="w-32 h-16 rounded-lg bg-blue-500">Прямоугольник со скруглением</div>
```

### ❌ Ошибка 5: `divide` без flex или grid контейнера

### ❌ Ошибка 6: Забывают про responsive границы

```html
<!-- ❌ Плохо: граница на всех экранах -->
<div class="border border-gray-300 p-4">Граница всегда</div>

<!-- ✅ Хорошо: граница только на десктопе -->
<div class="border-0 md:border border-gray-300 p-4">Граница только на md+</div>
```

### ❌ Ошибка 7: `ring-offset` без учёта фона

# 🎨 Цвета в Tailwind CSS

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
# ... (ещё 5 строк) ...
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
# ... (ещё 1 строк) ...
<svg class="w-6 h-6 stroke-red-500 fill-none" viewBox="0 0 24 24">
  <path d="..." stroke-width="2"/>
</svg>
```

## 💧 Прозрачность: модификатор `/{opacity}`

Tailwind позволяет легко задавать прозрачность любому цвету через слэш:

### Доступные значения прозрачности

```
/0   → 0%   (полностью прозрачный)
/5   → 5%
/10  → 10%
# ... (ещё 9 строк) ...
/90  → 90%
/95  → 95%
/100 → 100% (без прозрачности)
```

## 🌈 Градиенты

### Линейные градиенты

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
# ... (ещё 3 строк) ...
<div class="bg-conic from-red-500 via-yellow-500 to-green-500 h-32">
  Конический
</div>
```

## 🎨 Arbitrary values: кастомные цвета

Если нужного цвета нет в палитре, используйте квадратные скобки:

> ⚠️ **Не злоупотребляйте arbitrary values!** Если цвет используется часто — добавьте его в `tailwind.config.js`.

## ⚙️ Кастомизация палитры

### Добавление своих цветов

```js
// tailwind.config.js
module.exports = {
  theme: {
# ... (ещё 26 строк) ...
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
# ... (ещё 11 строк) ...
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
# ... (ещё 6 строк) ...
    },
  },
}
```

```css
/* styles.css */
:root {
  --color-primary: 59 130 246;    /* #3b82f6 */
# ... (ещё 6 строк) ...
  --color-secondary: 167 139 250; /* #a78bfa */
  --color-background: 17 24 39;   /* #111827 */
}
```

```html
<!-- Автоматически меняет цвет в dark mode -->
<div class="bg-primary text-background">Тема</div>
```

### Примеры хороших комбинаций

### Примеры плохих комбинаций

### Инструменты для проверки

- 🔍 [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)

- 🔍 [Colour Contrast Analyser](https://www.tpgi.com/color-contrast-checker/) (десктоп)

- 🔍 DevTools → Accessibility panel (встроен в Chrome)

### 1. 🎯 Цветовая схема для статусов

### 2. 🌙 Светлая и тёмная тема

```html
<div class="bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100 p-6 rounded-lg">
  <h2 class="text-xl font-bold mb-2">Адаптивная карточка</h2>
  <p class="text-gray-600 dark:text-gray-400">
# ... (ещё 3 строк) ...
    Действие
  </button>
</div>
```

### 3. 🏷️ Бейджи и теги

### 4. 🎨 Градиентные кнопки

```html
<!-- Простой градиент -->
<button class="bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 text-white font-medium px-6 py-3 rounded-lg shadow-lg transition">
  Премиум кнопка
# ... (ещё 3 строк) ...
<button class="bg-gradient-to-r from-pink-500 via-red-500 to-yellow-500 bg-[length:200%_auto] animate-gradient text-white font-bold px-6 py-3 rounded-lg">
  Радужная кнопка
</button>
```

### 5. 🎯 Semantic colors в дизайн-системе

```js
// tailwind.config.js
module.exports = {
  theme: {
# ... (ещё 18 строк) ...
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

### ❌ Ошибка 3: Забывают про dark mode

```html
<!-- ❌ Плохо: в тёмной теме не видно -->
<div class="bg-white text-gray-900">Карточка</div>

# ... (ещё 1 строк) ...
<div class="bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100">
  Карточка
</div>
```

### ❌ Ошибка 4: Arbitrary values для часто используемых цветов

```html
<!-- ❌ Плохо: дублирование, нет консистентности -->
<div class="bg-[#ff5722]">...</div>
<div class="bg-[#ff5722]">...</div>
# ... (ещё 1 строк) ...

<!-- ✅ Хорошо: добавлено в конфиг -->
<div class="bg-brand">...</div>
```

# ✨ Эффекты и тени в Tailwind CSS

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

### Цветные тени

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

### Hover-эффекты с прозрачностью

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

### Background blend mode

```html
<!-- Градиент с изображением -->
<div
  class="h-64 bg-[url('/photo.jpg')] bg-cover"
# ... (ещё 1 строк) ...
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

# ... (ещё 4 строк) ...
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

# ... (ещё 3 строк) ...
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
# ... (ещё 3 строк) ...
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
# ... (ещё 2 строк) ...
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

### 1. 🎴 Карточка с тенью при hover

```html
<div class="bg-white rounded-xl shadow-md hover:shadow-xl transition-shadow duration-300 p-6 max-w-sm">
  <h3 class="text-xl font-bold text-gray-900 mb-2">Интерактивная карточка</h3>
  <p class="text-gray-600 text-sm">
# ... (ещё 3 строк) ...
    Действие
  </button>
</div>
```

### 2. 🖼️ Галерея с hover-эффектами

### 3. 🪟 Glassmorphism навигация

```html
<nav class="sticky top-0 z-50 bg-white/80 backdrop-blur-lg border-b border-white/20 shadow-sm">
  <div class="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between">
    <div class="font-bold text-xl">Logo</div>
# ... (ещё 4 строк) ...
    </div>
  </div>
</nav>
```

### 4. 🎨 Фильтры для изображений

### 5. 🎯 Кнопка с цветной тенью

### 6. 🌙 Затемнение изображения для текста

### 7. 🎨 Изображение с mix-blend-mode

```html
<div class="relative bg-gradient-to-br from-purple-500 via-pink-500 to-orange-500 p-12">
  <img
    src="pattern.svg"
# ... (ещё 4 строк) ...
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
# ... (ещё 3 строк) ...
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
# ... (ещё 3 строк) ...
<div class="bg-white/50 backdrop-blur-md">
  Размытие видно
</div>
```

### ❌ Ошибка 4: Слишком много фильтров одновременно

### ❌ Ошибка 5: `backdrop-blur` на мобильных без проверки

```html
<!-- ❌ Плохо: backdrop-blur может тормозить на мобильных -->
<div class="backdrop-blur-xl bg-white/50">
  Тяжёлый эффект
# ... (ещё 3 строк) ...
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

# 🔤 Типографика в Tailwind CSS

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
# ... (ещё 3 строк) ...
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
# ... (ещё 1 строк) ...
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
# ... (ещё 1 строк) ...

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
# ... (ещё 3 строк) ...
<code class="break-all text-sm">
  550e8400e29b41d4a716446655440000
</code>
```

### Многострочная обрезка (line-clamp)

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
# ... (ещё 5 строк) ...
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
# ... (ещё 1 строк) ...
  font-weight: 400;
  font-display: swap;
}
```

```js
// tailwind.config.js
module.exports = {
  theme: {
# ... (ещё 4 строк) ...
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
# ... (ещё 3 строк) ...

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

## 📱 Responsive типограграфика

Меняйте размеры и параметры на разных экранах:

```html
<!-- Mobile-first подход -->
<h1 class="text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-bold">
  Адаптивный заголовок
# ... (ещё 2 строк) ...
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

### 1. 📰 Типовая иерархия статьи

### 2. 🏷️ Карточка с иерархией

### 3. 💻 Блок кода

### 4. 📊 Статистика с крупной цифрой

```html
<div class="text-center">
  <div class="text-5xl font-bold tracking-tight text-blue-600">
    80K+
# ... (ещё 2 строк) ...
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

### ❌ Ошибка 2: Забывают про `max-w-prose` для длинных текстов

```html
<!-- ❌ Плохо: строка на весь экран — тяжело читать -->
<p class="text-base">Очень длинный текст на всю ширину экрана...</p>

# ... (ещё 1 строк) ...
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
# ... (ещё 6 строк) ...
  src: url('custom.woff2');
  font-display: swap;
}
```

# 📱 Раздел: Responsive

# 📱 Breakpoints и адаптивный дизайн в Tailwind CSS

## 🎯 Mobile-first подход

```
┌─────────────────────────────────────────────────────────┐
│  Базовые стили (работают везде)                         │
│  + sm:  → от 640px                                      │
# ... (ещё 2 строк) ...
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
# ... (ещё 4 строк) ...
  <div class="bg-blue-500 p-4 text-white">3</div>
  <div class="bg-blue-500 p-4 text-white">4</div>
</div>
```

## 🔧 Синтаксис responsive-классов

Responsive-модификаторы добавляются **перед любым утилитарным классом** через двоеточие:

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
# ... (ещё 2 строк) ...
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
# ... (ещё 4 строк) ...
<div class="px-4 py-8 md:px-8 md:py-12 lg:px-16 lg:py-16">
  Контент с адаптивными отступами
</div>
```

### Ширина и высота

### Max-width

```html
<!-- Ограничение ширины контента -->
<article class="max-w-sm md:max-w-2xl lg:max-w-4xl mx-auto px-4">
  <h1 class="text-2xl md:text-4xl font-bold mb-4">Статья</h1>
# ... (ещё 1 строк) ...
    Длинный текст статьи с комфортной шириной для чтения.
  </p>
</article>
```

## 🎭 Скрытие и показ элементов

### `hidden` и `block`

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
# ... (ещё 3 строк) ...
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

### 1. 📱 Адаптивная навигация

### 2. 🎴 Адаптивная сетка карточек

### 3. 📄 Адаптивный layout с сайдбаром

### 4. 🖼️ Адаптивная hero-секция

### 5. 📊 Адаптивная таблица

## ⚙️ Кастомные breakpoints

Если стандартных breakpoints недостаточно, добавьте свои в `tailwind.config.js`:

```js
// tailwind.config.js
module.exports = {
  theme: {
# ... (ещё 13 строк) ...
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
# ... (ещё 3 строк) ...
    },
  },
}
```

### Когда использовать container queries

- ✅ **Переиспользуемые компоненты** — карточки, виджеты, которые могут быть в разных контекстах

- ✅ **Sidebar vs main content** — один компонент, разное поведение

- ❌ **Глобальный layout** — для этого используйте обычные breakpoints

## 🎯 Responsive spacing scale

Создайте консистентную систему отступов для всех экранов:

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
# ... (ещё 3 строк) ...
<div class="text-base md:text-lg xl:text-xl">
  Правильный подход
</div>
```

### ❌ Ошибка 2: Забывают про промежуточные размеры

```html
<!-- ❌ Плохо: прыжок от мобильного к десктопу -->
<div class="text-sm lg:text-xl">
  Слишком большой скачок
# ... (ещё 3 строк) ...
<div class="text-sm md:text-base lg:text-lg xl:text-xl">
  Плавное увеличение
</div>
```

### ❌ Ошибка 3: Фиксированная ширина без responsive

```html
<!-- ❌ Плохо: на мобильных будет горизонтальный скролл -->
<div class="w-[1200px]">
  Фиксированная ширина
# ... (ещё 3 строк) ...
<div class="w-full max-w-7xl mx-auto px-4">
  Адаптивная ширина с ограничениями
</div>
```

### ❌ Ошибка 4: `hidden` без альтернативы

```html
<!-- ❌ Плохо: элемент скрыт на всех экранах -->
<div class="hidden">
  Невидимый контент
# ... (ещё 3 строк) ...
<div class="hidden md:block">
  Контент для десктопа
</div>
```

### ❌ Ошибка 5: Игнорируют `max-w` для контента

```html
<!-- ❌ Плохо: текст на весь экран на больших мониторах -->
<p class="text-lg leading-relaxed">
  Очень длинный текст, который на больших экранах будет неудобно читать.
# ... (ещё 3 строк) ...
<p class="text-lg leading-relaxed max-w-prose mx-auto">
  Длинный текст с комфортной шириной для чтения.
</p>
```

### ❌ Ошибка 6: Забывают про `min-w` для flex-элементов

```html
<!-- ❌ Плохо: flex-элементы могут сжиматься слишком сильно -->
<div class="flex gap-4">
  <div class="flex-1">Длинный контент...</div>
# ... (ещё 3 строк) ...
<div class="flex gap-4">
  <div class="flex-1 min-w-0">Длинный контент...</div>
</div>
```

### ❌ Ошибка 7: Используют `sm:` для мобильных

```html
<!-- ❌ Плохо: sm: — это не мобильные, это от 640px -->
<div class="sm:text-base">
  Этот стиль применится только от 640px, на мобильных будет дефолтный
# ... (ещё 3 строк) ...
<div class="text-sm sm:text-base">
  Mobile-first подход
</div>
```

# 🌙 Dark Mode в Tailwind CSS

## 🎯 Два режима работы

Tailwind CSS поддерживает **два способа** включения dark mode:

### 1. `media` — по системным настройкам

Тема переключается автоматически в зависимости от настроек ОС/браузера.

```js
// tailwind.config.js
module.exports = {
  darkMode: 'media', // по умолчанию
}
```

**Плюсы:**

- ✅ Работает из коробки

- ✅ Следует системным настройкам пользователя

- ✅ Не нужен JavaScript

**Минусы:**

- ❌ Пользователь не может переключить тему вручную

- ❌ Нельзя сохранить выбор

### 2. `class` — ручное переключение

Тема переключается добавлением класса `dark` к `<html>` или `<body>`.

```js
// tailwind.config.js
module.exports = {
  darkMode: 'class',
}
```

**Плюсы:**

- ✅ Полный контроль над темой

- ✅ Можно сохранить выбор пользователя

- ✅ Можно комбинировать с системными настройками

**Минусы:**

- ❌ Нужен JavaScript

- ❌ Нужно писать логику переключения

> 💡 **Рекомендация:** используйте `class` — это самый гибкий подход. В этом разделе мы сосредоточимся именно на нём.

## 🎨 Синтаксис `dark:`

Модификатор `dark:` добавляется **перед любым утилитарным классом**:

### Комбинирование с другими модификаторами

## 🎯 Типовая цветовая схема

### Светлая тема

```
Фоны:
  - Основной: white
  - Вторичный: gray-50
# ... (ещё 5 строк) ...
  - Третичный: gray-400

Границы: gray-200
```

### Тёмная тема

```
Фоны:
  - Основной: gray-900
  - Вторичный: gray-800
# ... (ещё 5 строк) ...
  - Третичный: gray-500

Границы: gray-700
```

### Пример реализации

## 🔄 Переключатель темы

### Базовый переключатель

### Улучшенный переключатель с инициализацией до рендера

Чтобы избежать «мигания» темы при загрузке, добавьте этот скрипт в `<head>` **до** рендеринга body:

### React-компонент переключателя

### Vue-компонент переключателя

## 🎨 Три состояния: light / dark / system

Самый продвинутый подход — поддержка трёх режимов:

```js
// theme.js
const ThemeManager = {
  init() {
# ... (ещё 33 строк) ...
};

ThemeManager.init();
```

## 🖼️ Изображения в dark mode

### Разные изображения для разных тем

```html
<picture>
  <source srcset="logo-dark.svg" media="(prefers-color-scheme: dark)">
  <img src="logo-light.svg" alt="Логотип">
</picture>
```

### Инверсия SVG

```html
<!-- Светлая тема: чёрная иконка -->
<!-- Тёмная тема: белая иконка -->
<svg class="w-6 h-6 text-gray-900 dark:text-gray-100" fill="currentColor" viewBox="0 0 24 24">
  <path d="..."/>
</svg>
```

### Корректировка яркости изображений

```html
<!-- Фото в светлой теме: обычная яркость -->
<!-- Фото в тёмной теме: чуть темнее -->
<img
# ... (ещё 1 строк) ...
  class="brightness-100 dark:brightness-75 rounded-lg"
  alt="Фото"
>
```

### Инверсия для иконок

```html
<!-- Специальный класс для инверсии чёрно-белых изображений -->
<img
  src="icon.png"
  class="dark:invert"
  alt="Иконка"
>
```

### 4. 🎨 Градиенты с dark mode

```html
<!-- Светлая тема: яркий градиент -->
<!-- Тёмная тема: более приглушённый -->
<div class="bg-gradient-to-br from-blue-500 to-purple-600 dark:from-blue-700 dark:to-purple-900 p-8 rounded-xl text-white">
# ... (ещё 2 строк) ...
    Цвета градиента адаптируются под тему
  </p>
</div>
```

## ⚙️ Кастомные цвета для dark mode

### Через CSS-переменные (рекомендуется)

```js
// tailwind.config.js
module.exports = {
  darkMode: 'class',
# ... (ещё 12 строк) ...
    },
  },
}
```

```css
/* styles.css */
:root {
  --surface: 255 255 255;           /* white */
# ... (ещё 8 строк) ...
  --content: 243 244 246;           /* gray-100 */
  --content-secondary: 156 163 175; /* gray-400 */
}
```

```html
<!-- Автоматически адаптируется -->
<div class="bg-surface text-content">
  <p class="text-content-secondary">Вторичный текст</p>
</div>
```

### Преимущества подхода

- ✅ **Один класс** вместо `bg-white dark:bg-gray-900`

- ✅ **Централизованное управление** цветами

- ✅ **Легко менять палитру** — правим только CSS-переменные

- ✅ **Поддержка прозрачности** — `bg-surface/50`

## 📊 Шпаргалка: что когда использовать

| Задача | Классы |
| :-- | :-- |
| Фон | `bg-white dark:bg-gray-900` |
| Текст | `text-gray-900 dark:text-gray-100` |
| Вторичный текст | `text-gray-600 dark:text-gray-400` |
| Граница | `border-gray-200 dark:border-gray-700` |
| Hover фон | `hover:bg-gray-100 dark:hover:bg-gray-800` |
| Input фон | `bg-white dark:bg-gray-700` |
| Input граница | `border-gray-300 dark:border-gray-600` |
| Placeholder | `placeholder-gray-400 dark:placeholder-gray-500` |
| Бейдж | `bg-blue-100 dark:bg-blue-900/30 text-blue-800 dark:text-blue-300` |
| Тень | `shadow-md dark:shadow-gray-900/50` |
| Разделитель | `divide-gray-200 dark:divide-gray-700` |
| Инверсия SVG | `dark:invert` |
| Затемнение фото | `brightness-100 dark:brightness-75` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Забывают настроить `darkMode: 'class'`

```js
// ❌ Плохо: по умолчанию используется media
module.exports = {
  // darkMode не указан
# ... (ещё 3 строк) ...
module.exports = {
  darkMode: 'class',
}
```

### ❌ Ошибка 2: `dark:` без парного светлого класса

```html
<!-- ❌ Плохо: в светлой теме фон не задан -->
<div class="dark:bg-gray-900">Нет светлого фона</div>

<!-- ✅ Хорошо: оба варианта -->
<div class="bg-white dark:bg-gray-900">Оба варианта</div>
```

### ❌ Ошибка 3: Мигание темы при загрузке

### ❌ Ошибка 4: Игнорируют системные настройки

```js
// ❌ Плохо: только localStorage
const theme = localStorage.getItem('theme');

// ✅ Хорошо: localStorage + системные настройки
const theme = localStorage.getItem('theme') ||
  (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
```

### ❌ Ошибка 5: Используют `dark:` для акцентных цветов

```html
<!-- ❌ Плохо: акцентный синий не должен меняться -->
<button class="bg-blue-600 dark:bg-blue-400">
  Акцент меняется — плохо
# ... (ещё 3 строк) ...
<button class="bg-blue-600 hover:bg-blue-700 text-white">
  Акцент стабилен
</button>
```

### ❌ Ошибка 6: Забывают про тени в dark mode

```html
<!-- ❌ Плохо: чёрная тень на тёмном фоне не видна -->
<div class="bg-gray-900 shadow-lg">Тень не видна</div>

# ... (ещё 1 строк) ...
<div class="bg-gray-900 shadow-lg shadow-gray-900/50 dark:shadow-black/50">
  Тень видна
</div>
```

### ❌ Ошибка 7: Чистый белый в dark mode

```html
<!-- ❌ Плохо: слишком яркий контраст -->
<div class="bg-white dark:bg-white">Белый в dark mode</div>

<!-- ✅ Хорошо: используем оттенки серого -->
<div class="bg-white dark:bg-gray-900">Комфортный контраст</div>
```

### ❌ Ошибка 8: Забывают про focus-состояния

```html
<!-- ❌ Плохо: focus ring не виден в dark mode -->
<input class="focus:ring-2 focus:ring-blue-500">

<!-- ✅ Хорошо: настраиваем ring для dark mode -->
<input class="focus:ring-2 focus:ring-blue-500 dark:focus:ring-blue-400">
```

# 🎯 Состояния элементов в Tailwind CSS

## 🎨 Основные модификаторы состояний

Tailwind предоставляет **модификаторы состояний**, которые применяются **перед утилитарным классом** через двоеточие:

```
hover:bg-blue-600
focus:ring-2
active:scale-95
disabled:opacity-50
```

### Порядок имеет значение

```html
<!-- ✅ Правильно: hover перед focus -->
<button class="hover:bg-blue-600 focus:ring-2">...</button>

<!-- ❌ Неправильно: focus перед hover (может не работать) -->
<button class="focus:ring-2 hover:bg-blue-600">...</button>
```

## 🔥 Hover: `hover:`

Применяется при наведении курсора мыши:

### Hover с transition

Всегда добавляйте `transition` для плавных изменений:

### Доступные transition-утилиты

| Класс | CSS |
| :-- | :-- |
| `transition-none` | `transition-property: none` |
| `transition-all` | `transition-property: all` |
| `transition` | `transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter` |
| `transition-colors` | `transition-property: color, background-color, border-color, text-decoration-color, fill, stroke` |
| `transition-opacity` | `transition-property: opacity` |
| `transition-shadow` | `transition-property: box-shadow` |
| `transition-transform` | `transition-property: transform` |

### Длительность transition

| Класс | CSS |
| :-- | :-- |
| `duration-75` | `transition-duration: 75ms` |
| `duration-100` | `transition-duration: 100ms` |
| `duration-150` | `transition-duration: 150ms` |
| `duration-200` | `transition-duration: 200ms` |
| `duration-300` | `transition-duration: 300ms` |
| `duration-500` | `transition-duration: 500ms` |
| `duration-700` | `transition-duration: 700ms` |
| `duration-1000` | `transition-duration: 1000ms` |

### Функции easing

| Класс | CSS | Описание |
| :-- | :-- | :-- |
| `ease-linear` | `transition-timing-function: linear` | Линейная |
| `ease-in` | `transition-timing-function: cubic-bezier(0.4, 0, 1, 1)` | Ускорение |
| `ease-out` | `transition-timing-function: cubic-bezier(0, 0, 0.2, 1)` | Замедление |
| `ease-in-out` | `transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1)` | Ускорение и замедление |

## 🎯 Focus: `focus:`

Применяется когда элемент получает фокус (клавиатурой или мышью):

### Focus-within: `focus-within:`

Применяется когда **любой дочерний элемент** получает фокус:

```html
<!-- Подсветка контейнера при фокусе на input -->
<div class="border border-gray-300 focus-within:border-blue-500 focus-within:ring-2 focus-within:ring-blue-500/20 rounded-lg p-2">
  <input
# ... (ещё 2 строк) ...
    placeholder="Фокус подсветит контейнер"
  >
</div>
```

### Focus-visible: `focus-visible:`

Применяется только при **клавиатурной навигации** (Tab), но не при клике мышью:

```html
<!-- Focus ring только при клавиатурной навигации -->
<button class="focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2">
  Кнопка с focus-visible
</button>
```

> 💡 **Когда использовать:** `focus-visible` — современный подход для accessibility. Пользователи мыши не видят ring, но клавиатурные пользователи видят.

### Разница между focus, focus-within, focus-visible

| Модификатор | Когда применяется |
| :-- | :-- |
| `focus:` | Элемент получил фокус (мышь или клавиатура) |
| `focus-within:` | Любой дочерний элемент получил фокус |
| `focus-visible:` | Элемент получил фокус через клавиатуру |

## 🔘 Active: `active:`

Применяется в момент **нажатия** (между mousedown и mouseup):

```html
<!-- Кнопка "вдавливается" при клике -->
<button class="bg-blue-500 hover:bg-blue-600 active:bg-blue-700 active:scale-95 transition-all">
  Нажми меня
# ... (ещё 3 строк) ...
<a href="#" class="text-blue-600 hover:text-blue-700 active:text-blue-800">
  Ссылка
</a>
```

## 🚫 Disabled: `disabled:`

Применяется к элементам с атрибутом `disabled`:

## 👥 Group-hover: `group-hover:`

Применяется к **дочерним элементам** при hover на **родительском** элементе с классом `group`:

### Group-focus, group-active

## 🤝 Peer: `peer-*:`

Применяется к **соседним элементам** на основе состояния **предыдущего** элемента с классом `peer`:

### Peer-checked для чекбоксов и радиокнопок

```html
<!-- Кастомный чекбокс -->
<label class="flex items-center gap-3 cursor-pointer">
  <input type="checkbox" class="peer sr-only">
# ... (ещё 4 строк) ...
  </div>
  <span class="text-gray-700">Согласен с условиями</span>
</label>
```

### Peer-disabled

```html
<!-- Label меняется при disabled input -->
<div class="flex items-center gap-2">
  <input type="checkbox" id="option" disabled class="peer">
# ... (ещё 1 строк) ...
    Опция (недоступна)
  </label>
</div>
```

## ✅ Состояния форм

### Checked: `checked:`

```html
<!-- Кастомный чекбокс -->
<label class="flex items-center gap-2 cursor-pointer">
  <input type="checkbox" class="peer sr-only">
  <div class="w-5 h-5 border-2 border-gray-300 rounded peer-checked:bg-blue-500 peer-checked:border-blue-500"></div>
  <span>Выбрать</span>
</label>
```

### Indeterminate: `indeterminate:`

```html
<!-- Чекбокс в неопределённом состоянии -->
<input type="checkbox" class="indeterminate:bg-gray-400" id="select-all">
```

### Required: `required:`

```html
<!-- Звёздочка для обязательных полей -->
<label>
  Email <span class="required:text-red-500">*</span>
</label>
<input type="email" required class="required:border-red-500">
```

### Invalid: `invalid:`

```html
<!-- Красная граница при невалидном email -->
<input
  type="email"
  class="border border-gray-300 invalid:border-red-500 invalid:text-red-600 focus:outline-none focus:ring-2 focus:ring-blue-500 invalid:focus:ring-red-500"
  placeholder="you@example.com"
>
```

### Placeholder-shown: `placeholder-shown:`

### Autofill: `autofill:`

```html
<!-- Стилизация автозаполнения браузера -->
<input
  type="text"
  class="autofill:bg-yellow-100 autofill:text-yellow-900"
>
```

## 🎯 Комбинирование состояний

### Несколько состояний одновременно

```html
<!-- Hover + focus + active -->
<button class="
  bg-blue-500
# ... (ещё 4 строк) ...
">
  Кнопка
</button>
```

### Состояния + responsive

```html
<!-- Hover только на десктопе -->
<button class="hover:bg-blue-600 md:hover:bg-blue-700 lg:hover:bg-blue-800">
  Адаптивный hover
</button>
```

### Состояния + dark mode

```html
<!-- Hover в обеих темах -->
<button class="
  bg-blue-500 dark:bg-blue-600
# ... (ещё 2 строк) ...
">
  Кнопка
</button>
```

### Состояния + group-hover + peer

```html
<!-- Сложное взаимодействие -->
<div class="group">
  <input type="checkbox" class="peer sr-only">
# ... (ещё 4 строк) ...
    Текст
  </span>
</div>
```

## 📊 Шпаргалка: что когда использовать

| Задача | Модификатор |
| :-- | :-- |
| Hover эффект | `hover:` |
| Focus ring | `focus:ring-2 focus:ring-blue-500` |
| Focus только клавиатура | `focus-visible:` |
| Focus на дочерних | `focus-within:` |
| Активное состояние (клик) | `active:` |
| Disabled состояние | `disabled:` |
| Hover на родителе | `group` + `group-hover:` |
| Состояние предыдущего элемента | `peer` + `peer-checked:`, `peer-focus:` |
| Checked чекбокс | `peer-checked:` |
| Invalid input | `invalid:` |
| Required поле | `required:` |
| Placeholder показан | `placeholder-shown:` |
| Autofill браузера | `autofill:` |
| Плавный переход | `transition-all duration-200` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Забывают `transition` для hover-эффектов

```html
<!-- ❌ Плохо: резкое изменение -->
<button class="bg-blue-500 hover:bg-blue-600">Резко</button>

<!-- ✅ Хорошо: плавное изменение -->
<button class="bg-blue-500 hover:bg-blue-600 transition-colors duration-200">Плавно</button>
```

### ❌ Ошибка 2: `focus:` без `focus:outline-none`

```html
<!-- ❌ Плохо: двойная обводка (стандартная + ring) -->
<input class="focus:ring-2 focus:ring-blue-500">

<!-- ✅ Хорошо: убираем стандартный outline -->
<input class="focus:outline-none focus:ring-2 focus:ring-blue-500">
```

### ❌ Ошибка 3: `group-hover:` без класса `group` на родителе

```html
<!-- ❌ Плохо: group-hover не работает -->
<div>
  <span class="group-hover:text-blue-600">Не работает</span>
# ... (ещё 3 строк) ...
<div class="group">
  <span class="group-hover:text-blue-600">Работает</span>
</div>
```

### ❌ Ошибка 4: `peer:` без класса `peer` на предыдущем элементе

```html
<!-- ❌ Плохо: peer не работает -->
<input type="checkbox">
<span class="peer-checked:text-blue-600">Не работает</span>
# ... (ещё 1 строк) ...
<!-- ✅ Хорошо: добавляем peer -->
<input type="checkbox" class="peer">
<span class="peer-checked:text-blue-600">Работает</span>
```

### ❌ Ошибка 5: Неправильный порядок состояний

```html
<!-- ❌ Плохо: focus перед hover -->
<button class="focus:ring-2 hover:bg-blue-600">Неправильный порядок</button>

<!-- ✅ Хорошо: hover перед focus -->
<button class="hover:bg-blue-600 focus:ring-2">Правильный порядок</button>
```

### ❌ Ошибка 6: Забывают про accessibility

```html
<!-- ❌ Плохо: нет focus-состояния для клавиатурных пользователей -->
<button class="hover:bg-blue-600">Нет focus</button>

# ... (ещё 1 строк) ...
<button class="hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500">
  Есть focus
</button>
```

### ❌ Ошибка 7: `hover:` на мобильных устройствах

```html
<!-- ❌ Плохо: hover "залипает" на мобильных -->
<button class="hover:bg-blue-600">Hover на мобильных</button>

<!-- ✅ Хорошо: используем hover только на десктопе -->
<button class="md:hover:bg-blue-600">Hover только на десктопе</button>
```

### ❌ Ошибка 8: Слишком много transition-свойств

```html
<!-- ❌ Плохо: transition-all может тормозить -->
<div class="transition-all duration-500">Тяжёлая анимация</div>

<!-- ✅ Хорошо: transition только для нужных свойств -->
<div class="transition-colors duration-200">Лёгкая анимация</div>
```

# 🔴 Раздел: Advanced

# ⚙️ Кастомизация Tailwind CSS

## 📁 Структура `tailwind.config.js`

Полный конфиг выглядит так:

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  // 1. Какие файлы сканировать
# ... (ещё 38 строк) ...
  // 8. Вариации (какие состояния генерировать)
  variants: {},
}
```

## 🎨 Расширение темы: `theme.extend`

### Добавление своих цветов

```js
// tailwind.config.js
module.exports = {
  theme: {
# ... (ещё 26 строк) ...
    },
  },
}
```

```html
<!-- Использование -->
<div class="bg-brand-500 text-white">Брендовый цвет</div>
<button class="bg-success hover:bg-success/90 text-white">Успех</button>
```

### Добавление своих отступов

```js
module.exports = {
  theme: {
    extend: {
# ... (ещё 7 строк) ...
    },
  },
}
```

```html
<div class="p-18">Кастомный padding 72px</div>
<div class="h-screen/2">Половина экрана</div>
```

### Добавление своих размеров шрифтов

```js
module.exports = {
  theme: {
    extend: {
# ... (ещё 4 строк) ...
    },
  },
}
```

```html
<p class="text-2xs">Микро-текст</p>
<h1 class="text-display">Огромный заголовок</h1>
```

### Добавление своих breakpoints

```js
module.exports = {
  theme: {
    extend: {
# ... (ещё 9 строк) ...
    },
  },
}
```

```html
<!-- Использование -->
<div class="text-sm xs:text-base md:text-lg laptop:text-xl">
  Адаптивный текст
# ... (ещё 1 строк) ...

<!-- Только для портретной ориентации -->
<div class="portrait:hidden">Скрыть в портрете</div>
```

### Добавление своих шрифтов

```js
module.exports = {
  theme: {
    extend: {
# ... (ещё 6 строк) ...
    },
  },
}
```

### Добавление своих теней

```js
module.exports = {
  theme: {
    extend: {
# ... (ещё 6 строк) ...
    },
  },
}
```

```html
<div class="shadow-glow-blue">Светящаяся синяя тень</div>
<button class="shadow-3d">3D кнопка</button>
```

### Добавление своих анимаций

```js
module.exports = {
  theme: {
    extend: {
# ... (ещё 27 строк) ...
    },
  },
}
```

```html
<div class="animate-fade-in">Плавное появление</div>
<div class="animate-slide-up">Скольжение вверх</div>
```

## 🔄 Полная замена темы

Если вам нужно **полностью заменить** стандартную тему (а не расширять), используйте `theme` без `extend`:

```js
module.exports = {
  theme: {
    // Полностью заменяет стандартные цвета
# ... (ещё 30 строк) ...
    },
  },
}
```

> ⚠️ **Важно:** при полной замене вы **теряете все стандартные значения**. Используйте только если действительно нужно переопределить всё.

### Комбинирование: extend + полная замена

```js
module.exports = {
  theme: {
    // Полная замена для colors
# ... (ещё 10 строк) ...
    },
  },
}
```

## 🛠 Создание кастомных утилит

### Через `addUtilities` в плагине

```js
// tailwind.config.js
const plugin = require('tailwindcss/plugin')

# ... (ещё 29 строк) ...
    }),
  ],
}
```

```html
<h1 class="text-shadow-lg text-white">Текст с тенью</h1>
<div class="scrollbar-hide overflow-x-auto">...</div>
```

### Динамические утилиты

```js
const plugin = require('tailwindcss/plugin')

module.exports = {
# ... (ещё 11 строк) ...
    }),
  ],
}
```

```html
<h1 class="text-shadow-blue-500">Синяя тень</h1>
<h1 class="text-shadow-red-500">Красная тень</h1>
```

## 🧩 Создание компонентов

Компоненты — это **переиспользуемые группы утилит**, которые применяются через один класс:

```js
const plugin = require('tailwindcss/plugin')

module.exports = {
# ... (ещё 45 строк) ...
    }),
  ],
}
```

```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-danger btn-lg">Danger Large</button>
```

### Компоненты с responsive-вариантами

```js
const plugin = require('tailwindcss/plugin')

module.exports = {
# ... (ещё 31 строк) ...
    }),
  ],
}
```

## 🔌 Плагины

### Подключение готовых плагинов

```bash
npm install -D @tailwindcss/forms @tailwindcss/typography @tailwindcss/aspect-ratio @tailwindcss/container-queries
```

```js
// tailwind.config.js
module.exports = {
  plugins: [
# ... (ещё 3 строк) ...
    require('@tailwindcss/container-queries'), // Container queries
  ],
}
```

### Пример: @tailwindcss/forms

```html
<!-- Без плагина: нужно стилизовать каждое поле -->
<input type="text" class="border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500">

# ... (ещё 1 строк) ...
<input type="text" class="form-input rounded border-gray-300 focus:border-blue-500 focus:ring-blue-500">
<select class="form-select rounded border-gray-300">...</select>
<input type="checkbox" class="form-checkbox rounded border-gray-300 text-blue-600">
```

### Пример: @tailwindcss/typography

Варианты:

- `prose` — базовый

- `prose-sm`, `prose-base`, `prose-lg`, `prose-xl`, `prose-2xl` — размеры

- `prose-slate`, `prose-gray`, `prose-zinc`, `prose-neutral`, `prose-stone` — цвета

- `prose-invert` — для тёмной темы

### Создание собственного плагина

```js
// plugins/text-shadow.js
const plugin = require('tailwindcss/plugin')

# ... (ещё 12 строк) ...

  addUtilities(textShadows, ['responsive', 'hover'])
})
```

```js
// tailwind.config.js
module.exports = {
  plugins: [
    require('./plugins/text-shadow.js'),
  ],
}
```

### Плагин с конфигурацией

```js
// plugins/badges.js
const plugin = require('tailwindcss/plugin')

# ... (ещё 28 строк) ...
    }
  }
)
```

```js
// tailwind.config.js
module.exports = {
  plugins: [
# ... (ещё 2 строк) ...
    }),
  ],
}
```

```html
<span class="badge-primary">Primary</span>
<span class="badge-success">Success</span>
<span class="badge-danger">Danger</span>
```

## 📦 Presets

Presets позволяют **переиспользовать конфигурацию** между проектами:

```js
// presets/company-preset.js
module.exports = {
  theme: {
# ... (ещё 14 строк) ...
    require('@tailwindcss/forms'),
  ],
}
```

```js
// tailwind.config.js
module.exports = {
  presets: [
# ... (ещё 9 строк) ...
    },
  },
}
```

### 1. 🎨 Полная дизайн-система

```js
// tailwind.config.js
module.exports = {
  theme: {
# ... (ещё 72 строк) ...
    require('./plugins/text-shadow.js'),
  ],
}
```

### 2. 🎨 CSS-переменные для динамической темизации

```js
// tailwind.config.js
module.exports = {
  theme: {
# ... (ещё 9 строк) ...
    },
  },
}
```

```css
/* styles.css */
:root {
  --color-primary: 14 165 233;        /* #0ea5e9 */
# ... (ещё 12 строк) ...
  --color-content: 243 244 246;       /* gray-100 */
  --color-content-secondary: 156 163 175; /* gray-400 */
}
```

### 3. 🔌 Плагин для кастомных кнопок

```js
// plugins/buttons.js
const plugin = require('tailwindcss/plugin')

# ... (ещё 48 строк) ...
    },
  ])
})
```

```html
<button class="btn btn-md btn-primary">Primary</button>
<button class="btn btn-lg btn-secondary">Secondary</button>
<button class="btn btn-sm btn-outline">Outline</button>
<button class="btn btn-md btn-ghost">Ghost</button>
<button class="btn btn-md btn-primary" disabled>Disabled</button>
```

## 📊 Шпаргалка: что когда использовать

| Задача | Решение |
| :-- | :-- |
| Добавить свой цвет | `theme.extend.colors` |
| Заменить все цвета | `theme.colors` (без extend) |
| Добавить свой отступ | `theme.extend.spacing` |
| Добавить свой шрифт | `theme.extend.fontFamily` |
| Добавить свой breakpoint | `theme.extend.screens` |
| Добавить свою тень | `theme.extend.boxShadow` |
| Добавить свою анимацию | `theme.extend.animation` + `keyframes` |
| Создать утилиту | `addUtilities` в плагине |
| Создать компонент | `addComponents` в плагине |
| Переиспользовать конфиг | `presets` |
| Динамическая темизация | CSS-переменные + `theme.extend.colors` |
| Подключить готовый плагин | `plugins: [require('@tailwindcss/forms')]` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Забывают `content` в конфиге

```js
// ❌ Плохо: Tailwind не найдёт классы
module.exports = {
  theme: {
# ... (ещё 18 строк) ...
    },
  },
}
```

### ❌ Ошибка 2: Полная замена вместо расширения

```js
// ❌ Плохо: теряем все стандартные цвета
module.exports = {
  theme: {
# ... (ещё 13 строк) ...
    },
  },
}
```

### ❌ Ошибка 3: Конфликт имён со стандартными утилитами

```js
// ❌ Плохо: конфликт с .text-red-500
module.exports = {
  theme: {
# ... (ещё 15 строк) ...
    },
  },
}
```

### ❌ Ошибка 4: Забывают про `<alpha-value>` для CSS-переменных

```js
// ❌ Плохо: bg-primary/50 не будет работать
module.exports = {
  theme: {
# ... (ещё 15 строк) ...
    },
  },
}
```

### ❌ Ошибка 5: Изменяют конфиг без перезапуска

```bash
# ❌ Плохо: изменения не применятся
# Просто редактируем tailwind.config.js

# ... (ещё 1 строк) ...
npm run dev
# или
npx tailwindcss -i ./src/input.css -o ./src/output.css --watch
```

### ❌ Ошибка 6: Слишком много кастомных утилит

```js
// ❌ Плохо: раздуваем CSS
const plugin = require('tailwindcss/plugin')

# ... (ещё 13 строк) ...
// ✅ Хорошо: используем стандартные утилиты или arbitrary values
<div class="text-red-500 bg-blue-500 p-4">...</div>
<div class="text-[#ff0000] bg-[#0000ff]">...</div>
```

# 📝 Директивы в Tailwind CSS

## 🎯 Что такое директивы?

**Директивы** — это специальные CSS-конструкции, которые Tailwind обрабатывает при сборке. Они позволяют:

- Подключать базовые стили Tailwind

- Переиспользовать утилиты в кастомном CSS

- Управлять порядком применения стилей

- Получать значения из конфигурации

## 📦 Директива `@tailwind`

### Базовое подключение

`@tailwind` — это **главная директива**, которая подключает стили Tailwind в ваш CSS-файл:

```css
/* styles.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### Что делает каждая директива

| Директива | Что подключает | Когда нужна |
| :-- | :-- | :-- |
| `@tailwind base` | CSS-сброс (Preflight), базовые стили HTML | Всегда |
| `@tailwind components` | Стили компонентов из плагинов | Всегда |
| `@tailwind utilities` | Все утилитарные классы | Всегда |

### Preflight (CSS Reset)

`@tailwind base` включает **Preflight** — современную версию CSS reset:

```css
/* Что делает Preflight: */
/* 1. Убирает margin у всех элементов */
*, *::before, *::after {
# ... (ещё 24 строк) ...
  color: inherit;
  text-decoration: inherit;
}
```

> 💡 **Важно:** Preflight **агрессивно сбрасывает стили**. Если вы не хотите его использовать, можно отключить:

```js
// tailwind.config.js
module.exports = {
  corePlugins: {
    preflight: false,
  },
}
```

### Порядок директив имеет значение

```css
/* ✅ Правильно: base → components → utilities */
@tailwind base;
@tailwind components;
# ... (ещё 3 строк) ...
@tailwind utilities;
@tailwind components;
@tailwind base;
```

## 🎨 Директива `@apply`

`@apply` позволяет **встраивать утилитарные классы** в кастомный CSS:

### Базовое использование

```css
/* styles.css */
.btn-primary {
  @apply bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600;
# ... (ещё 2 строк) ...
.card {
  @apply bg-white rounded-lg shadow-md p-6;
}
```

```html
<!-- Использование -->
<button class="btn-primary">Кнопка</button>
<div class="card">Карточка</div>
```

### Когда использовать `@apply`

#### ✅ Хорошо использовать для:

1. **Повторяющихся паттернов**

```css
/* Вместо дублирования */
.btn {
  @apply px-4 py-2 rounded font-medium transition-colors;
# ... (ещё 6 строк) ...
.btn-secondary {
  @apply btn bg-gray-500 text-white hover:bg-gray-600;
}
```

2. **Интеграции с CMS** (WordPress, Ghost)

```css
/* Стили для контента из CMS */
.prose h1 {
  @apply text-4xl font-bold text-gray-900 mb-4;
# ... (ещё 10 строк) ...
.prose a {
  @apply text-blue-600 hover:underline;
}
```

3. **Компонентов в Vue/React**

#### ❌ Не стоит использовать для:

1. **Одноразовых стилей**

```css
/* ❌ Плохо: это не переиспользуется */
.my-special-button {
  @apply bg-blue-500 text-white px-4 py-2 rounded;
# ... (ещё 3 строк) ...
<button class="bg-blue-500 text-white px-4 py-2 rounded">
  Кнопка
</button>
```

2. **Когда можно использовать компоненты фреймворка**

### Ограничения `@apply`

#### ❌ Нельзя использовать с arbitrary values

```css
/* ❌ Плохо: arbitrary values не работают с @apply */
.custom {
  @apply bg-[#ff5722] text-[15px];
# ... (ещё 4 строк) ...
  background-color: #ff5722;
  font-size: 15px;
}
```

#### ❌ Нельзя использовать с модификаторами состояний

```css
/* ❌ Плохо: hover: не работает в @apply */
.btn {
  @apply bg-blue-500 hover:bg-blue-600;
# ... (ещё 7 строк) ...
.btn:hover {
  @apply bg-blue-600;
}
```

#### ❌ Нельзя использовать с responsive-модификаторами

```css
/* ❌ Плохо: md: не работает в @apply */
.container {
  @apply w-full md:w-1/2 lg:w-1/3;
# ... (ещё 15 строк) ...
    @apply w-1/3;
  }
}
```

## 📚 Директива `@layer`

`@layer` управляет **порядком применения стилей** и помогает избежать проблем со специфичностью:

### Базовое использование

```css
/* styles.css */
@tailwind base;
@tailwind components;
# ... (ещё 23 строк) ...
    text-shadow: 2px 2px 4px rgb(0 0 0 / 0.5);
  }
}
```

### Зачем нужны слои?

**Проблема без `@layer`:**

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
# ... (ещё 2 строк) ...
.btn {
  background-color: blue;
}
```

```html
<!-- Ожидание: bg-red-500 -->
<!-- Реальность: синий фон (переопределён) -->
<button class="btn bg-red-500">Кнопка</button>
```

**Решение с `@layer`:**

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
# ... (ещё 3 строк) ...
    background-color: blue;
  }
}
```

```html
<!-- Теперь bg-red-500 работает корректно -->
<button class="btn bg-red-500">Кнопка</button>
```

### Порядок слоёв

```
1. @layer base        (самый низкий приоритет)
2. @layer components
3. @layer utilities
4. Кастомный CSS      (самый высокий приоритет)
```

### Практический пример

```css
/* styles.css */
@tailwind base;
@tailwind components;
# ... (ещё 56 строк) ...
    display: none;
  }
}
```

## 🎯 Функция `theme()`

`theme()` позволяет **получать значения из конфигурации** прямо в CSS:

### Базовое использование

```css
/* styles.css */
.custom-shadow {
  box-shadow: 0 4px 6px -1px theme('colors.blue.500');
# ... (ещё 6 строк) ...
.custom-spacing {
  padding: theme('spacing.4');
}
```

### Доступ к значениям темы

```css
/* Цвета */
.btn-primary {
  background-color: theme('colors.blue.500');
# ... (ещё 25 строк) ...
    max-width: 768px;
  }
}
```

### Dot notation vs bracket notation

```css
/* Dot notation (проще) */
.btn {
  background-color: theme('colors.blue.500');
# ... (ещё 5 строк) ...
  /* или */
  background-color: theme('colors[blue-gray].500');
}
```

### Fallback значения

```css
/* С fallback значением */
.custom-color {
  color: theme('colors.brand.500', #ff5722);
}
```

### Практический пример

```css
/* styles.css */
@tailwind base;
@tailwind components;
# ... (ещё 24 строк) ...
    box-shadow: theme('boxShadow.lg');
  }
}
```

## 📱 Директива `@screen`

`@screen` позволяет создавать **медиа-запросы на основе breakpoints** из конфига:

### Базовое использование

```css
/* styles.css */
@screen md {
  .container {
# ... (ещё 6 строк) ...
    max-width: 1024px;
  }
}
```

Это эквивалентно:

```css
@media (min-width: 768px) {
  .container {
    max-width: 768px;
# ... (ещё 5 строк) ...
    max-width: 1024px;
  }
}
```

### Преимущества `@screen`

1. **Синхронизация с конфигом**

```js
// tailwind.config.js
module.exports = {
  theme: {
# ... (ещё 4 строк) ...
    },
  },
}
```

```css
/* Автоматически использует значения из конфига */
@screen tablet {
  .container {
# ... (ещё 6 строк) ...
    max-width: 1024px;
  }
}
```

2. **Меньше дублирования**

```css
/* ❌ Плохо: дублирование значений */
@media (min-width: 768px) {
  .card {
# ... (ещё 19 строк) ...
    @apply grid grid-cols-3;
  }
}
```

### Комбинирование с `@apply`

```css
@screen md {
  .hero {
    @apply flex items-center justify-between;
# ... (ещё 13 строк) ...
    @apply text-6xl;
  }
}
```

### Практический пример

```css
/* styles.css */
@tailwind base;
@tailwind components;
# ... (ещё 28 строк) ...
    }
  }
}
```

## 🔧 Директива `@config`

`@config` позволяет **указать путь к конфигу** прямо в CSS-файле:

```css
/* styles.css */
@config "./tailwind.config.js";

@tailwind base;
@tailwind components;
@tailwind utilities;
```

Это полезно, когда:

- У вас несколько CSS-файлов с разными конфигами

- Вы хотите явно указать, какой конфиг использовать

### 1. 🎨 Дизайн-система через `@layer`

```css
/* styles.css */
@tailwind base;
@tailwind components;
# ... (ещё 118 строк) ...
    display: none;
  }
}
```

### 2. 🎨 Типографика для CMS

```css
/* styles.css */
@layer components {
  .prose {
# ... (ещё 60 строк) ...
    @apply border border-gray-300 px-4 py-2;
  }
}
```

### 3. 🎨 Анимации через `@layer`

```css
/* styles.css */
@layer utilities {
  @keyframes fade-in {
# ... (ещё 54 строк) ...
    animation: scale-in 0.2s ease-out;
  }
}
```

### 4. 🎨 Темизация через CSS-переменные

```css
/* styles.css */
@layer base {
  :root {
# ... (ещё 42 строк) ...
    color: rgb(var(--color-content-secondary));
  }
}
```

### 5. 🎨 Печать стилей

```css
/* styles.css */
@media print {
  .no-print {
# ... (ещё 16 строк) ...
    @apply hidden;
  }
}
```

## 📊 Шпаргалка: что когда использовать

| Задача | Решение |
| :-- | :-- |
| Подключить Tailwind | `@tailwind base; @tailwind components; @tailwind utilities;` |
| Переиспользовать утилиты | `@apply bg-blue-500 text-white` |
| Управлять порядком стилей | `@layer base/components/utilities` |
| Получить значение из темы | `theme('colors.blue.500')` |
| Медиа-запрос из конфига | `@screen md { ... }` |
| Указать путь к конфигу | `@config "./tailwind.config.js"` |
| Отключить Preflight | `corePlugins: { preflight: false }` |
| Добавить кастомную утилиту | `@layer utilities { .my-utility { ... } }` |
| Добавить компонент | `@layer components { .my-component { ... } }` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: `@apply` с модификаторами состояний

```css
/* ❌ Плохо: hover: не работает в @apply */
.btn {
  @apply bg-blue-500 hover:bg-blue-600;
# ... (ещё 7 строк) ...
.btn:hover {
  @apply bg-blue-600;
}
```

### ❌ Ошибка 2: `@apply` с responsive-модификаторами

```css
/* ❌ Плохо: md: не работает в @apply */
.container {
  @apply w-full md:w-1/2;
# ... (ещё 9 строк) ...
    @apply w-1/2;
  }
}
```

### ❌ Ошибка 3: Забывают порядок `@tailwind`

```css
/* ❌ Плохо: утилиты перекроют компоненты */
@tailwind utilities;
@tailwind components;
# ... (ещё 3 строк) ...
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### ❌ Ошибка 4: Кастомный CSS без `@layer`

```css
/* ❌ Плохо: кастомный CSS может переопределить утилиты */
@tailwind base;
@tailwind components;
# ... (ещё 2 строк) ...
.btn {
  background-color: blue;
}
```

```html
<!-- Ожидание: bg-red-500 -->
<!-- Реальность: синий фон -->
<button class="btn bg-red-500">Кнопка</button>
```

```css
/* ✅ Хорошо: используем @layer */
@tailwind base;
@tailwind components;
# ... (ещё 4 строк) ...
    background-color: blue;
  }
}
```

### ❌ Ошибка 5: `theme()` без кавычек

```css
/* ❌ Плохо: синтаксическая ошибка */
.btn {
  background-color: theme(colors.blue.500);
# ... (ещё 3 строк) ...
.btn {
  background-color: theme('colors.blue.500');
}
```

### ❌ Ошибка 6: `@screen` с несуществующим breakpoint

```js
// tailwind.config.js
module.exports = {
  theme: {
# ... (ещё 3 строк) ...
    },
  },
}
```

```css
/* ❌ Плохо: breakpoint 'xl' не определён */
@screen xl {
  .container {
# ... (ещё 7 строк) ...
    max-width: 1024px;
  }
}
```

### ❌ Ошибка 7: `@apply` с arbitrary values

```css
/* ❌ Плохо: arbitrary values не работают */
.custom {
  @apply bg-[#ff5722] text-[15px];
# ... (ещё 4 строк) ...
  background-color: #ff5722;
  font-size: 15px;
}
```

### ❌ Ошибка 8: Забывают `@tailwind utilities`

```css
/* ❌ Плохо: утилиты не подключены */
@tailwind base;
@tailwind components;
# ... (ещё 2 строк) ...
@tailwind base;
@tailwind components;
@tailwind utilities;
```

# ⚡ Оптимизация Tailwind CSS

## 📊 Размеры Tailwind: до и после оптимизации

Посмотрим на разницу между dev и production:

| Состояние | Размер (gzip) | Описание |
| :-- | :-- | :-- |
| **Tailwind без очистки** | ~3-4 MB | Все 50 000+ утилит |
| **С JIT + content** | ~5-15 KB | Только используемые классы |
| **После минификации** | ~3-10 KB | Финальный production CSS |

> 💡 **Факт:** правильно настроенный Tailwind в production весит **меньше**, чем один файл Bootstrap (~25 KB gzip).

## 🚀 JIT-компилятор (Just-In-Time)

С Tailwind v3.0 JIT-компилятор включён **по умолчанию**. Это значит:

### Как работает JIT

```
1. Вы пишете HTML с классами:
   <div class="bg-blue-500 hover:bg-blue-600 p-4">

# ... (ещё 2 строк) ...
3. Генерирует CSS ТОЛЬКО для использованных классов

4. Результат: минимальный CSS без мусора
```

### Преимущества JIT

- ⚡ **Мгновенная сборка** — не нужно ждать генерации всех 50 000 классов

- 🎯 **Точная очистка** — в CSS попадают только использованные классы

- 🎨 **Arbitrary values** — `bg-[#ff5722]`, `w-[237px]` работают из коробки

- 📦 **Маленький бандл** — обычно 5-15 KB gzip

## 📁 Настройка `content`

Параметр `content` в `tailwind.config.js` говорит Tailwind, **какие файлы сканировать**:

### Базовая настройка

```js
// tailwind.config.js
module.exports = {
  content: [
# ... (ещё 1 строк) ...
    './public/**/*.html',
  ],
}
```

### Для разных фреймворков

#### React / Next.js

```js
module.exports = {
  content: [
    './src/**/*.{js,jsx,ts,tsx}',
# ... (ещё 2 строк) ...
    './components/**/*.{js,jsx,ts,tsx}',
  ],
}
```

#### Vue / Nuxt

```js
module.exports = {
  content: [
    './src/**/*.{vue,js,ts}',
# ... (ещё 2 строк) ...
    './layouts/**/*.vue',
  ],
}
```

#### Svelte / SvelteKit

```js
module.exports = {
  content: [
    './src/**/*.{html,js,svelte,ts}',
  ],
}
```

#### Laravel / PHP

```js
module.exports = {
  content: [
    './resources/**/*.blade.php',
# ... (ещё 1 строк) ...
    './resources/**/*.vue',
  ],
}
```

#### WordPress

```js
module.exports = {
  content: [
    './**/*.php',
    './src/**/*.{js,jsx,ts,tsx}',
  ],
}
```

### Исключения в `content`

```js
module.exports = {
  content: [
    './src/**/*.{js,jsx,ts,tsx}',
# ... (ещё 1 строк) ...
    '!./src/**/*.stories.{js,tsx}',   // Исключаем Storybook
  ],
}
```

## 🧹 Safelist: защита классов от удаления

Иногда классы генерируются **динамически** (например, через JavaScript), и Tailwind не может их найти в файлах. Используйте `safelist`:

### Базовый safelist

```js
module.exports = {
  content: ['./src/**/*.{js,jsx}'],
  safelist: [
# ... (ещё 3 строк) ...
    'text-white',
  ],
}
```

### Safelist с паттернами

```js
module.exports = {
  content: ['./src/**/*.{js,jsx}'],
  safelist: [
# ... (ещё 7 строк) ...
    'grid-cols-[0-9]+',  // Все grid-cols-N
  ],
}
```

### Когда использовать safelist

#### ✅ Хорошие случаи

```jsx
// Классы генерируются динамически
const colors = ['red', 'green', 'blue', 'yellow'];
const color = colors[Math.floor(Math.random() * colors.length)];

<div className={`bg-${color}-500`}>...</div>
```

```js
// Tailwind не увидит `bg-${color}-500`, поэтому:
module.exports = {
  safelist: [
    { pattern: /bg-(red|green|blue|yellow)-500/ }
  ]
}
```

#### ❌ Плохие случаи

```js
// ❌ Плохо: слишком широкий safelist
module.exports = {
  safelist: [
    { pattern: /.*/ }  // Сохранит ВСЕ классы!
  ]
}
```

## ⚙️ Production build

### Через Tailwind CLI

```bash
# Development (с watch)
npx tailwindcss -i ./src/input.css -o ./src/output.css --watch

# Production (минифицированный)
npx tailwindcss -i ./src/input.css -o ./dist/output.css --minify
```

### Через PostCSS

```js
// postcss.config.js
module.exports = {
  plugins: {
# ... (ещё 2 строк) ...
    ...(process.env.NODE_ENV === 'production' ? { cssnano: {} } : {}),
  },
}
```

### Через Vite

```js
// vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
# ... (ещё 9 строк) ...
    },
  },
})
```

### Через Next.js

Next.js **автоматически** минифицирует CSS в production:

```bash
npm run build  # CSS уже минифицирован
```

## 📉 Минификация CSS

### Через cssnano

```bash
npm install -D cssnano postcss
```

```js
// postcss.config.js
module.exports = {
  plugins: {
# ... (ещё 9 строк) ...
    } : {}),
  },
}
```

### Через Tailwind CLI

```bash
npx tailwindcss -o output.css --minify
```

### Что делает минификация

**До:**

```css
.btn {
  background-color: #3b82f6;
  color: #ffffff;
# ... (ещё 5 строк) ...
.btn:hover {
  background-color: #2563eb;
}
```

**После:**

```css
.btn{background-color:#3b82f6;color:#fff;padding:.5rem 1rem;border-radius:.375rem}.btn:hover{background-color:#2563eb}
```

### Через bundle analyzer

```bash
# Для Vite
npm install -D rollup-plugin-visualizer

# Для Webpack
npm install -D webpack-bundle-analyzer
```

```js
// vite.config.js
import { visualizer } from 'rollup-plugin-visualizer'

# ... (ещё 5 строк) ...
    }),
  ],
})
```

### Через PurgeCSS Standalone

```bash
npm install -g purgecss
purgecss --css output.css --content src/**/*.html --output purged/
```

### Ручная проверка

```bash
# Размер до gzip
ls -lh dist/assets/*.css

# Размер после gzip
gzip -c dist/assets/*.css | wc -c
```

### Chrome DevTools

1. Откройте DevTools → **Network**

2. Загрузите страницу

3. Найдите CSS-файл

4. Посмотрите **Size** (gzip) и **Transferred**

### 1. ⚡ Идеальный production build

```json
// package.json
{
  "scripts": {
# ... (ещё 2 строк) ...
    "build:analyze": "npm run build && gzip -c dist/output.css | wc -c"
  }
}
```

### 2. 🎨 Динамические классы без safelist

Вместо safelist используйте **полные имена классов**:

### 3. 📦 Разделение CSS на чанки

```js
// styles/critical.css — для above-the-fold
@tailwind base;
@tailwind components;
# ... (ещё 8 строк) ...
  .footer { @apply bg-gray-900 text-white p-8; }
  .modal { @apply fixed inset-0 bg-black/50; }
}
```

```html
<head>
  <!-- Critical CSS inline -->
  <style>/* содержимое critical.css */</style>
# ... (ещё 1 строк) ...
  <!-- Deferred CSS async -->
  <link rel="preload" href="/deferred.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
</head>
```

### 4. 🚀 Кэширование CSS

```js
// vite.config.js
export default defineConfig({
  build: {
# ... (ещё 6 строк) ...
    },
  },
})
```

```nginx
# nginx.conf
location /assets/ {
  expires 1y;
  add_header Cache-Control "public, immutable";
}
```

### 5. 🎯 Preload critical CSS

```html
<head>
  <!-- Preload основного CSS -->
  <link rel="preload" href="/assets/main-abc123.css" as="style">
# ... (ещё 2 строк) ...
  <!-- Prefetch для следующих страниц -->
  <link rel="prefetch" href="/assets/about-def456.css">
</head>
```

### 6. 📊 Мониторинг размера CSS в CI

```yaml
# .github/workflows/css-size.yml
name: CSS Size Check
on: [pull_request]
# ... (ещё 12 строк) ...
            echo "⚠️ CSS больше 20KB!"
            exit 1
          fi
```

### Целевые показатели

| Метрика | Цель | Инструмент |
| :-- | :-- | :-- |
| **CSS size (gzip)** | < 15 KB | `gzip -c` |
| **First Contentful Paint** | < 1.8s | Lighthouse |
| **Largest Contentful Paint** | < 2.5s | Lighthouse |
| **Total Blocking Time** | < 200ms | Lighthouse |
| **Cumulative Layout Shift** | < 0.1 | Lighthouse |

## 📊 Шпаргалка: что когда использовать

| Задача | Решение |
| :-- | :-- |
| Production build | `tailwindcss -o output.css --minify` |
| Настроить сканирование | `content: ['./src/**/*.{js,jsx}']` |
| Защитить динамические классы | `safelist: [{ pattern: /bg-/ }]` |
| Минифицировать CSS | `cssnano` или `--minify` |
| Анализ бандла | `rollup-plugin-visualizer` |
| Разделить CSS | Critical + Deferred |
| Кэшировать CSS | Хеш в имени + `Cache-Control` |
| Проверить размер | `gzip -c file.css \| wc -c` |
| Использовать динамические классы | Полные имена вместо конкатенации |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Забывают указать `content`

```js
// ❌ Плохо: Tailwind не знает, что сканировать
module.exports = {
  theme: { extend: { ... } },
# ... (ещё 5 строк) ...
  content: ['./src/**/*.{js,jsx,ts,tsx}'],
  theme: { extend: { ... } },
}
```

**Результат:** CSS будет пустым или содержать все классы.

### ❌ Ошибка 2: Динамическая конкатенация классов

### ❌ Ошибка 3: Safelist со всем подряд

```js
// ❌ Плохо: CSS раздуется до мегабайт
module.exports = {
  safelist: [{ pattern: /.*/ }],
# ... (ещё 5 строк) ...
    { pattern: /bg-(red|green|blue)-500/ }
  ],
}
```

### ❌ Ошибка 4: Не минифицируют в production

```bash
# ❌ Плохо: обычный build в production
npx tailwindcss -o dist/output.css

# ✅ Хорошо: с минификацией
npx tailwindcss -o dist/output.css --minify
```

### ❌ Ошибка 5: Забывают `NODE_ENV=production`

```js
// postcss.config.js
module.exports = {
  plugins: {
# ... (ещё 2 строк) ...
    cssnano: {},
  },
}
```

```bash
# ✅ Хорошо: устанавливаем переменную окружения
NODE_ENV=production npm run build

# Или cross-env для Windows
npm install -D cross-env
cross-env NODE_ENV=production npm run build
```

### ❌ Ошибка 6: Игнорируют gzip

```bash
# ❌ Плохо: смотрим только на "сырой" размер
ls -lh dist/output.css
# 50 KB
# ... (ещё 1 строк) ...
# ✅ Хорошо: gzip-размер (то, что получит пользователь)
gzip -c dist/output.css | wc -c
# 8 KB
```

### ❌ Ошибка 7: Весь CSS в одном файле

```html
<!-- ❌ Плохо: один огромный CSS-файл -->
<link rel="stylesheet" href="/app.css"> <!-- 200 KB -->

<!-- ✅ Хорошо: разделение на critical и deferred -->
<style>/* Critical CSS inline */</style>
<link rel="preload" href="/deferred.css" as="style">
```

### ❌ Ошибка 8: Не анализируют бандл

```bash
# ❌ Плохо: не знаем, что в бандле
npm run build

# ... (ещё 2 строк) ...
npx rollup-plugin-visualizer --open
# или
gzip -c dist/*.css | wc -c
```

### ❌ Ошибка 9: Используют `@import` для больших файлов

```css
/* ❌ Плохо: блокирует рендеринг */
@import url('https://fonts.googleapis.com/...');
@import url('large-library.css');
```

```html
<!-- ✅ Хорошо: async загрузка -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preload" href="large-library.css" as="style" onload="this.rel='stylesheet'">
```

### ❌ Ошибка 10: Нет кэширования

```nginx
# ❌ Плохо: CSS загружается каждый раз
location /assets/ {
  # без кэширования
# ... (ещё 4 строк) ...
  expires 1y;
  add_header Cache-Control "public, immutable";
}
```

# 🔌 Плагины в Tailwind CSS

## 🧩 Что такое плагины?

**Плагины** — это способ расширять функциональность Tailwind CSS. Они позволяют:

- Добавлять **новые утилиты** (например, `text-shadow`, `scrollbar-hide`)

- Создавать **компоненты** (например, `.btn`, `.card`)

- Добавлять **базовые стили** (например, сброс CSS, типографика)

- Расширять **тему** (цвета, шрифты, отступы)

- Добавлять **варианты** (модификаторы состояний)

## 📦 Официальные плагины

### @tailwindcss/forms

Автоматически стилизует формы для консистентного вида:

```bash
npm install -D @tailwindcss/forms
```

```js
// tailwind.config.js
module.exports = {
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
```

```html
<!-- Без плагина: нужно стилизовать каждое поле -->
<input type="text" class="border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500">

# ... (ещё 2 строк) ...
<select class="form-select rounded border-gray-300">...</select>
<input type="checkbox" class="form-checkbox rounded border-gray-300 text-blue-600">
<input type="radio" class="form-radio border-gray-300 text-blue-600">
```

#### Стратегии стилизации

```js
// tailwind.config.js
module.exports = {
  plugins: [
# ... (ещё 2 строк) ...
    }),
  ],
}
```

- `strategy: 'base'` (по умолчанию) — стили применяются ко всем формам

- `strategy: 'class'` — стили только к элементам с классом `form-*`

### @tailwindcss/typography

Добавляет класс `prose` для стилизации HTML-контента:

```bash
npm install -D @tailwindcss/typography
```

```js
// tailwind.config.js
module.exports = {
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
```

#### Варианты `prose`

- **Размеры:** `prose-sm`, `prose-base`, `prose-lg`, `prose-xl`, `prose-2xl`

- **Цвета:** `prose-slate`, `prose-gray`, `prose-zinc`, `prose-neutral`, `prose-stone`

- **Тёмная тема:** `prose-invert`

```html
<!-- Большая типографика в синих тонах -->
<article class="prose prose-lg prose-blue">...</article>

<!-- Тёмная тема -->
<article class="prose prose-invert">...</article>
```

### @tailwindcss/aspect-ratio

Полезно для старых браузеров, которые не поддерживают `aspect-ratio`:

```bash
npm install -D @tailwindcss/aspect-ratio
```

```js
// tailwind.config.js
module.exports = {
  plugins: [
    require('@tailwindcss/aspect-ratio'),
  ],
}
```

```html
<!-- 16:9 видео -->
<div class="aspect-w-16 aspect-h-9">
  <iframe src="..."></iframe>
# ... (ещё 3 строк) ...
<div class="aspect-w-1 aspect-h-1">
  <img src="..." class="object-cover">
</div>
```

### @tailwindcss/container-queries

Добавляет поддержку container queries:

```bash
npm install -D @tailwindcss/container-queries
```

```js
// tailwind.config.js
module.exports = {
  plugins: [
    require('@tailwindcss/container-queries'),
  ],
}
```

```html
<div class="@container">
  <div class="@md:flex @lg:grid @lg:grid-cols-3">
    <!-- Меняет layout в зависимости от ширины контейнера -->
  </div>
</div>
```

## 🛠 Создание собственных плагинов

### Базовая структура

```js
// plugins/my-plugin.js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ addUtilities, addComponents, addBase, theme }) {
  // Ваш код здесь
})
```

### Подключение плагина

```js
// tailwind.config.js
module.exports = {
  plugins: [
    require('./plugins/my-plugin.js'),
  ],
}
```

## 🎨 Добавление утилит: `addUtilities`

`addUtilities` добавляет **новые утилитарные классы**:

```js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ addUtilities }) {
# ... (ещё 35 строк) ...

  addUtilities(newUtilities)
})
```

```html
<h1 class="text-shadow-lg text-white">Текст с тенью</h1>
<div class="scrollbar-hide overflow-x-auto">...</div>
```

### Динамические утилиты: `matchUtilities`

`matchUtilities` создаёт **динамические утилиты** на основе темы:

```js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ matchUtilities, theme }) {
# ... (ещё 7 строк) ...
    { values: theme('colors') }
  )
})
```

```html
<h1 class="text-shadow-blue-500">Синяя тень</h1>
<h1 class="text-shadow-red-500">Красная тень</h1>
<h1 class="text-shadow-green-500">Зелёная тень</h1>
```

### Утилиты с вариантами

```js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ addUtilities }) {
# ... (ещё 5 строк) ...
    variants: ['responsive', 'hover', 'focus', 'dark'],
  })
})
```

```html
<!-- Работает с модификаторами -->
<h1 class="text-shadow hover:text-shadow-lg dark:text-shadow-sm">
  Адаптивная тень
</h1>
```

## 🧩 Добавление компонентов: `addComponents`

`addComponents` добавляет **переиспользуемые компоненты**:

```js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ addComponents }) {
# ... (ещё 46 строк) ...

  addComponents(buttons)
})
```

```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary btn-lg">Secondary Large</button>
<button class="btn btn-outline btn-sm">Outline Small</button>
```

### Компоненты с темой

```js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ addComponents, theme }) {
# ... (ещё 9 строк) ...
    },
  })
})
```

## 🎨 Добавление базовых стилей: `addBase`

`addBase` добавляет **глобальные стили** (как в `@layer base`):

```js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ addBase, theme }) {
# ... (ещё 22 строк) ...
    },
  })
})
```

## 🎯 Работа с темой: `theme()`

Функция `theme()` позволяет **получать значения из конфигурации**:

```js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ addUtilities, theme }) {
# ... (ещё 15 строк) ...
    },
  })
})
```

### Fallback значения

```js
const plugin = require('tailwindcss/plugin')

module.exports = plugin(function({ theme }) {
# ... (ещё 3 строк) ...
  // Без fallback (undefined, если не найдено)
  const maybeColor = theme('colors.maybe')
})
```

## 🔧 Плагины с конфигурацией

### `plugin.withOptions`

Позволяет создавать плагины **с параметрами**:

```js
// plugins/badges.js
const plugin = require('tailwindcss/plugin')

# ... (ещё 28 строк) ...
    }
  }
)
```

```js
// tailwind.config.js
module.exports = {
  plugins: [
# ... (ещё 2 строк) ...
    }),
  ],
}
```

```html
<span class="badge-primary">Primary</span>
<span class="badge-success">Success</span>
<span class="badge-danger">Danger</span>
<span class="badge-info">Info</span>
```

### 1. 🔤 Плагин для text-shadow

```js
// plugins/text-shadow.js
const plugin = require('tailwindcss/plugin')

# ... (ещё 13 строк) ...
    { values: theme('colors') }
  )
})
```

```html
<h1 class="text-shadow-blue-500 text-4xl font-bold">
  Синяя тень
</h1>
<h1 class="text-shadow-lg-red-500 text-4xl font-bold">
  Большая красная тень
</h1>
```

### 2. 🎴 Плагин для карточек

```js
// plugins/cards.js
const plugin = require('tailwindcss/plugin')

# ... (ещё 23 строк) ...
    },
  })
})
```

### 3. 🎨 Плагин для градиентных текстов

```js
// plugins/gradient-text.js
const plugin = require('tailwindcss/plugin')

# ... (ещё 17 строк) ...
    }
  )
})
```

```html
<h1 class="gradient-text-blue-purple text-5xl font-bold">
  Градиентный текст
</h1>
<h1 class="gradient-text-pink-red text-5xl font-bold">
  Розово-красный градиент
</h1>
```

### 4. 📏 Плагин для кастомных контейнеров

```js
// plugins/container.js
const plugin = require('tailwindcss/plugin')

# ... (ещё 21 строк) ...

  addComponents(containerStyles)
})
```

```html
<div class="container">
  <!-- Контент с автоматической шириной для каждого breakpoint -->
</div>
```

### 5. 🎯 Плагин для aspect-ratio

```js
// plugins/aspect-ratio.js
const plugin = require('tailwindcss/plugin')

# ... (ещё 16 строк) ...
    },
  })
})
```

```html
<div class="aspect-video bg-gray-200">
  <img src="video-thumbnail.jpg" class="w-full h-full object-cover">
</div>
```

## 📊 Шпаргалка: что когда использовать

| Задача | Метод |
| :-- | :-- |
| Добавить новую утилиту | `addUtilities` |
| Динамическая утилита на основе темы | `matchUtilities` |
| Создать переиспользуемый компонент | `addComponents` |
| Добавить глобальные стили | `addBase` |
| Получить значение из темы | `theme('colors.blue.500')` |
| Плагин с параметрами | `plugin.withOptions` |
| Подключить официальный плагин | `require('@tailwindcss/forms')` |
| Подключить свой плагин | `require('./plugins/my-plugin.js')` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Забывают `require('tailwindcss/plugin')`

```js
// ❌ Плохо: plugin не определён
module.exports = function({ addUtilities }) {
  // ...
# ... (ещё 5 строк) ...
module.exports = plugin(function({ addUtilities }) {
  // ...
})
```

### ❌ Ошибка 2: Забывают подключить плагин в конфиге

```js
// ❌ Плохо: плагин создан, но не подключён
// plugins/my-plugin.js создан, но tailwind.config.js не обновлён

# ... (ещё 3 строк) ...
    require('./plugins/my-plugin.js'),
  ],
}
```

### ❌ Ошибка 3: Конфликт имён со стандартными утилитами

```js
// ❌ Плохо: конфликт с .text-blue-500
addUtilities({
  '.text-blue-500': {
# ... (ещё 7 строк) ...
    color: '#0000ff',
  },
})
```

### ❌ Ошибка 4: Забывают про `&` для pseudo-классов

```js
// ❌ Плохо: :hover не работает
addComponents({
  '.btn': {
# ... (ещё 13 строк) ...
    },
  },
})
```

### ❌ Ошибка 5: Забывают про `theme()` для консистентности

```js
// ❌ Плохо: жёстко закодированные значения
addComponents({
  '.card': {
# ... (ещё 9 строк) ...
    borderRadius: theme('borderRadius.lg'),
  },
})
```

### ❌ Ошибка 6: Слишком сложные плагины

```js
// ❌ Плохо: плагин делает слишком много
module.exports = plugin(function({ addUtilities, addComponents, addBase }) {
  // 500 строк кода...
# ... (ещё 7 строк) ...
    require('./plugins/buttons.js'),
  ],
}
```