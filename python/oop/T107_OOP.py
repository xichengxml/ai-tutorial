# ---------------------------
# @description mro()方法
# @author xichengxml
# @date 2020/2/22 下午 12:51
# ---------------------------


class Mother:

    def eat(self):
        print("mother is eating")


class Father:

    def eat(self):
        print("father is eating")


class Son(Father, Mother):

    def __init__(self, name):
        self.name = name


son = Son("xichengxml")
print(Son.mro())
# 按继承顺序从左往右继承方法
print(son.eat())