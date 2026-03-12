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

y3 =[(1/510) * (d_fi[i]/510) * (m.log(V_0/V_n[i])/510) for i in range(12)]
x3 = (np.array(f_n) * 10**6)**1.5

fig, ax = plt.subplots()

t = np.polyfit(x3, y3, 1)
f = np.poly1d(t)

kof = (y3[11] - y3[0])/(x3[11] - x3[0])
print('kof = ', kof)
sigma = ((4 * 3.14 * 2.252) / (1.37 * 3 * 10**10 * kof))**2
print('sigma = ', sigma)

plt.plot(x3, np.polyval(np.polyfit(x3, y3, 1), x3), color='r')
ax.scatter(x3, y3, s=15, c='b', marker='o', zorder = 1)
plt.errorbar(x3, y3, xerr=5 * 10**9, linestyle='none', color='black')
plt.errorbar(x3, y3, yerr=0.000, linestyle='none', color='black')
plt.xlabel('x3, с^(-1.5)')
plt.ylabel('y3, см^(-3)')
plt.title('y3(x3)')
plt.grid(linewidth = 0.3)
plt.savefig('y3(x3).png')
plt.show()