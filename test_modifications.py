#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试脚本：验证GIS-PD实时分析平台的修改
"""

import sys
import os

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_default_settings():
    """测试默认设置"""
    print("=== 测试默认设置 ===")

    # 导入必要的模块
    from PySide6.QtWidgets import QApplication
    from gis_pd_mqtt_gui_ui_revamp import MainWindow, HistoricalChartsDialog

    # 创建QApplication实例
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    # 测试主窗口默认设置
    print("1. 测试主窗口默认设置...")
    main_window = MainWindow()
    
    # 检查默认单位设置
    assert main_window.use_dbm == True, f"主窗口默认单位应为dBm，实际为: {main_window.use_dbm}"
    assert main_window.unit_label == "幅值 (dBm)", f"主窗口默认单位标签应为'幅值 (dBm)'，实际为: {main_window.unit_label}"
    
    print("   ✓ 主窗口默认单位设置正确")
    
    # 测试历史数据对话框默认设置
    print("2. 测试历史数据对话框默认设置...")
    # 创建一个空的数据列表用于测试
    test_data = []
    dialog = HistoricalChartsDialog(test_data)
    
    # 检查默认单位设置
    assert dialog.use_dbm == True, f"对话框默认单位应为dBm，实际为: {dialog.use_dbm}"
    assert dialog.unit_label == "幅值 (dBm)", f"对话框默认单位标签应为'幅值 (dBm)'，实际为: {dialog.unit_label}"
    
    print("   ✓ 历史数据对话框默认单位设置正确")
    
    print("=== 默认设置测试通过 ===\n")

def test_axis_ranges():
    """测试轴范围设置"""
    print("=== 测试轴范围设置 ===")

    # 这里我们主要检查代码中是否包含了动态轴范围的设置
    with open('gis_pd_mqtt_gui_ui_revamp.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # 检查get_axis_range函数
    axis_range_count = content.count('def get_axis_range(self):')
    print(f"1. get_axis_range函数定义数量: {axis_range_count}")
    assert axis_range_count >= 2, f"应该至少有2处get_axis_range函数定义，实际找到: {axis_range_count}"
    print("   ✓ get_axis_range函数定义正确")

    # 检查get_sine_wave_params函数
    sine_params_count = content.count('def get_sine_wave_params(self):')
    print(f"2. get_sine_wave_params函数定义数量: {sine_params_count}")
    assert sine_params_count >= 2, f"应该至少有2处get_sine_wave_params函数定义，实际找到: {sine_params_count}"
    print("   ✓ get_sine_wave_params函数定义正确")

    # 检查动态轴范围调用
    dynamic_ylim_count = content.count('y_min, y_max = self.get_axis_range()')
    print(f"3. 动态Y轴范围设置数量: {dynamic_ylim_count}")
    assert dynamic_ylim_count >= 3, f"应该至少有3处动态Y轴范围设置，实际找到: {dynamic_ylim_count}"
    print("   ✓ 动态Y轴范围设置正确")

    # 检查动态Z轴范围调用
    dynamic_zlim_count = content.count('z_min, z_max = self.get_axis_range()')
    print(f"4. 动态Z轴范围设置数量: {dynamic_zlim_count}")
    assert dynamic_zlim_count >= 3, f"应该至少有3处动态Z轴范围设置，实际找到: {dynamic_zlim_count}"
    print("   ✓ 动态Z轴范围设置正确")

    print("=== 轴范围设置测试通过 ===\n")

def test_button_initialization():
    """测试按钮初始化"""
    print("=== 测试按钮初始化 ===")
    
    with open('gis_pd_mqtt_gui_ui_revamp.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查单位按钮初始化
    dbm_button_count = content.count('QPushButton("单位: dBm")')
    print(f"1. 单位按钮初始化为dBm的数量: {dbm_button_count}")
    assert dbm_button_count >= 2, f"应该至少有2处单位按钮初始化为dBm，实际找到: {dbm_button_count}"
    print("   ✓ 单位按钮初始化正确")
    
    # 检查MplCanvas默认单位标签
    canvas_dbm_count = content.count('unit_label="幅值 (dBm)"')
    print(f"2. MplCanvas默认单位标签为dBm的数量: {canvas_dbm_count}")
    assert canvas_dbm_count >= 1, f"应该至少有1处MplCanvas默认单位标签为dBm，实际找到: {canvas_dbm_count}"
    print("   ✓ MplCanvas默认单位标签正确")
    
    print("=== 按钮初始化测试通过 ===\n")

def test_sine_wave_and_unit_conversion():
    """测试正弦波参数和单位转换功能"""
    print("=== 测试正弦波参数和单位转换 ===")

    # 导入必要的模块
    from PySide6.QtWidgets import QApplication
    from gis_pd_mqtt_gui_ui_revamp import MainWindow, HistoricalChartsDialog

    # 创建QApplication实例
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    # 测试主窗口的单位转换和轴范围
    print("1. 测试主窗口单位转换和轴范围...")
    main_window = MainWindow()

    # 测试dBm单位下的轴范围
    assert main_window.use_dbm == True, "默认应该使用dBm单位"
    axis_range = main_window.get_axis_range()
    assert axis_range == (-50, 0), f"dBm单位下轴范围应为(-50, 0)，实际为: {axis_range}"
    print("   ✓ dBm单位下轴范围正确")

    # 测试dBm单位下的正弦波参数
    sine_params = main_window.get_sine_wave_params()
    assert sine_params == (25, -25), f"dBm单位下正弦波参数应为(25, -25)，实际为: {sine_params}"
    print("   ✓ dBm单位下正弦波参数正确")

    # 切换到mV单位
    main_window.toggle_unit()
    assert main_window.use_dbm == False, "切换后应该使用mV单位"

    # 测试mV单位下的轴范围
    axis_range_mv = main_window.get_axis_range()
    expected_min = main_window.convert_unit(-50, False)  # -50 dBm转mV
    expected_max = main_window.convert_unit(0, False)    # 0 dBm转mV
    assert abs(axis_range_mv[0] - expected_min) < 0.01, f"mV单位下最小值应为{expected_min:.3f}，实际为: {axis_range_mv[0]:.3f}"
    assert abs(axis_range_mv[1] - expected_max) < 0.01, f"mV单位下最大值应为{expected_max:.3f}，实际为: {axis_range_mv[1]:.3f}"
    print("   ✓ mV单位下轴范围正确")

    # 测试mV单位下的正弦波参数
    sine_params_mv = main_window.get_sine_wave_params()
    print(f"   mV单位下正弦波参数: 振幅={sine_params_mv[0]:.3f}, 偏移={sine_params_mv[1]:.3f}")
    assert sine_params_mv[0] > 0, "正弦波振幅应为正值"
    print("   ✓ mV单位下正弦波参数正确")

    print("=== 正弦波参数和单位转换测试通过 ===\n")

def main():
    """主测试函数"""
    print("开始测试GIS-PD实时分析平台的修改...")
    print("=" * 50)
    
    try:
        # 测试默认设置
        test_default_settings()
        
        # 测试轴范围设置
        test_axis_ranges()

        # 测试按钮初始化
        test_button_initialization()

        # 测试正弦波参数和单位转换
        test_sine_wave_and_unit_conversion()
        
        print("🎉 所有测试通过！修改成功！")
        print("\n修改总结:")
        print("1. ✓ 默认单位已改为dBm")
        print("2. ✓ PRPD图Y轴动态范围设置（dBm: -50到0，mV: 对应转换值）")
        print("3. ✓ PRPS图Z轴动态范围设置（dBm: -50到0，mV: 对应转换值）")
        print("4. ✓ 单位按钮初始化为'单位: dBm'")
        print("5. ✓ 正弦波参数动态调整（dBm: 振幅25，偏移-25）")
        print("6. ✓ 所有相关函数都已更新")
        print("7. ✓ 单位切换时轴范围自动调整")
        
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
