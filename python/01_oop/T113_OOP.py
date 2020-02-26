# ---------------------------
# @description 代码复用的两种方式：继承和组合
# @author xichengxml
# @date 2020/2/26 下午 02:10
# ---------------------------


class Animal:

    def shout(self):
        print("动物会叫")


class Cat(Animal):
    pass


cat = Cat()
cat.shout()


class Bed:

    def sleep(self):
        print("床能用来睡觉")


class House:

    def __init__(self, bed):
        self.bed = bed


bed = Bed()
house = House(bed)
house.bed.sleep()

