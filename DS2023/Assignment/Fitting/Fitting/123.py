import numpy as np
from scipy.interpolate import BSpline
import matplotlib.pyplot as plt

# 准备二维数据点
data = np.loadtxt("ssn.dat")
x_data = data[:,0] + (data[:,1]-0.5)/12.0 # 输入数据点的x坐标,生成0.5偏移
y_data = data[:,2] # 输入数据点的y坐标

# 创建三阶等距B样条曲线拟合器
k = 4  # 三阶
t = np.linspace(0, len(x_data) - k, len(x_data) - k + 1)  # 节点序列
spl_x = BSpline(t, x_data, k)
spl_y = BSpline(t, y_data, k)

# 生成拟合曲线上的点
t_new = np.linspace(0, len(x_data) - k, 1000)  # 用于插值的新t值
x_new = spl_x(t_new)
x_new=x_new[8:-8]
y_new = spl_y(t_new)
y_new=y_new[8:-8]
# 绘制原始数据和拟合曲线
plt.figure(figsize=(8, 6))
plt.plot(x_data, y_data, 'ro')
plt.plot(x_new, y_new, 'b-')
plt.xlabel('Year')
plt.ylabel('Temperature(C)')
plt.title('Cubic Bspline')
plt.legend()
plt.grid(True)
plt.show()
