#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试脚本：验证正弦波控制组件的移除
"""

import sys
import os

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_code_cleanup():
    """测试代码清理"""
    print("=== 测试代码清理 ===")
    
    # 读取主文件
    try:
        with open('gis_pd_mqtt_gui_ui_revamp.py', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("❌ 主文件未找到")
        return False
    
    # 检查已移除的组件
    removed_checks = [
        ("正弦波振幅标签", "正弦波振幅:"),
        ("sine_amplitude_spin控件", "sine_amplitude_spin"),
        ("update_sine_params函数", "def update_sine_params"),
        ("sine_amplitude属性", "self.sine_amplitude = 1.0"),
    ]
    
    passed = 0
    total = len(removed_checks)
    
    for check_name, check_text in removed_checks:
        if check_text not in content:
            print(f"   ✓ {check_name} 已成功移除")
            passed += 1
        else:
            print(f"   ❌ {check_name} 仍然存在: {check_text}")
    
    # 检查保留的功能
    preserved_checks = [
        ("正弦波显示复选框", "显示参考正弦波"),
        ("toggle_sine_wave函数", "def toggle_sine_wave"),
        ("get_sine_wave_params函数", "def get_sine_wave_params"),
        ("正弦波绘制逻辑", "参考正弦波"),
        ("show_sine_wave属性", "self.show_sine_wave"),
    ]
    
    for check_name, check_text in preserved_checks:
        if check_text in content:
            print(f"   ✓ {check_name} 已保留")
            passed += 1
        else:
            print(f"   ❌ {check_name} 意外丢失: {check_text}")
    
    total += len(preserved_checks)
    
    print(f"\n检查结果: {passed}/{total} 项通过")
    
    if passed == total:
        print("🎉 代码清理验证通过！")
        return True
    else:
        print("❌ 代码清理验证失败")
        return False

def test_ui_functionality():
    """测试UI功能"""
    print("\n=== 测试UI功能 ===")
    
    try:
        # 导入必要的模块
        from PySide6.QtWidgets import QApplication
        from gis_pd_mqtt_gui_ui_revamp import MainWindow, HistoricalChartsDialog
        
        # 创建QApplication实例
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
        
        # 测试主窗口
        print("1. 测试主窗口...")
        main_window = MainWindow()
        
        # 检查正弦波显示复选框是否存在
        assert hasattr(main_window, 'show_sine_checkbox'), "主窗口应该有show_sine_checkbox"
        print("   ✓ 正弦波显示复选框存在")
        
        # 检查正弦波振幅控件是否已移除
        assert not hasattr(main_window, 'sine_amplitude_spin'), "主窗口不应该有sine_amplitude_spin"
        print("   ✓ 正弦波振幅控件已移除")
        
        # 检查正弦波相关函数是否存在
        assert hasattr(main_window, 'toggle_sine_wave'), "主窗口应该有toggle_sine_wave函数"
        assert hasattr(main_window, 'get_sine_wave_params'), "主窗口应该有get_sine_wave_params函数"
        print("   ✓ 正弦波相关函数存在")
        
        # 检查update_sine_params函数是否已移除
        assert not hasattr(main_window, 'update_sine_params'), "主窗口不应该有update_sine_params函数"
        print("   ✓ update_sine_params函数已移除")
        
        # 测试历史数据对话框
        print("2. 测试历史数据对话框...")
        test_data = []
        dialog = HistoricalChartsDialog(test_data)
        
        # 检查正弦波显示复选框是否存在
        assert hasattr(dialog, 'show_sine_checkbox'), "对话框应该有show_sine_checkbox"
        print("   ✓ 正弦波显示复选框存在")
        
        # 检查正弦波振幅控件是否已移除
        assert not hasattr(dialog, 'sine_amplitude_spin'), "对话框不应该有sine_amplitude_spin"
        print("   ✓ 正弦波振幅控件已移除")
        
        # 检查正弦波相关函数是否存在
        assert hasattr(dialog, 'get_sine_wave_params'), "对话框应该有get_sine_wave_params函数"
        print("   ✓ 正弦波相关函数存在")
        
        print("=== UI功能测试通过 ===")
        return True
        
    except Exception as e:
        print(f"❌ UI功能测试失败: {str(e)}")
        return False

def test_sine_wave_parameters():
    """测试正弦波参数功能"""
    print("\n=== 测试正弦波参数功能 ===")
    
    try:
        # 导入必要的模块
        from PySide6.QtWidgets import QApplication
        from gis_pd_mqtt_gui_ui_revamp import MainWindow
        
        # 创建QApplication实例
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
        
        # 测试主窗口的正弦波参数
        main_window = MainWindow()
        
        # 测试dBm模式下的正弦波参数
        assert main_window.use_dbm == True, "默认应该使用dBm单位"
        sine_params = main_window.get_sine_wave_params()
        assert sine_params == (25, -25), f"dBm模式下正弦波参数应为(25, -25)，实际为: {sine_params}"
        print("   ✓ dBm模式下正弦波参数正确")
        
        # 切换到mV模式测试
        main_window.toggle_unit()
        assert main_window.use_dbm == False, "切换后应该使用mV单位"
        sine_params_mv = main_window.get_sine_wave_params()
        assert sine_params_mv[0] > 0, "正弦波振幅应为正值"
        print("   ✓ mV模式下正弦波参数正确")
        
        print("=== 正弦波参数功能测试通过 ===")
        return True
        
    except Exception as e:
        print(f"❌ 正弦波参数功能测试失败: {str(e)}")
        return False

def main():
    """主测试函数"""
    print("开始测试正弦波控制组件的移除...")
    print("=" * 50)
    
    try:
        # 测试代码清理
        cleanup_ok = test_code_cleanup()
        
        # 测试UI功能
        ui_ok = test_ui_functionality()
        
        # 测试正弦波参数功能
        params_ok = test_sine_wave_parameters()
        
        if cleanup_ok and ui_ok and params_ok:
            print("\n🎉 所有测试通过！正弦波控制组件移除成功！")
            print("\n修改总结:")
            print("1. ✓ 移除了主界面中的正弦波振幅调整控件")
            print("2. ✓ 移除了历史数据对话框中的正弦波振幅调整控件")
            print("3. ✓ 移除了update_sine_params函数和sine_amplitude属性")
            print("4. ✓ 保留了正弦波显示/隐藏切换功能")
            print("5. ✓ 保留了正弦波绘制逻辑和智能参数计算")
            print("6. ✓ 界面布局调整正确，功能完整")
            return True
        else:
            print("\n❌ 测试失败")
            return False
            
    except Exception as e:
        print(f"❌ 测试过程中发生错误: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
