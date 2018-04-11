#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import numpy as np
from decimal import Decimal


def sigmoid(inX):
    return  1.0 / (1 + np.exp(-inX))


# e的x的2次方  int 不能大于19  longfloat不能超过110 ，Decimal 256仍然无压力
x = np.arange(1, 256)
xx = np.exp(x ** 2)
xx2 = np.longfloat(xx)
xxx = np.exp(np.longfloat(x ** 2))
print(xx)
print(xx2)
print(xxx)
y = np.arange(Decimal(30), Decimal(256))
z = np.exp(y ** 2)
print(z)

a = np.arange(1, 5000)
for i in a:
    print(sigmoid(i))
print("end")
