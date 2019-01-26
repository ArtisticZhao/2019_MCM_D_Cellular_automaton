# coding:utf-8

import numpy as np
from emun_def import Direction, Block, Weight

from functions import d_list, weight_choice, find_op


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

    def move(self, direction):
        if(direction == Direction.UP):
            self.current_direction = Direction.UP
            if(self.env[self.inner_y-1, self.inner_x] == Block.EMPTY.value):
                self.y = self.y - 1
                self.env[self.inner_y, self.inner_x] = Block.EMPTY.value
                self.env[self.inner_y-1, self.inner_x] = Block.MAN.value
            elif(self.env[self.inner_y-1, self.inner_x] == Block.GATE.value):
                self.y = self.y - 1
                self.env[self.inner_y, self.inner_x] = Block.EMPTY.value

        elif(direction == Direction.DOWN):
            self.current_direction = Direction.DOWN
            if(self.env[self.inner_y+1, self.inner_x] == Block.EMPTY.value):
                self.y = self.y + 1
                self.env[self.inner_y, self.inner_x] = Block.EMPTY.value
                self.env[self.inner_y+1, self.inner_x] = Block.MAN.value
            elif(self.env[self.inner_y+1, self.inner_x] == Block.GATE.value):
                self.y = self.y + 1
                self.env[self.inner_y, self.inner_x] = Block.EMPTY.value

        elif(direction == Direction.LEFT):
            self.current_direction = Direction.LEFT
            if(self.env[self.inner_y, self.inner_x-1] == Block.EMPTY.value):
                self.x = self.x - 1
                self.env[self.inner_y, self.inner_x] = Block.EMPTY.value
                self.env[self.inner_y, self.inner_x-1] = Block.MAN.value
            elif(self.env[self.inner_y, self.inner_x-1] == Block.GATE.value):
                self.x = self.x - 1
                self.env[self.inner_y, self.inner_x] = Block.EMPTY.value
        elif(direction == Direction.RIGHT):
            self.current_direction = Direction.RIGHT
            if(self.env[self.inner_y, self.inner_x+1] == Block.EMPTY.value):
                self.x = self.x + 1
                self.env[self.inner_y, self.inner_x] = Block.EMPTY.value
                self.env[self.inner_y, self.inner_x+1] = Block.MAN.value
            elif(self.env[self.inner_y, self.inner_x+1] == Block.GATE.value):
                self.x = self.x + 1
                self.env[self.inner_y, self.inner_x] = Block.EMPTY.value

        elif(direction == Direction.UP_LEFT):
            self.current_direction = Direction.UP_LEFT
            if(self.env[self.inner_y-1, self.inner_x-1] == Block.EMPTY.value):
                self.y = self.y - 1
                self.x = self.x - 1
                self.env[self.inner_y, self.inner_x] = Block.EMPTY.value
                self.env[self.inner_y-1, self.inner_x-1] = Block.MAN.value
            elif(self.env[self.inner_y-1, self.inner_x-1] == Block.GATE.value):
                self.y = self.y - 1
                self.x = self.x - 1
                self.env[self.inner_y, self.inner_x] = Block.EMPTY.value
        elif(direction == Direction.UP_RIGHT):
            self.current_direction = Direction.UP_RIGHT
            if(self.env[self.inner_y-1, self.inner_x+1] == Block.EMPTY.value):
                self.y = self.y - 1
                self.x = self.x + 1
                self.env[self.inner_y, self.inner_x] = Block.EMPTY.value
                self.env[self.inner_y-1, self.inner_x+1] = Block.MAN.value
            elif(self.env[self.inner_y-1, self.inner_x+1] == Block.GATE.value):
                self.y = self.y - 1
                self.x = self.x + 1
                self.env[self.inner_y, self.inner_x] = Block.EMPTY.value
        elif(direction == Direction.DOWN_LEFT):
            self.current_direction = Direction.DOWN_LEFT
            if(self.env[self.inner_y+1, self.inner_x-1] == Block.EMPTY.value):
                self.y = self.y + 1
                self.x = self.x - 1
                self.env[self.inner_y, self.inner_x] = Block.EMPTY.value
                self.env[self.inner_y+1, self.inner_x-1] = Block.MAN.value
            elif(self.env[self.inner_y+1, self.inner_x-1] == Block.GATE.value):
                self.y = self.y + 1
                self.x = self.x - 1
                self.env[self.inner_y, self.inner_x] = Block.EMPTY.value
        elif(direction == Direction.DOWN_RIGHT):
            self.current_direction = Direction.DOWN_RIGHT
            if(self.env[self.inner_y+1, self.inner_x+1] == Block.EMPTY.value):
                self.y = self.y + 1
                self.x = self.x + 1
                self.env[self.inner_y, self.inner_x] = Block.EMPTY.value
                self.env[self.inner_y+1, self.inner_x+1] = Block.MAN.value
            elif(self.env[self.inner_y+1, self.inner_x+1] == Block.GATE.value):
                self.y = self.y + 1
                self.x = self.x + 1
                self.env[self.inner_y, self.inner_x] = Block.EMPTY.value

    def policy(self, env_mat, inner_x, inner_y):
        self.env = env_mat
        self.inner_x = inner_x
        self.inner_y = inner_y
        is_hit_wall = False
        # 计算权值
        weights = list()
        # man go up
        if(env_mat[inner_y-1, inner_x] != Block.WALL.value):
            env_block = env_mat[0:inner_y, :]
            weight = 0
            find_block = np.where(env_block == Block.GATE.value)
            weight = weight + find_block[0].size * Weight.GATE.value
            find_block = np.where(env_block == Block.MAN.value)
            weight = weight + find_block[0].size * Weight.MAN.value
            weights.append(weight/2)
        else:
            weights.append(0)
            is_hit_wall = True

        # man go Down
        if(env_mat[inner_y+1, inner_x] != Block.WALL.value):
            env_block = env_mat[inner_y+1:, :]
            weight = 0
            find_block = np.where(env_block == Block.GATE.value)
            weight = weight + find_block[0].size * Weight.GATE.value
            find_block = np.where(env_block == Block.MAN.value)
            weight = weight + find_block[0].size * Weight.MAN.value
            weights.append(weight/2)
        else:
            weights.append(0)
            is_hit_wall = True

        # man go Left
        if(env_mat[inner_y, inner_x-1] != Block.WALL.value):
            env_block = env_mat[:, 0:inner_x]
            weight = 0
            find_block = np.where(env_block == Block.GATE.value)
            weight = weight + find_block[0].size * Weight.GATE.value
            find_block = np.where(env_block == Block.MAN.value)
            weight = weight + find_block[0].size * Weight.MAN.value
            weights.append(weight/2)
        else:
            weights.append(0)
            is_hit_wall = True

        # man go Right
        if(env_mat[inner_y, inner_x+1] != Block.WALL.value):
            env_block = env_mat[:, inner_x+1:]
            weight = 0
            find_block = np.where(env_block == Block.GATE.value)
            weight = weight + find_block[0].size * Weight.GATE.value
            find_block = np.where(env_block == Block.MAN.value)
            weight = weight + find_block[0].size * Weight.MAN.value
            weights.append(weight/2)
        else:
            weights.append(0)
            is_hit_wall = True

        # man go UP_LEFT
        if(env_mat[inner_y-1, inner_x-1] != Block.WALL.value):
            env_block = env_mat[0:inner_y, 0:inner_x]
            weight = 0
            find_block = np.where(env_block == Block.GATE.value)
            weight = weight + find_block[0].size * Weight.GATE.value
            find_block = np.where(env_block == Block.MAN.value)
            weight = weight + find_block[0].size * Weight.MAN.value
            weights.append(weight)
        else:
            weights.append(0)
            is_hit_wall = True

        # man go UP_RIGHT
        if(env_mat[inner_y-1, inner_x+1] != Block.WALL.value):
            env_block = env_mat[0:inner_y, inner_x+1:]
            weight = 0
            find_block = np.where(env_block == Block.GATE.value)
            weight = weight + find_block[0].size * Weight.GATE.value
            find_block = np.where(env_block == Block.MAN.value)
            weight = weight + find_block[0].size * Weight.MAN.value
            weights.append(weight)
        else:
            weights.append(0)
            is_hit_wall = True

        # man go DOWN_LEFT
        if(env_mat[inner_y+1, inner_x-1] != Block.WALL.value):
            env_block = env_mat[inner_y+1:, 0:inner_x]
            weight = 0
            find_block = np.where(env_block == Block.GATE.value)
            weight = weight + find_block[0].size * Weight.GATE.value
            find_block = np.where(env_block == Block.MAN.value)
            weight = weight + find_block[0].size * Weight.MAN.value
            weights.append(weight)
        else:
            weights.append(0)
            is_hit_wall = True

        # man go DOWN_RIGHT
        if(env_mat[inner_y+1, inner_x+1] != Block.WALL.value):
            env_block = env_mat[inner_y+1:, inner_x+1:]
            weight = 0
            find_block = np.where(env_block == Block.GATE.value)
            weight = weight + find_block[0].size * Weight.GATE.value
            find_block = np.where(env_block == Block.MAN.value)
            weight = weight + find_block[0].size * Weight.MAN.value
            weights.append(weight)
        else:
            weights.append(0)
            is_hit_wall = True
        # 权值计算完毕
        # 倾向于向同一个方向
        if(self.current_direction is not None and not is_hit_wall):
            index = d_list.index(self.current_direction)
            weights[index] = weights[index] + Weight.SAME_DIRECTION.value
        if(self.current_direction is not None):
            index = d_list.index(find_op(self.current_direction))
            weights[index] = 0  # 绝不回头
        go_direction = weight_choice(weights)
        self.move(go_direction)
