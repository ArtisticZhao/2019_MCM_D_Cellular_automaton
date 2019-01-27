import random
from emun_def import Direction

d_list = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT,
          Direction.UP_LEFT, Direction.UP_RIGHT, Direction.DOWN_LEFT,
          Direction.DOWN_RIGHT]


def weight_choice(weight):
    """
    :param weight: list对应的权重序列
    :return:选取的值在原列表里的索引
    """
    sum_weight = int(sum(weight))
    if(sum_weight == 0):
        # 权重等于0 随机产生一个方向
        return d_list[random.randint(0, len(d_list)-1)]
    t = random.randint(0, sum_weight - 1)
    for i, val in enumerate(weight):
        t -= val
        if t < 0:
            return d_list[i]


def find_op_directions(direction):
    # 相反方向:只身后的三个方向!
    if(direction == Direction.UP):
        return [Direction.DOWN, Direction.DOWN_LEFT, Direction.DOWN_RIGHT]

    if(direction == Direction.DOWN):
        return [Direction.UP, Direction.UP_LEFT, Direction.UP_RIGHT]

    if(direction == Direction.LEFT):
        return [Direction.RIGHT, Direction.UP_RIGHT, Direction.DOWN_RIGHT]

    if(direction == Direction.RIGHT):
        return [Direction.LEFT, Direction.UP_LEFT, Direction.DOWN_LEFT]

    if(direction == Direction.UP_LEFT):
        return [Direction.DOWN_RIGHT, Direction.DOWN, Direction.DOWN_RIGHT]

    if(direction == Direction.UP_RIGHT):
        return [Direction.DOWN_LEFT, Direction.DOWN, Direction.LEFT]

    if(direction == Direction.DOWN_LEFT):
        return [Direction.UP_RIGHT, Direction.UP, Direction.RIGHT]

    if(direction == Direction.DOWN_RIGHT):
        return [Direction.UP_LEFT, Direction.UP, Direction.LEFT]


def is_in_corner(direction):
    if(direction == Direction.UP_LEFT or
       direction == Direction.UP_RIGHT or
       direction == Direction.DOWN_LEFT or
       direction == Direction.DOWN_RIGHT):
        return True
    else:
        return False
