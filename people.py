# coding:utf-8

import numpy as np
from emun_def import Direction, Block, Weight

from functions import d_list, weight_choice, find_op_directions, is_in_corner


class People(object):
    '''
    定义人类:
    '''
    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.inner_x = None
        self.inner_y = None
        self.env = None
        self.distance_to_gate = distance
        self.current_direction = None
        self.speed = 1
        self.is_wisdom_man = False

    def move(self, direction):
        ID = 0
        GOUND = Block.EMPTY.value
        # 判断是否为智慧的人
        find_block = np.where(self.env == Block.GATE.value)
        if(find_block[0].size != 0):
            self.is_wisdom_man = True
            ID = Block.WISDOM_MAN.value
            GOUND = Block.EMPTY_NEAR_GATE.value
        else:
            self.is_wisdom_man = False
            ID = Block.MAN.value
            GOUND = Block.EMPTY.value

        for _ in range(0, self.speed):
            if(direction == Direction.UP):
                self.current_direction = Direction.UP
                if(self.env[self.inner_y-1, self.inner_x] == Block.EMPTY.value or
                   self.env[self.inner_y-1, self.inner_x] == Block.EMPTY_NEAR_GATE.value):
                    self.y = self.y - 1
                    self.env[self.inner_y, self.inner_x] = GOUND
                    self.env[self.inner_y-1, self.inner_x] = ID
                elif(self.env[self.inner_y-1, self.inner_x] == Block.GATE.value):
                    self.y = self.y - 1
                    self.env[self.inner_y, self.inner_x] = GOUND
                    return
            elif(direction == Direction.DOWN):
                self.current_direction = Direction.DOWN
                if(self.env[self.inner_y+1, self.inner_x] == Block.EMPTY.value or
                   self.env[self.inner_y+1, self.inner_x] == Block.EMPTY_NEAR_GATE.value):
                    self.y = self.y + 1
                    self.env[self.inner_y, self.inner_x] = GOUND
                    self.env[self.inner_y+1, self.inner_x] = ID
                elif(self.env[self.inner_y+1, self.inner_x] == Block.GATE.value):
                    self.y = self.y + 1
                    self.env[self.inner_y, self.inner_x] = GOUND
                    return
            elif(direction == Direction.LEFT):
                self.current_direction = Direction.LEFT
                if(self.env[self.inner_y, self.inner_x-1] == Block.EMPTY.value or
                   self.env[self.inner_y, self.inner_x-1] == Block.EMPTY_NEAR_GATE.value):
                    self.x = self.x - 1
                    self.env[self.inner_y, self.inner_x] = GOUND
                    self.env[self.inner_y, self.inner_x-1] = ID
                elif(self.env[self.inner_y, self.inner_x-1] == Block.GATE.value):
                    self.x = self.x - 1
                    self.env[self.inner_y, self.inner_x] = GOUND
                    return
            elif(direction == Direction.RIGHT):
                self.current_direction = Direction.RIGHT
                if(self.env[self.inner_y, self.inner_x+1] == Block.EMPTY.value or
                   self.env[self.inner_y, self.inner_x+1] == Block.EMPTY_NEAR_GATE.value):
                    self.x = self.x + 1
                    self.env[self.inner_y, self.inner_x] = GOUND
                    self.env[self.inner_y, self.inner_x+1] = ID
                elif(self.env[self.inner_y, self.inner_x+1] == Block.GATE.value):
                    self.x = self.x + 1
                    self.env[self.inner_y, self.inner_x] = GOUND
                    return

            elif(direction == Direction.UP_LEFT):
                self.current_direction = Direction.UP_LEFT
                if(self.env[self.inner_y-1, self.inner_x-1] == Block.EMPTY.value or
                   self.env[self.inner_y-1, self.inner_x-1] == Block.EMPTY_NEAR_GATE.value
                   ):
                    self.y = self.y - 1
                    self.x = self.x - 1
                    self.env[self.inner_y, self.inner_x] = GOUND
                    self.env[self.inner_y-1, self.inner_x-1] = ID
                elif(self.env[self.inner_y-1, self.inner_x-1] == Block.GATE.value):
                    self.y = self.y - 1
                    self.x = self.x - 1
                    self.env[self.inner_y, self.inner_x] = GOUND
                    return
            elif(direction == Direction.UP_RIGHT):
                self.current_direction = Direction.UP_RIGHT
                if(self.env[self.inner_y-1, self.inner_x+1] == Block.EMPTY.value or
                   self.env[self.inner_y-1, self.inner_x+1] == Block.EMPTY_NEAR_GATE.value
                   ):
                    self.y = self.y - 1
                    self.x = self.x + 1
                    self.env[self.inner_y, self.inner_x] = GOUND
                    self.env[self.inner_y-1, self.inner_x+1] = ID
                elif(self.env[self.inner_y-1, self.inner_x+1] == Block.GATE.value):
                    self.y = self.y - 1
                    self.x = self.x + 1
                    self.env[self.inner_y, self.inner_x] = GOUND
                    return
            elif(direction == Direction.DOWN_LEFT):
                self.current_direction = Direction.DOWN_LEFT
                if(self.env[self.inner_y+1, self.inner_x-1] == Block.EMPTY.value or
                   self.env[self.inner_y+1, self.inner_x-1] == Block.EMPTY_NEAR_GATE.value
                   ):
                    self.y = self.y + 1
                    self.x = self.x - 1
                    self.env[self.inner_y, self.inner_x] = GOUND
                    self.env[self.inner_y+1, self.inner_x-1] = ID
                elif(self.env[self.inner_y+1, self.inner_x-1] == Block.GATE.value):
                    self.y = self.y + 1
                    self.x = self.x - 1
                    self.env[self.inner_y, self.inner_x] = GOUND
                    return
            elif(direction == Direction.DOWN_RIGHT):
                self.current_direction = Direction.DOWN_RIGHT
                if(self.env[self.inner_y+1, self.inner_x+1] == Block.EMPTY.value or
                   self.env[self.inner_y+1, self.inner_x+1] == Block.EMPTY_NEAR_GATE.value
                   ):
                    self.y = self.y + 1
                    self.x = self.x + 1
                    self.env[self.inner_y, self.inner_x] = GOUND
                    self.env[self.inner_y+1, self.inner_x+1] = ID
                elif(self.env[self.inner_y+1, self.inner_x+1] == Block.GATE.value):
                    self.y = self.y + 1
                    self.x = self.x + 1
                    self.env[self.inner_y, self.inner_x] = GOUND
                    return

    def policy(self, env_mat, inner_x, inner_y):
        self.env = env_mat
        self.inner_x = inner_x
        self.inner_y = inner_y
        is_hit_wall_or_man = False
        # 计算权值----------------------------------------------------------------
        weights = list()
        for direc in d_list:
            # 绝不回头
            if self.current_direction is not None:
                if direc in find_op_directions(self.current_direction):
                    weights.append(0)
                    continue
            # 绝不撞向什么东西
            if self.is_not_hit_something(direc):
                env_block = self.see_direction(direc)
                weight = 0
                # 倾向于走相同的方向
                if(direc == self.current_direction):
                    weight = weight + Weight.SAME_DIRECTION.value
                # 倾向于走向大门
                find_block = np.where(env_block == Block.GATE.value)
                weight = weight + find_block[0].size * Weight.GATE.value
                # 愚者乐于向往大门附近的地方
                if(is_hit_wall_or_man or not self.is_wisdom_man):
                    find_block = np.where(env_block == Block.EMPTY_NEAR_GATE.value)
                    weight = weight + find_block[0].size * Weight.EMPTY_NEAR_GATE.value
                # 从众心理
                find_block = np.where(env_block == Block.MAN.value)
                weight = weight + find_block[0].size * Weight.MAN.value
                find_block = np.where(env_block == Block.WISDOM_MAN.value)
                weight = weight + find_block[0].size * Weight.MAN.value
                # 愚者跟随智慧的人
                if(not self.is_wisdom_man):
                    find_block = np.where(env_block == Block.WISDOM_MAN.value)
                    weight = weight + find_block[0].size * Weight.WISDOM_MAN.value
                if(is_in_corner(direc)):
                    weights.append(weight/2)
                else:
                    weights.append(weight)
            else:
                weights.append(0)
                is_hit_wall_or_man = True
        # 权值计算完毕----------------------------------------------------------------
        # 愚者跟随指示牌
        if(not self.is_wisdom_man):
            index = d_list.index(Direction.UP)
            find_block = np.where(env_mat == Block.DIRECTION_UP.value)
            weights[index] = (weights[index] +
                              find_block[0].size * Weight.DIRECTION_UP.value)
            index = d_list.index(Direction.DOWN)
            find_block = np.where(env_mat == Block.DIRECTION_DOWN.value)
            weights[index] = (weights[index] +
                              find_block[0].size * Weight.DIRECTION_DOWN.value)
            index = d_list.index(Direction.LEFT)
            find_block = np.where(env_mat == Block.DIRECTION_LEFT.value)
            weights[index] = (weights[index] +
                              find_block[0].size * Weight.DIRECTION_LEFT.value)
            index = d_list.index(Direction.RIGHT)
            find_block = np.where(env_mat == Block.DIRECTION_RIGHT.value)
            weights[index] = (weights[index] +
                              find_block[0].size * Weight.DIRECTION_RIGHT.value)

        # 根据概率产生方向
        go_direction = weight_choice(weights)
        self.move(go_direction)

    def see_direction(self, direction):
        if(direction == Direction.UP):
            return self.env[0:self.inner_y, :]
        elif(direction == Direction.DOWN):
            return self.env[self.inner_y+1:, :]
        elif(direction == Direction.LEFT):
            return self.env[:, 0:self.inner_x]
        elif(direction == Direction.RIGHT):
            return self.env[:, self.inner_x+1:]
        elif(direction == Direction.UP_LEFT):
            return self.env[0:self.inner_y, 0:self.inner_x]
        elif(direction == Direction.UP_RIGHT):
            return self.env[0:self.inner_y, self.inner_x+1:]
        elif(direction == Direction.DOWN_LEFT):
            return self.env[self.inner_y+1:, 0:self.inner_x]
        elif(direction == Direction.DOWN_RIGHT):
            return self.env[self.inner_y+1:, self.inner_x+1:]

    def is_not_hit_something(self, direction):
        if(direction == Direction.UP):
            next_block = self.env[self.inner_y-1, self.inner_x]
            return (next_block != Block.WALL.value and
                    next_block != Block.DIRECTION_DOWN.value and
                    next_block != Block.DIRECTION_LEFT.value and
                    next_block != Block.DIRECTION_RIGHT.value and
                    next_block != Block.DIRECTION_UP.value and
                    next_block != Block.WISDOM_MAN.value and
                    next_block != Block.MAN.value)
        elif(direction == Direction.DOWN):
            next_block = self.env[self.inner_y+1, self.inner_x]
            return (next_block != Block.WALL.value and
                    next_block != Block.DIRECTION_DOWN.value and
                    next_block != Block.DIRECTION_LEFT.value and
                    next_block != Block.DIRECTION_RIGHT.value and
                    next_block != Block.DIRECTION_UP.value and
                    next_block != Block.WISDOM_MAN.value and
                    next_block != Block.MAN.value)
        elif(direction == Direction.LEFT):
            next_block = self.env[self.inner_y, self.inner_x-1]
            return (next_block != Block.WALL.value and
                    next_block != Block.DIRECTION_DOWN.value and
                    next_block != Block.DIRECTION_LEFT.value and
                    next_block != Block.DIRECTION_RIGHT.value and
                    next_block != Block.DIRECTION_UP.value and
                    next_block != Block.WISDOM_MAN.value and
                    next_block != Block.MAN.value)
        elif(direction == Direction.RIGHT):
            next_block = self.env[self.inner_y, self.inner_x+1]
            return (next_block != Block.WALL.value and
                    next_block != Block.DIRECTION_DOWN.value and
                    next_block != Block.DIRECTION_LEFT.value and
                    next_block != Block.DIRECTION_RIGHT.value and
                    next_block != Block.DIRECTION_UP.value and
                    next_block != Block.WISDOM_MAN.value and
                    next_block != Block.MAN.value)
        elif(direction == Direction.UP_LEFT):
            next_block = self.env[self.inner_y-1, self.inner_x-1]
            return (next_block != Block.WALL.value and
                    next_block != Block.DIRECTION_DOWN.value and
                    next_block != Block.DIRECTION_LEFT.value and
                    next_block != Block.DIRECTION_RIGHT.value and
                    next_block != Block.DIRECTION_UP.value and
                    next_block != Block.WISDOM_MAN.value and
                    next_block != Block.MAN.value)
        elif(direction == Direction.UP_RIGHT):
            next_block = self.env[self.inner_y-1, self.inner_x+1]
            return (next_block != Block.WALL.value and
                    next_block != Block.DIRECTION_DOWN.value and
                    next_block != Block.DIRECTION_LEFT.value and
                    next_block != Block.DIRECTION_RIGHT.value and
                    next_block != Block.DIRECTION_UP.value and
                    next_block != Block.WISDOM_MAN.value and
                    next_block != Block.MAN.value)
        elif(direction == Direction.DOWN_LEFT):
            next_block = self.env[self.inner_y+1, self.inner_x-1]
            return (next_block != Block.WALL.value and
                    next_block != Block.DIRECTION_DOWN.value and
                    next_block != Block.DIRECTION_LEFT.value and
                    next_block != Block.DIRECTION_RIGHT.value and
                    next_block != Block.DIRECTION_UP.value and
                    next_block != Block.WISDOM_MAN.value and
                    next_block != Block.MAN.value)
        elif(direction == Direction.DOWN_RIGHT):
            next_block = self.env[self.inner_y+1, self.inner_x+1]
            return (next_block != Block.WALL.value and
                    next_block != Block.DIRECTION_DOWN.value and
                    next_block != Block.DIRECTION_LEFT.value and
                    next_block != Block.DIRECTION_RIGHT.value and
                    next_block != Block.DIRECTION_UP.value and
                    next_block != Block.WISDOM_MAN.value and
                    next_block != Block.MAN.value)
