# 📦 Установка Tailwind CSS

> **Полное руководство по установке Tailwind CSS:** от быстрого старта через CDN до production-ready настройки с PostCSS и интеграции с фреймворками

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Поймёте все способы установки Tailwind CSS
- ✅ Настроите Tailwind через CDN для быстрых экспериментов
- ✅ Установите Tailwind через npm для production-проекта
- ✅ Настроите Tailwind CLI для простых проектов
- ✅ Интегрируете Tailwind с PostCSS (рекомендуемый способ)
- ✅ Настроите Tailwind в Vite, Next.js, Vue, React, Laravel
- ✅ Проверите, что всё работает корректно
- ✅ Избежите типичных ошибок при установке
- ✅ Поймёте разницу между Tailwind v3 и v4

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

```html
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tailwind CDN</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 p-8">
  <h1 class="text-3xl font-bold text-blue-600">
    Привет, Tailwind!
  </h1>
  <p class="mt-4 text-gray-700">
    Это мой первый проект на Tailwind CSS
  </p>
  <button class="mt-4 bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-lg">
    Нажми меня
  </button>
</body>
</html>
```

### Шаг 2: Откройте в браузере

Просто откройте файл в браузере — Tailwind уже работает!

### ⚙️ Кастомизация Play CDN

Можно настроить Tailwind прямо в HTML:

```html
<script>
  tailwind.config = {
    theme: {
      extend: {
        colors: {
          'brand': '#ff5722',
        },
      },
    },
  }
</script>
```

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
  theme: {
    extend: {},
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

# С watch-режимом (автоматическая пересборка)
npx tailwindcss -i ./src/input.css -o ./src/output.css --watch

# С минификацией (для production)
npx tailwindcss -i ./src/input.css -o ./src/output.css --minify
```

### Шаг 5: Подключите CSS в HTML

```html
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <link href="./src/output.css" rel="stylesheet">
</head>
<body class="bg-gray-100 p-8">
  <h1 class="text-3xl font-bold text-blue-600">Tailwind CLI</h1>
</body>
</html>
```

### 📁 Структура проекта

```
my-project/
├── src/
│   ├── input.css       ← Исходный CSS с директивами
│   ├── output.css      ← Сгенерированный CSS
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
  content: ["./src/**/*.{html,js,jsx,ts,tsx,vue,svelte}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

```js
// postcss.config.js
module.exports = {
  plugins: {
    tailwindcss: {},
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
    // HTML
    "./src/**/*.html",
    // JavaScript / TypeScript
    "./src/**/*.{js,jsx,ts,tsx}",
    // Vue
    "./src/**/*.vue",
    // Svelte
    "./src/**/*.svelte",
    // PHP (Laravel)
    "./resources/**/*.blade.php",
    "./resources/**/*.js",
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

export default defineConfig({
  css: {
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
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          'style-loader',
          {
            loader: 'postcss-loader',
            options: {
              postcssOptions: {
                plugins: [
                  'tailwindcss',
                  'autoprefixer',
                ],
              },
            },
          },
          'css-loader',
        ],
      },
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
│   ├── index.html
│   └── main.js
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

# Установка Tailwind
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

```js
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
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

```jsx
// src/main.jsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
```

```jsx
// src/App.jsx
function App() {
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="bg-white p-8 rounded-xl shadow-lg max-w-md">
        <h1 className="text-3xl font-bold text-gray-900">
          Привет, React + Tailwind!
        </h1>
        <p className="mt-4 text-gray-600">
          Это мой первый проект
        </p>
        <button className="mt-6 bg-blue-500 hover:bg-blue-600 text-white px-6 py-2 rounded-lg transition-colors">
          Нажми меня
        </button>
      </div>
    </div>
  )
}

export default App
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

# Установка Tailwind
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

```js
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
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

```vue
<!-- src/App.vue -->
<template>
  <div class="min-h-screen bg-gray-100 flex items-center justify-center">
    <div class="bg-white p-8 rounded-xl shadow-lg max-w-md">
      <h1 class="text-3xl font-bold text-gray-900">
        Привет, Vue + Tailwind!
      </h1>
      <p class="mt-4 text-gray-600">
        Это мой первый проект
      </p>
      <button class="mt-6 bg-blue-500 hover:bg-blue-600 text-white px-6 py-2 rounded-lg transition-colors">
        Нажми меня
      </button>
    </div>
  </div>
</template>
```

> 📚 **Подробнее:** см. разделы [React + Tailwind](../integrations/react.md) и [Vue + Tailwind](../integrations/vue.md).

## 🚀 Вариант 5: Next.js

Next.js имеет **встроенную поддержку** Tailwind CSS.

### Шаг 1: Создание проекта

```bash
npx create-next-app@latest my-app
cd my-app

# Tailwind уже установлен по умолчанию!
# Если нет:
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

### Шаг 2: Настройка конфигурации

```js
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx}',
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
    './src/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {},
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

```tsx
// app/layout.tsx
import './globals.css'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="ru">
      <body>{children}</body>
    </html>
  )
}
```

### Шаг 5: Использование

```tsx
// app/page.tsx
export default function Home() {
  return (
    <main className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="bg-white p-8 rounded-xl shadow-lg max-w-md">
        <h1 className="text-3xl font-bold text-gray-900">
          Привет, Next.js!
        </h1>
      </div>
    </main>
  )
}
```

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
  tailwindcss: {
    configPath: 'tailwind.config.js',
  },
})
```

### Шаг 3: Конфигурация

```js
// tailwind.config.js
module.exports = {
  content: [
    './components/**/*.{vue,js,ts}',
    './layouts/**/*.vue',
    './pages/**/*.vue',
    './plugins/**/*.{js,ts}',
    './app.vue',
  ],
}
```

### Шаг 4: Использование

```vue
<!-- pages/index.vue -->
<template>
  <div class="min-h-screen bg-gray-100 flex items-center justify-center">
    <div class="bg-white p-8 rounded-xl shadow-lg max-w-md">
      <h1 class="text-3xl font-bold text-gray-900">
        Привет, Nuxt 3!
      </h1>
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

