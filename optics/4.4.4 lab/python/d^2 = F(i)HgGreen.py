import matplotlib.pyplot as plt
import numpy as np

d_up = [197.64, 195.95, 193.93, 191.91, 189.67, 187.23] #mm
d_down = [152.14, 153.56, 155.03, 156.41, 158.28, 159.95] #mm

d = np.array(d_up) - np.array(d_down) #mm
print(d)
m = list(range(6, 0, -1))

sigma = 0.02 #mm
foc = 110 #mm

fig, ax = plt.subplots()
t = np.polyfit(np.array(d)**2, m, 1)
f = np.poly1d(t)

k = (d[0]**2 - d[5]**2)/6
print('k =', k, 'мм^2')

sigma_k = ((2*sigma)**2 + (2*sigma)**2)**0.5
print('sigma_k=', sigma_k, 'мм^2')

lam = 5461 #Арм

L = lam * 0.1 * 10**(-9) * 4 * (foc * 10**(-3))**2 / (k*10**(-6))
print('L =', L, 'm')

sigma_L = L*((sigma_k/k)**2 + (0.05/foc)**2)**0.5
print('sigma_L =', sigma_L, 'm')

delta = 2*np.array(d)*sigma

plt.plot(m, np.polyval(np.polyfit(m, np.array(d)**2, 1), m), color = 'green')
plt.scatter(m, np.array(d)**2, s=7, c='black', marker='o', zorder = 1)
plt.errorbar(m, np.array(d)**2, yerr=delta, linestyle='none', color='black')
plt.xlabel('m')
plt.ylabel('d^2, мм^2')
plt.grid(linewidth = 0.5)
plt.title('График зависимости d^2(i) \n ртуть, зелёный фильтр')
plt.savefig('График зависимости d^2(i) для зелёного фильтра ртутной лампы.png')
plt.show()