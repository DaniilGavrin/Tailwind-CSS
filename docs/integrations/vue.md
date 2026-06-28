# 🔌 Vue + Tailwind CSS

> **Полное руководство по интеграции Tailwind CSS с Vue 3:** от базовой настройки до Composition API, composables и компонентных библиотек

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Настроите Tailwind CSS в Vue 3 проекте (Vite, Nuxt 3)
- ✅ Освоите `:class` binding — объекты, массивы, computed
- ✅ Научитесь создавать переиспользуемые компоненты
- ✅ Освоите composables для логики стилей
- ✅ Интегрируете TypeScript с `defineProps`
- ✅ Поймёте паттерны для Button, Card, Input и других компонентов
- ✅ Настроите dark mode через composable
- ✅ Избежите типичных ошибок при работе с Vue + Tailwind

## 🚀 Установка и настройка

### Вариант 1: Vite + Vue 3 (рекомендуется)

```bash
# Создание проекта
npm create vite@latest my-app -- --template vue-ts
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

```ts
// src/main.ts
import { createApp } from 'vue'
import App from './App.vue'
import './style.css'

createApp(App).mount('#app')
```

### Вариант 2: Nuxt 3

```bash
npx nuxi@latest init my-app
cd my-app
npm install -D @nuxtjs/tailwindcss
```

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  modules: ['@nuxtjs/tailwindcss'],
  tailwindcss: {
    configPath: 'tailwind.config.js',
  },
})
```

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

## 🎨 Базовое использование `:class`

В Vue используется **`:class` binding** (сокращение от `v-bind:class`) для динамических классов:

### Статические классы

```vue
<template>
  <div class="bg-white rounded-lg shadow-md p-6">
    <h3 class="text-xl font-bold text-gray-900">Заголовок</h3>
    <p class="text-gray-600 mt-2">Описание</p>
  </div>
</template>
```

### Динамические классы через объект

```vue
<template>
  <button
    :class="{
      'bg-blue-600 text-white': isPrimary,
      'bg-gray-200 text-gray-900': !isPrimary,
      'opacity-50 cursor-not-allowed': disabled,
      'px-4 py-2 rounded-lg': true,
    }"
    :disabled="disabled"
  >
    <slot />
  </button>
</template>

<script setup lang="ts">
defineProps<{
  isPrimary?: boolean
  disabled?: boolean
}>()
</script>
```

### Динамические классы через массив

```vue
<template>
  <div :class="[baseClass, sizeClass, variantClass]">
    <slot />
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  size?: 'sm' | 'md' | 'lg'
  variant?: 'primary' | 'secondary' | 'danger'
}>(), {
  size: 'md',
  variant: 'primary',
})

const baseClass = 'px-4 py-2 rounded-lg font-medium transition-colors'

const sizeClass = computed(() => ({
  sm: 'text-sm px-3 py-1.5',
  md: 'text-base px-4 py-2',
  lg: 'text-lg px-6 py-3',
}[props.size]))

const variantClass = computed(() => ({
  primary: 'bg-blue-600 text-white hover:bg-blue-700',
  secondary: 'bg-gray-200 text-gray-900 hover:bg-gray-300',
  danger: 'bg-red-600 text-white hover:bg-red-700',
}[props.variant]))
</script>
```

### Тернарный оператор

```vue
<template>
  <div
    :class="isActive
      ? 'bg-blue-600 text-white'
      : 'bg-gray-100 text-gray-900'"
  >
    Контент
  </div>
</template>
```

## 🛠 Библиотеки для работы с классами

### clsx + tailwind-merge (рекомендуется)

```bash
npm install clsx tailwind-merge
```

```ts
// lib/utils.ts
import { type ClassValue, clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
```

```vue
<template>
  <button :class="cn(
    'px-4 py-2 rounded-lg font-medium',
    variant === 'primary' && 'bg-blue-600 text-white hover:bg-blue-700',
    variant === 'secondary' && 'bg-gray-200 text-gray-900 hover:bg-gray-300',
    size === 'lg' && 'px-6 py-3 text-lg',
    className
  )">
    <slot />
  </button>
</template>

<script setup lang="ts">
import { cn } from '@/lib/utils'

withDefaults(defineProps<{
  variant?: 'primary' | 'secondary' | 'danger'
  size?: 'sm' | 'md' | 'lg'
  className?: string
}>(), {
  variant: 'primary',
  size: 'md',
})
</script>
```

