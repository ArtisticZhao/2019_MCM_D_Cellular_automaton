# coding:utf-8
from map import Map
from matplotlib import pyplot as plt


def run_manul(file_name, stop):
    m = Map(20, 3)
    m.load_map(file_name)
    m.gen_people_by_density(0.2)
    m.check_map()
    m.draw_map()
    plt.savefig('0.png')
    # input(':')
    m.everybody_move(stop)

    plt.ioff()
    # 图形显示
    plt.show()


def test_door():
    for i in range(1, 40):
        m = Map(55, i)
        m.draw_map()
        m.check_map()

        m.gen_people_by_density(0.2)
        m.draw_map()
        time = m.everybody_move(False)
        print(str(i) + " " + str(time))


def test_density():
    for i in [20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]:
        m = Map(40, 3)
        m.draw_map()
        m.check_map()

        m.gen_people_by_density(i/100)
        m.draw_map()
        time = m.everybody_move(False)
        print(str(i) + " " + str(time))


def test_room_size():
    for i in range(40, 50):
        m = Map(i, 3)
        m.draw_map()
        m.gen_people_by_density(0.2)
        m.check_map()
        m.draw_map()
        time = m.everybody_move(False)
        print(str(i) + " " + str(time))


if __name__ == '__main__':
    # test_gate_pos()
    run_manul('maps/m0.csv', True)
    # test_door()
    # test_room_size()
    # m = Map(20, 3)
    # m.draw_map()
    # m.gen_people_by_density(0.2)
    # m.check_map()
    # m.draw_map()
    # time = m.everybody_move(False)


# def test_gate_pos():
#     for i in range(-15, 15):
#         m = Map(40, 5, i)
#         m.draw_map()
#         m.gen_people_by_density(0.2)
#         m.check_map()
#         m.draw_map()
#         time = m.everybody_move(False)
#         print(str(i) + " " + str(time))
