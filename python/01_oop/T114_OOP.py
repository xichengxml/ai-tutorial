# ---------------------------
# @description 工厂模式
# @author xichengxml
# @date 2020/2/26 下午 03:39
# ---------------------------


class CarFactory:

    def createCar(self, brand):
        if '奔驰' == brand:
            return Benz()
        elif '奥迪' == brand:
            return Audi()
        elif '比亚迪' == brand:
            return BYD()
        else:
            print("不支持该品牌")


class Benz:

    def __init__(self):
        print('Benz init...')


class Audi:

    def __init__(self):
        print('Audi init...')


class BYD:

    def __init__(self):
        print('BYD init...')


factory = CarFactory()
factory.createCar('奔驰')
factory.createCar('奥迪')
factory.createCar('比亚迪')
factory.createCar('宝马')

