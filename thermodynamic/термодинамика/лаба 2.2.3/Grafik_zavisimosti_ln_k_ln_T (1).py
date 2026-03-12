import numpy as np
import matplotlib.pyplot as plt

k = (np.array([0.025, 0.0311, 0.026, 0.028, 0.0276, 0.031]))
T = (np.array([23, 30, 40, 50, 60, 70]))

fig, ax = plt.subplots()

t = np.polyfit(T, k, 1)
f = np.poly1d(t)
print(f)

print(np.log(k))
ax.scatter(np.log(T), np.log(k), c="r", zorder = 1)
ax.plot(np.log(T), np.log(f(T)), label = 'T6 = 70℃',
         linestyle='-', alpha = 1,
         color = 'orange', ms=5, zorder = 0)
ax.set_ylim(-5, 0)
ax.grid(linewidth = 0.5)

plt.show()