import numpy as np
import matplotlib.pyplot as plt
import math

nu = [28.32, 42.4, 56.6, 70.7,  84.9,  98.8,  113.2, 127,   141.5, 155.6, 140,   170,   200,   230,   260,   280,   290,   410,   540,   670, 800,   930,  1060, 1180, 1320,  1415]
I =  np.array([437.6, 431.3, 432, 413.8, 404.3, 395.2, 386.3, 378.4, 370.8, 364.2, 370.2, 356.9, 346.3, 337.9, 331.2, 327.4, 325.6, 310.3, 298.9, 289, 279.5, 270.1, 260, 251.1, 241.8, 235]) * 10**(-3)
U =  [0.233, 0.338, 0.432, 0.514, 0.584, 0.64, 0.692, 0.732, 0.767, 0.795, 0.763, 0.818, 0.856, 0.882, 0.899, 0.908, 0.912, 0.930, 0.924, 0.908, 0.885, 0.858, 0.831, 0.804, 0.772, 0.753]

ksi = np.array(U)/(np.array(nu) * np.array(I))
y = 1/np.array(ksi**2)
x = np.array(nu) ** 2
print('x =', x)
print('y =', y)


fig, ax = plt.subplots()
t = np.polyfit(y, x, 1)
f = np.poly1d(t)
print('k = ', f)

ksi0 = (-t[1]*10**(-1))**0.5
print('ksi0 = ', ksi0)

sigma = (t[0]/(ksi0 * 3.14 * (45/2)*10**(-3) * 1.5*10**(-3))**2)**0.5
print('sigma = ', sigma)

plt.plot(x, np.polyval(np.polyfit(x, y, 1), x), color='orange')
ax.scatter(x, y, s=4, c='red', marker='o', zorder = 1)
plt.errorbar(x, y, xerr=2 * 10**4, yerr=3000, linestyle='none', color='black')
plt.ylabel('1/ksi^2')
plt.xlabel('nu^2, Гц^2')
plt.title('ksi(nu)')
plt.grid(linewidth = 0.3)
plt.savefig('график зависимости ksi(nu).png')
plt.show()

import math
import matplotlib.pyplot as plt
import numpy as np

R = [20, 30, 40, 50, 60, 60, 70, 80, 90]
x = [13.5, 9.7, 7.4, 5.9, 5.1, 4.4, 4.0, 3.5]

U0 = 1.39
R1_2 = 1 / 1000
R0 = 560
a = 1.14  # м
I = [U0 * R1_2 / (R[i] * 1000 + R0) for i in range(len(R))]
print('I =', I)

fig1, ax1 = plt.subplots()

plt.scatter(x, I * 10 ** 8, s=30, c='black', marker='s', zorder = 1)
plt.plot(x, np.polyval(np.polyfit(x, I * 10 ** 8, 1), x), color='orange')
ax1.errorbar(x, I * 10 ** 8, xerr=0.5, yerr=0.1, linewidth=2, capsize=2)
plt.grid(linewidth = 0.3)
plt.xlabel('x, cм')
plt.ylabel('I, 10^(-8) A')
plt.savefig('I(x).png')
plt.show()