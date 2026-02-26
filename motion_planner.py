"""
运动规划器 - 规划和管理运动序列
Motion Planner - Plans and manages motion sequences
"""

import time


class MotionPlanner:
    """运动规划器"""
    
    def __init__(self):
        """初始化运动规划器"""
        self.current_mode = 'stop'
        self.current_speed = 0
        self.mode_start_time = time.time()
        
    def set_mode(self, mode, speed=0.5):
        """
        设置运动模式
        :param mode: 运动模式 ('forward', 'backward', 'turn_left', 'turn_right', 'climb', 'stop')
        :param speed: 速度 (0.0 到 1.0)
        """
        if mode != self.current_mode:
            print(f"切换运动模式: {self.current_mode} -> {mode}")
            self.mode_start_time = time.time()
            
        self.current_mode = mode
        self.current_speed = max(0, min(1.0, speed))
        
    def get_current_command(self):
        """获取当前运动命令"""
        return {
            'mode': self.current_mode,
            'speed': self.current_speed,
            'timestamp': time.time()
        }
        
    def get_mode_duration(self):
        """获取当前模式持续时间"""
        return time.time() - self.mode_start_time
        
    def execute_sequence(self, sequence):
        """
        执行运动序列
        :param sequence: 运动序列列表
        """
        for motion in sequence:
            mode = motion.get('mode', 'stop')
            duration = motion.get('duration', 1.0)
            speed = motion.get('speed', 0.5)
            
            self.set_mode(mode, speed)
            time.sleep(duration)
            
    def stop(self):
        """停止运动"""
        self.set_mode('stop', 0)