### class-variance-authority (cva)

```bash
npm install class-variance-authority
```

```ts
// components/ui/button.ts
import { cva, type VariantProps } from 'class-variance-authority'
import { cn } from '@/lib/utils'

export const buttonVariants = cva(
  'inline-flex items-center justify-center rounded-lg font-medium transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:pointer-events-none disabled:opacity-50',
  {
    variants: {
      variant: {
        primary: 'bg-blue-600 text-white hover:bg-blue-700 focus:ring-blue-500',
        secondary: 'bg-gray-100 text-gray-900 hover:bg-gray-200 focus:ring-gray-500',
        danger: 'bg-red-600 text-white hover:bg-red-700 focus:ring-red-500',
        outline: 'border border-gray-300 bg-transparent hover:bg-gray-50',
        ghost: 'bg-transparent hover:bg-gray-100',
      },
      size: {
        sm: 'h-8 px-3 text-sm',
        md: 'h-10 px-4',
        lg: 'h-12 px-6 text-lg',
        icon: 'h-10 w-10',
      },
    },
    defaultVariants: {
      variant: 'primary',
      size: 'md',
    },
  }
)

export type ButtonVariants = VariantProps<typeof buttonVariants>
```

```vue
<!-- components/ui/Button.vue -->
<template>
  <button
    :class="cn(buttonVariants({ variant, size }), $attrs.class)"
    v-bind="$attrs"
  >
    <slot />
  </button>
</template>

<script setup lang="ts">
import { buttonVariants, type ButtonVariants } from './button'
import { cn } from '@/lib/utils'

defineProps<ButtonVariants>()
</script>
```

```vue
<!-- Использование -->
<template>
  <Button variant="primary" size="md">Сохранить</Button>
  <Button variant="danger" size="lg">Удалить</Button>
  <Button variant="outline" size="sm">Отмена</Button>
</template>
```

## 🧩 Composables для переиспользования

### useTheme — управление темой

```ts
// composables/useTheme.ts
import { ref, watchEffect, computed } from 'vue'

type Theme = 'light' | 'dark' | 'system'

const theme = ref<Theme>(
  (localStorage.getItem('theme') as Theme) || 'system'
)

export function useTheme() {
  const resolvedTheme = computed<'light' | 'dark'>(() => {
    if (theme.value === 'system') {
      return window.matchMedia('(prefers-color-scheme: dark)').matches
        ? 'dark'
        : 'light'
    }
    return theme.value
  })

  const isDark = computed(() => resolvedTheme.value === 'dark')

  function setTheme(newTheme: Theme) {
    theme.value = newTheme
    localStorage.setItem('theme', newTheme)
  }

  function toggleTheme() {
    setTheme(isDark.value ? 'light' : 'dark')
  }

  watchEffect(() => {
    const root = document.documentElement
    root.classList.remove('light', 'dark')
    root.classList.add(resolvedTheme.value)
  })

  return {
    theme,
    resolvedTheme,
    isDark,
    setTheme,
    toggleTheme,
  }
}
```

```vue
<!-- components/ThemeToggle.vue -->
<template>
  <div class="inline-flex items-center gap-1 bg-gray-100 dark:bg-gray-800 p-1 rounded-lg">
    <button
      v-for="mode in (['light', 'dark', 'system'] as const)"
      :key="mode"
      @click="setTheme(mode)"
      :class="cn(
        'p-2 rounded-md transition-colors',
        theme === mode && 'bg-white dark:bg-gray-700 shadow-sm'
      )"
      :aria-label="`Тема: ${mode}`"
    >
      <Sun v-if="mode === 'light'" class="w-4 h-4" />
      <Moon v-else-if="mode === 'dark'" class="w-4 h-4" />
      <Monitor v-else class="w-4 h-4" />
    </button>
  </div>
</template>

<script setup lang="ts">
import { useTheme } from '@/composables/useTheme'
import { cn } from '@/lib/utils'
import { Sun, Moon, Monitor } from 'lucide-vue-next'

const { theme, setTheme } = useTheme()
</script>
```

### useClassMerge — объединение классов

