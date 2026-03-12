import matplotlib.pyplot as plt
import numpy as np
import math

R0 = 50 #kOm
U0 = 1.39
a = 114  # см
C = 2 #мкФ

R = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
l = [63, 78, 90, 101, 104, 116, 122, 126, 131, 137]

#R_cr =
#print('Rcr = ', R_cr)
print('tau = ', C * R0 * 10**3, 'мкс')
print('Ckrq = ', 2 * a * 10**(-2) * C * 10**(-6) * U0 / (30 * 137 * 10**(-3)), 'Кл')

fig, ax = plt.subplots()

plt.scatter(np.array(R) / 1000 + R0, l, s=30, c='black', marker='*', zorder = 1)
plt.plot(np.array(R) / 1000 + R0, np.polyval(np.polyfit(np.array(R) / 1000 + R0, l, 1), np.array(R) / 1000 + R0), color='orange')
ax.errorbar(np.array(R) / 1000 + R0, l, xerr=0.0005, yerr=0, linestyle='none', color='black')
plt.grid(linewidth = 0.5)
plt.xlabel('R + R0, Oм')
plt.ylabel('l, мм')
plt.title('x(R + R0)')
plt.savefig('x(R + R0).png')
plt.show()