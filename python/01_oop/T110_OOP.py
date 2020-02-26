# ---------------------------
# @description 特殊方法和运算符的重载
# @author xichengxml
# @date 2020/2/22 下午 04:52
# ---------------------------


class Person:

    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Person):
            print("{0}--{1}", self.name, other.name)
        else:
            print("非同类对象不能相加")

    def __mul__(self, times):
        if isinstance(times, int):
            print(self.name * times * 2)
        else:
            print("请输入数字型参数")


p1 = Person("xichengxml")
p2 = Person("ooop")
print(p1 + p2)
print(p1 * 3)