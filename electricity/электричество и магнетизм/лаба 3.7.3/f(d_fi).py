import numpy as np
import matplotlib.pyplot as plt

f = [6.8, 6.6, 6.4, 6.2, 6, 5.8, 5.6, 5, 4]
fi = [0.32, 0.33, 0.33, 0.33, 0.32, 0.30, 0.29, 0.26, 0.22]

fig, ax = plt.subplots()


plt.plot(f, np.polyval(np.polyfit(f, fi, 1), f), color='r')
ax.scatter(f, fi, s=15, c='b', marker='o', zorder = 1)
plt.errorbar(f, fi, xerr=0.2, linestyle='none', color='black')
plt.errorbar(f, fi, yerr=0.005, linestyle='none', color='black')
plt.xlabel('частота, кГц')
plt.ylabel('разность фаз, рад')
plt.title('fi(f) модели длинной линии')
plt.grid(linewidth = 0.3)
plt.legend()
plt.savefig('fi(f) модели длинной линии.png')
plt.show()