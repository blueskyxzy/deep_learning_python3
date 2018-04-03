#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# 3D图标必须的模块，project='3d'的定义
from mpl_toolkits.mplot3d import Axes3D
# 测试
nf = 2

noise = [np.complex(x, y) for x, y in np.random.uniform(-1, 1, ((2 * nf + 1) ** 2 // 2, 2))]

for x, y, z in np.random.uniform(-1, 1, (7 // 2, 3)):
    print("x:"+str(x))
    print("y:"+str(y))
    print("z:"+str(z))

s = np.random.uniform(0, 1, 12)

print(noise)

print(s)