```ts
// composables/useClassMerge.ts
import { computed, type MaybeRefOrGetter } from 'vue'
import { cn } from '@/lib/utils'

export function useClassMerge(
  ...classes: MaybeRefOrGetter<string | undefined | null | false>[]
) {
  return computed(() => {
    const resolved = classes.map(cls => {
      if (typeof cls === 'function') return cls()
      return cls
    })
    return cn(...resolved)
  })
}
```

```vue
<template>
  <div :class="mergedClass">
    <slot />
  </div>
</template>

<script setup lang="ts">
import { useClassMerge } from '@/composables/useClassMerge'

const props = defineProps<{
  variant?: 'primary' | 'secondary'
  class?: string
}>()

const mergedClass = useClassMerge(
  'base-classes',
  () => props.variant === 'primary' ? 'bg-blue-500' : 'bg-gray-500',
  () => props.class
)
</script>
```

## 📘 TypeScript + Vue

### Типизация пропсов

```vue
<template>
  <button
    :class="cn(buttonVariants({ variant, size }), $attrs.class)"
    :disabled="disabled || isLoading"
    v-bind="$attrs"
  >
    <Loader2 v-if="isLoading" class="mr-2 h-4 w-4 animate-spin" />
    <slot />
  </button>
</template>

<script setup lang="ts">
import { buttonVariants, type ButtonVariants } from './button'
import { cn } from '@/lib/utils'
import { Loader2 } from 'lucide-vue-next'

interface Props extends ButtonVariants {
  isLoading?: boolean
  disabled?: boolean
}

withDefaults(defineProps<Props>(), {
  variant: 'primary',
  size: 'md',
  isLoading: false,
  disabled: false,
})
</script>
```

### Типизация emits

```vue
<template>
  <input
    :value="modelValue"
    @input="$emit('update:modelValue', ($event.target as HTMLInputElement).value)"
    :class="cn(
      'w-full px-4 py-2 border rounded-lg',
      error ? 'border-red-500' : 'border-gray-300'
    )"
  >
</template>

<script setup lang="ts">
import { cn } from '@/lib/utils'

defineProps<{
  modelValue: string
  error?: string
}>()

defineEmits<{
  'update:modelValue': [value: string]
}>()
</script>
```

### defineModel (Vue 3.4+)

```vue
<template>
  <input
    v-model="model"
    :class="cn(
      'w-full px-4 py-2 border rounded-lg',
      error ? 'border-red-500 focus:ring-red-500' : 'border-gray-300 focus:ring-blue-500'
    )"
  >
</template>

<script setup lang="ts">
import { cn } from '@/lib/utils'

const model = defineModel<string>({ required: true })

defineProps<{
  error?: string
}>()
</script>
```

## 🎨 Практические паттерны компонентов

### 1. 🔘 Button (полноценный)

```vue
<!-- components/ui/Button.vue -->
<template>
  <component
    :is="as"
    :class="cn(buttonVariants({ variant, size }), $attrs.class)"
    :disabled="disabled || isLoading"
    v-bind="$attrs"
  >
    <Loader2 v-if="isLoading" class="mr-2 h-4 w-4 animate-spin" />
    <slot />
  </component>
</template>

<script setup lang="ts">
import { cn } from '@/lib/utils'
import { buttonVariants, type ButtonVariants } from './button'
import { Loader2 } from 'lucide-vue-next'

interface Props extends ButtonVariants {
  as?: string | Component
  isLoading?: boolean
  disabled?: boolean
}

withDefaults(defineProps<Props>(), {
  as: 'button',
  variant: 'primary',
  size: 'md',
  isLoading: false,
  disabled: false,
})
</script>
```

### 2. 🎴 Card

```vue
<!-- components/ui/Card.vue -->
<template>
  <div :class="cn(
    'bg-white rounded-xl shadow-sm border border-gray-200',
    hover && 'transition-shadow hover:shadow-md',
    $attrs.class
  )">
    <slot />
  </div>
</template>

<script setup lang="ts">
import { cn } from '@/lib/utils'

defineProps<{
  hover?: boolean
}>()
</script>
```

```vue
<!-- components/ui/CardHeader.vue -->
<template>
  <div :class="cn('flex flex-col space-y-1.5 p-6 border-b', $attrs.class)">
    <slot />
  </div>
</template>

<script setup lang="ts">
import { cn } from '@/lib/utils'
</script>
```

