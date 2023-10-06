import numpy as np
import matplotlib.pyplot as plt

def compute_basis_function(t, i, p, knots):
    if p == 0:
        if knots[i] <= t < knots[i+1]:
            return 1
        else:
            return 0
    else:
        numerator1 = t - knots[i]
        denominator1 = knots[i+p] - knots[i]
        numerator2 = knots[i+p+1] - t
        denominator2 = knots[i+p+1] - knots[i+1]
        N1 = 0 if denominator1 == 0 else (numerator1 / denominator1) * compute_basis_function(t, i, p-1, knots)
        N2 = 0 if denominator2 == 0 else (numerator2 / denominator2) * compute_basis_function(t, i+1, p-1, knots)
        return N1 + N2

def evaluate_bspline(t, control_points, knots, p):
    n = len(control_points) - 1
    result = 0
    for i in range(n+1):
        basis = compute_basis_function(t, i, p, knots)
        result += control_points[i] * basis
    return result

# 准备数据
data = np.loadtxt("ssn.dat")
x = data[:,0] + (data[:,1]-0.5)/12.0  # 输入数据点的x坐标
y = data[:,2]  # 输入数据点的y坐标

# 创建节点序列
k = 3  # 三阶
n = len(x) - 1
knots = np.concatenate(([0] * k, np.arange(0, n - k + 2), [n - k + 1] * k))

# 生成曲线上的点
x_new = data[:,0] + (data[:,1]-0.5)/12.0
y_new = [evaluate_bspline(t, y, knots, k) for t in x_new]

n = len(y)
m = len()
print("dim x:", m,", dim y:", n)

# Observation matrix
Hmat = np.zeros(( n, m ))
for i in range(n):
  for j in range(m):
    Hmat[i,j] = bspline3( zobs[i], znode[j], zintvl )





# 绘制原始数据和拟合曲线
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'ro', label='raw')
plt.plot(x_new, y_new, 'b-', label='ni')
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.legend()
plt.grid(True)
plt.show()
