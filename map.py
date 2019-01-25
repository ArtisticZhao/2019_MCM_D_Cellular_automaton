# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
import random
import time

from people import People
from emun_def import Block


class Map(object):
    def __init__(self, n):
        self.fig = plt.figure()
        plt.ion()  # 打开交互模式
        plt.show()
        self.map = np.zeros((n, n))
        # 添加边框
        self.map[0, :] = Block.WALL.value
        self.map[n-1, :] = Block.WALL.value
        self.map[:, 0] = Block.WALL.value
        self.map[:, n-1] = Block.WALL.value
        # 添加大门
        self.map[0, 1:3] = Block.GATE.value
        # 人员列表
        self.mans = list()

    def gen_people(self, num):
        #  随机放入游客在空白的地图中
        while(num != 0):
            x = random.randint(1, self.map.shape[0]-1)
            y = random.randint(1, self.map.shape[0]-1)
            if(self.map[y, x] == 0):
                self.mans.append(People(x, y))
                num = num - 1
                # self.map[y, x] = Block.MAN.value

    def get_env(self, size, man):
        ''' 获得一个人周围环境矩阵
            这时存在几种情况: 非边界, 边界
            无论那种情况,只需要确定环境区域四个顶点位置, 如下图 星号位置
            1*-----------------*2
             |                 |
             |        *        |
             |                 |
            4*-----------------*3
        '''
        max_x = self.map.shape[1]
        max_y = self.map.shape[0]

        x1 = man.x - size if man.x - size > 0 else 0
        y1 = man.y - size if man.y - size > 0 else 0

        # x2 = man.x + size if man.x + size < max_x else max_x
        # y2 = man.y - size if man.y - size > 0 else 0

        x3 = man.x + size if man.x + size < max_x else max_x
        y3 = man.y + size if man.y + size < max_y else max_y

        # x4 = man.x - size if man.x - size > 0 else 0
        # y4 = man.x + size if man.x + size < max_x else max_x
        inner_x = size
        inner_y = size
        if(x1 == 0):
            inner_x = man.x
        if(y1 == 0):
            inner_y = man.y
        return self.map[y1:y3, x1:x3], inner_x, inner_y

    def draw_map(self):
        # 清除原有图像
        self.fig.clf()
        ax = self.fig.add_subplot(111)
        # 绘制所有人
        for man in self.mans:
            self.map[man.y, man.x] = Block.MAN.value
        # interpolation: nearest
        # [具体参数选择]
        # [https://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html] 
        ax.imshow(self.map, interpolation="nearest", cmap=plt.cm.rainbow)
        # shrink 图例表长度
        # plt.colorbar(im, shrink=1)
        plt.draw()
        plt.pause(0.001)

    def test(self):
        for each in self.mans:
            envs = self.get_env(5, each)
            each.policy(envs[0], envs[1], envs[2])


if __name__ == '__main__':
    m = Map(20)
    m.gen_people(10)
    m.draw_map()
    m.test()
    time.sleep(1)

    m.map[0, 0] = 4
    m.draw_map()

    plt.ioff()
    # 图形显示
    plt.show()
