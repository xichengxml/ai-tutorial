import numpy as np
import math

# ---------------------------
# @description 
# @author xichengxml
# @date 2020/4/18 下午 02:46
# ---------------------------


arr = [1, 4, 9]

# 使用普通方式对所有列表元素开方
sqrt_arr = []
for i in arr:
    tmp = int(math.sqrt(i))
    sqrt_arr.append(tmp)
print(sqrt_arr)

# 使用numpy操作
np_sqrt_arr = np.sqrt(arr)
print(np_sqrt_arr)
