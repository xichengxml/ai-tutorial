import copy
# ---------------------------
# @description 测试浅复制和深复制
# @author xichengxml
# @date 2020/2/26 上午 11:00
# ---------------------------


class CPU:

    def print(self):
        print("CPU address: {0}".format(self))


class Screen:

    def print(self):
        print("Screen address: {0}".format(self))


class MobilePhone:

    def __init__(self, cpu, screen):
        self.cpu = cpu
        self.screen = screen

    def print(self):
        print("MobilePhone address: {0}".format(self))


# 测试对象复制
c1 = CPU()
c2 = c1
print("c1: {0}".format(c1))
print("c2: {0}".format(c2))

# 测试浅复制
s1 = Screen()
m1 = MobilePhone(c1, s1)
m2 = copy.copy(m1)
print("m1: {0}, m1.cpu: {1}, m1.screen: {2}".format(m1, m1.cpu, m1.screen))
print("m2: {0}, m2.cpu: {1}, m2.screen: {2}".format(m2, m2.cpu, m2.screen))

# 测试深复制
m3 = copy.deepcopy(m1)
print("m1: {0}, m1.cpu: {1}, m1.screen: {2}".format(m1, m1.cpu, m1.screen))
print("m3: {0}, m3.cpu: {1}, m3.screen: {2}".format(m3, m3.cpu, m3.screen))


