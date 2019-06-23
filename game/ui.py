from bll import GameCoreController
from model import Direction
import os


class GameConsoleView:
    """
    定义实例变量
    """
    def __init__(self):
        self.__controller = GameCoreController()

    def game_start(self):
        """
        游戏开始
        :return:
        """
        self.__controller.generate_new_number()
        self.__controller.generate_new_number()
        self.__print_map()

    def __print_map(self):
        """
        打印地图
        :return:
        """
        os.system("clear")  # 清空控制台
        for item in self.__controller.map:
            for obj in item:
                print("\033[32;1m%d\033[0m" % obj, end="\t")
            print()

    # ------------测试----------------
    # a = GameConsoleView()
    # a.game_start()

    def update(self):
        """
        移动并跟新地图
        :return:
        """
        while True:
            self.__move_map()
            if self.__controller.is_change:
                self.__controller.generate_new_number()
                self.__print_map()
                if self.__controller.is_game_over():
                    print("\033[31;1m游戏结束!\033[0m")
                    break

    def __move_map(self):
        """
        根据输入的指令，进行移动
        :return:
        """
        move_dir = input("\033[34;1m请输入移动方向(wasd):\033[0m")
        if move_dir == "w":
            self.__controller.move(Direction.up)
        if move_dir == "s":
            self.__controller.move(Direction.down)
        if move_dir == "a":
            self.__controller.move(Direction.left)
        if move_dir == "d":
            self.__controller.move(Direction.right)


# ------------测试---------------------a = GameConsoleView()
# # a.game_start()
# # a.updat
# e()
