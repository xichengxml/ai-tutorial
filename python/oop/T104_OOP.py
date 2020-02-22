# ---------------------------
# @description dir()测试
# @author xichengxml
# @date 2020/2/22 下午 12:42
# ---------------------------


class Person:

    def __init__(self, name):
        self.name = name

    def sayName(self):
        print("name: {0}".format(self.name))


obj = object()
print(dir(obj))

person = Person("xichengxml")
print(dir(person))
