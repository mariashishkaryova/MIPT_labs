import numpy as np
import matplotlib.pyplot as plt

m = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
a_osn = [585]*8
a_bok = [57.5, 87.8, 115.4, 145.5, 174, 204.5, 233.4, 262.2]

fig3, ax3 = plt.subplots()
t3 = np.polyfit(m, np.array(a_bok)/np.array(a_osn), 1)
f3 = np.poly1d(t3)

plt.plot(m, np.polyval(np.polyfit(m, np.array(a_bok)/np.array(a_osn), 1), m), color='c')
plt.title('a_bok/a_osn(m)')
plt.xlabel('m')
plt.ylabel('a_bok/a_osn')
plt.grid(linewidth = 1)
plt.savefig('3.png')

plt.show()