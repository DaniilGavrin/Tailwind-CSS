# 🌙 Dark Mode в Tailwind CSS

> **Полное руководство по тёмной теме:** от базовой настройки до переключателя, сохранения выбора пользователя и продвинутых паттернов

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Поймёте два режима работы dark mode: `media` и `class`
- ✅ Настроите dark mode в `tailwind.config.js`
- ✅ Освоите синтаксис модификатора `dark:`
- ✅ Создадите полноценный переключатель темы
- ✅ Научитесь сохранять выбор пользователя в localStorage
- ✅ Оптимизируете изображения и цвета для тёмной темы
- ✅ Избежите типичных ошибок при реализации dark mode
- ✅ Реализуете поддержку системных настроек + ручного переключения

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

```html
<!-- Светлая тема -->
<html>
  <body class="bg-white text-gray-900">...</body>
</html>

<!-- Тёмная тема -->
<html class="dark">
  <body class="bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100">
    ...
  </body>
</html>
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

```html
<!-- Фон -->
<div class="bg-white dark:bg-gray-900">...</div>

<!-- Текст -->
<p class="text-gray-900 dark:text-gray-100">...</p>

<!-- Граница -->
<div class="border-gray-200 dark:border-gray-700">...</div>

<!-- Hover -->
<button class="hover:bg-gray-100 dark:hover:bg-gray-800">...</button>

<!-- Focus -->
<input class="focus:ring-blue-500 dark:focus:ring-blue-400">
```

### Комбинирование с другими модификаторами

```html
<!-- Dark + responsive -->
<div class="bg-white md:bg-gray-50 dark:bg-gray-900 md:dark:bg-gray-800">
  Адаптивная тёмная тема
</div>

<!-- Dark + hover -->
<button class="bg-blue-500 hover:bg-blue-600 dark:bg-blue-600 dark:hover:bg-blue-700">
  Кнопка
</button>

<!-- Dark + group-hover -->
<div class="group">
  <span class="text-gray-600 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-gray-100">
    Текст
  </span>
</div>
```

## 🎯 Типовая цветовая схема

### Светлая тема

```
Фоны:
  - Основной: white
  - Вторичный: gray-50
  - Третичный: gray-100

Текст:
  - Основной: gray-900
  - Вторичный: gray-600
  - Третичный: gray-400

Границы: gray-200
```

### Тёмная тема

```
Фоны:
  - Основной: gray-900
  - Вторичный: gray-800
  - Третичный: gray-700

Текст:
  - Основной: gray-100
  - Вторичный: gray-400
  - Третичный: gray-500

Границы: gray-700
```

### Пример реализации

```html
<div class="bg-white dark:bg-gray-900 p-6 rounded-lg shadow-md">
  <h2 class="text-xl font-bold text-gray-900 dark:text-gray-100 mb-2">
    Заголовок карточки
  </h2>
  <p class="text-gray-600 dark:text-gray-400 mb-4">
    Описание карточки с поддержкой тёмной темы.
  </p>
  <div class="border-t border-gray-200 dark:border-gray-700 pt-4">
    <button class="bg-blue-600 hover:bg-blue-700 dark:bg-blue-500 dark:hover:bg-blue-600 text-white px-4 py-2 rounded">
      Действие
    </button>
  </div>
</div>
```

## 🔄 Переключатель темы

### Базовый переключатель

```html
<button
  id="theme-toggle"
  type="button"
  class="text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 rounded-lg text-sm p-2.5"
>
  <!-- Иконка солнца (для тёмной темы) -->
  <svg id="theme-toggle-dark-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
    <path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"/>
  </svg>
  <!-- Иконка луны (для светлой темы) -->
  <svg id="theme-toggle-light-icon" class="hidden w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
    <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/>
  </svg>
</button>

