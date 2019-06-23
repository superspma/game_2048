import random
from model import *
import copy


class GameCoreController:
    def __init__(self):
        # 定义初始4X4地图
        self.__map = [
            [0] * 4,
            [0] * 4,
            [0] * 4,
            [0] * 4
        ]
        self.__get_all_zero = []  # 存储地图中的空位置
        self.is_change = False  # 判断地图是否移动

    @property
    def map(self):
        return self.__map

    @property
    def is_change(self):
        return self.__is_change

    @is_change.setter
    def is_change(self, value):
        self.__is_change = value

    def __get_total_zero(self):
        """
        获取地图中所有空位置
        :return:
        """
        self.__get_all_zero.clear()
        for x in range(4):
            for y in range(4):
                if self.__map[x][y] == 0:
                    self.__get_all_zero.append(Location(x, y))

    def generate_new_number(self):
        """
        生成新数字并添加到地图中
        :return:
        """
        self.__get_total_zero()
        if len(self.__get_all_zero) == 0:
            return
        site = random.choice(self.__get_all_zero)
        new_num = 4 if random.choice(range(10)) == 1 else 2  # 10%的概率生成数字4，90%的概率生成2
        self.__map[site.index_r][site.index_c] = new_num
        self.__get_all_zero.remove(site)

    # ----------------测试---------------------
    # a = GameCoreController()
    # a.get_total_zero()
    # a.generate_new_number()
    # print(a.map)

    def __zero_to_end(self, list_target):
        # 删除0元素,再末尾增加.
        for i in range(len(list_target) - 1, -1, -1):
            if list_target[i] == 0:
                del list_target[i]
                list_target.append(0)
        return list_target

    def __merge(self, list_target):
        self.__zero_to_end(list_target)
        # 如果相邻且相同 # [2,0,0,2] -->  [2,2,0,0]
        for i in range(len(list_target) - 1):
            if list_target[i] == list_target[i + 1]:
                # 合并[2,2,2,0] ->[4,2,2,0] --> [4,2,0,0]
                list_target[i] += list_target[i + 1]
                del list_target[i + 1]
                list_target.append(0)

    def move(self, dir):
        """
        根据指令移动整个地图中的数字
        :param dir: 移动方向
        :return:
        """
        start_map = copy.deepcopy(self.__map)
        if dir == Direction.up:
            self.__move_up()
        if dir == Direction.down:
            self.__move_down()
        if dir == Direction.left:
            self.__move_left()
        if dir == Direction.right:
            self.__move_right()
        self.__is_change = start_map != self.__map

    def __move_left(self):
        """
        向上移动
        :return:
        """
        # 将每行(从左向右获取行数据)传递给合并函数
        for row in self.__map:
            # 传递给merge函数的是二维列表中的元素(一维列表对象地址)
            # 函数都是操作对象,所以无需通过返回值拿到操作结果.
            self.__merge(row)

    def __move_right(self):
        """
        向右移动
        :return:
        """
        # 将每行(从右向左获取行数据)传递给合并函数
        for i in range(len(self.__map)):
            # map[0][::-1] 从右向左获取行数据(新列表)
            list_merge = self.__map[i][::-1]
            self.__merge(list_merge)
            # 将合并后的结果,从右向左获还给二维列表
            self.__map[i][::-1] = list_merge

    def __move_up(self):
        """
        向下移动
        :return:
        """
        # 00  10  20  30
        # 01  11  21  31
        for c in range(4):
            list_merge = []
            for r in range(4):
                list_merge.append(self.__map[r][c])

            self.__merge(list_merge)

            for r in range(4):
                self.__map[r][c] = list_merge[r]

    def __move_down(self):
        """
        向上移动
        :return:
        """
        # 30  20  10  00
        for c in range(4):
            list_merge = []
            for r in range(3, -1, -1):
                list_merge.append(self.__map[r][c])

            self.__merge(list_merge)

            # list_merge(从左到右) 赋值给 二维列表(从下到上)
            for r in range(3, -1, -1):  # 3 2 1 0
                self.__map[r][c] = list_merge[3 - r]

    def is_game_over(self):
        """
        判断游戏是否结束
        :return: bool
        """
        self.__get_total_zero()
        if len(self.__get_all_zero) > 0:  # 地图中是否存在空位
            return False
        # 相邻数字是否存在相同的
        for x in range(4):
            for y in range(3):
                if self.__map[x][y] == self.__map[x][y + 1] or self.__map[y][x] == self.__map[y + 1][x]:
                    return False
        return True  # 如果以上都不满足则返回Ture

# a = GameCoreController()
# a.__get_total_zero()
# a.generate_new_number()
# a.is_geme_over()

# 测试
# double_list = [
#     [2, 2, 0, 2],
#     [0, 2, 0, 4],
#     [2, 0, 4, 2],
#     [0, 4, 2, 2],
# ]
# move_down(double_list)
# print(double_list)
# move_right(double_list)
# print(double_list)
