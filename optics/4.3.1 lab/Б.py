import matplotlib.pyplot as plt
import numpy as np

zero = 2 * 0.02 * 10**(-3) #m

x2 = np.array([49, 40, 30, 20, 9, -10, -21, -30, -41, -49]) * 0.02 * 10**(-3) #m

x = np.array(x2) - np.array(zero)
n = np.concatenate((np.arange(5, 0, -1), np.arange(-1, -6, -1)))

fig, ax = plt.subplots()
t = np.polyfit(x * 10**(3), n, 1)
f = np.poly1d(t)
print('kоэффициент наклона =', t[0])

plt.scatter(n, x * 10**(3), s = 7, c='black', marker='o', zorder = 1)
plt.plot(n, np.polyval(np.polyfit(n, x * 10**(3), 1), n), color = 'blue', lw = '2')
plt.errorbar(n, x * 10**(3), yerr=0.1 * 2**0.5, linestyle='none', color='darkgreen')
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
plt.xlabel('n')
plt.ylabel(r'x, cm')
plt.title(r'график зависимости x от n')
plt.savefig('x(n).png')
plt.show()