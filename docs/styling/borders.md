# 🔲 Границы в Tailwind CSS

> **Полное руководство по работе с границами:** от базовых border и radius до ring-эффектов, разделителей и outline

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Освоите все способы задания границ: ширина, цвет, стиль
- ✅ Научитесь управлять скруглением углов (border-radius)
- ✅ Поймёте разницу между `border`, `ring` и `outline`
- ✅ Создадите красивые карточки, кнопки и разделители
- ✅ Освоите отдельные стороны границ (top, right, bottom, left)
- ✅ Настроите кастомные радиусы и цвета границ
- ✅ Избежите типичных ошибок при работе с границами

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

```html
<!-- Только нижняя граница (для разделителей) -->
<div class="border-b border-gray-200 pb-4 mb-4">
  Элемент с нижней границей
</div>

<!-- Только левая граница (для акцентов) -->
<div class="border-l-4 border-blue-500 pl-4">
  Важная информация
</div>

<!-- Горизонтальные границы (сверху и снизу) -->
<div class="border-y border-gray-300 py-4">
  Элемент с границами сверху и снизу
</div>
```

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

```html
<!-- Без скругления -->
<div class="border-2 border-gray-300 p-4 rounded-none">Острые углы</div>

<!-- Маленькое скругление -->
<div class="border-2 border-gray-300 p-4 rounded">Немного скруглено</div>

<!-- Среднее скругление -->
<div class="border-2 border-gray-300 p-4 rounded-lg">Скруглено</div>

<!-- Большое скругление -->
<div class="border-2 border-gray-300 p-4 rounded-xl">Сильно скруглено</div>

<!-- Полное скругление (для кнопок-пилюль) -->
<button class="border-2 border-blue-500 px-6 py-2 rounded-full">
  Кнопка-пилюля
</button>

<!-- Круг (для аватаров) -->
<img src="avatar.jpg" class="w-16 h-16 rounded-full border-2 border-white">
```

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

```html
<!-- Скруглены только верхние углы -->
<div class="border-2 border-gray-300 p-4 rounded-t-lg">
  Скруглённые верхние углы
</div>

<!-- Скруглён только правый верхний угол -->
<div class="border-2 border-gray-300 p-4 rounded-tr-lg">
  Только правый верхний угол
</div>

<!-- Асимметричное скругление -->
<div class="border-2 border-gray-300 p-4 rounded-tl-lg rounded-br-lg">
  Диагональное скругление
</div>
```

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
</button>

<!-- Outline с отступом -->
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

```html
<!-- Вертикальные разделители -->
<div class="divide-y divide-gray-200">
  <div class="py-2">Пункт 1</div>
  <div class="py-2">Пункт 2</div>
  <div class="py-2">Пункт 3</div>
</div>

<!-- Горизонтальные разделители -->
<div class="flex divide-x divide-gray-200">
  <div class="px-4 py-2">Элемент 1</div>
  <div class="px-4 py-2">Элемент 2</div>
  <div class="px-4 py-2">Элемент 3</div>
</div>

<!-- Цветные разделители -->
<div class="divide-y divide-blue-200">
  <div class="py-2">Пункт 1</div>
  <div class="py-2">Пункт 2</div>
</div>
```

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

## 🎨 Практические паттерны

### 1. 🎴 Карточка с границей

```html
<div class="bg-white border border-gray-200 rounded-xl shadow-sm p-6 max-w-sm">
  <h3 class="text-xl font-bold text-gray-900 mb-2">Название карточки</h3>
  <p class="text-gray-600 text-sm">
    Описание карточки с границей и скруглением.
  </p>
  <button class="mt-4 w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 rounded-lg transition">
    Действие
  </button>
</div>
```

### 2. 🎯 Input с focus ring

```html
<div class="space-y-4 max-w-md">
  <div>
    <label class="block text-sm font-medium text-gray-700 mb-1">Email</label>
    <input
      type="email"
      class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
      placeholder="you@example.com"
    >
  </div>

  <div>
    <label class="block text-sm font-medium text-gray-700 mb-1">Пароль</label>
    <input
      type="password"
      class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
      placeholder="••••••••"
    >
  </div>
</div>
```

### 3. 📊 Список с разделителями

```html
<div class="bg-white border border-gray-200 rounded-lg divide-y divide-gray-200 max-w-md">
  <div class="flex items-center justify-between p-4">
    <div>
      <div class="font-medium text-gray-900">Профиль</div>
      <div class="text-sm text-gray-500">Настройки аккаунта</div>
    </div>
    <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
    </svg>
  </div>

  <div class="flex items-center justify-between p-4">
    <div>
      <div class="font-medium text-gray-900">Уведомления</div>
      <div class="text-sm text-gray-500">Email и push-уведомления</div>
    </div>
    <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
    </svg>
  </div>

  <div class="flex items-center justify-between p-4">
    <div>
      <div class="font-medium text-gray-900">Безопасность</div>
      <div class="text-sm text-gray-500">Пароль и 2FA</div>
    </div>
    <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
    </svg>
  </div>
</div>
```

