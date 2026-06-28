# ⚛️ React + Tailwind CSS

> **Полное руководство по интеграции Tailwind CSS с React:** от базовой настройки до продвинутых паттернов с TypeScript, динамическими классами и компонентными библиотеками

## 🎯 Что вы узнаете

После прочтения этого раздела вы:

- ✅ Настроите Tailwind CSS в React-проекте (Vite, CRA, Next.js)
- ✅ Освоите работу с `className` и динамическими классами
- ✅ Научитесь использовать `clsx`, `classnames`, `tailwind-merge`
- ✅ Создадите компонентные библиотеки с `cva` (class-variance-authority)
- ✅ Интегрируете TypeScript с типизацией классов
- ✅ Освоите паттерны для Button, Card, Input и других компонентов
- ✅ Настроите dark mode в React-приложении
- ✅ Избежите типичных ошибок при работе с React + Tailwind

## 🚀 Установка и настройка

### Вариант 1: Vite + React (рекомендуется)

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

### Вариант 2: Create React App (legacy)

```bash
npx create-react-app my-app
cd my-app
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

### Вариант 3: Next.js

```bash
npx create-next-app@latest my-app
cd my-app
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

Next.js автоматически настраивает PostCSS, поэтому конфиг проще:

```js
// tailwind.config.js
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
    './app/**/*.{js,ts,jsx,tsx}',
  ],
}
```

## 🎨 Базовое использование в JSX

### `className` вместо `class`

В React используется `className` вместо `class` (так как `class` — зарезервированное слово в JS):

```jsx
// ❌ Неправильно
<div class="bg-blue-500 text-white">...</div>

// ✅ Правильно
<div className="bg-blue-500 text-white">...</div>
```

### Динамические стили через JavaScript

```jsx
function Card({ title, description, variant = 'default' }) {
  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <h3 className="text-xl font-bold text-gray-900">{title}</h3>
      <p className="text-gray-600 mt-2">{description}</p>
    </div>
  )
}
```

## 🔄 Динамические классы

### Условные классы через template literals

```jsx
function Button({ variant = 'primary', size = 'md', children }) {
  return (
    <button
      className={`
        rounded-lg font-medium transition-colors
        ${variant === 'primary' ? 'bg-blue-600 text-white hover:bg-blue-700' : ''}
        ${variant === 'secondary' ? 'bg-gray-200 text-gray-900 hover:bg-gray-300' : ''}
        ${variant === 'danger' ? 'bg-red-600 text-white hover:bg-red-700' : ''}
        ${size === 'sm' ? 'px-3 py-1.5 text-sm' : ''}
        ${size === 'md' ? 'px-4 py-2' : ''}
        ${size === 'lg' ? 'px-6 py-3 text-lg' : ''}
      `}
    >
      {children}
    </button>
  )
}
```

### Условные классы через тернарный оператор

```jsx
function Badge({ status }) {
  return (
    <span
      className={`
        px-2 py-1 rounded-full text-xs font-medium
        ${status === 'active' ? 'bg-green-100 text-green-800' : ''}
        ${status === 'pending' ? 'bg-yellow-100 text-yellow-800' : ''}
        ${status === 'error' ? 'bg-red-100 text-red-800' : ''}
      `}
    >
      {status}
    </span>
  )
}
```

### Условные классы через объект

```jsx
function Button({ isActive, isDisabled, children }) {
  return (
    <button
      className={{
        'bg-blue-600 text-white': isActive,
        'bg-gray-200 text-gray-500': !isActive,
        'opacity-50 cursor-not-allowed': isDisabled,
        'px-4 py-2 rounded-lg': true,
      }}
    >
      {children}
    </button>
  )
}
```

> ⚠️ **Важно:** объект в `className` не работает нативно в React! Нужна библиотека `classnames` или `clsx`.

## 🛠 Библиотеки для работы с классами

### clsx (рекомендуется)

Лёгкая утилита для условных классов:

```bash
npm install clsx
```

```jsx
import clsx from 'clsx'

function Button({ variant = 'primary', size = 'md', isActive, children }) {
  return (
    <button
      className={clsx(
        // Базовые классы
        'rounded-lg font-medium transition-colors',
        
        // Варианты
        {
          'bg-blue-600 text-white hover:bg-blue-700': variant === 'primary',
          'bg-gray-200 text-gray-900 hover:bg-gray-300': variant === 'secondary',
          'bg-red-600 text-white hover:bg-red-700': variant === 'danger',
        },
        
        // Размеры
        {
          'px-3 py-1.5 text-sm': size === 'sm',
          'px-4 py-2': size === 'md',
          'px-6 py-3 text-lg': size === 'lg',
        },
        
        // Состояния
        isActive && 'ring-2 ring-blue-500'
      )}
    >
      {children}
    </button>
  )
}
```

