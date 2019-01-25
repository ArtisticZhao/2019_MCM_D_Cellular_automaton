# coding:utf-8
import numpy as np
from emun_def import Direction, Block


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

    def policy(self, env_mat, inner_x, inner_y):
        # max_x = env_mat.shape[1]
        # max_y = env_mat.shape[0]
        if(env_mat[inner_y, inner_x] != Block.MAN.value):
            print("算法错误, 未找到周围环境!")
        # find gate
        res = np.where(env_mat == Block.GATE.value)
        if(res[0].size != 0):
            # find gate !
            gates = list(zip(list(res[0]), list(res[1])))  # y,x
            print(env_mat)
            print(gates)
