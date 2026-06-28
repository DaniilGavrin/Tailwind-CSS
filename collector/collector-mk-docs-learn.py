#!/usr/bin/env python3
"""
Сжиматель Tailwind CSS Guide v2 — АГРЕССИВНЫЙ РЕЖИМ
Цель: 355 → 60-70 страниц
"""

import re
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import List
from dataclasses import dataclass


# ═══════════════════════════════════════════════════════════
# КОНФИГУРАЦИЯ
# ═══════════════════════════════════════════════════════════

@dataclass
class CompressionConfig:
    # УДАЛИТЬ ЦЕЛИКОМ (H1 разделы)
    remove_sections: List[str] = field(default_factory=lambda: [
        r'Интеграции',
        r'Integrations',
        r'React \+ Tailwind',
        r'Vue \+ Tailwind',
        r'Next\.js \+ Tailwind',
        r'Vue \+ Tailwind CSS',
        r'React \+ Tailwind CSS',
        r'Next\.js \+ Tailwind CSS',
    ])
    
    # Подсекции-паразиты (удаляем H2/H3)
    remove_subsections: List[str] = field(default_factory=lambda: [
        r'Что вы узнаете',
        r'Что дальше',
        r'Следующий шаг',
        r'Для кого этот гайд',
        r'Как использовать этот гайд',
        r'Вклад в проект',
        r'Лицензия',
        r'Структура документации',
        r'История создания',
        r'Сравнение с традиционным CSS',
        r'Tailwind vs',
        r'Когда использовать Tailwind',
        r'Checklist',
        r'Checklist перед деплоем',
        r'Практические паттерны',      # ← 50% объёма!
        r'Что изучить дальше',
        r'Performance метрики',
        r'Анализ размера бандла',
        r'Проверка через',
        r'Интеграция с популярными',
        r'Основные концепции',
        r'Лучшие практики',
        r'Почему это работает',
        r'Доступность',
        r'WCAG',
    ])
    
    # Оставляем ТОЛЬКО это
    keep_subsections: List[str] = field(default_factory=lambda: [
        r'Шпаргалка',
        r'Частые ошибки',
        r'Структура',
        r'Секция',
        r'Типовые конфигурации',
    ])
    
    # АГРЕССИВНЫЕ лимиты
    max_code_lines: int = 6
    max_paragraph_chars: int = 150
    keep_exercises: bool = False


# ═══════════════════════════════════════════════════════════
# БЛОК
# ═══════════════════════════════════════════════════════════

@dataclass
class Block:
    type: str          # 'h1', 'h2', 'h3', 'h4', 'p', 'code', 'table', 'list', 'hr', 'comment', 'quote'
    content: str
    level: int = 0
    lang: str = ''


# ═══════════════════════════════════════════════════════════
# ПАРСЕР MARKDOWN
# ═══════════════════════════════════════════════════════════

