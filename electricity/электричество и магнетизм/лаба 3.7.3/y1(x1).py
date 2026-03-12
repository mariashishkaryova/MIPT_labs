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

y1 =[(d_fi[i]/510)**2 - (m.log(V_0/V_n[i])/510)**2 for i in range(12)]
x1 = (2 * 3.14 * np.array(f_n))**2

fig, ax = plt.subplots()

t = np.polyfit(x1, y1, 1)
f = np.poly1d(t)
kof = (y1[11] - y1[0])/(x1[11] - x1[0])
print('kof = ', kof)
LC = kof * (2.9 * 10 ** (10))**2
print('LC = ', LC*10**(-14))

plt.plot(x1, np.polyval(np.polyfit(x1, y1, 1), x1), color='r')
ax.scatter(x1, y1, s=15, c='b', marker='o', zorder = 1)
plt.errorbar(x1, y1, xerr=300, linestyle='none', color='black')
plt.errorbar(x1, y1, yerr=0.0002, linestyle='none', color='black')
plt.xlabel('x1, с^(-2)')
plt.ylabel('y1, см^(-2)')
plt.title('y1(x1)')
plt.grid(linewidth = 0.3)
plt.savefig('y1(x1).png')
plt.show()