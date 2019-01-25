# coding:utf-8

from enum import Enum, unique


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


class People(object):
    '''
    定义人类:
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction):
        if(direction == Direction.UP):
            self.y = self.y - 1
        elif(direction == Direction.DOWN):
            self.y = self.y + 1
        elif(direction == Direction.LEFT):
            self.x = self.x - 1
        elif(direction == Direction.RIGHT):
            self.x = self.x + 1

        elif(direction == Direction.UP_LEFT):
            self.y = self.y - 1
            self.x = self.x - 1
        elif(direction == Direction.UP_RIGHT):
            self.y = self.y - 1
            self.x = self.x + 1
        elif(direction == Direction.DOWN_LEFT):
            self.y = self.y + 1
            self.x = self.x - 1
        elif(direction == Direction.DOWN_RIGHT):
            self.y = self.y + 1
            self.x = self.x + 1