### classnames

Альтернатива `clsx` с тем же API:

```bash
npm install classnames
```

```jsx
import classNames from 'classnames'

const buttonClass = classNames(
  'px-4 py-2 rounded-lg',
  {
    'bg-blue-600': isPrimary,
    'bg-red-600': isDanger,
  }
)
```

### tailwind-merge

Решает проблему **конфликта классов** при их объединении:

```bash
npm install tailwind-merge
```

```jsx
import { twMerge } from 'tailwind-merge'

// ❌ Без twMerge: p-4 перезаписывается p-8, но оба остаются в строке
const className = twMerge('p-4 bg-blue-500', 'p-8')
// Результат: "bg-blue-500 p-8" (p-4 удалён!)

// ✅ С twMerge: корректное разрешение конфликтов
const className = twMerge('px-4 py-2', 'px-8')
// Результат: "py-2 px-8" (px-4 заменён на px-8)
```

### clsx + tailwind-merge (идеальная комбинация)

```bash
npm install clsx tailwind-merge
```

```jsx
// lib/utils.js
import { clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'

export function cn(...inputs) {
  return twMerge(clsx(inputs))
}
```

```jsx
// Использование
import { cn } from '@/lib/utils'

function Button({ className, variant = 'primary', children }) {
  return (
    <button
      className={cn(
        'px-4 py-2 rounded-lg font-medium',
        {
          'bg-blue-600 text-white hover:bg-blue-700': variant === 'primary',
          'bg-red-600 text-white hover:bg-red-700': variant === 'danger',
        },
        className // пользовательские классы корректно перезапишут базовые
      )}
    >
      {children}
    </button>
  )
}
```

> 💡 **Паттерн `cn()`** — это стандарт в современных React-проектах (используется в shadcn/ui).

## 🧩 class-variance-authority (cva)

Мощная библиотека для создания **вариативных компонентов**:

```bash
npm install class-variance-authority
```

```jsx
// components/button.tsx
import { cva } from 'class-variance-authority'
import { cn } from '@/lib/utils'

const buttonVariants = cva(
  // Базовые классы
  'inline-flex items-center justify-center rounded-lg font-medium transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2',
  {
    variants: {
      variant: {
        primary: 'bg-blue-600 text-white hover:bg-blue-700 focus:ring-blue-500',
        secondary: 'bg-gray-200 text-gray-900 hover:bg-gray-300 focus:ring-gray-500',
        danger: 'bg-red-600 text-white hover:bg-red-700 focus:ring-red-500',
        outline: 'border border-gray-300 bg-transparent hover:bg-gray-50',
        ghost: 'bg-transparent hover:bg-gray-100',
      },
      size: {
        sm: 'px-3 py-1.5 text-sm',
        md: 'px-4 py-2',
        lg: 'px-6 py-3 text-lg',
        icon: 'p-2',
      },
    },
    defaultVariants: {
      variant: 'primary',
      size: 'md',
    },
  }
)

function Button({ variant, size, className, children, ...props }) {
  return (
    <button
      className={cn(buttonVariants({ variant, size }), className)}
      {...props}
    >
      {children}
    </button>
  )
}

export { Button, buttonVariants }
```

```jsx
// Использование
<Button variant="primary" size="md">Сохранить</Button>
<Button variant="danger" size="lg">Удалить</Button>
<Button variant="outline" size="sm">Отмена</Button>
<Button variant="ghost" size="icon">
  <Icon />
</Button>
```

## 📘 TypeScript + Tailwind

### Типизация пропсов компонентов

