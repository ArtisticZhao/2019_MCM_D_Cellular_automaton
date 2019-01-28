# coding:utf-8

from enum import Enum, unique

VISION_SIZE = 10
GATE_AREA = 20  # 请等于上一个值
IS_SHOW = True
# IS_SHOW = False


@unique
class Block(Enum):
    '''
    枚举类, 方块,确定物体的类型
    '''
    EMPTY = 0             # 空白
    EMPTY_NEAR_GATE = 1   # 人们更乐于趋向的位置
    WALL = 10             # 障碍物
    MAN = 20              # 人
    MAN_NEW = 22          # 新人类
    WISDOM_MAN = 21       # 真-智叟
    GATE = 30             # 门
    GATE_MAN_OUT = 40     # 传送门
    DIRECTION_UP = 2      # 方向指示牌
    DIRECTION_DOWN = 3    # 方向指示牌
    DIRECTION_LEFT = 4    # 方向指示牌
    DIRECTION_RIGHT = 5   # 方向指示牌


@unique
class Direction(Enum):
    '''
    枚举类, 方向,用于确定物体移动方向
    '''
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    UP_LEFT = 4
    UP_RIGHT = 5
    DOWN_LEFT = 6
    DOWN_RIGHT = 7


class Weight(Enum):
    EMPTY = 0            # 空白
    WALL = -0.1             # 障碍物
    MAN = 1              # 人
    WISDOM_MAN = 20
    GATE = 2000             # 门
    EMPTY_NEAR_GATE = 20    # 近门空白区域
    DIRECTION_UP = 1000     # 方向指示牌
    DIRECTION_DOWN = 1000   # 方向指示牌
    DIRECTION_LEFT = 1100   # 方向指示牌
    DIRECTION_RIGHT = 900  # 方向指示牌
    SAME_DIRECTION = 10000
