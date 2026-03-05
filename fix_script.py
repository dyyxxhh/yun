#!/usr/bin/env python3
# 修复语音识别导致的标点错误和数字格式

import re

def fix_chinese_numbers(text):
    """修复中文数字"""
    # 修复"一运"、"二运"等
    chinese_to_arabic = {
        '一': '1',
        '二': '2', 
        '三': '3',
        '四': '4',
        '五': '5',
        '六': '6',
        '七': '7',
        '八': '8',
        '九': '9',
        '十': '10',
        '零': '0'
    }
    
    # 修复"减X运"为"-X运"
    text = re.sub(r'减(\d+)(运|魔力|点魔力)', r'-\1\2', text)
    
    # 修复"减零运"为"-0运"
    text = re.sub(r'减零运', '-0运', text)
    
    # 修复"一运"、"二运"等
    for chinese, arabic in chinese_to_arabic.items():
        text = re.sub(f'{chinese}运', f'{arabic}运', text)
    
    # 修复"正三魔力"为"+3魔力"
    text = re.sub(r'正(\d+)魔力', r'+\1魔力', text)
    
    # 修复"加一运"为"+1运"
    text = re.sub(r'加(\d+)运', r'+\1运', text)
    
    # 修复"运减2"为"运-2"
    text = re.sub(r'运减(\d+)', r'运-\1', text)
    
    # 修复"减一个运"为"-1运"
    text = re.sub(r'减一个运', '-1运', text)
    
    # 修复"减4点5点魔力"为"-4.5魔力"
    text = re.sub(r'减(\d+)点(\d+)点魔力', r'-\1.\2魔力', text)
    
    return text

def main():
    # 读取原始文件
    with open('game_rules_fixed.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 修复内容
    fixed_content = fix_chinese_numbers(content)
    
    # 写入修复后的文件
    with open('game_rules_fixed_fixed.md', 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print("修复完成！已保存为 game_rules_fixed_fixed.md")
    
    # 显示修复前后的对比
    original_lines = content.split('\n')
    fixed_lines = fixed_content.split('\n')
    
    print("\n=== 修复前后对比示例 ===")
    for i in range(min(20, len(original_lines))):
        if original_lines[i] != fixed_lines[i]:
            print(f"行 {i+1}:")
            print(f"  原: {original_lines[i]}")
            print(f"  新: {fixed_lines[i]}")
            print()

if __name__ == '__main__':
    main()