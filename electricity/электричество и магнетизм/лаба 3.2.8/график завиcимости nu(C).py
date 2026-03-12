import numpy as np
import matplotlib.pyplot as plt
import math

nu = [44, 57, 68, 80, 101, 122, 209]
C = [50, 44, 38, 32, 26, 20, 14]

nu_t = 1/(786*1000 * np.array(C)*10**(-9) * math.log((142.8 - 78.3)/ (142.8 - 94.3)))
#print(nu_t)

V_din = []
for i in range(len(nu)):
    v_din_i = (math.exp(786*1000 * C[i]*10**(-9))*142.8 - (142.8 - 94.3)*math.exp(1/nu[i]))/ (math.exp(786*1000 * C[i]*10**(-9)))
    V_din.append(v_din_i)

V_d = sum(V_din)/(len(V_din))
print('v_d = ', V_d)

error_nu_t = ((0.5/786)**2 + (0.1/50)**2 + (0.1/ 142.8) + (0.1/94.3)**2 + (0.1/ 78.3)**2)**0.5
error_nu = (error_nu_t**2 + 1)**0.5
print(error_nu)

fig, ax = plt.subplots()
t = np.polyfit(nu, C, 1)
f = np.poly1d(t)
print('k = ', t)

plt.plot(C, np.polyval(np.polyfit(C, nu_t, 1), C), color='orange')
ax.scatter(C, nu_t, s=2, c='orange', marker='o', zorder = 1)
plt.errorbar(C, nu_t, xerr=0.5, linestyle='none', color='black', label = '+/- 0.1нФ')
plt.errorbar(C, nu_t, yerr=1.5, linestyle='none', color='black', label = '+/- 1Гц')

plt.plot(C, np.polyval(np.polyfit(C, nu, 1), C), color='g')
ax.scatter(C, nu, s=2, c='b', marker='o', zorder = 1)
plt.errorbar(C, nu, xerr=0.5, linestyle='none', color='r', label = '+/- 0.1нФ')
plt.errorbar(C, nu, yerr=1.5, linestyle='none', color='r', label = '+/- 1Гц')
plt.legend()
plt.xlabel('Ёмкость, нФ')
plt.ylabel('Частота, Гц')
plt.title('зависимость частоты от ёмкости')
plt.grid(linewidth = 0.3)
plt.savefig('график зависимости частоты от ёмкости.png')
plt.show()