<script>
  var themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
  var themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');

  // Показываем правильную иконку при загрузке
  if (localStorage.getItem('color-theme') === 'dark' ||
      (!('color-theme' in localStorage) &&
       window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    themeToggleLightIcon.classList.remove('hidden');
  } else {
    themeToggleDarkIcon.classList.remove('hidden');
  }

  var themeToggleBtn = document.getElementById('theme-toggle');
  themeToggleBtn.addEventListener('click', function() {
    // Переключаем иконки
    themeToggleDarkIcon.classList.toggle('hidden');
    themeToggleLightIcon.classList.toggle('hidden');

    // Переключаем тему
    if (localStorage.getItem('color-theme')) {
      if (localStorage.getItem('color-theme') === 'light') {
        document.documentElement.classList.add('dark');
        localStorage.setItem('color-theme', 'dark');
      } else {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('color-theme', 'light');
      }
    } else {
      if (document.documentElement.classList.contains('dark')) {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('color-theme', 'light');
      } else {
        document.documentElement.classList.add('dark');
        localStorage.setItem('color-theme', 'dark');
      }
    }
  });
</script>
```

### Улучшенный переключатель с инициализацией до рендера

Чтобы избежать «мигания» темы при загрузке, добавьте этот скрипт в `<head>` **до** рендеринга body:

```html
<!DOCTYPE html>
<html>
<head>
  <script>
    // Применяем тему ДО рендеринга страницы
    if (localStorage.theme === 'dark' ||
        (!('theme' in localStorage) &&
         window.matchMedia('(prefers-color-scheme: dark)').matches)) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  </script>
  <!-- Остальной head -->
</head>
<body>
  <!-- Контент -->
</body>
</html>
```

### React-компонент переключателя

```jsx
import { useEffect, useState } from 'react';

function ThemeToggle() {
  const [theme, setTheme] = useState(() => {
    if (typeof window !== 'undefined') {
      return localStorage.getItem('theme') ||
        (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    }
    return 'light';
  });

  useEffect(() => {
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
    localStorage.setItem('theme', theme);
  }, [theme]);

  return (
    <button
      onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
      className="p-2 rounded-lg bg-gray-200 dark:bg-gray-700 hover:bg-gray-300 dark:hover:bg-gray-600 transition"
      aria-label="Переключить тему"
    >
      {theme === 'dark' ? (
        <svg className="w-5 h-5 text-yellow-500" fill="currentColor" viewBox="0 0 20 20">
          <path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"/>
        </svg>
      ) : (
        <svg className="w-5 h-5 text-gray-700" fill="currentColor" viewBox="0 0 20 20">
          <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/>
        </svg>
      )}
    </button>
  );
}

export default ThemeToggle;
```

### Vue-компонент переключателя

```vue
<template>
  <button
    @click="toggleTheme"
    class="p-2 rounded-lg bg-gray-200 dark:bg-gray-700 hover:bg-gray-300 dark:hover:bg-gray-600 transition"
    aria-label="Переключить тему"
  >
    <svg v-if="theme === 'dark'" class="w-5 h-5 text-yellow-500" fill="currentColor" viewBox="0 0 20 20">
      <path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"/>
    </svg>
    <svg v-else class="w-5 h-5 text-gray-700" fill="currentColor" viewBox="0 0 20 20">
      <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/>
    </svg>
  </button>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const theme = ref('light');

onMounted(() => {
  theme.value = localStorage.getItem('theme') ||
    (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');

  applyTheme();
});

function toggleTheme() {
  theme.value = theme.value === 'dark' ? 'light' : 'dark';
  localStorage.setItem('theme', theme.value);
  applyTheme();
}

function applyTheme() {
  if (theme.value === 'dark') {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
}
</script>
```

## 🎨 Три состояния: light / dark / system

Самый продвинутый подход — поддержка трёх режимов:

```js
// theme.js
const ThemeManager = {
  init() {
    const saved = localStorage.getItem('theme');
    const system = window.matchMedia('(prefers-color-scheme: dark)').matches;

    if (saved === 'dark' || (!saved && system)) {
      document.documentElement.classList.add('dark');
    }

    // Следим за изменениями системной темы
    window.matchMedia('(prefers-color-scheme: dark)')
      .addEventListener('change', (e) => {
        if (!localStorage.getItem('theme')) {
          document.documentElement.classList.toggle('dark', e.matches);
        }
      });
  },

  setTheme(mode) {
    localStorage.setItem('theme', mode);

    if (mode === 'dark') {
      document.documentElement.classList.add('dark');
    } else if (mode === 'light') {
      document.documentElement.classList.remove('dark');
    } else {
      // system
      const system = window.matchMedia('(prefers-color-scheme: dark)').matches;
      document.documentElement.classList.toggle('dark', system);
    }
  },

  getTheme() {
    return localStorage.getItem('theme') || 'system';
  }
};

ThemeManager.init();
```

```html
<!-- Переключатель с тремя режимами -->
<div class="flex items-center gap-2 bg-gray-100 dark:bg-gray-800 p-1 rounded-lg">
  <button onclick="ThemeManager.setTheme('light')" class="px-3 py-1 rounded hover:bg-white dark:hover:bg-gray-700">
    ☀️ Светлая
  </button>
  <button onclick="ThemeManager.setTheme('dark')" class="px-3 py-1 rounded hover:bg-white dark:hover:bg-gray-700">
    🌙 Тёмная
  </button>
  <button onclick="ThemeManager.setTheme('system')" class="px-3 py-1 rounded hover:bg-white dark:hover:bg-gray-700">
    💻 Системная
  </button>
</div>
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
  src="photo.jpg"
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

## 🎯 Практические паттерны

### 1. 🎴 Карточка с полной поддержкой dark mode

```html
<div class="bg-white dark:bg-gray-800 rounded-xl shadow-md dark:shadow-gray-900/50 overflow-hidden max-w-sm">
  <img
    src="product.jpg"
    class="w-full h-48 object-cover brightness-100 dark:brightness-90"
    alt="Товар"
  >
  <div class="p-6">
    <div class="flex items-center gap-2 mb-2">
      <span class="bg-blue-100 dark:bg-blue-900/30 text-blue-800 dark:text-blue-300 text-xs font-medium px-2 py-1 rounded">
        Новинка
      </span>
    </div>
    <h3 class="text-xl font-bold text-gray-900 dark:text-gray-100 mb-2">
      Название товара
    </h3>
    <p class="text-gray-600 dark:text-gray-400 text-sm mb-4">
      Описание товара с поддержкой тёмной темы.
    </p>
    <div class="flex items-center justify-between">
      <div>
        <span class="text-2xl font-bold text-gray-900 dark:text-gray-100">2 990 ₽</span>
        <span class="text-sm text-gray-400 dark:text-gray-500 line-through ml-2">3 990 ₽</span>
      </div>
      <button class="bg-blue-600 dark:bg-blue-500 hover:bg-blue-700 dark:hover:bg-blue-600 text-white px-4 py-2 rounded-lg transition">
        Купить
      </button>
    </div>
  </div>
</div>
```

### 2. 📝 Форма с dark mode

```html
<form class="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 max-w-md space-y-4">
  <h2 class="text-2xl font-bold text-gray-900 dark:text-gray-100">Вход</h2>

  <div>
    <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
      Email
    </label>
    <input
      type="email"
      class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100 placeholder-gray-400 dark:placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 dark:focus:ring-blue-400"
      placeholder="you@example.com"
    >
  </div>

  <div>
    <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
      Пароль
    </label>
    <input
      type="password"
      class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100 placeholder-gray-400 dark:placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 dark:focus:ring-blue-400"
      placeholder="••••••••"
    >
  </div>

  <div class="flex items-center justify-between">
    <label class="flex items-center gap-2">
      <input type="checkbox" class="rounded border-gray-300 dark:border-gray-600 text-blue-600 dark:text-blue-500 focus:ring-blue-500 dark:focus:ring-blue-400">
      <span class="text-sm text-gray-700 dark:text-gray-300">Запомнить меня</span>
    </label>
    <a href="#" class="text-sm text-blue-600 dark:text-blue-400 hover:underline">
      Забыли пароль?
    </a>
  </div>

  <button
    type="submit"
    class="w-full bg-blue-600 dark:bg-blue-500 hover:bg-blue-700 dark:hover:bg-blue-600 text-white font-medium py-2 rounded-lg transition"
  >
    Войти
  </button>
</form>
```

### 3. 📊 Таблица с dark mode

```html
<div class="overflow-x-auto">
  <table class="w-full bg-white dark:bg-gray-800 rounded-lg shadow-md">
    <thead class="bg-gray-50 dark:bg-gray-700 border-b border-gray-200 dark:border-gray-600">
      <tr>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Имя</th>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Email</th>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Роль</th>
        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase">Статус</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-gray-200 dark:divide-gray-700">
      <tr class="hover:bg-gray-50 dark:hover:bg-gray-700/50 transition">
        <td class="px-6 py-4 font-medium text-gray-900 dark:text-gray-100">Иван Иванов</td>
        <td class="px-6 py-4 text-gray-600 dark:text-gray-400">ivan@example.com</td>
        <td class="px-6 py-4 text-gray-600 dark:text-gray-400">Администратор</td>
        <td class="px-6 py-4">
          <span class="bg-green-100 dark:bg-green-900/30 text-green-800 dark:text-green-300 text-xs px-2 py-1 rounded">
            Активен
          </span>
        </td>
      </tr>
      <tr class="hover:bg-gray-50 dark:hover:bg-gray-700/50 transition">
        <td class="px-6 py-4 font-medium text-gray-900 dark:text-gray-100">Мария Петрова</td>
        <td class="px-6 py-4 text-gray-600 dark:text-gray-400">maria@example.com</td>
        <td class="px-6 py-4 text-gray-600 dark:text-gray-400">Пользователь</td>
        <td class="px-6 py-4">
          <span class="bg-yellow-100 dark:bg-yellow-900/30 text-yellow-800 dark:text-yellow-300 text-xs px-2 py-1 rounded">
            Ожидает
          </span>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

### 4. 🎨 Градиенты с dark mode

```html
<!-- Светлая тема: яркий градиент -->
<!-- Тёмная тема: более приглушённый -->
<div class="bg-gradient-to-br from-blue-500 to-purple-600 dark:from-blue-700 dark:to-purple-900 p-8 rounded-xl text-white">
  <h2 class="text-3xl font-bold mb-2">Градиентный блок</h2>
  <p class="text-blue-100 dark:text-purple-200">
    Цвета градиента адаптируются под тему
  </p>
</div>
```

### 5. 🌫️ Glassmorphism с dark mode

```html
<div class="relative h-96 bg-gradient-to-br from-purple-500 via-pink-500 to-orange-500 dark:from-purple-900 dark:via-pink-900 dark:to-orange-900">
  <!-- Декоративные круги -->
  <div class="absolute top-10 left-10 w-32 h-32 bg-yellow-300 dark:bg-yellow-700 rounded-full blur-2xl"></div>
  <div class="absolute bottom-10 right-10 w-40 h-40 bg-blue-400 dark:bg-blue-800 rounded-full blur-2xl"></div>

  <!-- Стеклянная карточка -->
  <div class="absolute inset-0 flex items-center justify-center">
    <div class="bg-white/20 dark:bg-black/30 backdrop-blur-lg border border-white/30 dark:border-white/10 rounded-2xl p-8 shadow-2xl max-w-md">
      <h2 class="text-2xl font-bold text-white mb-4">Glassmorphism</h2>
      <p class="text-white/90 dark:text-white/80">
        Стеклянный эффект работает в обеих темах
      </p>
    </div>
  </div>
</div>
```

## ⚙️ Кастомные цвета для dark mode

### Через CSS-переменные (рекомендуется)

```js
// tailwind.config.js
module.exports = {
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        'surface': {
          DEFAULT: 'rgb(var(--surface) / <alpha-value>)',
          secondary: 'rgb(var(--surface-secondary) / <alpha-value>)',
        },
        'content': {
          DEFAULT: 'rgb(var(--content) / <alpha-value>)',
          secondary: 'rgb(var(--content-secondary) / <alpha-value>)',
        },
      },
    },
  },
}
```

```css
/* styles.css */
:root {
  --surface: 255 255 255;           /* white */
  --surface-secondary: 249 250 251; /* gray-50 */
  --content: 17 24 39;              /* gray-900 */
  --content-secondary: 75 85 99;    /* gray-600 */
}

.dark {
  --surface: 17 24 39;              /* gray-900 */
  --surface-secondary: 31 41 55;    /* gray-800 */
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
}

// ✅ Хорошо: явно указываем class
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

```html
<!-- ❌ Плохо: скрипт в конце body -->
<body>
  <!-- Контент -->
  <script>
    // Применяем тему
  </script>
</body>

<!-- ✅ Хорошо: скрипт в <head> до рендеринга -->
<head>
  <script>
    // Применяем тему ДО рендеринга
  </script>
</head>
<body>
  <!-- Контент -->
</body>
```

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
</button>

<!-- ✅ Хорошо: акцент остаётся, меняется только фон/текст -->
<button class="bg-blue-600 hover:bg-blue-700 text-white">
  Акцент стабилен
</button>
```

### ❌ Ошибка 6: Забывают про тени в dark mode

```html
<!-- ❌ Плохо: чёрная тень на тёмном фоне не видна -->
<div class="bg-gray-900 shadow-lg">Тень не видна</div>

<!-- ✅ Хорошо: настраиваем цвет тени -->
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

## 🎯 Что дальше?

Теперь вы полностью владеете тёмной темой! Но интерактивность — это не только темы. Следующий важный аспект — **состояния элементов**: hover, focus, active, disabled.

**Следующий шаг:** [🎯 Состояния элементов в Tailwind CSS](states.md) — изучим все модификаторы состояний и научимся создавать отзывчивые интерфейсы.

---