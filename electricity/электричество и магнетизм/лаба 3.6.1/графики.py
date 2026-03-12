import numpy as np
import matplotlib.pyplot as plt

tau = [20, 22.2, 22.5, 28.6, 33.3, 40, 50, 66.7, 100, 200] #mks
delta_nu = [50, 45.2, 40.2, 35, 30, 25, 20, 15, 10, 5] #kHz

nu = [200, 500, 1000, 1500, 2000, 3000, 4000] #Hz
d_nu = [203, 491, 992, 1532, 2025, 2986, 4039] #Hz

m = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
a_osn = [585]*8
a_bok = [57.5, 87.8, 115.4, 145.5, 174, 204.5, 233.4, 262.2]

fig1, ax1 = plt.subplots()
t1 = np.polyfit(1/np.array(tau), delta_nu, 1)
f1 = np.poly1d(t1)

fig2, ax2 = plt.subplots()
t2 = np.polyfit(nu, d_nu, 1)
f2 = np.poly1d(t2)

fig3, ax3 = plt.subplots()
t3 = np.polyfit(m, np.array(a_bok)/np.array(a_osn), 1)
f3 = np.poly1d(t3)

ax1.plot(1/np.array(tau), np.polyval(np.polyfit(1/np.array(tau), delta_nu, 1), 1/np.array(tau)), color='c')
ax1.set_title('deltanu(1/tau)')
ax1.set_xlabel('1/tau, кГц')
ax1.set_ylabel('delta_nu, кГц')
plt.grid(linewidth = 1)
plt.savefig('график зависимости delta_nu(1/tau).png')

ax2.plot(nu, np.polyval(np.polyfit(nu, d_nu, 1), nu), color='c')
ax2.set_title('d_nu(nu)')
ax2.set_xlabel('nu, Гц')
ax2.set_ylabel('d_nu, Гц')
ax2.set_grid(linewidth = 1)
ax2.set_savefig('график зависимости d_nu(nu).png')

ax3.plot(m, np.polyval(np.polyfit(m, np.array(a_bok)/np.array(a_osn), 1), m), color='c')
ax3.set_title('a_bok/a_osn(m)')
ax3.set_xlabel('m')
ax3.set_ylabel('a_bok/a_osn')
ax3.set_grid(linewidth = 1)
ax2.set_savefig('график зависимости a_bok/a_osn(m).png')

plt.show()