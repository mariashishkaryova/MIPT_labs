import numpy as np
import matplotlib.pyplot as plt

nu = [200, 400, 500, 750, 1000, 1500, 2000, 2500, 3000, 5000, 6000, 10000, 12000, 15000, 20000]
L = [6.51, 4.31, 3.9, 3.43, 3.25, 3.12, 3.07, 3.05, 3.04, 3.04, 3.05, 3.14, 3.23, 3.44, 4.04]

L1 = [6.51, 4.31, 3.9, 3.43, 3.25, 3.12]
nu2 = [200, 400, 500, 750, 1000, 1500]

Lmax = 6.51
Lmin = 3.04

fig, ax2 = plt.subplots()
t = np.polyfit(L, nu, 1)
f = np.poly1d(t)

y = (Lmax - Lmin)/(np.array(L1) - Lmin)
x = np.array(nu2)**2
t1 = np.polyfit(y, x, 1)
f1 = np.poly1d(t1)
sigma = abs(t[0])**0.5/ (3.14 * (45/2)*10**(-3) * 1.5*10**(-3))
print('sigma = ', sigma)

ax2.scatter(x, y, s=20, c='red', marker='o', zorder = 1)
plt.plot(x, np.polyval(np.polyfit(x, y, 1), x), color='orange')
plt.errorbar(x, y, xerr=0.1*10**(6), yerr=2, linestyle='none', color='black')
plt.ylabel('(Lmax - Lmin)/(L - Lmin)')
plt.xlabel('nu^0.5, Гц^0.5')
plt.title('(Lmax - Lmin)/(L - Lmin)(nu^0.5)')
plt.grid(linewidth = 0.3)
plt.savefig('график Lmax и тд.png')
plt.show()

fig, ax1 = plt.subplots()
t = np.polyfit(L, nu, 1)
f = np.poly1d(t)

#plt.plot(nu, np.polyval(np.polyfit(nu, L, 1), nu), color='orange')
ax1.scatter(nu, L, s=40, c='red', marker='o', zorder = 1)
plt.errorbar(nu, L, xerr=500, yerr=0.1, linestyle='none', color='black')
plt.ylabel('L, мГн')
plt.xlabel('nu, Гц')
plt.title('L(nu)')
plt.grid(linewidth = 0.3)
plt.savefig('график частоты от индуктивности.png')
plt.show()