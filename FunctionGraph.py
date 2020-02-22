import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# @description 
# @author xichengxml
# @date 2020/2/11 上午 07:19
# ---------------------------


x = np.linspace(-20, 20, 100)
y = x * x
plt.plot(x, y)

plt.title('y = x ^ 2')
plt.xlabel('x')
plt.ylabel('y')
plt.show()