```vue
<!-- Использование -->
<Card hover>
  <CardHeader>
    <h3 class="text-xl font-bold">Заголовок</h3>
    <p class="text-sm text-gray-500">Описание</p>
  </CardHeader>
  <div class="p-6">
    <p>Содержимое карточки</p>
  </div>
  <div class="p-6 pt-0">
    <Button>Действие</Button>
  </div>
</Card>
```

### 3. 📝 Input с v-model

```vue
<!-- components/ui/Input.vue -->
<template>
  <div class="w-full">
    <label
      v-if="label"
      :for="inputId"
      class="block text-sm font-medium text-gray-700 mb-1"
    >
      {{ label }}
    </label>
    <input
      :id="inputId"
      :value="modelValue"
      @input="$emit('update:modelValue', ($event.target as HTMLInputElement).value)"
      :type="type"
      :placeholder="placeholder"
      :class="cn(
        'flex h-10 w-full rounded-lg border bg-white px-3 py-2 text-sm',
        'placeholder:text-gray-400',
        'focus:outline-none focus:ring-2 focus:ring-offset-1',
        'disabled:cursor-not-allowed disabled:opacity-50',
        error
          ? 'border-red-500 focus:border-red-500 focus:ring-red-500'
          : 'border-gray-300 focus:border-blue-500 focus:ring-blue-500',
        $attrs.class
      )"
    >
    <p v-if="error" class="mt-1 text-sm text-red-500">{{ error }}</p>
    <p v-else-if="hint" class="mt-1 text-sm text-gray-500">{{ hint }}</p>
  </div>
</template>

<script setup lang="ts">
import { cn } from '@/lib/utils'

defineProps<{
  modelValue: string
  label?: string
  type?: string
  placeholder?: string
  error?: string
  hint?: string
}>()

defineEmits<{
  'update:modelValue': [value: string]
}>()

const inputId = `input-${Math.random().toString(36).slice(2)}`
</script>
```

```vue
<!-- Использование -->
<Input
  v-model="email"
  label="Email"
  type="email"
  placeholder="you@example.com"
  :error="errors.email"
/>
```

### 4. 🏷️ Badge

```vue
<!-- components/ui/Badge.vue -->
<template>
  <div :class="cn(badgeVariants({ variant }), $attrs.class)">
    <slot />
  </div>
</template>

<script setup lang="ts">
import { cn } from '@/lib/utils'
import { cva, type VariantProps } from 'class-variance-authority'

const badgeVariants = cva(
  'inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-semibold transition-colors',
  {
    variants: {
      variant: {
        default: 'bg-blue-100 text-blue-800',
        secondary: 'bg-gray-100 text-gray-800',
        success: 'bg-green-100 text-green-800',
        warning: 'bg-yellow-100 text-yellow-800',
        danger: 'bg-red-100 text-red-800',
        outline: 'border border-gray-300 text-gray-700',
      },
    },
    defaultVariants: {
      variant: 'default',
    },
  }
)

defineProps<VariantProps<typeof badgeVariants>>()
</script>
```

### 5. 🎚️ Toggle / Switch

```vue
<!-- components/ui/Toggle.vue -->
<template>
  <label :class="cn(
    'inline-flex items-center cursor-pointer',
    disabled && 'opacity-50 cursor-not-allowed'
  )">
    <input
      type="checkbox"
      class="sr-only peer"
      :checked="modelValue"
      @change="$emit('update:modelValue', ($event.target as HTMLInputElement).checked)"
      :disabled="disabled"
    >
    <div :class="cn(
      'relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300',
      'rounded-full peer',
      'peer-checked:after:translate-x-full peer-checked:after:border-white',
      'after:content-[\'\'] after:absolute after:top-[2px] after:left-[2px]',
      'after:bg-white after:border-gray-300 after:border after:rounded-full',
      'after:h-5 after:w-5 after:transition-all',
      'dark:bg-gray-700 dark:peer-focus:ring-blue-800',
      modelValue && 'bg-blue-600'
    )" />
    <span v-if="label" class="ml-3 text-sm font-medium text-gray-900 dark:text-gray-300">
      {{ label }}
    </span>
  </label>
</template>

<script setup lang="ts">
import { cn } from '@/lib/utils'

defineProps<{
  modelValue: boolean
  label?: string
  disabled?: boolean
}>()

defineEmits<{
  'update:modelValue': [value: boolean]
}>()
</script>
```

### 6. 📋 Select

