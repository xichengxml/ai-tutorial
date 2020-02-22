# ---------------------------
# @description super()获得父类定义
# @author xichengxml
# @date 2020/2/22 下午 01:02
# ---------------------------


class Father:

    def eat(self):
        print("father is eating")


class Son(Father):

    def eat(self):
        super().eat()
        print("son is eating")


son = Son()
son.eat()