```tsx
import { cva, type VariantProps } from 'class-variance-authority'
import { cn } from '@/lib/utils'

const buttonVariants = cva(
  'inline-flex items-center justify-center rounded-lg font-medium',
  {
    variants: {
      variant: {
        primary: 'bg-blue-600 text-white hover:bg-blue-700',
        secondary: 'bg-gray-200 text-gray-900 hover:bg-gray-300',
      },
      size: {
        sm: 'px-3 py-1.5 text-sm',
        md: 'px-4 py-2',
        lg: 'px-6 py-3 text-lg',
      },
    },
    defaultVariants: {
      variant: 'primary',
      size: 'md',
    },
  }
)

// Извлекаем типы вариантов
type ButtonVariants = VariantProps<typeof buttonVariants>

interface ButtonProps extends ButtonVariants, React.ButtonHTMLAttributes<HTMLButtonElement> {
  className?: string
}

function Button({ variant, size, className, children, ...props }: ButtonProps) {
  return (
    <button
      className={cn(buttonVariants({ variant, size }), className)}
      {...props}
    >
      {children}
    </button>
  )
}

export { Button }
```

### Типизация className

```tsx
import type { ClassNameValue } from 'clsx'

interface CardProps {
  className?: ClassNameValue
  title: string
  children: React.ReactNode
}

function Card({ className, title, children }: CardProps) {
  return (
    <div className={cn('bg-white rounded-lg shadow-md p-6', className)}>
      <h3 className="text-xl font-bold">{title}</h3>
      {children}
    </div>
  )
}
```

## 🎨 Практические паттерны компонентов

### 1. 🔘 Button (полноценный)

```tsx
import { cva, type VariantProps } from 'class-variance-authority'
import { cn } from '@/lib/utils'
import { Loader2 } from 'lucide-react'

const buttonVariants = cva(
  'inline-flex items-center justify-center rounded-lg font-medium transition-all focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:pointer-events-none disabled:opacity-50',
  {
    variants: {
      variant: {
        primary: 'bg-blue-600 text-white hover:bg-blue-700 focus:ring-blue-500',
        secondary: 'bg-gray-100 text-gray-900 hover:bg-gray-200 focus:ring-gray-500',
        danger: 'bg-red-600 text-white hover:bg-red-700 focus:ring-red-500',
        outline: 'border border-gray-300 bg-transparent hover:bg-gray-50',
        ghost: 'hover:bg-gray-100',
        link: 'text-blue-600 underline-offset-4 hover:underline',
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

interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  isLoading?: boolean
}

function Button({
  variant,
  size,
  className,
  isLoading,
  children,
  disabled,
  ...props
}: ButtonProps) {
  return (
    <button
      className={cn(buttonVariants({ variant, size }), className)}
      disabled={disabled || isLoading}
      {...props}
    >
      {isLoading && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
      {children}
    </button>
  )
}

export { Button, buttonVariants }
```

### 2. 🎴 Card

```tsx
import { cn } from '@/lib/utils'

interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  hover?: boolean
}

function Card({ className, hover, children, ...props }: CardProps) {
  return (
    <div
      className={cn(
        'bg-white rounded-xl shadow-sm border border-gray-200',
        hover && 'transition-shadow hover:shadow-md',
        className
      )}
      {...props}
    >
      {children}
    </div>
  )
}

function CardHeader({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) {
  return (
    <div
      className={cn('flex flex-col space-y-1.5 p-6 border-b', className)}
      {...props}
    />
  )
}

function CardTitle({ className, ...props }: React.HTMLAttributes<HTMLHeadingElement>) {
  return (
    <h3
      className={cn('text-xl font-semibold leading-none tracking-tight', className)}
      {...props}
    />
  )
}

function CardDescription({ className, ...props }: React.HTMLAttributes<HTMLParagraphElement>) {
  return (
    <p
      className={cn('text-sm text-gray-500', className)}
      {...props}
    />
  )
}

function CardContent({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) {
  return <div className={cn('p-6', className)} {...props} />
}

function CardFooter({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) {
  return (
    <div
      className={cn('flex items-center p-6 pt-0', className)}
      {...props}
    />
  )
}

export { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter }
```

```jsx
// Использование
<Card hover>
  <CardHeader>
    <CardTitle>Заголовок</CardTitle>
    <CardDescription>Описание карточки</CardDescription>
  </CardHeader>
  <CardContent>
    <p>Содержимое карточки</p>
  </CardContent>
  <CardFooter>
    <Button>Действие</Button>
  </CardFooter>
</Card>
```

### 3. 📝 Input с floating label