```vue
<!-- components/ui/Select.vue -->
<template>
  <div class="w-full">
    <label
      v-if="label"
      :for="selectId"
      class="block text-sm font-medium text-gray-700 mb-1"
    >
      {{ label }}
    </label>
    <select
      :id="selectId"
      :value="modelValue"
      @change="$emit('update:modelValue', ($event.target as HTMLSelectElement).value)"
      :class="cn(
        'flex h-10 w-full rounded-lg border bg-white px-3 py-2 text-sm',
        'focus:outline-none focus:ring-2 focus:ring-offset-1',
        'disabled:cursor-not-allowed disabled:opacity-50',
        error
          ? 'border-red-500 focus:border-red-500 focus:ring-red-500'
          : 'border-gray-300 focus:border-blue-500 focus:ring-blue-500',
        $attrs.class
      )"
    >
      <option v-if="placeholder" value="" disabled>{{ placeholder }}</option>
      <option
        v-for="option in options"
        :key="option.value"
        :value="option.value"
      >
        {{ option.label }}
      </option>
    </select>
    <p v-if="error" class="mt-1 text-sm text-red-500">{{ error }}</p>
  </div>
</template>

<script setup lang="ts">
import { cn } from '@/lib/utils'

defineProps<{
  modelValue: string
  options: Array<{ value: string; label: string }>
  label?: string
  placeholder?: string
  error?: string
}>()

defineEmits<{
  'update:modelValue': [value: string]
}>()

const selectId = `select-${Math.random().toString(36).slice(2)}`
</script>
```

## 🎯 Практические паттерны

### 1. 📱 Responsive Sidebar с composables

```vue
<!-- composables/useSidebar.ts -->
import { ref } from 'vue'

const isOpen = ref(false)

export function useSidebar() {
  function toggle() {
    isOpen.value = !isOpen.value
  }

  function close() {
    isOpen.value = false
  }

  return { isOpen, toggle, close }
}
```

```vue
<!-- components/Dashboard.vue -->
<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Mobile header -->
    <div class="lg:hidden flex items-center justify-between p-4 bg-white border-b">
      <span class="font-bold text-xl">Logo</span>
      <button
        @click="toggle"
        class="p-2 rounded-lg hover:bg-gray-100"
      >
        <Menu v-if="!isOpen" class="w-6 h-6" />
        <X v-else class="w-6 h-6" />
      </button>
    </div>

    <div class="flex">
      <!-- Sidebar -->
      <aside
        :class="cn(
          'fixed inset-y-0 left-0 z-50 w-64 bg-white border-r transform transition-transform lg:translate-x-0 lg:static lg:inset-0',
          isOpen ? 'translate-x-0' : '-translate-x-full'
        )"
      >
        <div class="p-4">
          <h2 class="font-bold text-xl mb-4 hidden lg:block">Logo</h2>
          <nav class="space-y-1">
            <RouterLink
              v-for="item in menuItems"
              :key="item.path"
              :to="item.path"
              class="block px-4 py-2 rounded-lg text-gray-700 hover:bg-gray-100"
              active-class="bg-blue-50 text-blue-600"
            >
              {{ item.label }}
            </RouterLink>
          </nav>
        </div>
      </aside>

      <!-- Overlay -->
      <div
        v-if="isOpen"
        class="fixed inset-0 bg-black/50 z-40 lg:hidden"
        @click="close"
      />

      <!-- Main content -->
      <main class="flex-1 p-4 lg:p-8">
        <RouterView />
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useSidebar } from '@/composables/useSidebar'
import { cn } from '@/lib/utils'
import { Menu, X } from 'lucide-vue-next'
import { RouterLink, RouterView } from 'vue-router'

const { isOpen, toggle, close } = useSidebar()

const menuItems = [
  { path: '/', label: 'Главная' },
  { path: '/profile', label: 'Профиль' },
  { path: '/settings', label: 'Настройки' },
]
</script>
```

### 2. 🎴 Карточка товара с hover-эффектами

