# ---------------------------
# @description 单例模式
# @author xichengxml
# @date 2020/2/26 下午 04:00
# ---------------------------


class MySingleton:

    __obj = None
    __initFlag = True

    def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = object.__new__(cls)
        return cls.__obj

    def __init__(self, name):
        if MySingleton.__initFlag:
            print('MySingleton init...')
            self.name = name
            MySingleton.__initFlag = False


m1 = MySingleton('aa')
m2 = MySingleton('bb')
print(m1)
print(m2)