def parse_markdown(text: str) -> List[Block]:
    """Разбивает Markdown на структурированные блоки"""
    blocks: List[Block] = []
    lines = text.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # HTML-комментарии
        if line.strip().startswith('<!--'):
            comment_lines = [line]
            while i < len(lines) and '-->' not in lines[i]:
                i += 1
                if i < len(lines):
                    comment_lines.append(lines[i])
            if i < len(lines) and '-->' in lines[i]:
                i += 1
            blocks.append(Block('comment', '\n'.join(comment_lines)))
            continue
        
        # Заголовки
        m = re.match(r'^(#{1,6})\s+(.+)$', line)
        if m:
            level = len(m.group(1))
            blocks.append(Block(f'h{level}', m.group(2), level=level))
            i += 1
            continue
        
        # Блоки кода
        if line.strip().startswith('```'):
            lang = line.strip()[3:].strip()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            blocks.append(Block('code', '\n'.join(code_lines), lang=lang))
            if i < len(lines):
                i += 1  # пропустить закрывающие ```
            continue
        
        # Горизонтальная линия
        if re.match(r'^---+\s*$', line.strip()):
            blocks.append(Block('hr', line))
            i += 1
            continue
        
        # Таблицы
        if '|' in line and i + 1 < len(lines) and re.match(r'^\s*\|?\s*[-:]+', lines[i + 1]):
            table_lines = [line]
            i += 1
            while i < len(lines) and '|' in lines[i]:
                table_lines.append(lines[i])
                i += 1
            blocks.append(Block('table', '\n'.join(table_lines)))
            continue
        
        # Списки
        if re.match(r'^\s*[-*+]\s+', line) or re.match(r'^\s*\d+\.\s+', line):
            list_lines = [line]
            i += 1
            while i < len(lines) and (
                re.match(r'^\s+[-*+\d]', lines[i]) or 
                (lines[i].strip() and lines[i].startswith('  '))
            ):
                list_lines.append(lines[i])
                i += 1
            blocks.append(Block('list', '\n'.join(list_lines)))
            continue
        
        # Цитаты
        if line.startswith('>'):
            quote_lines = [line]
            i += 1
            while i < len(lines) and lines[i].startswith('>'):
                quote_lines.append(lines[i])
                i += 1
            blocks.append(Block('quote', '\n'.join(quote_lines)))
            continue
        
        # Пустая строка
        if not line.strip():
            i += 1
            continue
        
        # Обычный абзац
        para_lines = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].startswith(('#', '```', '>', '-', '*', '|')) and not re.match(r'^\s*\d+\.', lines[i]) and not re.match(r'^---+\s*$', lines[i]):
            para_lines.append(lines[i])
            i += 1
        blocks.append(Block('p', '\n'.join(para_lines)))
    
    return blocks


# ═══════════════════════════════════════════════════════════
# ФИЛЬТРЫ
# ═══════════════════════════════════════════════════════════

def matches_any(text: str, patterns: List[str]) -> bool:
    for p in patterns:
        if re.search(p, text, re.IGNORECASE):
            return True
    return False