```vue
<!-- components/ProductCard.vue -->
<template>
  <div class="group bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-lg transition-shadow">
    <!-- Изображение -->
    <div class="relative aspect-square overflow-hidden">
      <img
        :src="image"
        :alt="title"
        class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
      >
      
      <!-- Бейдж -->
      <Badge
        v-if="badge"
        variant="danger"
        class="absolute top-3 left-4"
      >
        {{ badge }}
      </Badge>

      <!-- Кнопка избранного -->
      <button
        @click="isFavorite = !isFavorite"
        :class="cn(
          'absolute top-3 right-3 p-2 rounded-full transition-all',
          isFavorite
            ? 'bg-red-500 text-white'
            : 'bg-white/80 text-gray-700 hover:bg-white'
        )"
      >
        <Heart :class="cn('w-5 h-5', isFavorite && 'fill-current')" />
      </button>

      <!-- Overlay с кнопкой -->
      <div class="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-colors flex items-center justify-center opacity-0 group-hover:opacity-100">
        <Button variant="outline" class="bg-white">
          Быстрый просмотр
        </Button>
      </div>
    </div>

    <!-- Контент -->
    <div class="p-4">
      <h3 class="font-medium text-gray-900 line-clamp-2">{{ title }}</h3>
      <div class="mt-2 flex items-baseline gap-2">
        <span class="text-xl font-bold text-gray-900">
          {{ price.toLocaleString('ru-RU') }} ₽
        </span>
        <span v-if="oldPrice" class="text-sm text-gray-400 line-through">
          {{ oldPrice.toLocaleString('ru-RU') }} ₽
        </span>
      </div>
      <Button class="mt-3 w-full" @click="$emit('addToCart')">
        <ShoppingCart class="w-4 h-4 mr-2" />
        В корзину
      </Button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { cn } from '@/lib/utils'
import { Heart, ShoppingCart } from 'lucide-vue-next'
import Badge from './ui/Badge.vue'
import Button from './ui/Button.vue'

defineProps<{
  title: string
  price: number
  oldPrice?: number
  image: string
  badge?: string
}>()

defineEmits<{
  addToCart: []
}>()

const isFavorite = ref(false)
</script>
```

### 3. 📊 Таблица с сортировкой

```vue
<!-- components/UsersTable.vue -->
<template>
  <div class="bg-white rounded-xl shadow-sm border overflow-hidden">
    <div class="overflow-x-auto">
      <table class="w-full">
        <thead class="bg-gray-50 border-b">
          <tr>
            <th
              v-for="column in columns"
              :key="column.key"
              @click="handleSort(column.key)"
              class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100"
            >
              <div class="flex items-center gap-1">
                {{ column.label }}
                <ArrowUpDown :class="cn(
                  'w-3 h-3',
                  sortField === column.key ? 'text-blue-600' : 'text-gray-400'
                )" />
              </div>
            </th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-200">
          <tr
            v-for="user in sortedUsers"
            :key="user.id"
            class="hover:bg-gray-50 transition-colors"
          >
            <td class="px-6 py-4 font-medium text-gray-900">{{ user.name }}</td>
            <td class="px-6 py-4 text-gray-600">{{ user.email }}</td>
            <td class="px-6 py-4 text-gray-600">{{ user.role }}</td>
            <td class="px-6 py-4">
              <Badge :variant="statusVariant(user.status)">
                {{ user.status }}
              </Badge>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { cn } from '@/lib/utils'
import { ArrowUpDown } from 'lucide-vue-next'
import Badge from './ui/Badge.vue'

interface User {
  id: number
  name: string
  email: string
  role: string
  status: 'active' | 'pending' | 'inactive'
}

const props = defineProps<{
  users: User[]
}>()

const columns = [
  { key: 'name', label: 'Имя' },
  { key: 'email', label: 'Email' },
  { key: 'role', label: 'Роль' },
  { key: 'status', label: 'Статус' },
]

const sortField = ref<keyof User>('name')
const sortDirection = ref<'asc' | 'desc'>('asc')

function handleSort(field: keyof User) {
  if (sortField.value === field) {
    sortDirection.value = sortDirection.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortField.value = field
    sortDirection.value = 'asc'
  }
}

const sortedUsers = computed(() => {
  return [...props.users].sort((a, b) => {
    const aValue = a[sortField.value]
    const bValue = b[sortField.value]
    if (aValue < bValue) return sortDirection.value === 'asc' ? -1 : 1
    if (aValue > bValue) return sortDirection.value === 'asc' ? 1 : -1
    return 0
  })
})

function statusVariant(status: User['status']) {
  return {
    active: 'success',
    pending: 'warning',
    inactive: 'secondary',
  }[status] as 'success' | 'warning' | 'secondary'
}
</script>
```

