# 🎯 Состояния элементов в Tailwind CSS

> **Полное руководство по интерактивным состояниям:** от hover и focus до group-hover, peer и кастомных модификаторов

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Освоите все основные модификаторы состояний: hover, focus, active, disabled
- ✅ Поймёте разницу между focus, focus-within и focus-visible
- ✅ Научитесь использовать group-hover и peer для сложных взаимодействий
- ✅ Освоите модификаторы для форм: checked, indeterminate, required, invalid
- ✅ Поймёте порядок применения состояний (specificity)
- ✅ Создадите отзывчивые интерфейсы с богатой интерактивностью
- ✅ Избежите типичных ошибок при работе с состояниями

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

```html
<!-- Изменение фона -->
<button class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded">
  Наведи на меня
</button>

<!-- Изменение текста -->
<a href="#" class="text-gray-600 hover:text-blue-600 hover:underline">
  Ссылка
</a>

<!-- Изменение тени -->
<div class="shadow-md hover:shadow-xl transition-shadow">
  Карточка с усилением тени
</div>

<!-- Изменение масштаба -->
<button class="hover:scale-105 transition-transform">
  Увеличение при hover
</button>
```

### Hover с transition

Всегда добавляйте `transition` для плавных изменений:

```html
<!-- ❌ Плохо: резкое изменение -->
<button class="bg-blue-500 hover:bg-blue-600">Резко</button>

<!-- ✅ Хорошо: плавное изменение -->
<button class="bg-blue-500 hover:bg-blue-600 transition-colors duration-200">
  Плавно
</button>

<!-- ✅ Отлично: плавное изменение всех свойств -->
<button class="bg-blue-500 hover:bg-blue-600 hover:scale-105 hover:shadow-lg transition-all duration-300">
  Все свойства плавно
</button>
```

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

```html
<!-- Focus ring для input -->
<input
  type="text"
  class="border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
  placeholder="Фокус с ring"
>

<!-- Focus для кнопки -->
<button class="focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
  Кнопка с focus ring
</button>

<!-- Focus для ссылки -->
<a href="#" class="focus:outline-none focus:underline focus:text-blue-600">
  Ссылка с focus
</a>
```

### Focus-within: `focus-within:`

Применяется когда **любой дочерний элемент** получает фокус:

```html
<!-- Подсветка контейнера при фокусе на input -->
<div class="border border-gray-300 focus-within:border-blue-500 focus-within:ring-2 focus-within:ring-blue-500/20 rounded-lg p-2">
  <input
    type="text"
    class="w-full focus:outline-none"
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
</button>

<!-- Ссылка меняет цвет при клике -->
<a href="#" class="text-blue-600 hover:text-blue-700 active:text-blue-800">
  Ссылка
</a>
```

## 🚫 Disabled: `disabled:`

Применяется к элементам с атрибутом `disabled`:

```html
<!-- Недоступная кнопка -->
<button
  disabled
  class="bg-blue-500 hover:bg-blue-600 disabled:bg-gray-300 disabled:cursor-not-allowed disabled:opacity-50 text-white px-4 py-2 rounded"
>
  Недоступна
</button>

<!-- Недоступный input -->
<input
  type="text"
  disabled
  class="border border-gray-300 disabled:bg-gray-100 disabled:cursor-not-allowed"
  placeholder="Недоступно"
>
```

## 👥 Group-hover: `group-hover:`

Применяется к **дочерним элементам** при hover на **родительском** элементе с классом `group`:

```html
<!-- Карточка: при hover на карточке меняется стрелка -->
<div class="group bg-white p-6 rounded-lg shadow hover:shadow-lg transition-shadow">
  <h3 class="text-xl font-bold mb-2">Заголовок</h3>
  <p class="text-gray-600 mb-4">Описание</p>
  <div class="flex items-center gap-2 text-blue-600">
    <span>Подробнее</span>
    <svg class="w-4 h-4 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
    </svg>
  </div>
</div>
```

### Group-focus, group-active

```html
<!-- Group-focus -->
<div class="group">
  <input type="text" class="border focus:outline-none">
  <span class="text-gray-400 group-focus-within:text-blue-600">
    Подсказка
  </span>
</div>

<!-- Group-active -->
<div class="group">
  <button class="bg-blue-500 active:bg-blue-700">Кнопка</button>
  <span class="text-gray-600 group-active:text-blue-600">
    Активно
  </span>
</div>
```

