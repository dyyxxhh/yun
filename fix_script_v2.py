#!/usr/bin/env python3
# 修复语音识别导致的标点错误和数字格式 - 改进版

import re

def fix_content(text):
    """修复语音识别导致的标点错误和数字格式"""
    
    # 修复规则列表
    fixes = [
        # 1. 修复"减X运"为"-X运"（X是数字）
        (r'减(\d+)运', r'-\1运'),
        
        # 2. 修复"减零运"为"-0运"
        (r'减零运', '-0运'),
        
        # 3. 修复"减一个运"为"-1运"
        (r'减一个运', '-1运'),
        
        # 4. 修复"一运"、"二运"等为"1运"、"2运"
        (r'一运', '1运'),
        (r'二运', '2运'),
        (r'三运', '3运'),
        (r'四运', '4运'),
        (r'五运', '5运'),
        (r'六运', '6运'),
        (r'七运', '7运'),
        (r'八运', '8运'),
        (r'九运', '9运'),
        (r'十运', '10运'),
        
        # 5. 修复"正三魔力"为"+3魔力"
        (r'正(\d+)魔力', r'+\1魔力'),
        
        # 6. 修复"加一运"为"+1运"
        (r'加(\d+)运', r'+\1运'),
        
        # 7. 修复"运减2"为"运-2"
        (r'运减(\d+)', r'运-\1'),
        
        # 8. 修复"减X魔力"为"-X魔力"
        (r'减(\d+)魔力', r'-\1魔力'),
        
        # 9. 修复"减X点魔力"为"-X魔力"
        (r'减(\d+)点魔力', r'-\1魔力'),
        
        # 10. 修复"减4点5点魔力"为"-4.5魔力"
        (r'减(\d+)点(\d+)点魔力', r'-\1.\2魔力'),
        
        # 11. 修复"减九魔力"为"-9魔力"
        (r'减九魔力', '-9魔力'),
        
        # 12. 修复其他中文数字
        (r'一', '1'),
        (r'二', '2'),
        (r'三', '3'),
        (r'四', '4'),
        (r'五', '5'),
        (r'六', '6'),
        (r'七', '7'),
        (r'八', '8'),
        (r'九', '9'),
        (r'十', '10'),
        (r'零', '0'),
    ]
    
    # 应用所有修复规则
    for pattern, replacement in fixes:
        text = re.sub(pattern, replacement, text)
    
    return text

def main():
    # 读取原始文件
    with open('game_rules_fixed.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 修复内容
    fixed_content = fix_content(content)
    
    # 写入修复后的文件（覆盖之前的修复文件）
    with open('game_rules_fixed_fixed.md', 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print("修复完成！已保存为 game_rules_fixed_fixed.md")
    
    # 显示修复统计
    original_lines = content.split('\n')
    fixed_lines = fixed_content.split('\n')
    
    changed_count = 0
    for i in range(min(len(original_lines), len(fixed_lines))):
        if original_lines[i] != fixed_lines[i]:
            changed_count += 1
    
    print(f"总共修复了 {changed_count} 行")
    
    # 显示前10个修复示例
    print("\n=== 修复示例（前10个）===")
    count = 0
    for i in range(min(len(original_lines), len(fixed_lines))):
        if original_lines[i] != fixed_lines[i] and count < 10:
            print(f"行 {i+1}:")
            print(f"  原: {original_lines[i]}")
            print(f"  新: {fixed_lines[i]}")
            print()
            count += 1

if __name__ == '__main__':
    main()