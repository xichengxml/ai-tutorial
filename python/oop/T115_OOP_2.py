# ---------------------------
# @description 把工厂模式改造成单例的
# @author xichengxml
# @date 2020/2/26 下午 04:05
# ---------------------------


class CarFactory:

    __obj = None
    __initFlag = True

    def createCar(self):
        pass

    def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = object.__new__(cls)
        return cls.__obj

    def __init__(self):
        if CarFactory.__initFlag:
            print("init..")
            CarFactory.__initFlag = False


f1 = CarFactory()
f2 = CarFactory()
print(f1)
print(f2)