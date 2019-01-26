# coding:utf-8

from enum import Enum, unique

VISION_SIZE = 20


@unique
class Block(Enum):
    '''
    枚举类, 方块,确定物体的类型
    '''
    EMPTY = 0             # 空白
    WALL = 10             # 障碍物
    MAN = 20              # 人
    WISDOM_MAN = 21       # 真-智叟
    GATE = 30             # 门
    DIRECTION_UP = 40     # 方向指示牌
    DIRECTION_DOWN = 50   # 方向指示牌
    DIRECTION_LEFT = 60   # 方向指示牌
    DIRECTION_RIGHT = 70  # 方向指示牌


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
    GATE = 1000             # 门
    DIRECTION_UP = 10     # 方向指示牌
    DIRECTION_DOWN = 10   # 方向指示牌
    DIRECTION_LEFT = 10   # 方向指示牌
    DIRECTION_RIGHT = 10  # 方向指示牌
    SAME_DIRECTION = 10