```tsx
import { cn } from '@/lib/utils'
import { forwardRef } from 'react'

interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string
  error?: string
  hint?: string
}

const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ className, label, error, hint, id, ...props }, ref) => {
    const inputId = id || `input-${Math.random().toString(36).slice(2)}`

    return (
      <div className="w-full">
        {label && (
          <label
            htmlFor={inputId}
            className="block text-sm font-medium text-gray-700 mb-1"
          >
            {label}
          </label>
        )}
        <input
          id={inputId}
          ref={ref}
          className={cn(
            'flex h-10 w-full rounded-lg border bg-white px-3 py-2 text-sm',
            'placeholder:text-gray-400',
            'focus:outline-none focus:ring-2 focus:ring-offset-1',
            'disabled:cursor-not-allowed disabled:opacity-50',
            error
              ? 'border-red-500 focus:border-red-500 focus:ring-red-500'
              : 'border-gray-300 focus:border-blue-500 focus:ring-blue-500',
            className
          )}
          {...props}
        />
        {error && (
          <p className="mt-1 text-sm text-red-500">{error}</p>
        )}
        {hint && !error && (
          <p className="mt-1 text-sm text-gray-500">{hint}</p>
        )}
      </div>
    )
  }
)

Input.displayName = 'Input'

export { Input }
```

```jsx
// Использование
<Input
  label="Email"
  type="email"
  placeholder="you@example.com"
  error="Неверный email"
  hint="Введите рабочий email"
/>
```

### 4. 🏷️ Badge

```tsx
import { cva, type VariantProps } from 'class-variance-authority'
import { cn } from '@/lib/utils'

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

interface BadgeProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof badgeVariants> {}

function Badge({ className, variant, ...props }: BadgeProps) {
  return (
    <div
      className={cn(badgeVariants({ variant }), className)}
      {...props}
    />
  )
}

export { Badge, badgeVariants }
```

### 5. 🎚️ Toggle / Switch

```tsx
import { cn } from '@/lib/utils'

interface ToggleProps {
  checked: boolean
  onChange: (checked: boolean) => void
  label?: string
  disabled?: boolean
}

function Toggle({ checked, onChange, label, disabled }: ToggleProps) {
  return (
    <label className={cn(
      'inline-flex items-center cursor-pointer',
      disabled && 'opacity-50 cursor-not-allowed'
    )}>
      <input
        type="checkbox"
        className="sr-only peer"
        checked={checked}
        onChange={(e) => onChange(e.target.checked)}
        disabled={disabled}
      />
      <div className={cn(
        'relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300',
        'rounded-full peer',
        'peer-checked:after:translate-x-full peer-checked:after:border-white',
        'after:content-[""] after:absolute after:top-[2px] after:left-[2px]',
        'after:bg-white after:border-gray-300 after:border after:rounded-full',
        'after:h-5 after:w-5 after:transition-all',
        'dark:bg-gray-700 dark:peer-focus:ring-blue-800',
        checked && 'bg-blue-600'
      )} />
      {label && (
        <span className="ml-3 text-sm font-medium text-gray-900 dark:text-gray-300">
          {label}
        </span>
      )}
    </label>
  )
}
```

### 6. 📋 Select

```tsx
import { cn } from '@/lib/utils'
import { forwardRef } from 'react'

interface SelectProps extends React.SelectHTMLAttributes<HTMLSelectElement> {
  label?: string
  error?: string
  options: Array<{ value: string; label: string }>
}

const Select = forwardRef<HTMLSelectElement, SelectProps>(
  ({ className, label, error, options, id, ...props }, ref) => {
    const selectId = id || `select-${Math.random().toString(36).slice(2)}`

    return (
      <div className="w-full">
        {label && (
          <label htmlFor={selectId} className="block text-sm font-medium text-gray-700 mb-1">
            {label}
          </label>
        )}
        <select
          id={selectId}
          ref={ref}
          className={cn(
            'flex h-10 w-full rounded-lg border bg-white px-3 py-2 text-sm',
            'focus:outline-none focus:ring-2 focus:ring-offset-1',
            'disabled:cursor-not-allowed disabled:opacity-50',
            error
              ? 'border-red-500 focus:border-red-500 focus:ring-red-500'
              : 'border-gray-300 focus:border-blue-500 focus:ring-blue-500',
            className
          )}
          {...props}
        >
          {options.map((option) => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
        </select>
        {error && <p className="mt-1 text-sm text-red-500">{error}</p>}
      </div>
    )
  }
)

Select.displayName = 'Select'

export { Select }
```

## 🌙 Dark Mode в React

### Через контекст (рекомендуется)