### 4. 📝 Форма с валидацией

```vue
<!-- components/RegisterForm.vue -->
<template>
  <form @submit.prevent="handleSubmit" class="space-y-4 max-w-md mx-auto p-6 bg-white rounded-xl shadow-md">
    <h2 class="text-2xl font-bold text-gray-900">Регистрация</h2>

    <Input
      v-model="form.name"
      label="Имя"
      placeholder="Иван Иванов"
      :error="errors.name"
    />

    <Input
      v-model="form.email"
      label="Email"
      type="email"
      placeholder="you@example.com"
      :error="errors.email"
    />

    <Input
      v-model="form.password"
      label="Пароль"
      type="password"
      placeholder="••••••••"
      :error="errors.password"
    />

    <Toggle
      v-model="form.newsletter"
      label="Получать новости"
    />

    <Button
      type="submit"
      class="w-full"
      :is-loading="isSubmitting"
    >
      Зарегистрироваться
    </Button>
  </form>
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue'
import Input from './ui/Input.vue'
import Button from './ui/Button.vue'
import Toggle from './ui/Toggle.vue'

const form = reactive({
  name: '',
  email: '',
  password: '',
  newsletter: false,
})

const errors = reactive({
  name: '',
  email: '',
  password: '',
})

const isSubmitting = ref(false)

function validate() {
  errors.name = form.name.length < 2 ? 'Минимум 2 символа' : ''
  errors.email = /^\S+@\S+$/.test(form.email) ? '' : 'Неверный email'
  errors.password = form.password.length < 8 ? 'Минимум 8 символов' : ''
  return !errors.name && !errors.email && !errors.password
}

async function handleSubmit() {
  if (!validate()) return

  isSubmitting.value = true
  try {
    await new Promise(resolve => setTimeout(resolve, 1000))
    console.log('Form submitted:', form)
  } finally {
    isSubmitting.value = false
  }
}
</script>
```

## 🛣️ Vue Router + Tailwind

### Активные ссылки

```vue
<!-- components/Navigation.vue -->
<template>
  <nav class="bg-white border-b border-gray-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16">
        <div class="flex">
          <RouterLink to="/" class="flex items-center font-bold text-xl text-gray-900">
            Logo
          </RouterLink>
          <div class="hidden sm:ml-6 sm:flex sm:space-x-8">
            <RouterLink
              v-for="item in links"
              :key="item.path"
              :to="item.path"
              :class="cn(
                'inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium transition-colors',
                $route.path === item.path
                  ? 'border-blue-500 text-gray-900'
                  : 'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700'
              )"
            >
              {{ item.label }}
            </RouterLink>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { RouterLink, useRoute } from 'vue-router'
import { cn } from '@/lib/utils'

const route = useRoute()

const links = [
  { path: '/', label: 'Главная' },
  { path: '/about', label: 'О нас' },
  { path: '/contact', label: 'Контакты' },
]
</script>
```

### useRoute в composables

```ts
// composables/useActiveLink.ts
import { computed } from 'vue'
import { useRoute } from 'vue-router'

export function useActiveLink(path: string) {
  const route = useRoute()
  
  const isActive = computed(() => route.path === path)
  const isExactActive = computed(() => route.path === path)
  
  return {
    isActive,
    isExactActive,
    activeClass: computed(() => isActive.value ? 'text-blue-600 font-medium' : 'text-gray-600'),
  }
}
```

## 📊 Шпаргалка: что когда использовать

| Задача | Решение |
| :-- | :-- |
| Статические классы | `class="..."` |
| Динамические классы (объект) | `:class="{ active: isActive }"` |
| Динамические классы (массив) | `:class="[base, condition && 'active']"` |
| Объединение классов | `cn()` = `twMerge(clsx(...))` |
| Вариативные компоненты | `cva` (class-variance-authority) |
| Передача классов в дочерний | `$attrs.class` |
| v-model для классов | `defineModel()` |
| Переиспользование логики | Composables |
| Dark mode | `useTheme()` composable |
| Активные ссылки | `useRoute()` + `cn()` |
| Формы | `reactive()` + валидация |

## 🚫 Частые ошибки

### ❌ Ошибка 1: Забывают `:` перед `class`

