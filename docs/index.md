# 📘 Tailwind CSS Guide

> Utility-first CSS фреймворк для быстрого создания современных интерфейсов

## Что такое Tailwind CSS?

**Tailwind CSS** — это CSS фреймворк, который предоставляет сотни утилитарных классов прямо в вашем HTML. Вместо того чтобы придумывать имена классов, вы собираете дизайн из готовых блоков.

```html
<!-- Пример: карточка на Tailwind -->
<div class="max-w-sm rounded overflow-hidden shadow-lg bg-white p-6">
  <h2 class="text-xl font-bold text-gray-800 mb-2">Заголовок</h2>
  <p class="text-gray-600 text-sm">Описание карточки</p>
  <button class="mt-4 bg-cyan-500 hover:bg-cyan-600 text-white px-4 py-2 rounded">
    Подробнее
  </button>
</div>
```

## 🎯 Для кого этот гайд?

- 🟢 **Новички** — изучите основы и начните верстать за час
- 🟡 **Уверенные** — освойте адаптивность, dark mode и состояния
- 🔴 **Профи** — кастомизация, плагины, оптимизация и интеграции

## 📚 Разделы

| Раздел | Что внутри |
| :-- | :-- |
| **Основы** | Установка, конфигурация, первые шаги |
| **Макет** | Flexbox, Grid, отступы, размеры |
| **Стили** | Цвета, типографика, фоны, границы |
| **Адаптивность** | Breakpoints, dark mode, состояния |
| **Продвинутое** | Кастомизация, плагины, директивы |
| **Интеграции** | React, Vue, Next.js |

## 🚀 Быстрый старт

```bash
# Установка через npm
npm install -D tailwindcss
npx tailwindcss init
```

Затем в вашем CSS файле:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

---

_Начните с раздела [Введение](basics/introduction.md) или сразу перейдите к [Установке](basics/installation.md)._