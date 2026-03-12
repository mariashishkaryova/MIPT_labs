import numpy as np
import matplotlib.pyplot as plt
import math

nu = [42, 47, 53, 61, 72, 88, 172]
R = [999, 899, 799, 699, 599, 499, 364]

nu_t = 1/(50*10**(-9) * np.array(R)*10**(3) * math.log((142.8 - 78.3)/ (142.8 - 94.3)))
print(nu_t)

V_din = []
for i in range(len(nu)):
    v_din_i = (math.exp(R[i]*1000 * 50*10**(-9))*142.8 - (142.8 - 94.3)*math.exp(1/nu[i]))/ (math.exp(R[i]*1000 * 50*10**(-9)))
    V_din.append(v_din_i)

V_d = sum(V_din)/(len(V_din))
print('v_d = ', V_d)

error_nu_t = ((0.5/786)**2 + (0.1/50)**2 + (0.1/ 142.8) + (0.1/94.3)**2 + (0.1/ 78.3)**2)**0.5
error_nu = (error_nu_t**2 + 1)**0.5
print(error_nu)

fig, ax = plt.subplots()
t = np.polyfit(nu, R, 1)
f = np.poly1d(t)
print('k = ', t)


plt.plot(R, np.polyval(np.polyfit(R, nu_t, 1), R), color='orange')
ax.scatter(R, nu_t, s=2, c='orange', marker='o', zorder = 1)
plt.errorbar(R, nu_t, xerr=0.5, linestyle='none', color='black', label = '+/- 0.1нФ')
plt.errorbar(R, nu_t, yerr=1.5, linestyle='none', color='black', label = '+/- 1Гц')

plt.plot(R, np.polyval(np.polyfit(R, nu, 1), R), color='g')
ax.scatter(R, nu, s=2, c='b', marker='o', zorder = 1)
plt.errorbar(R, nu, xerr=5, linestyle='none', color='r', label = '+/- 0.5кОм')
plt.errorbar(R, nu, yerr=2, linestyle='none', color='black', label = '+/- 1Гц')
plt.legend()
plt.xlabel('Сопротивление, кОм')
plt.ylabel('Частота, Гц')
plt.title('зависимость частоты от сопротивления')
plt.grid(linewidth = 0.3)
plt.savefig('график зависимости частоты от сопротивления.png')
plt.show()