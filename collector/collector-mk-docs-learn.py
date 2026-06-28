#!/usr/bin/env python3
"""
Сжиматель Tailwind CSS Guide v5 — ХИРУРГИЧЕСКИЙ
Удаляет ТОЛЬКО указанные блоки, всё остальное оставляет нетронутым.
"""

import re
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import List


@dataclass
class Block:
    type: str  # 'h1','h2','h3','h4','p','code','table','list','hr','comment','quote'
    content: str
    level: int = 0
    lang: str = ''


# ═══════════════════════════════════════════════════════════
# ПАРСЕР
# ═══════════════════════════════════════════════════════════

def parse_markdown(text: str) -> List[Block]:
    blocks: List[Block] = []
    lines = text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # HTML-комментарии
        if line.strip().startswith('<!--'):
            buf = [line]
            while i < len(lines) and '-->' not in lines[i]:
                i += 1
                if i < len(lines):
                    buf.append(lines[i])
            if i < len(lines) and '-->' in lines[i]:
                i += 1
            blocks.append(Block('comment', '\n'.join(buf)))
            continue
        
        # Заголовки
        m = re.match(r'^(#{1,6})\s+(.+)$', line)
        if m:
            level = len(m.group(1))
            blocks.append(Block(f'h{level}', m.group(2), level=level))
            i += 1
            continue
        
        # Код
        if line.strip().startswith('```'):
            lang = line.strip()[3:].strip()
            buf = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                buf.append(lines[i])
                i += 1
            blocks.append(Block('code', '\n'.join(buf), lang=lang))
            if i < len(lines):
                i += 1
            continue
        
        # HR
        if re.match(r'^---+\s*$', line.strip()):
            blocks.append(Block('hr', line))
            i += 1
            continue
        
        # Таблицы
        if '|' in line and i + 1 < len(lines) and re.match(r'^\s*\|?\s*[-:]+', lines[i + 1]):
            buf = [line]
            i += 1
            while i < len(lines) and '|' in lines[i]:
                buf.append(lines[i])
                i += 1
            blocks.append(Block('table', '\n'.join(buf)))
            continue
        
        # Списки
        if re.match(r'^\s*[-*+]\s+', line) or re.match(r'^\s*\d+\.\s+', line):
            buf = [line]
            i += 1
            while i < len(lines) and (
                re.match(r'^\s+[-*+\d]', lines[i]) or
                (lines[i].strip() and lines[i].startswith('  '))
            ):
                buf.append(lines[i])
                i += 1
            blocks.append(Block('list', '\n'.join(buf)))
            continue
        
        # Цитаты
        if line.startswith('>'):
            buf = [line]
            i += 1
            while i < len(lines) and lines[i].startswith('>'):
                buf.append(lines[i])
                i += 1
            blocks.append(Block('quote', '\n'.join(buf)))
            continue
        
        # Пустая строка
        if not line.strip():
            i += 1
            continue
        
        # Абзац
        buf = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].startswith(('#', '```', '>', '-', '*', '|')) and not re.match(r'^\s*\d+\.', lines[i]) and not re.match(r'^---+\s*$', lines[i]):
            buf.append(lines[i])
            i += 1
        blocks.append(Block('p', '\n'.join(buf)))
    
    return blocks


# ═══════════════════════════════════════════════════════════
# ФИЛЬТРЫ
# ═══════════════════════════════════════════════════════════

def is_removable_h1(title: str) -> bool:
    """H1, которые удаляем целиком (Integrations и всё что после)"""
    return bool(re.search(r'Integrations|Интеграции', title, re.IGNORECASE))


def is_removable_h2(title: str) -> bool:
    """H2, которые удаляем целиком (всё содержимое до следующего H2/H1)"""
    patterns = [
        r'Для кого',
        r'Структура документации',
        r'Что вы узнаете',
        r'Что дальше',
        r'Следующий шаг',
        r'Следующий раздел',
        r'Следующая секция',
        r'Частые ошибки',
        r'Что такое',
        r'Как использовать',
        r'Для кого этот',
        r'Checklist',
    ]
    return any(re.search(p, title, re.IGNORECASE) for p in patterns)


def is_removable_h3(title: str) -> bool:
    """H3, которые удаляем целиком"""
    patterns = [
        r'Что вы узнаете',
        r'Что дальше',
        r'Следующий шаг',
        r'Частые ошибки',
    ]
    return any(re.search(p, title, re.IGNORECASE) for p in patterns)


