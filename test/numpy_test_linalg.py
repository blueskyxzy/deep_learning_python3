#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 在深度学习相关的数据处理和运算中，线性代数模块（linalg）是最常用的之一。
# 结合numpy提供的基本函数，可以对向量，矩阵，或是说多维张量进行一些基本的运算
import numpy as np

a = np.array([3, 4])
np.linalg.norm(a)   #范数是对向量（或者矩阵）的度量，是一个标量（scalar）           范数理论的一个小推论告诉我们：ℓ1≥ℓ2≥ℓ∞
np.linalg.norm(a, 2)
np.linalg.norm(a, 1)
np.linalg.norm(a, np.inf)

b = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
c = np.array([1, 0, 1])

# 矩阵和向量之间的乘法
bc1 = np.dot(b, c)  # array([ 4, 10, 16])
bc2 = np.dot(c, b.T)  # array([ 4, 10, 16])
print(bc1)
print(bc2)
aa = [[1, 0],
      [0, 1]]
bb = [[4, 1],
      [2, 2]]
np.dot(aa, bb)
a3 = np.array([
    [1, 0, 1],
    [0, 1, 1]
])
b3 = np.array([
    [4, 1, 0],
    [2, 2, 1]
])

b_trace = np.trace(b)  # 求矩阵的迹，15    一个n×n矩阵A的主对角线（从左上方至右下方的对角线）上各个元素的总和被称为矩阵A的迹（或迹数），一般记作tr(A)。
b_det = np.linalg.det(b)  # 求矩阵的行列式值，0
b_matrix = np.linalg.matrix_rank(b)  # 求矩阵的秩，2，不满秩，因为行与行之间等差
print(b_matrix)
print(b_trace)
print(b_det)

d = np.array([
    [2, 1],
    [1, 2]
])

'''
对正定矩阵求本征值和本征向量
本征值为u，array([ 3.,  1.])
本征向量构成的二维array为v，
array([[ 0.70710678, -0.70710678],
       [ 0.70710678,  0.70710678]])
是沿着45°方向
eig()是一般情况的本征值分解，对于更常见的对称实数矩阵，
eigh()更快且更稳定，不过输出的值的顺序和eig()是相反的
'''
u, v = np.linalg.eig(d)
print(u)
print(v)
print(u*v)
print(np.dot(u, v))

# Cholesky分解并重建
l = np.linalg.cholesky(d)
print(l)
'''
array([[ 2.,  1.],
       [ 1.,  2.]])
'''
x = np.dot(l, l.T)
print(x)

e = np.array([
    [1, 2],
    [3, 4]
])

# 对不镇定矩阵，进行SVD分解并重建
U, s, V = np.linalg.svd(e)
print(U)
print(s)
print(V)

S = np.array([
    [s[0], 0],
    [0, s[1]]
])

'''
array([[ 1.,  2.],
       [ 3.,  4.]])
'''
y = np.dot(U, np.dot(S, V))
print(y)
print("end")
