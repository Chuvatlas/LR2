import random

import numpy as np
from sympy import *
import math as m
import matplotlib.pyplot as plt
import random as rand


def search_grad():  # поиск производных
    f = pow(w1, 2) + pow(w2, 2) + 6 * w1 - 4 * w2
    deriative = [diff(f, w1), diff(f, w2)]
    # dF = lambdify([w1, w2], deriative, "numpy")
    return deriative

#initialized variables
max_iter = 10000
rate = 0.01
eps = 1E-6

w1, w2 = symbols('w1, w2')
x = random.uniform(-1,1)
y = random.uniform(-1,1)
W = np.array([x,y])
print("Начальная точка - ", W)


#main
i=0
while (True):
    i=i+1

    common_grad = search_grad()             # получаем функции производных

    dFw1 = common_grad[0].subs(w1, W[0])
    dFw2 = common_grad[1].subs(w2, W[1])
    grad_W = np.array([dFw1, dFw2])

    W = W - rate*np.array(grad_W)        # новое положение точки
    #print(W)

    if i>max_iter:
        print("решение не найдено")
        break

    if (sqrt(grad_W[0]**2+grad_W[1]**2)*rate<eps):
        print("Решение найдено ", W, ". Потребовалось ", i," итераций ")
        break





# flg = False
# i=0
# while (flg==False) or (i < max_iter):
#     i+=1
#     W_prev = grad_W
#     W = W - rate * grad_W
#     W_curr = grad_W



#
# #От простого к сложному
# w1 = 1
# w2 = 1
# i=0
# flg=False
#
# def dfw1(w1):
#     return 2*w1+6
# def dfw2(w2):
#     return 2*w2-4
#
# while (flg==False):
#     w1_prev = w1
#     w1 = w1 - rate * dfw1(w1)
#     w1_curr = w1
#
#     w2_prev = w2
#     w2 = w2 - rate * dfw2(w2)
#     w2_curr = w2
#
#     if abs(w1_curr-w1_prev)<eps and abs(w2_curr-w2_prev)<eps:
#         flg=True
#     else:
#         i+=1
#     print(i, w1, w2)








# arr = [[] for _ in range(2)]
#
# arr[0].append(grad_W[0]*rate)
# arr[1].append(grad_W[1]*rate)
# print(arr)
# W_i = rate * arr
# print(W_i)