def is_exercise(block: Block) -> bool:
    """Блоки с упражнениями 💬"""
    return '💬' in block.content and ('Упражнение' in block.content or 'упражнение' in block.content)


def is_intro_quote(block: Block) -> bool:
    """Описательные цитаты типа '> **Полное руководство по...**'"""
    if block.type != 'quote':
        return False
    # Цитаты-описания в начале разделов
    return bool(re.search(r'\*\*(Полное руководство|Руководство|Обзор)', block.content))


def is_next_step_paragraph(block: Block) -> bool:
    """Абзацы со ссылками на следующий шаг"""
    if block.type != 'p':
        return False
    return bool(re.search(r'Следующий шаг|Следующий раздел|Следующая секция|Что дальше', block.content, re.IGNORECASE))


# ═══════════════════════════════════════════════════════════
# ГЛАВНЫЙ ФИЛЬТР
# ═══════════════════════════════════════════════════════════

def filter_blocks(blocks: List[Block]) -> List[Block]:
    result: List[Block] = []
    skip_level = 0  # 0 = не пропускаем, иначе уровень заголовка, до которого пропускаем
    in_integrations = False  # флаг: внутри раздела Integrations
    
    i = 0
    while i < len(blocks):
        block = blocks[i]
        
        # ─── H1: проверяем Integrations ───
        if block.type == 'h1':
            if is_removable_h1(block.content):
                in_integrations = True
                i += 1
                continue
            else:
                in_integrations = False
                skip_level = 0
                result.append(block)
                i += 1
                continue
        
        # Если в Integrations — пропускаем всё
        if in_integrations:
            i += 1
            continue
        
        # ─── Если мы в режиме пропуска секции ───
        if skip_level > 0:
            # Проверяем, не встретился ли заголовок того же или более высокого уровня
            if block.type in ('h1', 'h2', 'h3', 'h4'):
                if block.level <= skip_level:
                    skip_level = 0
                    # Не увеличиваем i — обработаем этот заголовок
                    continue
            i += 1
            continue
        
        # ─── H2: проверяем удаляемые секции ───
        if block.type == 'h2':
            if is_removable_h2(block.content):
                skip_level = 2  # пропускаем всё до следующего H2 или H1
                i += 1
                continue
            result.append(block)
            i += 1
            continue
        
        # ─── H3: проверяем удаляемые ───
        if block.type == 'h3':
            if is_removable_h3(block.content):
                skip_level = 3  # пропускаем до следующего H3/H2/H1
                i += 1
                continue
            result.append(block)
            i += 1
            continue
        
        # ─── Пропуск мусора ───
        if block.type in ('comment', 'hr'):
            i += 1
            continue
        
        # ─── Упражнения ───
        if is_exercise(block):
            i += 1
            continue
        
        # ─── Описательные цитаты в начале разделов ───
        if is_intro_quote(block):
            i += 1
            continue
        
        # ─── Абзацы "Следующий шаг" ───
        if is_next_step_paragraph(block):
            i += 1
            continue
        
        # ─── Всё остальное оставляем ───
        result.append(block)
        i += 1
    
    return result


# ═══════════════════════════════════════════════════════════
# СБОРКА
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
    print('📊 СТАТИСТИКА (v5 — ХИРУРГИЧЕСКИЙ)')
    print('═' * 60)
    print(f'  Оригинал:  {orig_chars:>10,} символов  |  {orig_lines:>6,} строк  |  ~{orig_pages:.0f} стр.')
    print(f'  Результат: {comp_chars:>10,} символов  |  {comp_lines:>6,} строк  |  ~{comp_pages:.0f} стр.')
    print(f'  Удалено:   {(1 - comp_chars/orig_chars)*100:>9.1f}%')
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
    
    print('🔪 Хирургическое удаление...')
    filtered = filter_blocks(blocks)
    print(f'   Осталось блоков: {len(filtered)}')
    
    print('📝 Собираю Markdown...')
    compressed = blocks_to_markdown(filtered)
    
    print(f'💾 Сохраняю: {output_path}')
    output_path.write_text(compressed, encoding='utf-8')
    
    print_stats(original, compressed)
    print('✅ Готово!')


if __name__ == '__main__':
    main()