## 🤝 Peer: `peer-*:`

Применяется к **соседним элементам** на основе состояния **предыдущего** элемента с классом `peer`:

```html
<!-- Input с валидацией: при фокусе на input меняется label -->
<div class="relative">
  <input
    type="email"
    id="email"
    class="peer border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20 px-4 py-2 rounded w-full"
    placeholder=" "
  >
  <label
    for="email"
    class="absolute left-4 top-2 text-gray-500 peer-focus:top-0 peer-focus:text-xs peer-focus:text-blue-600 peer-[:not(:placeholder-shown)]:top-0 peer-[:not(:placeholder-shown)]:text-xs transition-all"
  >
    Email
  </label>
</div>
```

### Peer-checked для чекбоксов и радиокнопок

```html
<!-- Кастомный чекбокс -->
<label class="flex items-center gap-3 cursor-pointer">
  <input type="checkbox" class="peer sr-only">
  <div class="w-5 h-5 border-2 border-gray-300 rounded peer-checked:bg-blue-500 peer-checked:border-blue-500 flex items-center justify-center transition-colors">
    <svg class="w-3 h-3 text-white opacity-0 peer-checked:opacity-100 transition-opacity" fill="currentColor" viewBox="0 0 20 20">
      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
    </svg>
  </div>
  <span class="text-gray-700">Согласен с условиями</span>
</label>
```

### Peer-disabled

```html
<!-- Label меняется при disabled input -->
<div class="flex items-center gap-2">
  <input type="checkbox" id="option" disabled class="peer">
  <label for="option" class="peer-disabled:text-gray-400 peer-disabled:cursor-not-allowed">
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

```html
<!-- Label поднимается при вводе текста -->
<div class="relative">
  <input
    type="text"
    class="peer pt-5 pb-2 px-4 border rounded w-full"
    placeholder=" "
  >
  <label class="absolute left-4 top-2 text-sm text-gray-500 peer-placeholder-shown:top-4 peer-placeholder-shown:text-base transition-all">
    Имя
  </label>
</div>
```

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
  hover:bg-blue-600
  focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2
  active:bg-blue-700 active:scale-95
  transition-all duration-200
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
  hover:bg-blue-600 dark:hover:bg-blue-700
  focus:ring-blue-500 dark:focus:ring-blue-400
">
  Кнопка
</button>
```

### Состояния + group-hover + peer

```html
<!-- Сложное взаимодействие -->
<div class="group">
  <input type="checkbox" class="peer sr-only">
  <div class="peer-checked:bg-green-500 group-hover:scale-110 transition-all">
    Чекбокс
  </div>
  <span class="group-hover:text-blue-600 peer-checked:text-green-600">
    Текст
  </span>
</div>
```

## 🎨 Практические паттерны

### 1. 🔘 Кнопка с полным набором состояний

```html
<button class="
  bg-blue-600
  hover:bg-blue-700
  focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2
  active:bg-blue-800 active:scale-95
  disabled:bg-gray-300 disabled:cursor-not-allowed disabled:opacity-50
  text-white font-medium px-6 py-3 rounded-lg
  transition-all duration-200
">
  Нажми меня
</button>
```

### 2. 🎴 Карточка с hover-эффектами

```html
<div class="group bg-white rounded-xl shadow-md hover:shadow-xl transition-shadow duration-300 overflow-hidden max-w-sm">
  <div class="relative overflow-hidden">
    <img
      src="product.jpg"
      class="w-full h-48 object-cover group-hover:scale-110 transition-transform duration-500"
      alt="Товар"
    >
    <div class="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-colors duration-300"></div>
    <button class="absolute bottom-4 left-1/2 -translate-x-1/2 bg-white text-gray-900 px-4 py-2 rounded-lg opacity-0 group-hover:opacity-100 transition-opacity duration-300">
      Быстрый просмотр
    </button>
  </div>
  <div class="p-6">
    <h3 class="text-xl font-bold text-gray-900 group-hover:text-blue-600 transition-colors">
      Название товара
    </h3>
    <p class="text-gray-600 mt-2">Описание товара</p>
    <div class="mt-4 flex items-center justify-between">
      <span class="text-2xl font-bold text-gray-900">2 990 ₽</span>
      <button class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg transition-colors">
        В корзину
      </button>
    </div>
  </div>
</div>
```

### 3. 📝 Input с floating label

