import numpy as np

# ---------------------------
# @description array创建数组
# @author xichengxml
# @date 2020/4/18 下午 02:52
# ---------------------------


# 一维数组
one_dim_arr = np.array([1, 2, 3])
print(type(one_dim_arr))


# 二维数组
two_dim_arr = np.array([[1, 2, 3], [4, 5, 6]])
print(type(two_dim_arr))


# 指定数据类型
float_arr = np.array([1, 2, 3], dtype=float)
print(float_arr)


# 指定维度
target_dim_arr = np.array([1, 2, 3], ndmin=3)
print(target_dim_arr)



