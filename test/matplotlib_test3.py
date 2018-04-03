#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# 3D图标必须的模块，project='3d'的定义
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(42)

n_grids = 51  # x-y平面的格点数
c = n_grids // 2  # 中心位置
nf = 2  # 低频成分的个数

# 生成格点
x = np.linspace(0, 1, n_grids)
y = np.linspace(0, 1, n_grids)

# x和y是长度为n_grids的array
# meshgrid会把x和y组合成n_grids*n_grids的array，X和Y对应位置就是所有格点的坐标

# meshgrid的作用是根据传入的两个一维数组参数生成两个数组元素的列表。
# 如果第一个参数是xarray，维度是xdimesion，第二个参数是yarray，维度是ydimesion。
# 那么生成的第一个二维数组是以xarray为行，ydimesion行的向量；而第二个二维数组是以yarray的转置为列，xdimesion列的向量。
X, Y = np.meshgrid(x, y)

# 生成一个0值的傅里叶谱
# np.zeros生成相应大小的零矩阵
spectrum = np.zeros((n_grids, n_grids), dtype=np.complex)

# 生成一段噪音，长度是(2*nf+1)**2/2
# np.random.uniform  从一个均匀分布[low,high)中随机采样，注意定义域是左闭右开，即包含low，不包含high.
noise = [np.complex(x, y) for x, y in np.random.uniform(-1, 1, ((2 * nf + 1) ** 2 // 2, 2))]

# 傅里叶频谱的每一项和其共轭关于中心对称
# numpy提供了numpy.concatenate((a1,a2,...), axis=0)函数。能够一次完成多个数组的拼接。其中a1,a2,...是数组类型的参数
# conjugate()   返回该复数的共轭复数
# [x:y:z]切片索引,x是左端,y是右端,z是步长,在[x,y)区间从左到右每隔z取值,默认z为1可以省略z参数.
# 步长的负号就是反向,从右到左取值.
# python的[::-1]那就是nohtyp
noisy_block = np.concatenate((noise, [0j], np.conjugate(noise[::-1])))

# 将生成的频谱作为低频成分
# reshape（）是数组对象中的方法，用于改变数组的形状
spectrum[c - nf:c + nf + 1, c - nf:c + nf + 1] = noisy_block.reshape((2 * nf + 1, 2 * nf + 1))

# 进行反傅里叶变换
Z = np.real(np.fft.ifft2(np.fft.ifftshift(spectrum)))

# 创建图表
fig = plt.figure('3D surface & wire')

# 第一个子图，surface图
ax = fig.add_subplot(1, 2, 1, projection='3d')

# alpha定义透明度，cmap是color map
# rstride和cstride是两个方向上的采样，越小越精细，lw是线宽
ax.plot_surface(X, Y, Z, alpha=0.7, cmap='jet', rstride=1, cstride=1, lw=0)

# 第二个子图，网线图
ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=3, cstride=3, lw=0.5)

plt.show()