# coding:utf-8
from map import Map
from matplotlib import pyplot as plt


if __name__ == '__main__':
    m = Map(20)
    m.load_map('l0.csv')
    m.check_map()

    m.gen_people_by_density(0.2)
    m.draw_map()
    m.everybody_move()

    plt.ioff()
    # 图形显示
    plt.show()
