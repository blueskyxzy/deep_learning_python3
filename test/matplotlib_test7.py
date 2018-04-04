#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 快速傅里叶变换
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, 30)  # 创建一个包含30个点的余弦波信号
wave = np.cos(x)
transformed = np.fft.fft(wave)  # 使用fft函数对余弦波信号进行傅里叶变换。
print(np.all(np.abs(np.fft.ifft(transformed) - wave) < 10 ** -9))  # 对变换后的结果应用ifft函数，应该可以近似地还原初始信号。

plt.subplot(221)
plt.plot(wave)
plt.title('原余弦波')

plt.subplot(222)
plt.plot(transformed)  # 使用Matplotlib绘制变换后的信号。
plt.title('变fft变换后的信号')

plt.subplot(223)
plt.plot(np.fft.ifft(transformed))
plt.title('ifft变换回的信号')

plt.show()
