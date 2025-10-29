from math import atan2, pi

x0, y0 = (0, 0)
x1, y1 = (1, 1)

dx = x1 - x0
dy = y1 - y0

radian = atan2(dy, dx)
degree = radian * 180 / pi

tmp1 = atan2(0, 100) * 180 / pi
tmp2 = atan2(100, 0) * 180 / pi
tmp3 = atan2(0, 0) * 180 / pi

test = 0