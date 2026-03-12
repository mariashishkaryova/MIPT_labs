import numpy as np
import matplotlib.pyplot as plt

k = np.array([0.025, 0.0311, 0.026, 0.028, 0.0276, 0.031])
T = np.array([23, 30, 40, 50, 60, 70])


fig, ax = plt.subplots()

t = np.polyfit(T, k, 2)
f = np.poly1d(t)

ax.scatter(T, k, c="r", zorder = 1)
ax.plot(T, f(T), label = 'T6 = 70℃',
         linestyle='-', alpha = 1,
         color = 'orange', ms=5, zorder = 0)
ax.set_ylim(0, 0.05)
ax.grid(linewidth = 0.5)
yerr = [0.0034, 0.0051, 0.002, 0.001, 0.002, 0.001]
ax.errorbar(T, k, yerr=yerr, c="b", fmt='o', linewidth=2, capsize=6)
plt.xlabel('T, ℃', fontsize=10)
plt.ylabel('k, Вт/(м*с)', fontsize=10)
plt.savefig("График зависимости теплопроводности от температуры", dpi=600)
plt.show()