```tsx
// contexts/theme.tsx
import { createContext, useContext, useEffect, useState } from 'react'

type Theme = 'dark' | 'light' | 'system'

interface ThemeContextType {
  theme: Theme
  setTheme: (theme: Theme) => void
}

const ThemeContext = createContext<ThemeContextType | undefined>(undefined)

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useState<Theme>(() => {
    if (typeof window === 'undefined') return 'light'
    return (localStorage.getItem('theme') as Theme) || 'system'
  })

  useEffect(() => {
    const root = window.document.documentElement
    root.classList.remove('light', 'dark')

    if (theme === 'system') {
      const systemTheme = window.matchMedia('(prefers-color-scheme: dark)').matches
        ? 'dark'
        : 'light'
      root.classList.add(systemTheme)
    } else {
      root.classList.add(theme)
    }

    localStorage.setItem('theme', theme)
  }, [theme])

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  )
}

export function useTheme() {
  const context = useContext(ThemeContext)
  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider')
  }
  return context
}
```

```tsx
// App.tsx
import { ThemeProvider } from './contexts/theme'

function App() {
  return (
    <ThemeProvider>
      <YourApp />
    </ThemeProvider>
  )
}
```

```tsx
// components/ThemeToggle.tsx
import { useTheme } from '@/contexts/theme'
import { Moon, Sun, Monitor } from 'lucide-react'
import { cn } from '@/lib/utils'

export function ThemeToggle() {
  const { theme, setTheme } = useTheme()

  return (
    <div className="inline-flex items-center gap-1 bg-gray-100 dark:bg-gray-800 p-1 rounded-lg">
      <button
        onClick={() => setTheme('light')}
        className={cn(
          'p-2 rounded-md transition-colors',
          theme === 'light' && 'bg-white dark:bg-gray-700 shadow-sm'
        )}
        aria-label="Светлая тема"
      >
        <Sun className="h-4 w-4" />
      </button>
      <button
        onClick={() => setTheme('dark')}
        className={cn(
          'p-2 rounded-md transition-colors',
          theme === 'dark' && 'bg-white dark:bg-gray-700 shadow-sm'
        )}
        aria-label="Тёмная тема"
      >
        <Moon className="h-4 w-4" />
      </button>
      <button
        onClick={() => setTheme('system')}
        className={cn(
          'p-2 rounded-md transition-colors',
          theme === 'system' && 'bg-white dark:bg-gray-700 shadow-sm'
        )}
        aria-label="Системная тема"
      >
        <Monitor className="h-4 w-4" />
      </button>
    </div>
  )
}
```

### Инициализация до рендера (без мигания)

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="ru">
  <head>
    <script>
      // Применяем тему ДО рендеринга React
      ;(function() {
        const theme = localStorage.getItem('theme') || 'system'
        const root = document.documentElement
        
        if (theme === 'system') {
          const systemTheme = window.matchMedia('(prefers-color-scheme: dark)').matches
            ? 'dark'
            : 'light'
          root.classList.add(systemTheme)
        } else {
          root.classList.add(theme)
        }
      })()
    </script>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

## 📦 Интеграция с популярными библиотеками

### React Hook Form + Tailwind

```tsx
import { useForm } from 'react-hook-form'
import { cn } from '@/lib/utils'

interface FormData {
  email: string
  password: string
}

function LoginForm() {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<FormData>()

  const onSubmit = async (data: FormData) => {
    // Отправка данных
    await new Promise((resolve) => setTimeout(resolve, 1000))
    console.log(data)
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4 max-w-md mx-auto p-6">
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">
          Email
        </label>
        <input
          type="email"
          {...register('email', {
            required: 'Email обязателен',
            pattern: {
              value: /^\S+@\S+$/i,
              message: 'Неверный формат email',
            },
          })}
          className={cn(
            'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2',
            errors.email
              ? 'border-red-500 focus:ring-red-500'
              : 'border-gray-300 focus:ring-blue-500'
          )}
        />
        {errors.email && (
          <p className="mt-1 text-sm text-red-500">{errors.email.message}</p>
        )}
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">
          Пароль
        </label>
        <input
          type="password"
          {...register('password', {
            required: 'Пароль обязателен',
            minLength: {
              value: 8,
              message: 'Минимум 8 символов',
            },
          })}
          className={cn(
            'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2',
            errors.password
              ? 'border-red-500 focus:ring-red-500'
              : 'border-gray-300 focus:ring-blue-500'
          )}
        />
        {errors.password && (
          <p className="mt-1 text-sm text-red-500">{errors.password.message}</p>
        )}
      </div>

      <button
        type="submit"
        disabled={isSubmitting}
        className="w-full bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 disabled:opacity-50 transition-colors"
      >
        {isSubmitting ? 'Вход...' : 'Войти'}
      </button>
    </form>
  )
}
```

