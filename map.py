# coding:utf-8

from enum import Enum, unique
import numpy as np
import matplotlib.pyplot as plt
import random
import time

from people import People


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
                self.map[y, x] = Block.MAN.value

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
        # print(((x1, y1), (x3, y3)))
        return self.map[y1:y3, x1:x3]

    def draw_map(self):
        # 清除原有图像
        self.fig.clf()
        ax = self.fig.add_subplot(111)
        # interpolation: nearest
        # [具体参数选择]
        # [https://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html] 
        ax.imshow(self.map, interpolation="nearest", cmap=plt.cm.rainbow)
        # shrink 图例表长度
        # plt.colorbar(im, shrink=1)
        plt.draw()
        plt.pause(0.001)

    def test(self):
        man = self.mans[0]
        print((man.x, man.y))
        print(self.get_env(5, man))


if __name__ == '__main__':
    m = Map(20)
    m.gen_people(10)
    m.draw_map()
    time.sleep(1)

    m.map[0, 0] = 4
    m.draw_map()

    plt.ioff()
    # 图形显示
    plt.show()
