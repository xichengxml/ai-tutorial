import importlib

# ---------------------------
# @description 动态导入
# @author xichengxml
# @date 2020/3/4 下午 08:22
# ---------------------------


# 不建议这种方式
m1 = __import__("math")
print(m1.pi)

# 建议方式
m2 = importlib.import_module("math")
print(m2.pi)
