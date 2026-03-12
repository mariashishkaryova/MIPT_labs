import numpy as np
import matplotlib.pyplot as plt
import math as m

f_n = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
d_V = [1.6, 2.4, 2.4, 3.2, 3.2, 3.2, 4, 4, 4, 4, 4, 4.4]
d_t = [258, 78, 55.2, 31.2, 32.8, 18.8, 24.0, 12, 18.8, 8.8, 15.8, 7]
V_0 = [16.4]*12
V_n = np.array(V_0) - np.array(d_V)
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

fig, ax = plt.subplots()

t = np.polyfit(f_n, V_n, 1)
f = np.poly1d(t)

ax.scatter(f_n, V_n, s=15, c='b', marker='o', zorder = 1)
plt.errorbar(f_n, V_n, xerr=1, linestyle='none', color='black')
plt.errorbar(f_n, V_n, yerr=0.1, linestyle='none', color='black')
plt.xlabel('частота, МГц')
plt.ylabel('Амплитуда, В')
plt.title('АЧХ')
plt.grid(linewidth = 0.3)
plt.savefig('АЧХ.png')
plt.show()