# ---------------------------
# @description 多态
# @author xichengxml
# @date 2020/2/22 下午 01:06
# ---------------------------


class Animal:

    def shout(self):
        print("动物叫了一声")


class Dog(Animal):

    def shout(self):
        print("小狗叫, 汪汪汪")


class Cat(Animal):

    def shout(self):
        print("小猫叫，喵喵喵")


def animalShout(object):

    if isinstance(object, Animal):
        object.shout()
    else:
        print("传入的对象不是动物")


animalShout(Dog())
animalShout(Cat())
animalShout(object())

