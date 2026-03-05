#!/usr/bin/env python3
# 最终修复脚本 - 修复剩余问题并优化格式

import re

def final_fix_content(text):
    """修复剩余问题和优化格式"""
    
    # 修复规则列表
    fixes = [
        # 1. 修复"魔力减2"为"魔力-2"
        (r'魔力减(\d+)', r'魔力-\1'),
        
        # 2. 修复"减灵运，减灵魔力"为"-0运，-0魔力"
        (r'减灵运，减灵魔力', '-0运，-0魔力'),
        
        # 3. 修复"减灵运"为"-0运"
        (r'减灵运', '-0运'),
        
        # 4. 修复"减灵魔力"为"-0魔力"
        (r'减灵魔力', '-0魔力'),
        
        # 5. 优化格式：确保所有数字都是阿拉伯数字
        (r'(\d+)个', r'\1个'),
        
        # 6. 修复"1个"为"1个"（保持一致性）
        (r'1个', '1个'),
        
        # 7. 修复"2个"为"2个"
        (r'2个', '2个'),
        
        # 8. 修复"3个"为"3个"
        (r'3个', '3个'),
        
        # 9. 修复"4个"为"4个"
        (r'4个', '4个'),
        
        # 10. 修复"5个"为"5个"
        (r'5个', '5个'),
        
        # 11. 修复"6个"为"6个"
        (r'6个', '6个'),
        
        # 12. 修复"7个"为"7个"
        (r'7个', '7个'),
        
        # 13. 修复"8个"为"8个"
        (r'8个', '8个'),
        
        # 14. 修复"9个"为"9个"
        (r'9个', '9个'),
        
        # 15. 修复"10个"为"10个"
        (r'10个', '10个'),
    ]
    
    # 应用所有修复规则
    for pattern, replacement in fixes:
        text = re.sub(pattern, replacement, text)
    
    return text

def main():
    # 读取最新修复文件
    with open('game_rules_fixed_fixed.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 应用最终修复
    final_content = final_fix_content(content)
    
    # 写入最终文件
    with open('game_rules_final.md', 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print("最终修复完成！已保存为 game_rules_final.md")
    
    # 显示修复统计
    original_lines = content.split('\n')
    final_lines = final_content.split('\n')
    
    changed_count = 0
    for i in range(min(len(original_lines), len(final_lines))):
        if original_lines[i] != final_lines[i]:
            changed_count += 1
    
    print(f"总共修复了 {changed_count} 行")
    
    # 显示修复示例
    print("\n=== 修复示例 ===")
    count = 0
    for i in range(min(len(original_lines), len(final_lines))):
        if original_lines[i] != final_lines[i] and count < 5:
            print(f"行 {i+1}:")
            print(f"  原: {original_lines[i]}")
            print(f"  新: {final_lines[i]}")
            print()
            count += 1

if __name__ == '__main__':
    main()