# 轮腿式机器人 (Wheel-Leg Robot)

一个初学者友好的开源轮腿式机器人项目，结合了轮式运动的效率和腿式运动的越野能力。

## 项目特性

- 🤖 **模块化设计**: 易于扩展和修改
- 🔄 **多种运动模式**: 前进、后退、转向、爬升
- 📡 **传感器集成**: IMU传感器用于稳定性检测
- 🎮 **简单易用的控制接口**
- 📚 **详细的代码注释**: 适合初学者学习

## 硬件需求

### 必需组件
- Raspberry Pi 4 (推荐)
- 4个直流电机 (6V-12V)
- 4个电机驱动模块 (L298N或类似)
- MPU6050 IMU传感器
- 供电电源 (电池组或电源适配器)
- 连接线和母头接头

### 可选组件
- 超声波传感器 (HC-SR04) - 障碍物检测
- 摄像头模块 - 视觉处理
- 舵机 - 腿部精细控制

## 软件环境

### 安装依赖

```bash
# 更新系统
sudo apt-get update
sudo apt-get upgrade -y

# 安装Python3和pip
sudo apt-get install python3-pip python3-dev -y

# 安装项目依赖
pip3 install -r requirements.txt
