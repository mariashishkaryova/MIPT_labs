import numpy as np
import matplotlib.pyplot as plt

#воздух
F = [223.2, 433.2, 642.2, 855, 1068, 1280]
k = [1, 2, 3, 4, 5, 6]

kof = (F[5]- F[0]) / (k[5] - k[0])
sigma_kof = kof * ((0.05/F[5])**2 + (0.05/F[0])**2)**0.5
print('kof =',kof)
print('sigma_kof =',sigma_kof)

c = kof * 2 * 0.795
sigma_c = c * ((0.05/F[5])**2 + (0.05/F[0])**2 + (5/795)**2 +(sigma_kof/kof)**2 )**0.5
print('c =',c)
print('sigma_c =',sigma_c)

g = (28.97 * (c)**2)*10**(-3)/(8.31*296)
sigma_g = g * ((0.1/269)**2 + (sigma_c/c)**2)
print('g =',g)
print('sigma_g =',sigma_g)

Fk = np.array(F) - 223.2

t = np.polyfit(k, Fk, 1)
f = np.poly1d(t)

fig, ax = plt.subplots()

plt.title("Воздух")
plt.scatter(k, Fk, c="blue", zorder = 1)
plt.plot(k, f(k),
         linestyle='-', alpha = 1,
         color = "black", ms=5, zorder = 0)
plt.grid(linewidth = 0.5)

plt.ylabel('f, Гц', fontsize=10)
plt.xlabel('k, №', fontsize=10)
plt.savefig("График зависимости частоты от номера резонанса", dpi=600)

plt.show()