#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

# 3D的散点图也是常常用来查看空间样本分布的一种手段，并且画起来比表面图和网线图更加简单

# 这个例子中，为了方便，直接先采样了一堆3维的正态分布样本，保证方向上的均匀性。
# 然后归一化，让每个样本到原点的距离为1，相当于得到了一个均匀分布在球面上的样本。
# 再接着把每个样本都乘上一个均匀分布随机数的开3次方，这样就得到了在球体内均匀分布的样本，
# 最后根据判别平面3x+2y-z-1=0对平面两侧样本用不同的形状和颜色画出，图像如下

np.random.seed(42)

# 采样个数500
n_samples = 500
dim = 3

# 先生成一组3维正态分布数据，数据方向完全随机
# 若随机变量X服从一个数学期望为μ、方差为σ^2的正态分布，记为N(μ，σ^2)。
# 其概率密度函数为正态分布的期望值μ决定了其位置，其标准差σ决定了分布的幅度。
# 当μ = 0,σ = 1时的正态分布是标准正态分布。
samples = np.random.multivariate_normal(
    np.zeros(dim),
    np.eye(dim),
    n_samples
)

# 通过把每个样本到原点距离和均匀分布吻合得到球体内均匀分布的样本
# w.shape[0]返回的是w的行数
# np.power求n次方
for i in range(samples.shape[0]):
    r = np.power(np.random.random(), 1.0 / 3.0)
    samples[i] *= r / np.linalg.norm(samples[i])

upper_samples = []
lower_samples = []

for x, y, z in samples:
    # 3x+2y-z=1作为判别平面
    if z > 3 * x + 2 * y - 1:
        upper_samples.append((x, y, z))
    else:
        lower_samples.append((x, y, z))

fig = plt.figure('3D scatter plot')
ax = fig.add_subplot(111, projection='3d')

uppers = np.array(upper_samples)
lowers = np.array(lower_samples)
print(uppers[:, 0])

# 用不同颜色不同形状的图标表示平面上下的样本
# 判别平面上半部分为红色圆点，下半部分为绿色三角
ax.scatter(uppers[:, 0], uppers[:, 1], uppers[:, 2], c='r', marker='o')
ax.scatter(lowers[:, 0], lowers[:, 1], lowers[:, 2], c='g', marker='^')

plt.show()