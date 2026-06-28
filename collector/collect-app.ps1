# Tailwind CSS Guide Export Script
# Собирает все markdown-файлы из /docs в один файл

# Настройки
$PROJECT_ROOT = Split-Path -Parent $PSScriptRoot
$DOCS_DIR = Join-Path $PROJECT_ROOT "docs"
$OUTPUT_DIR = Join-Path $PROJECT_ROOT "output"
$OUTPUT_FILE = Join-Path $OUTPUT_DIR "tailwind-css-guide-full.md"

# Создаём output директорию если её нет
if (-not (Test-Path $OUTPUT_DIR)) {
    New-Item -ItemType Directory -Path $OUTPUT_DIR | Out-Null
    Write-Host "✓ Создана директория: $OUTPUT_DIR" -ForegroundColor Green
}

# Исключения (директории и файлы)
$EXCLUDE = @(
    "node_modules",
    ".git",
    "site",
    "__pycache__",
    ".venv",
    ".tox",
    ".DS_Store",
    "Thumbs.db"
)

# Удаляем старый файл
if (Test-Path $OUTPUT_FILE) {
    Remove-Item $OUTPUT_FILE
}

# ============================================
# ЗАГОЛОВОК
# ============================================
$utf8NoBom = New-Object System.Text.UTF8Encoding $false

$header = @"
# 📘 Tailwind CSS Guide — Полная версия

> Автоматически сгенерированная версия всей документации
> Дата генерации: $(Get-Date -Format 'dd.MM.yyyy HH:mm:ss')
> Источник: https://github.com/DaniilGavrin/tailwind-css-guide

---

"@

[System.IO.File]::WriteAllText($OUTPUT_FILE, $header, $utf8NoBom)

$processedCount = 0
$skippedCount = 0
$totalSize = 0

# ============================================
# ФУНКЦИИ
# ============================================

# Проверка исключений
function Test-Excluded {
    param($path)
    
    foreach ($ex in $EXCLUDE) {
        if ($path -like "*$ex*") {
            return $true
        }
    }
    return $false
}

# Получение "человеческого" заголовка из имени файла
function Get-SectionTitle {
    param($fileName)
    
    $name = [System.IO.Path]::GetFileNameWithoutExtension($fileName)
    
    # Маппинг имён файлов на русские заголовки
    $titles = @{
        "index" = "Главная"
        "introduction" = "Введение"
        "installation" = "Установка"
        "configuration" = "Конфигурация"
        "utility-classes" = "Утилитарные классы"
        "flexbox" = "Flexbox"
        "grid" = "Grid"
        "spacing" = "Отступы"
        "sizing" = "Размеры"
        "colors" = "Цвета"
        "typography" = "Типографика"
        "backgrounds" = "Фоны"
        "borders" = "Границы"
        "effects" = "Эффекты и тени"
        "breakpoints" = "Breakpoints"
        "dark-mode" = "Dark Mode"
        "states" = "Состояния"
        "customization" = "Кастомизация"
        "plugins" = "Плагины"
        "directives" = "Директивы"
        "optimization" = "Оптимизация"
        "react" = "React"
        "vue" = "Vue"
        "nextjs" = "Next.js"
    }
    
    if ($titles.ContainsKey($name)) {
        return $titles[$name]
    }
    
    # Если не нашли — капитализируем имя
    return (Get-Culture).TextInfo.ToTitleCase($name -replace '-', ' ')
}

# Получение emoji для раздела
function Get-SectionEmoji {
    param($folderName)
    
    $emojis = @{
        "basics" = "🟢"
        "layout" = "📐"
        "styling" = "🎨"
        "responsive" = "📱"
        "advanced" = "🔴"
        "integrations" = "🔌"
    }
    
    if ($emojis.ContainsKey($folderName)) {
        return $emojis[$folderName]
    }
    return "📄"
}

# ============================================
# СБОР ВСЕХ MD ФАЙЛОВ
# ============================================

Write-Host ""
Write-Host "🔍 Сканирование $DOCS_DIR..." -ForegroundColor Cyan

