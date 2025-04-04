import matplotlib.pyplot as plt
import numpy as np

#пока очень странные значения

N = 13
f2 = 13.8 * 10**(-2) #m
f1 = 10.2 * 10**(-2) #m
lam = 5461 * 10**(-10) #m

d_x = 35 * 0.02 * 10**(-3) / 13 #m
b0 = 7.5 * 10 **(-5) #m
b1 = 8.2 * 10 **(-5) #m
d = 1 * 10**(-3) #m
#ширина щелей
a1 = 13 * 0.02 * 10**(-3) #m
a2 = 10 * 0.02 * 10**(-3) #m
D = (a1 + a2) / 2

d_teor = f2 * lam /d_x
s_d = d_teor * ((0.01*10**(-2)/f2)**2 + (0.01 * 10**(-3)/d_x)**2)**0.5
print("d_teor =", d_teor * 10**3, 'pm', s_d * 10**3, 'm')

N_teor = 2 * d_teor/ D
print("N_teor", N_teor)

b_teor = lam * f1/ d_teor
s_b_teor = b_teor * ((0.01*10**(-2)/f1)**2 + (s_d /d_teor)**2)**0.5
print('b_teor =', b_teor * 10**3, 'pm', s_b_teor * 10**3, 'm')

