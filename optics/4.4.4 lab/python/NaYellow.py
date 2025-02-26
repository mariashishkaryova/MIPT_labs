import matplotlib.pyplot as plt
import numpy as np

sigma = 0.02 #mm
foc = 94 #mm

d_up1 = [174.5, 173, 171.44, 169.74, 167.73, 165.31, 162.19] #mm
d_down1 = [136.71, 138.05, 139.6, 141.38, 143.37, 145.75, 149.05] #mm

d_up2 = [174.01, 172.52, 170.91, 169.11, 167.14, 164.35, 160.53] #mm
d_down2 = [137.12, 138.51, 140.13, 141.99, 144.05, 146.61, 150.63] #mm

d_1 = np.array(d_up1) - np.array(d_down1) #mm
d_2 = np.array(d_up2) - np.array(d_down2) #mm

d_sred = (np.array(d_2) + np.array(d_1))/2 #mm
delta_d = np.array(d_1) - np.array(d_2) #mm
print(d_sred)
print(delta_d)

fig, ax = plt.subplots()
t = np.polyfit(d_sred, 1/np.array(delta_d), 1)
f = np.poly1d(t)

k = (d_sred[6] - d_sred[0])/(1/delta_d[6] - 1/delta_d[0])
print('k =', k, 'мм^2')

sigma_k = k*((sigma/d_sred[6])**2 + (sigma/d_sred[0])**2 + (sigma/delta_d[6])**2 + (sigma/delta_d[0])**2)**0.5
print('sigma_k =', sigma_k, 'мм^2')

lam = 5893 #Арм

delta_lam = lam * k * 10**(-6)/ (4 * (foc * 10**(-3))**2)
print('delta_lam =', delta_lam, 'Арм')
sigma_lam = delta_lam * ((sigma_k/k)**2 + (0.5/foc)**2)**0.5
print('sigma_lam =', sigma_lam, 'Арм')


Dexp = np.array(delta_d)/(2*delta_lam)
print('Dexp =', Dexp, 'кто-то')
sigma_Dexp = Dexp * ((sigma)**2 + (sigma_lam/delta_lam)**2)
print('sigma_Dexp =', sigma_Dexp, 'кто-то')

Dther = foc**2/np.array(d_1) * lam
sigma_Dther = Dther * ((sigma)**2 + (0.5/foc)**2)/(len(delta_d))**0.5
print('Dther =', Dther, '+/-', sigma_Dther)


R = sum(4 * foc**2/ (np.array(d_1) * 0.24))/len(delta_d)
sigmaR = R * (2*(sigma)**2 + (0.5/foc)**2)/(len(delta_d))**0.5
print('R =', R, '+/-', sigmaR)

L = lam * 0.1 * 10**(-9) * 4 * (foc * 10**(-3))**2 / (k*10**(-6))
N = R * lam / (2 * L)
print('N = ', N)



plt.plot(1/np.array(delta_d), np.polyval(np.polyfit(1/np.array(delta_d), d_sred, 1), 1/np.array(delta_d)), color = 'orange')
plt.scatter(1/np.array(delta_d), d_sred, s=10, c='black', marker='o', zorder = 1)
plt.errorbar(1/np.array(delta_d), d_sred, yerr = sigma/(2)**0.5, xerr = sigma*(2)**0.5/(np.array(delta_d)**2), linestyle = 'none', color = 'black')
plt.xlabel('1/delta_d, 1/мм')
plt.ylabel('d_sred, мм')
plt.grid(linewidth = 0.5)
plt.title('График зависимости d_sred(1/delta_d) \n натрий, жёлтый фильтр')
plt.savefig('График зависимости d_sred(1delta_d) для жёлтого фильтра натриевого лампы.png')
plt.show()