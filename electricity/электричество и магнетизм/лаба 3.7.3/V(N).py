import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

N = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
V1 = [1.2, 2, 3.2, 3.6, 3.6, 4, 4, 4.8, 6.4, 8]
V2 = [2.4, 1.6, 0, 0, 0, 1.2, 3.2, 5.6, 8, 11.6]

fig, ax = plt.subplots()

t1 = np.polyfit(N, V1, 1)
f1= np.poly1d(t1)

NV2_spline = make_interp_spline(N, V2)
N_ = np.linspace(np.array(N).min(), np.array(N).max(), 100)
V2_ = NV2_spline(N_)

plt.plot(N, V1, color='r', label = 'f1 = 2.14кГц', linestyle = '-')
ax.scatter(N, V1, s=15, c='b', marker='v', zorder = 1)
plt.errorbar(N, V1, xerr=0.2, linestyle='none', color='black')
plt.errorbar(N, V1, yerr=0.005, linestyle='none', color='black')

plt.plot(N, V2, color='g', label = 'f1 = 7.09кГц', linestyle = '--')
ax.scatter(N, V2, s=15, c='black', marker='o', zorder = 1)
plt.errorbar(N, V2, xerr=0.2, linestyle='none', color='black')
plt.errorbar(N, V2, yerr=0.005, linestyle='none', color='black')

plt.xlabel('номер')
plt.ylabel('напряжение, В')
plt.title('V(N) модели длинной линии')
plt.grid(linewidth = 0.3)
plt.legend()
plt.savefig('V(N) модели длинной линии.png')
plt.show()