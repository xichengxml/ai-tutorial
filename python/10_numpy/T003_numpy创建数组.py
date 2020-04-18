import numpy as np

# ---------------------------
# @description 使用arange创建数组
# @author xichengxml
# @date 2020/4/18 下午 03:37
# ---------------------------

int_arr = np.arange(1, 10, dtype=int)
print(int_arr)

step_2_arr = np.arange(1, 10, 2)
print(step_2_arr)

# 创建二维数组
two_dim_arr = np.array([np.arange(1, 3), np.arange(4, 6), np.arange(7, 9)])
print(two_dim_arr)

