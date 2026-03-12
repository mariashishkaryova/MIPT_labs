import numpy as np
import matplotlib.pyplot as plt

I, U, nu = [370.2, 356.9, 346.3, 337.9, 331.2, 327.4, 325.6, 310.3, 298.9, 289, 279.5, 270.1, 260, 251.1, 241.8, 235], [ 0.763, 0.818, 0.856, 0.882, 0.899, 0.908, 0.912, 0.930, 0.924, 0.908, 0.885, 0.858, 0.831, 0.804, 0.772, 0.753], [140,   170,   200,   230,   260,   280,   290,   410,   540,   670, 800,   930,  1060, 1180, 1320,  1415]

nu = np.array(nu)
I = np.array(I) * 10 ** (-3)
U = np.array(U)

xi = U / (nu * I)
xi_0 = 13.99 * 10 ** (-3)

x = nu
y = xi / xi_0

fig, axs = plt.subplots(dpi=80, figsize=(10, 6))
plt.xscale("log")
plt.plot(x, y, ms=5)
axs.scatter(x, y, s=30, c='red', marker='o', zorder = 1, label='Экспериментальные данные')

sigma = (5.077 + 4.49) / 2 * 10 ** 7
mu0 = 1.256 * 10 ** (-6)
h = 1.5 * 10 ** (-3)
a = 22.5 * 10 ** (-3)
alpha = np.array([np.sqrt(complex(0, 2 * np.pi * sigma * mu0 * x)) for x in nu])
h1h0 = 1 / (np.cosh(h * alpha) + 0.5 * a * alpha * np.sinh(0.4 * h * alpha))

x = nu
y = np.array([(x.real**2 + x.imag**2) for x in h1h0])

plt.plot(x, y, ms=5)
axs.scatter(x, y, s=30, c='black', marker='s', zorder = 1, label='Теоретические данные')

plt.ylabel('H1/H0')
plt.xlabel('nu, Гц')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.title('H1/H0')
plt.grid()
plt.legend()

plt.savefig('image6.jpg')
plt.show()
