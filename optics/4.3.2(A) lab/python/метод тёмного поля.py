import matplotlib.pyplot as plt
import numpy as np

nu = [1.17, 1.6, 1.83, 1.43] #МГц
s_nu = 0.005 #МГц
x1 = np.array([101, 72, 62, 90])/6 #мм
x2 = np.array([11, 21, 0, 0])/6 #мм
s_x = 1/12 #мм
            #половина цены деления
N = [24, 22, 37, 28]

L = 2 * (np.array(x1) - np.array(x2)) / np.array(N)
s_L = np.array(L) * (s_x/(np.array(x1) - np.array(x2)))

v = np.array(L) * np.array(nu) * 10**(3)
s_v = np.array(v) * ((s_nu/np.array(nu))**2 + (s_L/np.array(L))**2)**0.5

for i in range(len(N)):
    print(i + 1, 'L = ', L[i], '+/-', s_L[i], 'мм')
    print(i + 1, 'v = ', v[i], '+/-', s_v[i], 'м/с')
