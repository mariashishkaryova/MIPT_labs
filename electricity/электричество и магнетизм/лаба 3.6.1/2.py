import numpy as np
import matplotlib.pyplot as plt

tau = [20, 22.2, 22.5, 28.6, 33.3, 40, 50, 66.7, 100, 200] #mks
delta_nu = [50, 45.2, 40.2, 35, 30, 25, 20, 15, 10, 5] #kHz

nu = [200, 500, 1000, 1500, 2000, 3000, 4000] #Hz
d_nu = [203, 491, 992, 1532, 2025, 2986, 4039] #Hz

m = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
a_osn = [585]*8
a_bok = [57.5, 87.8, 115.4, 145.5, 174, 204.5, 233.4, 262.2]

fig2, ax2 = plt.subplots()
t2 = np.polyfit(nu, d_nu, 1)
f2 = np.poly1d(t2)

plt.plot(nu, np.polyval(np.polyfit(nu, d_nu, 1), nu), color='c')
plt.title('d_nu(nu)')
plt.xlabel('nu, Гц')
plt.ylabel('d_nu, Гц')
plt.grid(linewidth = 1)
plt.savefig('2.png')

plt.show()