### React Router + Tailwind

```tsx
import { Link, NavLink } from 'react-router-dom'
import { cn } from '@/lib/utils'

function Navigation() {
  return (
    <nav className="bg-white border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex">
            <Link to="/" className="flex items-center font-bold text-xl text-gray-900">
              Logo
            </Link>
            <div className="hidden sm:ml-6 sm:flex sm:space-x-8">
              <NavLink
                to="/"
                className={({ isActive }) =>
                  cn(
                    'inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium',
                    isActive
                      ? 'border-blue-500 text-gray-900'
                      : 'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700'
                  )
                }
              >
                Главная
              </NavLink>
              <NavLink
                to="/about"
                className={({ isActive }) =>
                  cn(
                    'inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium',
                    isActive
                      ? 'border-blue-500 text-gray-900'
                      : 'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700'
                  )
                }
              >
                О нас
              </NavLink>
            </div>
          </div>
        </div>
      </div>
    </nav>
  )
}
```

## 🎯 Практические паттерны

### 1. 📱 Responsive Sidebar

```tsx
import { useState } from 'react'
import { cn } from '@/lib/utils'
import { Menu, X } from 'lucide-react'

function Dashboard() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false)

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Mobile header */}
      <div className="lg:hidden flex items-center justify-between p-4 bg-white border-b">
        <span className="font-bold text-xl">Logo</span>
        <button
          onClick={() => setIsSidebarOpen(!isSidebarOpen)}
          className="p-2 rounded-lg hover:bg-gray-100"
        >
          {isSidebarOpen ? <X /> : <Menu />}
        </button>
      </div>

      <div className="flex">
        {/* Sidebar */}
        <aside
          className={cn(
            'fixed inset-y-0 left-0 z-50 w-64 bg-white border-r transform transition-transform lg:translate-x-0 lg:static lg:inset-0',
            isSidebarOpen ? 'translate-x-0' : '-translate-x-full'
          )}
        >
          <div className="p-4">
            <h2 className="font-bold text-xl mb-4 hidden lg:block">Logo</h2>
            <nav className="space-y-1">
              {['Главная', 'Профиль', 'Настройки', 'Выход'].map((item) => (
                <a
                  key={item}
                  href="#"
                  className="block px-4 py-2 rounded-lg text-gray-700 hover:bg-gray-100"
                >
                  {item}
                </a>
              ))}
            </nav>
          </div>
        </aside>

        {/* Overlay */}
        {isSidebarOpen && (
          <div
            className="fixed inset-0 bg-black/50 z-40 lg:hidden"
            onClick={() => setIsSidebarOpen(false)}
          />
        )}

        {/* Main content */}
        <main className="flex-1 p-4 lg:p-8">
          <h1 className="text-2xl font-bold mb-6">Дашборд</h1>
          {/* Контент */}
        </main>
      </div>
    </div>
  )
}
```

### 2. 🎴 Карточка товара с hover-эффектами

```tsx
import { cn } from '@/lib/utils'
import { ShoppingCart, Heart } from 'lucide-react'
import { useState } from 'react'

interface ProductCardProps {
  title: string
  price: number
  oldPrice?: number
  image: string
  badge?: string
}

function ProductCard({ title, price, oldPrice, image, badge }: ProductCardProps) {
  const [isFavorite, setIsFavorite] = useState(false)

  return (
    <div className="group bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-lg transition-shadow">
      {/* Изображение */}
      <div className="relative aspect-square overflow-hidden">
        <img
          src={image}
          alt={title}
          className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
        />
        
        {/* Бейдж */}
        {badge && (
          <span className="absolute top-3 left-3 bg-red-500 text-white text-xs font-bold px-2 py-1 rounded">
            {badge}
          </span>
        )}

        {/* Кнопка избранного */}
        <button
          onClick={() => setIsFavorite(!isFavorite)}
          className={cn(
            'absolute top-3 right-3 p-2 rounded-full transition-all',
            isFavorite
              ? 'bg-red-500 text-white'
              : 'bg-white/80 text-gray-700 hover:bg-white'
          )}
        >
          <Heart className={cn('w-5 h-5', isFavorite && 'fill-current')} />
        </button>

        {/* Overlay с кнопкой */}
        <div className="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-colors flex items-center justify-center opacity-0 group-hover:opacity-100">
          <button className="bg-white text-gray-900 px-4 py-2 rounded-lg font-medium hover:bg-gray-100 transition">
            Быстрый просмотр
          </button>
        </div>
      </div>

      {/* Контент */}
      <div className="p-4">
        <h3 className="font-medium text-gray-900 line-clamp-2">{title}</h3>
        <div className="mt-2 flex items-baseline gap-2">
          <span className="text-xl font-bold text-gray-900">
            {price.toLocaleString('ru-RU')} ₽
          </span>
          {oldPrice && (
            <span className="text-sm text-gray-400 line-through">
              {oldPrice.toLocaleString('ru-RU')} ₽
            </span>
          )}
        </div>
        <button className="mt-3 w-full bg-blue-600 hover:bg-blue-700 text-white py-2 rounded-lg font-medium transition-colors flex items-center justify-center gap-2">
          <ShoppingCart className="w-4 h-4" />
          В корзину
        </button>
      </div>
    </div>
  )
}
```

