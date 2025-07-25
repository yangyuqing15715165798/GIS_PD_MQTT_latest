#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
验证脚本：检查SVM架构分析文档的完整性
"""

import os

def verify_document():
    """验证文档完整性"""
    print("=== 验证SVM架构分析文档 ===")
    
    # 检查文件是否存在
    file_path = "SVM_PD_Classification_Architecture_Analysis.md"
    if not os.path.exists(file_path):
        print("❌ 文档文件不存在")
        return False
    
    # 读取文档内容
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ 读取文档失败: {e}")
        return False
    
    # 检查必要的章节
    required_sections = [
        "# GIS-PD实时分析平台SVM局部放电类型识别功能技术架构分析",
        "## 用户原始问题",
        "## 技术架构分析",
        "### 📊 技术架构分析",
        "#### **方案一：集成式架构**",
        "#### **方案二：微服务架构**",
        "### 🎯 **推荐方案：混合式集成架构**",
        "## 🔧 **具体实现建议**",
        "## 📈 **性能优化策略**",
        "## 🎯 **最终推荐**",
        "## 文档信息"
    ]
    
    print("检查必要章节:")
    missing_sections = []
    for section in required_sections:
        if section in content:
            print(f"   ✓ {section}")
        else:
            print(f"   ❌ {section}")
            missing_sections.append(section)
    
    # 检查关键内容
    key_contents = [
        "方案一：集成式架构",
        "方案二：微服务架构",
        "性能要求",
        "部署复杂度",
        "维护性",
        "扩展性",
        "资源消耗",
        "数据安全",
        "用户体验",
        "PySide6 GUI、MQTT实时数据、SQLite数据库、matplotlib可视化",
        "PDClassificationEngine",
        "ClassificationWorker",
        "QThread",
        "scikit-learn",
        "推荐采用集成式架构"
    ]
    
    print("\n检查关键内容:")
    missing_contents = []
    for content_item in key_contents:
        if content_item in content:
            print(f"   ✓ {content_item}")
        else:
            print(f"   ❌ {content_item}")
            missing_contents.append(content_item)
    
    # 检查代码块
    code_blocks = content.count("```python")
    print(f"\n代码块数量: {code_blocks}")
    if code_blocks >= 3:
        print("   ✓ 包含足够的代码示例")
    else:
        print("   ❌ 代码示例不足")
    
    # 统计信息
    lines = content.split('\n')
    words = len(content.split())
    chars = len(content)
    
    print(f"\n文档统计:")
    print(f"   总行数: {len(lines)}")
    print(f"   总字数: {words}")
    print(f"   总字符数: {chars}")
    
    # 最终结果
    if not missing_sections and not missing_contents and code_blocks >= 3:
        print("\n🎉 文档验证通过！内容完整且格式正确。")
        return True
    else:
        print("\n❌ 文档验证失败，存在缺失内容。")
        return False

if __name__ == "__main__":
    success = verify_document()
    exit(0 if success else 1)
