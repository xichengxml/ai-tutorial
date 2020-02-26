# ---------------------------
# @description 特殊属性
# @author xichengxml
# @date 2020/2/22 下午 05:02
# ---------------------------


class Father:
    pass


class Mother:
    pass


class Son(Father, Mother):

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("say something")


son = Son("xichengxml")
print("dir: {0}".format(dir(son)))
print("__dict__: {0}".format(son.__dict__))
print("__class__: {0}".format(son.__class__))

print("mro: {0}".format(Son.mro()))
print("__subclasses__: {0}".format(Father.__subclasses__()))
