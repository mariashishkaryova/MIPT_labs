import numpy as np
import matplotlib.pyplot as plt

#I1 = [8, 9, 9]
#V1 = [94, 94.1, 95]


I1 = [80, 90, 90, 90]
V1_r = [94, 93.9, 94.1, 95]

V1 = np.array(V1_r) - 5.2*1000 * np.array(I1) * 10 **(-6)

I2 = [70, 53, 45, 71]
V2_r = [79, 77.7, 77.2, 79.1]

V2 = np.array(V2_r) - 5.2*1000 * np.array(I2) * 10 **(-6)

fig, ax = plt.subplots()
t1 = np.polyfit(I1, V1, 1)
f1 = np.poly1d(t1)

t2 = np.polyfit(I2, V2, 1)
f2 = np.poly1d(t2)


plt.plot(V1_r, np.polyval(np.polyfit(V1_r, I1, 1), V1_r), color='b')
ax.scatter(V1_r, I1, s=20, c='b', marker='o', zorder = 1, label = 'с дополнительным сопр r')
plt.errorbar(V1_r, I1, xerr=0.1, linestyle='none', color='black', label = '+/- 0.5В')
plt.errorbar(V1_r, I1, yerr=1, linestyle='none', color='black', label = '+/- 1мкА')

plt.plot(V1, np.polyval(np.polyfit(V1, I1, 1), V1), color='c')
ax.scatter(V1, I1, s=20, c='c', marker='o', zorder = 1, label = 'без дополнительного сопр r')
plt.errorbar(V1, I1, xerr=0.1, linestyle='none', color='black')
plt.errorbar(V1, I1, yerr=1, linestyle='none', color='black')

plt.plot(V2_r, np.polyval(np.polyfit(V2_r, I2, 1), V2_r), color='r')
ax.scatter(V2_r, I2, s=20, c='r', marker='o', zorder = 1, label = 'с дополнительным сопр r')
plt.errorbar(V2_r, I2, xerr=0.1, linestyle='none', color='black')
plt.errorbar(V2_r, I2, yerr=1, linestyle='none', color='black')

plt.plot(V2, np.polyval(np.polyfit(V2, I2, 1), V2), color='c')
ax.scatter(V2, I2, s=20, c='c', marker='o', zorder = 1, label = 'без дополнительного сопр r')
plt.errorbar(V2, I2, xerr=0.1, linestyle='none', color='black')
plt.errorbar(V2, I2, yerr=1, linestyle='none', color='black')

plt.legend()
plt.xlabel('Напряжение, В')
plt.ylabel('Сила тока, мкА')
plt.title('ВАХ')
plt.grid(linewidth = 0.3)
plt.savefig('ВАХ.png')
plt.show()