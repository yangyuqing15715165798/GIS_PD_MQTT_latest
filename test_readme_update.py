#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试脚本：验证README文档更新
"""

import os
import sys

def test_readme_content():
    """测试README文档内容"""
    print("=== 测试README文档更新 ===")
    
    # 读取README文件
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("❌ README.md文件未找到")
        return False
    
    # 检查新增的功能描述
    checks = [
        ("2025年7月23日更新", "### 2025年7月23日"),
        ("最新更新标识", "🆕 最新更新 (2025.7.23)"),
        ("默认单位优化", "默认单位优化"),
        ("智能正弦波显示", "智能正弦波显示优化"),
        ("动态轴范围调整", "动态轴范围调整系统"),
        ("代码架构优化", "代码架构优化"),
        ("get_axis_range函数", "get_axis_range()"),
        ("get_sine_wave_params函数", "get_sine_wave_params()"),
        ("dBm模式描述", "dBm模式：固定专业范围(-50到0 dBm)"),
        ("mV模式描述", "mV模式：自动计算对应毫伏值范围"),
        ("正弦波参数描述", "振幅25 dBm，偏移-25 dBm"),
        ("单位转换公式", "dBm = 毫伏值 × 54.545 - 81.818"),
        ("专业单位系统", "专业单位系统"),
        ("智能参考正弦波", "智能参考正弦波显示"),
        ("动态轴范围系统", "动态轴范围系统"),
        ("单位转换引擎", "单位转换引擎"),
        ("使用方法更新", "默认使用dBm单位显示"),
        ("数据格式更新", "显示范围"),
    ]
    
    passed = 0
    total = len(checks)
    
    for check_name, check_text in checks:
        if check_text in content:
            print(f"   ✓ {check_name}")
            passed += 1
        else:
            print(f"   ❌ {check_name} - 未找到: {check_text}")
    
    print(f"\n检查结果: {passed}/{total} 项通过")
    
    if passed == total:
        print("🎉 README文档更新验证通过！")
        return True
    else:
        print("❌ README文档更新验证失败")
        return False

def test_readme_structure():
    """测试README文档结构"""
    print("\n=== 测试README文档结构 ===")
    
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("❌ README.md文件未找到")
        return False
    
    # 检查主要章节
    sections = [
        "# GIS-PD实时分析平台",
        "## 功能特点",
        "## 更新日志",
        "### 2025年7月23日",
        "## 技术实现",
        "## 使用方法",
        "## 数据格式",
        "## 系统要求"
    ]
    
    found_sections = []
    for line in lines:
        line = line.strip()
        for section in sections:
            if line.startswith(section):
                found_sections.append(section)
                break
    
    print(f"找到的章节: {len(found_sections)}/{len(sections)}")
    for section in found_sections:
        print(f"   ✓ {section}")
    
    missing_sections = set(sections) - set(found_sections)
    if missing_sections:
        print("缺失的章节:")
        for section in missing_sections:
            print(f"   ❌ {section}")
        return False
    
    print("✓ README文档结构完整")
    return True

def main():
    """主测试函数"""
    print("开始测试README文档更新...")
    print("=" * 50)
    
    try:
        # 测试文档内容
        content_ok = test_readme_content()
        
        # 测试文档结构
        structure_ok = test_readme_structure()
        
        if content_ok and structure_ok:
            print("\n🎉 README文档更新测试全部通过！")
            print("\n更新总结:")
            print("1. ✓ 添加了2025年7月23日的更新日志")
            print("2. ✓ 更新了功能特点描述")
            print("3. ✓ 添加了最新功能亮点")
            print("4. ✓ 更新了使用方法说明")
            print("5. ✓ 完善了数据格式描述")
            print("6. ✓ 增加了新的技术实现特性")
            print("7. ✓ 文档结构完整且格式正确")
            return True
        else:
            print("\n❌ README文档更新测试失败")
            return False
            
    except Exception as e:
        print(f"❌ 测试过程中发生错误: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