### 3. 📊 Таблица с сортировкой

```tsx
import { useState } from 'react'
import { cn } from '@/lib/utils'
import { ArrowUpDown } from 'lucide-react'

interface User {
  id: number
  name: string
  email: string
  role: string
  status: 'active' | 'pending' | 'inactive'
}

function UsersTable({ users }: { users: User[] }) {
  const [sortField, setSortField] = useState<keyof User>('name')
  const [sortDirection, setSortDirection] = useState<'asc' | 'desc'>('asc')

  const handleSort = (field: keyof User) => {
    if (sortField === field) {
      setSortDirection(sortDirection === 'asc' ? 'desc' : 'asc')
    } else {
      setSortField(field)
      setSortDirection('asc')
    }
  }

  const sortedUsers = [...users].sort((a, b) => {
    const aValue = a[sortField]
    const bValue = b[sortField]
    if (aValue < bValue) return sortDirection === 'asc' ? -1 : 1
    if (aValue > bValue) return sortDirection === 'asc' ? 1 : -1
    return 0
  })

  return (
    <div className="bg-white rounded-xl shadow-sm border overflow-hidden">
      <div className="overflow-x-auto">
        <table className="w-full">
          <thead className="bg-gray-50 border-b">
            <tr>
              {(['name', 'email', 'role', 'status'] as const).map((field) => (
                <th
                  key={field}
                  onClick={() => handleSort(field)}
                  className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100"
                >
                  <div className="flex items-center gap-1">
                    {field}
                    <ArrowUpDown className={cn(
                      'w-3 h-3',
                      sortField === field ? 'text-blue-600' : 'text-gray-400'
                    )} />
                  </div>
                </th>
              ))}
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-200">
            {sortedUsers.map((user) => (
              <tr key={user.id} className="hover:bg-gray-50 transition-colors">
                <td className="px-6 py-4 font-medium text-gray-900">{user.name}</td>
                <td className="px-6 py-4 text-gray-600">{user.email}</td>
                <td className="px-6 py-4 text-gray-600">{user.role}</td>
                <td className="px-6 py-4">
                  <span
                    className={cn(
                      'px-2 py-1 rounded-full text-xs font-medium',
                      {
                        'bg-green-100 text-green-800': user.status === 'active',
                        'bg-yellow-100 text-yellow-800': user.status === 'pending',
                        'bg-gray-100 text-gray-800': user.status === 'inactive',
                      }
                    )}
                  >
                    {user.status}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}
```

## 📊 Шпаргалка: что когда использовать

| Задача | Решение |
| :-- | :-- |
| Условные классы | `clsx` или `classnames` |
| Разрешение конфликтов классов | `tailwind-merge` |
| Идеальная комбинация | `cn()` = `twMerge(clsx(...))` |
| Вариативные компоненты | `cva` (class-variance-authority) |
| TypeScript + варианты | `VariantProps<typeof cva>` |
| Динамические классы | `cn()` с объектом или массивом |
| Dark mode | Контекст + `localStorage` + `useEffect` |
| Без мигания темы | Скрипт в `<head>` до рендера |
| Переиспользование паттернов | Компоненты Button, Card, Input |
| Формы | React Hook Form + `cn()` для ошибок |
| Навигация | React Router `NavLink` + `cn()` |