def compress_code_block(block: Block, max_lines: int) -> Block:
    lines = block.content.split('\n')
    if len(lines) <= max_lines:
        return block
    # Оставляем начало и конец
    head = lines[:max_lines // 2]
    tail = lines[-(max_lines // 2):]
    compressed = head + [f'# ... (ещё {len(lines) - max_lines} строк) ...'] + tail
    return Block('code', '\n'.join(compressed), level=0, lang=block.lang)


def is_html_example(block: Block) -> bool:
    """Проверяет, является ли блок кода большим HTML-примером"""
    if block.type != 'code':
        return False
    if block.lang.lower() not in ('html', 'vue', 'jsx', 'tsx'):
        return False
    lines = block.content.split('\n')
    # Если больше 10 строк HTML — это паттерн, режем
    return len(lines) > 10


# ═══════════════════════════════════════════════════════════
# ГЛАВНЫЙ КОМПРЕССОР
# ═══════════════════════════════════════════════════════════

def compress_document(blocks: List[Block], cfg: CompressionConfig) -> List[Block]:
    result: List[Block] = []
    skip_until_h1 = False
    skip_until_h2 = False
    
    i = 0
    while i < len(blocks):
        block = blocks[i]
        
        # ─── H1: удаление целых разделов ───
        if block.type == 'h1':
            if matches_any(block.content, cfg.remove_sections):
                skip_until_h1 = True
                i += 1
                continue
            else:
                skip_until_h1 = False
                result.append(block)
                i += 1
                continue
        
        if skip_until_h1:
            i += 1
            continue
        
        # ─── H2/H3: проверка подсекций ───
        if block.type in ('h2', 'h3'):
            if matches_any(block.content, cfg.keep_subsections):
                skip_until_h2 = False
                result.append(block)
                i += 1
                continue
            
            if matches_any(block.content, cfg.remove_subsections):
                skip_until_h2 = True
                i += 1
                continue
            
            skip_until_h2 = False
            result.append(block)
            i += 1
            continue
        
        if skip_until_h2:
            if block.type in ('h1', 'h2', 'h3'):
                skip_until_h2 = False
                continue
            i += 1
            continue
        
        # ─── Пропуск мусора ───
        if block.type in ('comment', 'hr'):
            i += 1
            continue
        
        # ─── Блоки кода ───
        if block.type == 'code':
            # Удаляем большие HTML-примеры целиком
            if is_html_example(block):
                i += 1
                continue
            compressed = compress_code_block(block, cfg.max_code_lines)
            if compressed.content.strip():
                result.append(compressed)
            i += 1
            continue
        
        # ─── Абзацы ───
        if block.type == 'p':
            # Вырезаем упражнения/вопросы/примечания
            if any(x in block.content for x in ['💬 **Упражнение', '💬 **Вопрос', 
                                                  '> 💡', '> ⚠️', '> 📚']):
                i += 1
                continue
            # Длинные абзацы = вода
            if len(block.content) > cfg.max_paragraph_chars:
                i += 1
                continue
            result.append(block)
            i += 1
            continue
        
        # ─── Списки — только короткие ───
        if block.type == 'list':
            if len(block.content) < 300:
                result.append(block)
            i += 1
            continue
        
        # ─── Цитаты — только короткие ───
        if block.type == 'quote':
            if len(block.content) < 200:
                result.append(block)
            i += 1
            continue
        
        # ─── Таблицы — оставляем все ───
        result.append(block)
        i += 1
    
    return result


# ═══════════════════════════════════════════════════════════
# СБОРКА MARKDOWN
# ═══════════════════════════════════════════════════════════

def blocks_to_markdown(blocks: List[Block]) -> str:
    lines = []
    for block in blocks:
        if block.type.startswith('h'):
            level = int(block.type[1])
            lines.append('')
            lines.append(f'{"#" * level} {block.content}')
            lines.append('')
        elif block.type == 'code':
            lines.append(f'```{block.lang}')
            lines.append(block.content)
            lines.append('```')
            lines.append('')
        elif block.type in ('table', 'list', 'quote', 'p'):
            lines.append(block.content)
            lines.append('')
    
    text = '\n'.join(lines)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip() + '\n'


# ═══════════════════════════════════════════════════════════
# СТАТИСТИКА
# ═══════════════════════════════════════════════════════════

def print_stats(original: str, compressed: str):
    orig_chars = len(original)
    comp_chars = len(compressed)
    orig_lines = original.count('\n')
    comp_lines = compressed.count('\n')
    orig_pages = orig_chars / 2500
    comp_pages = comp_chars / 2500
    
    print('\n' + '═' * 60)
    print('📊 СТАТИСТИКА СЖАТИЯ (v2 — АГРЕССИВ)')
    print('═' * 60)
    print(f'  Оригинал:  {orig_chars:>10,} символов  |  {orig_lines:>6,} строк  |  ~{orig_pages:.0f} стр.')
    print(f'  Сжатый:    {comp_chars:>10,} символов  |  {comp_lines:>6,} строк  |  ~{comp_pages:.0f} стр.')
    print(f'  Сжатие:    {(1 - comp_chars/orig_chars)*100:>9.1f}%')
    print(f'  Коэф.:     {orig_chars/comp_chars:>9.1f}x')
    print('═' * 60 + '\n')


# ═══════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════

def main():
    if len(sys.argv) < 3:
        print('Использование: python script.py input.md output.md')
        sys.exit(1)
    
    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    
    if not input_path.exists():
        print(f'❌ Файл не найден: {input_path}')
        sys.exit(1)
    
    print(f'📖 Читаю: {input_path}')
    original = input_path.read_text(encoding='utf-8')
    
    print('🔍 Парсю Markdown...')
    blocks = parse_markdown(original)
    print(f'   Найдено блоков: {len(blocks)}')
    
    print('⚙️  Сжимаю (агрессивный режим)...')
    cfg = CompressionConfig()
    compressed_blocks = compress_document(blocks, cfg)
    print(f'   Осталось блоков: {len(compressed_blocks)}')
    
    print('📝 Собираю Markdown...')
    compressed = blocks_to_markdown(compressed_blocks)
    
    print(f'💾 Сохраняю: {output_path}')
    output_path.write_text(compressed, encoding='utf-8')
    
    print_stats(original, compressed)
    print('✅ Готово!')


if __name__ == '__main__':
    main()