module.exports = {
  content: [
    './vendor/laravel/framework/src/Illuminate/Pagination/resources/views/*.blade.php',
    './storage/framework/views/*.php',
    './resources/views/**/*.blade.php',
    './resources/js/**/*.vue',
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Figtree', ...defaultTheme.fontFamily.sans],
      },
    },
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

```html
<!-- resources/views/layouts/app.blade.php -->
<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  @vite(['resources/css/app.css', 'resources/js/app.js'])
</head>
<body class="font-sans antialiased">
  {{ $slot }}
</body>
</html>
```

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
    './templates/**/*.html',
    './**/templates/**/*.html',
  ],
}
```

### Шаг 3: Сборка CSS

```json
// package.json
{
  "scripts": {
    "dev": "npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch",
    "build": "npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --minify"
  }
}
```

### Шаг 4: Подключение в шаблоне

```html
<!-- templates/base.html -->
{% load static %}
<!DOCTYPE html>
<html lang="ru">
<head>
  <link href="{% static 'css/output.css' %}" rel="stylesheet">
</head>
<body>
  {% block content %}{% endblock %}
</body>
</html>
```

## ✅ Проверка установки

После установки убедитесь, что всё работает:

### Тестовая страница

```html
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <link href="./output.css" rel="stylesheet">
</head>
<body class="bg-gray-100 min-h-screen flex items-center justify-center p-4">
  <div class="bg-white rounded-xl shadow-lg p-8 max-w-md w-full">
    <h1 class="text-3xl font-bold text-gray-900 mb-4">
      ✅ Tailwind работает!
    </h1>
    <p class="text-gray-600 mb-6">
      Если вы видите эту карточку со стилями — всё настроено правильно.
    </p>
    <div class="flex gap-2">
      <button class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-lg transition-colors">
        Primary
      </button>
      <button class="bg-gray-200 hover:bg-gray-300 text-gray-800 px-4 py-2 rounded-lg transition-colors">
        Secondary
      </button>
    </div>
  </div>
</body>
</html>
```

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

## 🎯 Практические паттерны

### 1. 📁 Базовая структура проекта

```
my-project/
├── src/
│   ├── input.css          ← Директивы Tailwind
│   ├── output.css         ← Сгенерированный CSS
│   ├── index.html
│   └── main.js
├── tailwind.config.js     ← Конфигурация Tailwind
├── postcss.config.js      ← Конфигурация PostCSS
├── package.json
└── .gitignore
```

### 2. 📝 package.json scripts

```json
{
  "scripts": {
    "dev": "npx tailwindcss -i ./src/input.css -o ./src/output.css --watch",
    "build": "npx tailwindcss -i ./src/input.css -o ./src/output.css --minify",
    "analyze": "npx tailwindcss -i ./src/input.css -o ./src/output.css --minify && gzip -c ./src/output.css | wc -c"
  }
}
```

### 3. 🎨 .gitignore для Tailwind

```gitignore
# Зависимости
node_modules/

# Сгенерированный CSS (не коммитим)
src/output.css
dist/
build/

# Логи
*.log

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
  content: ["./src/**/*.{html,js,ts,jsx,tsx}"],
  theme: {
    extend: {},
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
  theme: { extend: {} },
}

// ✅ Хорошо: указываем пути
module.exports = {
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
}

/* ✅ Хорошо: директивы Tailwind */
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

# ✅ Хорошо: перезапускаем сервер
npm run dev
# или
npx tailwindcss -i input.css -o output.css --watch
```

### ❌ Ошибка 6: Неправильные пути в `content`

```js
// ❌ Плохо: пути не существуют
module.exports = {
  content: ["./app/**/*.html"], // папки app нет
}

// ✅ Хорошо: правильные пути
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

# Если нужно обновить
npm update tailwindcss

# Или переустановить
rm -rf node_modules package-lock.json
npm install
```

## 🎯 Checklist для нового проекта

Перед началом работы убедитесь:

- [ ] Выбрали подходящий способ установки
- [ ] Установили все зависимости (`tailwindcss`, `postcss`, `autoprefixer`)
- [ ] Создали `tailwind.config.js` с правильными путями в `content`
- [ ] Создали `postcss.config.js` (если используете PostCSS)
- [ ] Создали `input.css` с директивами `@tailwind`
- [ ] Настроили watch-режим для разработки
- [ ] Настроили минификацию для production
- [ ] Проверили, что стили применяются
- [ ] Добавили `output.css` в `.gitignore`
- [ ] Протестировали на разных устройствах

## 🎯 Что дальше?

Теперь у вас установлен и работает Tailwind CSS! Следующий шаг — **настройка конфигурации** под ваш проект.

**Следующий раздел:** [⚙️ Конфигурация Tailwind CSS](configuration.md) — изучим `tailwind.config.js`, как расширять тему, добавлять свои цвета, шрифты и breakpoints.

---