import numpy as np
import matplotlib.pyplot as plt

f_n = [3.90, 7.84, 11.80, 15.74, 19.70, 23.64]
n = [1, 2, 3, 4, 5, 6]

fig, ax = plt.subplots()

t = np.polyfit(f_n, n, 1)
f = np.poly1d(t)
k = (f_n[5] - f_n[0])/(n[5] - n[0])
sigma_k = k * ((0.05/f_n[5])**2 + (0.05/f_n[0])**2)**0.5
print('k = ', k, 'МГц')
print('sigma_k =', sigma_k)

V_f = k * 510 * 10**6
sigma_v = ((sigma_k/k)**2 + (1/510)**2)**0.5
print('V_f = ', V_f/10**9, '* 10^10 см/с')
print('sigma_v = ', sigma_v)

plt.plot(n, np.polyval(np.polyfit(n, f_n, 1), n), color='r', label = f'k ={"{:.3f}".format(k)}МГц')
ax.scatter(n, f_n, s=15, c='b', marker='o', zorder = 1)
plt.errorbar(n, f_n, yerr=0.01, linestyle='none', color='black')
plt.xlabel('номер')
plt.ylabel('резонансная частота, МГц')
plt.title('f(n) для синусоидального сигнала(согласованная линия)')
plt.grid(linewidth = 0.3)
plt.legend()
plt.savefig('синусоидальный сигнал(согласованная линия).png')
plt.show()