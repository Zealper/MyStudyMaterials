import numpy as np
import math
# 点A坐标
A = np.array([500.000, 500.000])
# 点B坐标
B = np.array([600.000, 700.000])
# 点C坐标
C = np.array([400.000, 800.000])
# 点D坐标
D = np.array([300.000, 700.000])
# AB\AD向量坐标
p1 = A - B
p2 = A - D
# BC\BA向量坐标
p3 = B - C
p4 = B - A
# CB\CD向量坐标
p5 = C - B
p6 = C - D
# DC\DA向量坐标
p7 = D - C
p8 = D - A
# 求出AB长度
res1 = math.hypot(p1[0], p1[1])
# AD长度
res2 = math.hypot(p2[0], p2[1])
# BC长度
res3 = math.hypot(p3[0], p3[1])
# CD长度
res4 = math.hypot(p6[0], p6[1])

# 输出四边长度
print('AB长度: {}'.format(res1))
print('AD长度: {}'.format(res2))
print('BC长度: {}'.format(res3))
print('CD长度: {}'.format(res4))


list_vector_quantity = [(p1, p2), (p3, p4), (p5, p6), (p7, p8)]
list_name = ['AB\AD', 'BC\BA', 'CB\CD', 'DC\DA']
j = 0
for number, i in enumerate(list_vector_quantity):
    x = np.array(i[0])
    y = np.array(i[1])
    # 两个向量
    Lx = np.sqrt(x.dot(x))
    Ly = np.sqrt(y.dot(y))
    # 相当于勾股定理，求得斜线的长度
    cos_angle = x.dot(y)/(Lx*Ly)
    # 求得cos_sita的值再反过来计算，绝对长度乘以cos角度为矢量长度.
    angle = np.arccos(cos_angle)
    angle2 = angle*360/2/np.pi
    # 变为角度
    if j == number:
        print('{} 向量夹角是：{}'.format(list_name[j], angle2))
    j += 1

    # x.dot(y) = y=∑(ai*bi)