```html
<div class="relative">
  <input
    type="email"
    id="email"
    class="peer w-full px-4 pt-6 pb-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
    placeholder=" "
  >
  <label
    for="email"
    class="absolute left-4 top-4 text-gray-500 pointer-events-none transition-all
           peer-focus:top-2 peer-focus:text-xs peer-focus:text-blue-600
           peer-[:not(:placeholder-shown)]:top-2 peer-[:not(:placeholder-shown)]:text-xs"
  >
    Email адрес
  </label>
</div>
```

### 4. ✅ Кастомный чекбокс

```html
<label class="flex items-center gap-3 cursor-pointer group">
  <input type="checkbox" class="peer sr-only">
  <div class="
    w-5 h-5 border-2 border-gray-300 rounded
    peer-checked:bg-blue-500 peer-checked:border-blue-500
    group-hover:border-blue-400
    flex items-center justify-center
    transition-colors duration-200
  ">
    <svg
      class="w-3 h-3 text-white opacity-0 peer-checked:opacity-100 transition-opacity duration-200"
      fill="currentColor"
      viewBox="0 0 20 20"
    >
      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
    </svg>
  </div>
  <span class="text-gray-700 group-hover:text-gray-900 transition-colors">
    Согласен с условиями использования
  </span>
</label>
```

### 5. 🎚️ Toggle switch

```html
<label class="relative inline-flex items-center cursor-pointer">
  <input type="checkbox" class="sr-only peer">
  <div class="
    w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300
    rounded-full peer
    peer-checked:after:translate-x-full peer-checked:after:border-white
    after:content-[''] after:absolute after:top-[2px] after:left-[2px]
    after:bg-white after:border-gray-300 after:border after:rounded-full
    after:h-5 after:w-5 after:transition-all
    peer-checked:bg-blue-600
  "></div>
  <span class="ml-3 text-sm font-medium text-gray-900">Уведомления</span>
</label>
```

### 6. 📋 Выпадающее меню

```html
<div class="relative group">
  <button class="bg-gray-100 hover:bg-gray-200 px-4 py-2 rounded-lg transition-colors">
    Меню
  </button>
  <div class="
    absolute top-full left-0 mt-2 w-48 bg-white rounded-lg shadow-lg
    opacity-0 invisible group-hover:opacity-100 group-hover:visible
    transition-all duration-200
  ">
    <a href="#" class="block px-4 py-2 hover:bg-gray-100 transition-colors">Пункт 1</a>
    <a href="#" class="block px-4 py-2 hover:bg-gray-100 transition-colors">Пункт 2</a>
    <a href="#" class="block px-4 py-2 hover:bg-gray-100 transition-colors">Пункт 3</a>
  </div>
</div>
```

### 7. 🎨 Галерея с hover-эффектами

```html
<div class="grid grid-cols-3 gap-4">
  <div class="relative overflow-hidden rounded-lg group cursor-pointer">
    <img
      src="photo1.jpg"
      class="w-full h-48 object-cover group-hover:scale-110 group-hover:brightness-75 transition-all duration-300"
      alt="Фото 1"
    >
    <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
      <span class="text-white text-lg font-bold bg-black/50 px-4 py-2 rounded">
        Просмотр
      </span>
    </div>
  </div>
  <!-- Повторить для других фото -->
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
</div>

<!-- ✅ Хорошо: добавляем group -->
<div class="group">
  <span class="group-hover:text-blue-600">Работает</span>
</div>
```

### ❌ Ошибка 4: `peer:` без класса `peer` на предыдущем элементе

```html
<!-- ❌ Плохо: peer не работает -->
<input type="checkbox">
<span class="peer-checked:text-blue-600">Не работает</span>

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

<!-- ✅ Хорошо: есть focus-состояние -->
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

## 🎯 Что дальше?

Теперь вы полностью владеете состояниями элементов! Но это только часть responsive-дизайна. Следующий уровень — **продвинутые техники Tailwind CSS**: кастомизация, плагины, директивы.

**Следующий шаг:** [⚙️ Кастомизация Tailwind CSS](../advanced/customization.md) — изучим, как расширять конфигурацию и создавать собственные утилиты.

---

> 💬 **Упражнение:** создайте форму регистрации с floating labels, кастомными чекбоксами, toggle switch для уведомлений, и кнопкой с полным набором состояний (hover, focus, active, disabled). Все элементы должны иметь плавные transition-эффекты.