# Получаем все .md файлы, сортируем по структуре
$allFiles = Get-ChildItem -Path $DOCS_DIR -Recurse -File -Filter "*.md" -ErrorAction SilentlyContinue |
            Where-Object { -not (Test-Excluded $_.FullName) } |
            Sort-Object {
                # Порядок сортировки: index.md первым, потом по папкам
                $rel = $_.FullName -replace [regex]::Escape("$DOCS_DIR\"), ""
                if ($rel -eq "index.md") { return "000_$rel" }
                
                # Порядок папок
                $folderOrder = @{
                    "basics" = "1"
                    "layout" = "2"
                    "styling" = "3"
                    "responsive" = "4"
                    "advanced" = "5"
                    "integrations" = "6"
                }
                
                $parts = $rel -split '\\'
                $folder = $parts[0]
                $order = if ($folderOrder.ContainsKey($folder)) { $folderOrder[$folder] } else { "9" }
                
                return "${order}_$rel"
            }

Write-Host "✓ Найдено файлов: $($allFiles.Count)" -ForegroundColor Green
Write-Host ""

# ============================================
# ОБРАБОТКА ФАЙЛОВ
# ============================================

$currentSection = ""

foreach ($file in $allFiles) {
    $relativePath = $file.FullName -replace [regex]::Escape("$DOCS_DIR\"), ""
    $parts = $relativePath -split '\\'
    
    # Определяем текущую секцию
    if ($parts.Count -gt 1) {
        $section = $parts[0]
    } else {
        $section = "root"
    }
    
    # Если сменилась секция — добавляем разделитель
    if ($section -ne $currentSection -and $section -ne "root") {
        $emoji = Get-SectionEmoji $section
        $sectionTitle = (Get-Culture).TextInfo.ToTitleCase($section)
        
        $sectionHeader = @"


---

# $emoji Раздел: $sectionTitle

---


"@
        [System.IO.File]::AppendAllText($OUTPUT_FILE, $sectionHeader, $utf8NoBom)
        $currentSection = $section
    }
    
    # Заголовок файла
    $title = Get-SectionTitle $file.Name
    $fileHeader = @"


<!-- ═══════════════════════════════════════════════════════════ -->
<!-- ФАЙЛ: $relativePath -->
<!-- ═══════════════════════════════════════════════════════════ -->


"@
    [System.IO.File]::AppendAllText($OUTPUT_FILE, $fileHeader, $utf8NoBom)
    
    # Содержимое файла
    try {
        $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
        [System.IO.File]::AppendAllText($OUTPUT_FILE, $content, $utf8NoBom)
        
        # Добавляем разрыв страницы между файлами
        "`n`n---`n`n" | Out-File $OUTPUT_FILE -Append -Encoding utf8
        
        $processedCount++
        $totalSize += $content.Length
        
        Write-Host "  ✓ $relativePath" -ForegroundColor Gray
    } catch {
        Write-Host "  ✗ $relativePath — ОШИБКА" -ForegroundColor Red
        $skippedCount++
    }
}

# ============================================
# ДЕРЕВО СТРУКТУРЫ
# ============================================

function Write-DirectoryTree {
    param(
        [string]$Path,
        [string]$Prefix = "",
        [int]$Depth = 0,
        [int]$MaxDepth = 5,
        [System.Text.StringBuilder]$Builder
    )
    
    if ($Depth -ge $MaxDepth) { return }
    
    try {
        $items = Get-ChildItem -Path $Path -ErrorAction SilentlyContinue |
                 Where-Object { -not (Test-Excluded $_.FullName) } |
                 Sort-Object @{Expression={$_.PSIsContainer};Descending=$true}, Name
        
        $count = $items.Count
        $i = 0
        
        foreach ($item in $items) {
            $i++
            $isLast = ($i -eq $count)
            $connector = if ($isLast) { "└── " } else { "├── " }
            
            if ($item.PSIsContainer) {
                $fileCount = (Get-ChildItem -Path $item.FullName -File -Recurse -ErrorAction SilentlyContinue |
                             Where-Object { -not (Test-Excluded $_.FullName) }).Count
                
                $dirCount = (Get-ChildItem -Path $item.FullName -Directory -ErrorAction SilentlyContinue |
                            Where-Object { -not (Test-Excluded $_.FullName) }).Count
                
                $status = " [$fileCount файлов"
                if ($dirCount -gt 0) { $status += ", $dirCount подпапок" }
                $status += "]"
                
                [void]$Builder.AppendLine("$Prefix$connector$($item.Name)/$status")
                
                $newPrefix = if ($isLast) { "$Prefix    " } else { "$Prefix│   " }
                Write-DirectoryTree -Path $item.FullName -Prefix $newPrefix -Depth ($Depth + 1) -MaxDepth $MaxDepth -Builder $Builder
            } else {
                $size = "{0:N0}" -f $item.Length
                [void]$Builder.AppendLine("$Prefix$connector$($item.Name) ($size байт)")
            }
        }
    } catch {
        # Игнорируем ошибки
    }
}

$treeBuilder = New-Object System.Text.StringBuilder
[void]$treeBuilder.AppendLine("")
[void]$treeBuilder.AppendLine("---")
[void]$treeBuilder.AppendLine("")
[void]$treeBuilder.AppendLine("# 📁 Структура проекта")
[void]$treeBuilder.AppendLine("")
[void]$treeBuilder.AppendLine("``````")
[void]$treeBuilder.AppendLine("tailwind-css-guide/")

Write-DirectoryTree -Path $PROJECT_ROOT -Prefix "" -Depth 0 -MaxDepth 4 -Builder $treeBuilder

[void]$treeBuilder.AppendLine("``````")
[void]$treeBuilder.AppendLine("")

[System.IO.File]::AppendAllText($OUTPUT_FILE, $treeBuilder.ToString(), $utf8NoBom)

# ============================================
# ИТОГОВАЯ СТАТИСТИКА
# ============================================

$footer = @"


---

## 📊 Статистика экспорта

| Параметр | Значение |
| :-- | :-- |
| **Обработано файлов** | $processedCount |
| **Пропущено файлов** | $skippedCount |
| **Общий объём контента** | $('{0:N0}' -f $totalSize) символов |
| **Размер итогового файла** | $('{0:N0}' -f (Get-Item $OUTPUT_FILE).Length) байт |
| **Дата генерации** | $(Get-Date -Format 'dd.MM.yyyy HH:mm:ss') |

---

_Сгенерировано автоматически скриптом ``collector/export-docs.ps1``_
"@

[System.IO.File]::AppendAllText($OUTPUT_FILE, $footer, $utf8NoBom)

# ============================================
# ВЫВОД РЕЗУЛЬТАТА
# ============================================

$fileSize = (Get-Item $OUTPUT_FILE).Length
$fileSizeKB = [math]::Round($fileSize / 1024, 2)

Write-Host ""
Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "✓ Готово!" -ForegroundColor Green
Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "📄 Файл: $OUTPUT_FILE" -ForegroundColor White
Write-Host "📦 Размер: $fileSizeKB KB ($fileSize байт)" -ForegroundColor White
Write-Host "✓ Обработано: $processedCount файлов" -ForegroundColor Green
if ($skippedCount -gt 0) {
    Write-Host "⚠ Пропущено: $skippedCount файлов" -ForegroundColor Yellow
}
Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""