## 🚫 Частые ошибки

### ❌ Ошибка 1: `class` вместо `className`

```jsx
// ❌ Плохо: class не работает в React
<div class="bg-blue-500">...</div>

// ✅ Хорошо: используем className
<div className="bg-blue-500">...</div>
```

### ❌ Ошибка 2: Динамическая конкатенация классов

```jsx
// ❌ Плохо: Tailwind не увидит эти классы
const variant = 'primary'
<button className={`btn-${variant}`}>Кнопка</button>

// ✅ Хорошо: полные имена классов
const variants = {
  primary: 'bg-blue-600 text-white',
  secondary: 'bg-gray-200 text-gray-900',
}
<button className={variants[variant]}>Кнопка</button>
```

### ❌ Ошибка 3: Конфликт классов без `tailwind-merge`

```jsx
// ❌ Плохо: p-4 и p-8 оба остаются, последний выигрывает непредсказуемо
<div className={`p-4 bg-blue-500 ${customClass}`}>
  {/* customClass = "p-8" — результат непредсказуем */}
</div>

// ✅ Хорошо: twMerge корректно разрешает конфликты
<div className={twMerge('p-4 bg-blue-500', customClass)}>
  {/* customClass = "p-8" — результат: "bg-blue-500 p-8" */}
</div>
```

### ❌ Ошибка 4: Мигание темы при загрузке

```jsx
// ❌ Плохо: тема применяется после рендера React
function App() {
  useEffect(() => {
    document.documentElement.classList.add('dark')
  }, [])
}

// ✅ Хорошо: тема применяется до рендера
// В index.html:
<script>
  ;(function() {
    const theme = localStorage.getItem('theme')
    if (theme === 'dark') document.documentElement.classList.add('dark')
  })()
</script>
```

### ❌ Ошибка 5: Забывают про `forwardRef` в компонентах

```tsx
// ❌ Плохо: ref не работает
function Input({ className, ...props }) {
  return <input className={className} {...props} />
}

// ✅ Хорошо: используем forwardRef
const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ className, ...props }, ref) => {
    return <input ref={ref} className={className} {...props} />
  }
)
Input.displayName = 'Input'
```

### ❌ Ошибка 6: Избыточные `div`-обёртки

```jsx
// ❌ Плохо: лишний div
<div>
  <div className="bg-white p-4 rounded-lg">
    <p>Контент</p>
  </div>
</div>

// ✅ Хорошо: применяем классы к существующему элементу
<div className="bg-white p-4 rounded-lg">
  <p>Контент</p>
</div>
```

### ❌ Ошибка 7: Забывают про `displayName` для `forwardRef`

```tsx
// ❌ Плохо: в DevTools будет "ForwardRef"
const Input = forwardRef<HTMLInputElement, InputProps>((props, ref) => {
  return <input ref={ref} {...props} />
})

// ✅ Хорошо: добавляем displayName
const Input = forwardRef<HTMLInputElement, InputProps>((props, ref) => {
  return <input ref={ref} {...props} />
})
Input.displayName = 'Input'
```

### ❌ Ошибка 8: Не типизируют варианты cva

```tsx
// ❌ Плохо: нет типов для variant и size
function Button({ variant, size, children }) {
  // ...
}

// ✅ Хорошо: типизируем через VariantProps
const buttonVariants = cva('...', { variants: { ... } })
type ButtonProps = VariantProps<typeof buttonVariants>
function Button({ variant, size, children }: ButtonProps) {
  // ...
}
```

### ❌ Ошибка 9: Забывают про `content` в `tailwind.config.js`

```js
// ❌ Плохо: Tailwind не найдёт классы в компонентах
module.exports = {
  // content отсутствует
}

// ✅ Хорошо: указываем все пути
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
}
```

### ❌ Ошибка 10: Дублирование классов вместо компонентов

```jsx
// ❌ Плохо: дублирование
<button className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
  Сохранить
</button>
<button className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
  Отмена
</button>

// ✅ Хорошо: переиспользуем компонент
<Button variant="primary">Сохранить</Button>
<Button variant="primary">Отмена</Button>
```

## 🎯 Что дальше?

Теперь вы полностью владеете интеграцией React + Tailwind CSS! Но это только одна из популярных связок.

**Следующий шаг:** [🔌 Vue + Tailwind CSS](vue.md) — изучим интеграцию с Vue.js, Composition API и SFC.

---