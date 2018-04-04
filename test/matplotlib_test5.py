#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 这段代码中第一个例子是读取一个本地图片并显示，
# 第二个例子中直接把上小节中反傅里叶变换生成的矩阵作为图像拿过来，原图和经过乘以3再加4变换的图直接绘制了两个形状一样，但是值的范围不一样的图案。
# 显示的时候imshow会自动进行归一化，把最亮的值显示为纯白，最暗的值显示为纯黑。
# 这是一种非常方便的设定，尤其是查看深度学习中某个卷积层的响应图时

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

n_grids = 51  # x-y平面的格点数
c = n_grids // 2  # 中心位置
nf = 2  # 低频成分的个数

x = np.linspace(0, 1, n_grids)
y = np.linspace(0, 1, n_grids)

X, Y = np.meshgrid(x, y)

spectrum = np.zeros((n_grids, n_grids), dtype=np.complex)

noise = [np.complex(x, y) for x, y in np.random.uniform(-1, 1, ((2 * nf + 1) ** 2 // 2, 2))]

noisy_block = np.concatenate((noise, [0j], np.conjugate(noise[::-1])))

spectrum[c - nf:c + nf + 1, c - nf:c + nf + 1] = noisy_block.reshape((2 * nf + 1, 2 * nf + 1))

Z = np.real(np.fft.ifft2(np.fft.ifftshift(spectrum)))



# 读取一张小白狗的照片并显示
plt.figure('dog picture')
little_dog_img = plt.imread('luckydog.jpeg')
plt.imshow(little_dog_img)

# Z是上小节生成的随机图案，img0就是Z，img1是Z做了个简单的变换
img0 = Z
img1 = 3 * Z + 4

# cmap指定为'gray'用来显示灰度图
fig = plt.figure('Auto Normalized Visualization')
ax0 = fig.add_subplot(121)
ax0.imshow(img0, cmap='gray')

ax1 = fig.add_subplot(122)
ax1.imshow(img1, cmap='gray')

plt.show()