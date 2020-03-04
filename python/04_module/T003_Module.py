# ---------------------------
# @description import用法
# @author xichengxml
# @date 2020/3/4 下午 07:39
# ---------------------------


# 无论一个模块被导入多少次，内存中都只有一份
import math
print(id(math))
import math
print(id(math))
import math as m
print(id(m))