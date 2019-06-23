class Location:
    """
    对行列坐标数据进行封装
    """
    def __init__(self, x, y):
        self.index_r = x
        self.index_c = y

    @property
    def index_r(self):
        return self.__index_r

    @index_r.setter
    def index_r(self, value):
        self.__index_r = value

    @property
    def index_c(self):
        return self.__index_c

    @index_c.setter
    def index_c(self, value):
        self.__index_c = value


class Direction:
    """
    封装方向
    """
    up = "w"
    down = "s"
    left = "a"
    right = "d"
