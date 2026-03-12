import numpy as np
import matplotlib.pyplot as plt
import math as m

f_n = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
d_V = [1.6, 2.4, 2.4, 3.2, 3.2, 3.2, 4, 4, 4, 4, 4, 4.4]
d_t = [258, 78, 55.2, 31.2, 32.8, 18.8, 24.0, 12, 18.8, 8.8, 15.8, 7]
V_0 = 16.4
V_n = np.array(V_0) - np.array(d_V)
n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

d_fi = 2 * 3.14 * np.array(f_n)*10**(6) * np.array(d_t)*10**(-9) + 3.14 * np.array(n)
print(d_fi)

y2 =[(m.log(V_0/V_n[i])/510) for i in range(12)]
x2 = (np.array(f_n))**0.5

fig, ax = plt.subplots()

t = np.polyfit(x2, y2, 1)
f = np.poly1d(t)
kof = (y2[11] - y2[0])/(x2[11] - x2[0])
print('kof = ', kof)
sigma = 10**(-18) * ((4 * 2.252 * 2 * 10**10)/(1.08 * 10**(-8) * 3 * 10**10 * 1.37))**2
print('sigma = ', sigma)

plt.plot(x2, np.polyval(np.polyfit(x2, y2, 1), x2), color='r')
ax.scatter(x2, y2, s=15, c='b', marker='o', zorder = 1)
plt.errorbar(x2, y2, xerr=0.05, linestyle='none', color='black')
plt.errorbar(x2, y2, yerr=0.00001, linestyle='none', color='black')
plt.xlabel('x2, с^(-0.5)')
plt.ylabel('y2, см^(-1)')
plt.title('y2(x2)')
plt.grid(linewidth = 0.3)
plt.savefig('y2(x2).png')
plt.show()