```vue
<!-- ❌ Плохо: статическая строка, не будет работать -->
<button class="{ 'bg-blue-500': isPrimary }">Кнопка</button>

<!-- ✅ Хорошо: v-bind для динамических классов -->
<button :class="{ 'bg-blue-500': isPrimary }">Кнопка</button>
```

### ❌ Ошибка 2: Динамическая конкатенация классов

```vue
<!-- ❌ Плохо: Tailwind не увидит эти классы -->
<button :class="`btn-${variant}`">Кнопка</button>

<!-- ✅ Хорошо: полные имена классов -->
<button :class="variants[variant]">Кнопка</button>
```

### ❌ Ошибка 3: Забывают про `$attrs.class`

```vue
<!-- ❌ Плохо: пользовательские классы игнорируются -->
<template>
  <button class="btn">
    <slot />
  </button>
</template>

<!-- ✅ Хорошо: передаём пользовательские классы -->
<template>
  <button :class="cn('btn', $attrs.class)">
    <slot />
  </button>
</template>
```

### ❌ Ошибка 4: Мутация пропсов

```vue
<!-- ❌ Плохо: нельзя мутировать пропсы -->
<script setup>
const props = defineProps<{ class: string }>()
props.class = 'new-class' // Ошибка!
</script>

<!-- ✅ Хорошо: используем локальную переменную или computed -->
<script setup>
const props = defineProps<{ class?: string }>()
const mergedClass = computed(() => cn('base', props.class))
</script>
```

### ❌ Ошибка 5: Забывают про `inheritAttrs: false`

```vue
<!-- ❌ Плохо: атрибуты дублируются -->
<template>
  <div class="wrapper">
    <input :class="$attrs.class" />
  </div>
</template>

<!-- ✅ Хорошо: отключаем автоматическое наследование -->
<template>
  <div class="wrapper">
    <input :class="$attrs.class" v-bind="$attrs" />
  </div>
</template>

<script setup>
defineOptions({ inheritAttrs: false })
</script>
```

### ❌ Ошибка 6: `watchEffect` без cleanup

```ts
// ❌ Плохо: подписка не очищается
watchEffect(() => {
  window.addEventListener('resize', handleResize)
})

// ✅ Хорошо: возвращаем cleanup функцию
watchEffect((onCleanup) => {
  window.addEventListener('resize', handleResize)
  onCleanup(() => {
    window.removeEventListener('resize', handleResize)
  })
})
```

### ❌ Ошибка 7: Забывают про `content` в конфиге

```js
// ❌ Плохо: Tailwind не найдёт классы в .vue файлах
module.exports = {
  content: ['./src/**/*.js'],
}

// ✅ Хорошо: указываем .vue файлы
module.exports = {
  content: ['./src/**/*.{vue,js,ts}'],
}
```

### ❌ Ошибка 8: Избыточные `<div>` обёртки

```vue
<!-- ❌ Плохо: лишний div -->
<template>
  <div>
    <div class="card">
      <p>Контент</p>
    </div>
  </div>
</template>

<!-- ✅ Хорошо: применяем классы напрямую -->
<template>
  <div class="card">
    <p>Контент</p>
  </div>
</template>
```

### ❌ Ошибка 9: Не типизируют emits

```vue
<!-- ❌ Плохо: нет типов для событий -->
<script setup>
defineEmits(['update:modelValue'])
</script>

<!-- ✅ Хорошо: типизированные emits -->
<script setup lang="ts">
defineEmits<{
  'update:modelValue': [value: string]
  'submit': []
}>()
</script>
```

### ❌ Ошибка 10: Забывают про `defineModel` (Vue 3.4+)

```vue
<!-- ❌ Плохо: много кода для v-model -->
<script setup>
const props = defineProps<{ modelValue: string }>()
const emit = defineEmits(['update:modelValue'])
</script>
<template>
  <input
    :value="props.modelValue"
    @input="emit('update:modelValue', $event.target.value)"
  >
</template>

<!-- ✅ Хорошо: defineModel упрощает код -->
<script setup>
const model = defineModel<string>()
</script>
<template>
  <input v-model="model">
</template>
```

## 🎯 Что дальше?

Теперь вы полностью владеете интеграцией Vue + Tailwind CSS! Но это только одна из популярных связок.

**Следующий шаг:** [🚀 Next.js + Tailwind CSS](nextjs.md) — изучим интеграцию с Next.js, Server Components и App Router.

---