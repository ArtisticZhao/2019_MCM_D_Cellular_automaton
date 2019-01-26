# coding:utf-8

from enum import Enum, unique

VISION_SIZE = 10


@unique
class Block(Enum):
    '''
    枚举类, 方块,确定物体的类型
    '''
    EMPTY = 0            # 空白
    WALL = 1             # 障碍物
    MAN = 2              # 人
    GATE = 3             # 门
    DIRECTION_UP = 4     # 方向指示牌
    DIRECTION_DOWN = 5   # 方向指示牌
    DIRECTION_LEFT = 6   # 方向指示牌
    DIRECTION_RIGHT = 7  # 方向指示牌


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
    GATE = 1000             # 门
    DIRECTION_UP = 10     # 方向指示牌
    DIRECTION_DOWN = 10   # 方向指示牌
    DIRECTION_LEFT = 10   # 方向指示牌
    DIRECTION_RIGHT = 10  # 方向指示牌
