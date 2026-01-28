# SunEnergyXT 500 Series

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

## Language / Sprache / 语言

- [English](README.md) (default)
- [中文](README.zh.md)
- [Deutsch](README.de.md)

## 介绍

SunEnergyXT 500 Series 是一个 Home Assistant 的自定义集成，用于监控和控制 SunEnergyXT 500 系列逆变器。

## 功能

- 监控逆变器的实时状态和数据
- 控制逆变器的各种模式和设置
- 调整逆变器的参数
- 支持通过 Zeroconf 自动发现设备

## 安装

### 通过 HACS 安装（推荐）

1. 在 Home Assistant 中打开 HACS
2. 点击 "集成"（Integrations）
3. 点击右下角的 "+ 浏览存储库"（+ Explore & Download Repositories）
4. 搜索 "SunEnergyXT 500 Series"
5. 点击 "下载"（Download）
6. 重启 Home Assistant

### 手动安装

1. 下载最新版本的 [发布包](https://github.com/GLORYFeonix/SunEnergyXT_500_Series/releases)
2. 解压到 `config/custom_components/` 目录下
3. 确保目录结构为 `config/custom_components/sunenergyxt/`
4. 重启 Home Assistant

## 配置

1. 在 Home Assistant 中，进入 "配置"（Configuration）> "设备与服务"（Devices & Services）
2. 点击 "+ 添加集成"（+ Add Integration）
3. 搜索 "SunEnergyXT 500 Series"
4. 按照提示完成配置流程
   - 输入逆变器的 IP 地址
   - 输入逆变器的序列号

## 实体说明

### 传感器（Sensor）

| 实体 ID | 名称 | 单位 | 描述 |
|--------|------|------|------|
| WS | 工作状态 | - | 逆变器的工作状态 |
| WR | 工作模式 | - | 逆变器的工作模式 |
| ST | 系统时间 | - | 逆变器的系统时间 |
| IW | 输入功率 | W | 逆变器的输入功率 |
| OP | 输出功率 | W | 逆变器的输出功率 |
| PV | 光伏总功率 | W | 光伏总功率 |
| PV1 | 光伏组串 1 功率 | W | 光伏组串 1 的功率 |
| PV2 | 光伏组串 2 功率 | W | 光伏组串 2 的功率 |
| PV3 | 光伏组串 3 功率 | W | 光伏组串 3 的功率 |
| PV4 | 光伏组串 4 功率 | W | 光伏组串 4 的功率 |
| II1 | 输入电流 1 | A | 输入电流 1 |
| II2 | 输入电流 2 | A | 输入电流 2 |
| II3 | 输入电流 3 | A | 输入电流 3 |
| II4 | 输入电流 4 | A | 输入电流 4 |
| VP1 | 输入电压 1 | V | 输入电压 1 |
| VP2 | 输入电压 2 | V | 输入电压 2 |
| VP3 | 输入电压 3 | V | 输入电压 3 |
| VP4 | 输入电压 4 | V | 输入电压 4 |
| GP | 电网功率 | W | 电网功率 |
| LP | 负载功率 | W | 负载功率 |
| GD1 | 电网发电总量 | kwh | 电网发电总量 |
| GD2 | 电网发电总量 2 | kwh | 电网发电总量 2 |
| LD | 负载消耗总量 | kwh | 负载消耗总量 |
| SC | 系统状态 | % | 系统状态 |
| SC0 | 系统状态 0 | % | 系统状态 0 |
| SC1 | 系统状态 1 | % | 系统状态 1 |
| SC2 | 系统状态 2 | % | 系统状态 2 |
| SC3 | 系统状态 3 | % | 系统状态 3 |
| SC4 | 系统状态 4 | % | 系统状态 4 |
| SC5 | 系统状态 5 | % | 系统状态 5 |
| ON | 在线状态 | - | 逆变器的在线状态 |
| ES | 错误状态 | - | 逆变器的错误状态 |
| BS0 | 电池状态 0 | - | 电池状态 0 |
| BS1 | 电池状态 1 | - | 电池状态 1 |
| BS2 | 电池状态 2 | - | 电池状态 2 |
| BS3 | 电池状态 3 | - | 电池状态 3 |
| BS4 | 电池状态 4 | - | 电池状态 4 |
| BS5 | 电池状态 5 | - | 电池状态 5 |
| AS | 告警状态 | - | 逆变器的告警状态 |
| DS | 设备状态 | - | 设备状态 |
| SN | 序列号 | - | 逆变器的序列号 |
| MS | 制造商 | - | 逆变器的制造商 |

### 数字（Number）

| 实体 ID | 名称 | 单位 | 范围 | 步长 | 描述 |
|--------|------|------|------|------|------|
| GS | 电网功率设置 | W | -2400 至 2400 | 10 | 电网功率设置 |
| IS | 输入功率设置 | W | 1 至 2400 | 10 | 输入功率设置 |
| SI | 起始充电电流 | % | 1 至 30 | 1 | 起始充电电流 |
| SA | 充电终止电压 | % | 70 至 100 | 1 | 充电终止电压 |
| SO | 放电终止电压 | % | 1 至 30 | 1 | 放电终止电压 |
| PT | 保护时间 | min | 30 至 1440 | 1 | 保护时间 |

### 按钮（Button）

| 实体 ID | 名称 | 描述 |
|--------|------|------|
| RT | 重启 | 重启逆变器 |

### 开关（Switch）

| 实体 ID | 名称 | 描述 |
|--------|------|------|
| LM | 灯光模式 | 灯光模式开关 |
| MM | 静音模式 | 静音模式开关 |
| PM | 电源模式 | 电源模式开关 |

### 文本（Text）

| 实体 ID | 名称 | 描述 |
|--------|------|------|
| MD | 设备型号 | 逆变器的设备型号 |
| TZ | 时区 | 逆变器的时区设置 |

## 故障排除

### 无法发现设备

- 确保逆变器已开机并连接到网络
- 确保 Home Assistant 与逆变器在同一网络段
- 尝试手动输入逆变器的 IP 地址

### 数据更新不及时

- 检查网络连接是否稳定
- 检查逆变器是否正常工作
- 尝试重启逆变器和 Home Assistant

## 贡献

欢迎贡献代码或提出建议！请在 [GitHub](https://github.com/GLORYFeonix/SunEnergyXT_500_Series) 上提交 issue 或 pull request。

## 许可证

此项目采用 MIT 许可证 - 有关详细信息，请参阅 [LICENSE](LICENSE) 文件。

[releases-shield]: https://img.shields.io/github/release/GLORYFeonix/SunEnergyXT_500_Series.svg
[releases]: https://github.com/GLORYFeonix/SunEnergyXT_500_Series/releases
[commits-shield]: https://img.shields.io/github/commit-activity/y/GLORYFeonix/SunEnergyXT_500_Series.svg
[commits]: https://github.com/GLORYFeonix/SunEnergyXT_500_Series/commits/main
[license-shield]: https://img.shields.io/github/license/GLORYFeonix/SunEnergyXT_500_Series.svg