### 4. 🏷️ Бейдж с границей

```html
<div class="flex flex-wrap gap-2">
  <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-blue-100 text-blue-800 border border-blue-200">
    Новое
  </span>
  <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-green-100 text-green-800 border border-green-200">
    Активно
  </span>
  <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-yellow-100 text-yellow-800 border border-yellow-200">
    В процессе
  </span>
  <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-red-100 text-red-800 border border-red-200">
    Закрыто
  </span>
</div>
```

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

```html
<div class="inline-flex border border-gray-300 rounded-lg divide-x divide-gray-300">
  <button class="px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50">
    День
  </button>
  <button class="px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50">
    Неделя
  </button>
  <button class="px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50">
    Месяц
  </button>
</div>
```

### 7. 🖼️ Аватар с границей

```html
<div class="flex items-center gap-3">
  <img
    src="avatar.jpg"
    alt="Аватар"
    class="w-12 h-12 rounded-full border-2 border-white shadow-md"
  >
  <div>
    <div class="font-medium text-gray-900">Иван Иванов</div>
    <div class="text-sm text-gray-500">Разработчик</div>
  </div>
</div>
```

### 8. 🎯 Drag-and-drop зона

```html
<div class="border-2 border-dashed border-gray-300 rounded-lg p-12 text-center hover:border-blue-500 transition-colors">
  <svg class="mx-auto w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"/>
  </svg>
  <p class="mt-2 text-sm text-gray-600">
    Перетащите файлы сюда или
    <button class="text-blue-600 hover:text-blue-700 font-medium">выберите</button>
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

```html
<!-- ❌ Плохо: двойная обводка (outline + ring) -->
<input
  type="text"
  class="border border-gray-300 focus:ring-2 focus:ring-blue-500"
>

<!-- ✅ Хорошо: убираем стандартный outline -->
<input
  type="text"
  class="border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
>
```

### ❌ Ошибка 4: `rounded-full` для неквадратных элементов

```html
<!-- ❌ Плохо: получится овал, не круг -->
<div class="w-32 h-16 rounded-full bg-blue-500">Овал</div>

<!-- ✅ Хорошо: квадратные пропорции -->
<div class="w-16 h-16 rounded-full bg-blue-500">Круг</div>

<!-- ✅ Или используйте rounded-{size} для прямоугольников -->
<div class="w-32 h-16 rounded-lg bg-blue-500">Прямоугольник со скруглением</div>
```

### ❌ Ошибка 5: `divide` без flex или grid контейнера

```html
<!-- ❌ Плохо: divide не работает без flex/grid -->
<div class="divide-y divide-gray-200">
  <div>Пункт 1</div>
  <div>Пункт 2</div>
</div>

<!-- ✅ Хорошо: добавляем flex flex-col -->
<div class="divide-y divide-gray-200 flex flex-col">
  <div>Пункт 1</div>
  <div>Пункт 2</div>
</div>
```

### ❌ Ошибка 6: Забывают про responsive границы

```html
<!-- ❌ Плохо: граница на всех экранах -->
<div class="border border-gray-300 p-4">Граница всегда</div>

<!-- ✅ Хорошо: граница только на десктопе -->
<div class="border-0 md:border border-gray-300 p-4">Граница только на md+</div>
```

### ❌ Ошибка 7: `ring-offset` без учёта фона

```html
<!-- ❌ Плохо: ring offset на белом фоне выглядит странно -->
<div class="bg-white p-4">
  <input
    type="text"
    class="border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
  >
</div>

<!-- ✅ Хорошо: ring offset того же цвета, что и фон -->
<div class="bg-white p-4">
  <input
    type="text"
    class="border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 focus:ring-offset-white"
  >
</div>
```

## 🎯 Что дальше?

Теперь вы полностью владеете границами и обводками! Но визуальный стиль — это не только границы. Следующий важный аспект — **эффекты и тени**.

**Следующий шаг:** [✨ Эффекты и тени в Tailwind CSS](effects.md) — изучим работу с box-shadow, opacity, mix-blend-mode и другими визуальными эффектами.

---

> 💬 **Упражнение:** создайте карточку профиля с аватаром (круглая граница), именем, должностью, списком настроек (с разделителями) и кнопкой действия (с focus ring). Используйте только border-утилиты Tailwind!