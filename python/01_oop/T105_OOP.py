# ---------------------------
# @description 重写__str__方法
# @author xichengxml
# @date 2020/2/21 上午 11:24
# ---------------------------


class Person01:

    def __init__(self, name):
        self.name = name


class Person02:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Person02: name={0}".format(self.name)


p1 = Person01("xichengxml")
p2 = Person02("xichengxml")
print(p1)
print(p2)
