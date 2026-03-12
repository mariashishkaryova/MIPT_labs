import matplotlib.pyplot as plt
import numpy as np

R = [20, 30, 40, 50, 60, 60, 70, 80, 90]
x = [13.5, 9.7, 7.4, 5.9, 5.1, 4.4, 4.0, 3.5]

U0 = 1.39
R1_2 = 1 / 1000
R0 = 560
a = 114  # см
I = np.array([U0 * R1_2 / (R[i] * 1000 + R0) for i in range(len(x))]) * 10**9
print('I =', I, 'нА')

k = (I[len(I) - 1] - I[0]) / (x[len(x) - 1] - x[0])
print('k =', k, 'нА/см')
print('C1 =', 2 * a * k, 'нА')
print('S1 =', 1 / (2 * a * k), 'нА')

fig, ax = plt.subplots()

plt.scatter(x, I, s=30, c='black', marker='d', zorder = 1)
plt.plot(x, np.polyval(np.polyfit(x, I, 1), x), color='orange')
ax.errorbar(x, I, xerr=0.5, yerr=0.9, linestyle='none', color='black')
plt.grid(linewidth = 0.5)
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.yticks(np.arange(min(I), max(I)+1, 7))
plt.xlabel('x, cм')
plt.ylabel('I, нA')
plt.title('I(x)')
plt.savefig('I(x).png')
plt.show()

