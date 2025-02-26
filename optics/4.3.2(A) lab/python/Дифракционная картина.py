import matplotlib.pyplot as plt
import numpy as np

nu_1 = 1.19 #МГц
xm_1 = [1188, 1044, 892, 752, 584, 440, 268] #мкм
m_1 = [-3, -2, -1, 0, 1, 2, 3]
sigma = 2 #мкм
          #половина цены деления

k_1 = (xm_1[6] - xm_1[0])/(m_1[6] - m_1[0])
sigma_k1 = abs(k_1) * ((sigma/xm_1[6])**2 + (sigma/xm_1[0])**2)**0.5
print('k_1 = ', k_1, '+/-', sigma_k1, 'мкм')

nu_2 = 3.97 #МГц
xm_2 = [1336, 828, 712, 156, -520] #мкм
m_2 = [-2, -1, 0, 1, 2]

k_2 = (xm_2[4] - xm_2[0])/(m_2[4] - m_2[0])
sigma_k2 = abs(k_2) * ((sigma/xm_2[4])**2 + (sigma/xm_2[0])**2)**0.5
print('k_2 = ', k_2, '+/-', sigma_k2, 'мкм')

nu_3 = 1.59 #МГц
xm_3 = [1120, 916, 696, 625, 284] #мкм
m_3 = m_2

k_3 = (xm_3[4] - xm_3[0])/(m_3[4] - m_3[0])
sigma_k3 = abs(k_3) * ((sigma/xm_3[4])**2 + (sigma/xm_3[0])**2)**0.5
print('k_3 = ', k_3, '+/-', sigma_k3, 'мкм')

nu_4 = 1.83 #МГц
xm_4 = [1192, 928, 696, 464, 240] #мкм
m_4 = m_2

k_4 = (xm_4[4] - xm_4[0])/(m_4[4] - m_4[0])
sigma_k4 = abs(k_4) * ((sigma/xm_4[4])**2 + (sigma/xm_4[0])**2)**0.5
print('k_4 = ', k_4, '+/-', sigma_k4, 'мкм')



f = 30 #cm
L_1 = f * 10**(-2) * 675*10**(-9) / (k_1 * 10**(-6))
L_2 = f * 10**(-2) * 675*10**(-9) / (k_2 * 10**(-6))
L_3 = f * 10**(-2) * 675*10**(-9) / (k_3 * 10**(-6))
L_4 = f * 10**(-2) * 675*10**(-9) / (k_4 * 10**(-6))

sigma_l = 85 #нм
sigma_L1 = L_1 * ((sigma_l/675)**2 + (sigma_k1/k_1)**2 + (0.05/30)**2)**0.5
sigma_L2 = L_2 * ((sigma_l/675)**2 + (sigma_k2/k_2)**2 + (0.05/30)**2)**0.5
sigma_L3 = L_3 * ((sigma_l/675)**2 + (sigma_k3/k_3)**2 + (0.05/30)**2)**0.5
sigma_L4 = L_1 * ((sigma_l/675)**2 + (sigma_k4/k_4)**2 + (0.05/30)**2)**0.5

print('L1 =', L_1 * 10**3, '$\pm$', sigma_L1 * 10**3, 'mm')
print('L2 =', L_2 * 10**3, '$\pm$', sigma_L2 * 10**3, 'mm')
print('L3 =', L_3 * 10**3, '$\pm$', sigma_L3 * 10**3, 'mm')
print('L4 =', L_4 * 10**3, '$\pm$', sigma_L4 * 10**3, 'mm')

v_1 = nu_1*10**(6) * L_1 #м/c
sigma_v1 = v_1 * ((sigma_L1/L_1)**2 + (0.005/nu_1)**2)**0.5
print('v1 =', v_1, '$\pm$', sigma_v1, 'м/с')
v_2 = nu_2*10**(6) * L_2 #м/c
sigma_v2 = v_2 * ((sigma_L2/L_2)**2 + (0.005/nu_2)**2)**0.5
print('v2 =', v_2, '$\pm$', sigma_v2, 'м/с')
v_3 = nu_3*10**(6) * L_3 #м/c
sigma_v3 = v_3 * ((sigma_L3/L_3)**2 + (0.005/nu_3)**2)**0.5
print('v3 =', v_3, '$\pm$', sigma_v3, 'м/с')
v_4 = nu_4*10**(6) * L_4 #м/c
sigma_v4 = v_4 * ((sigma_L4/L_4)**2 + (0.005/nu_4)**2)**0.5
print('v4 =', v_4, '$\pm$', sigma_v4, 'м/с')



fig, ax = plt.subplots(figsize=(16, 8))

plt.subplot(2, 2, 1)
plt.plot(m_1, np.polyval(np.polyfit(m_1, xm_1, 1), m_1), color = 'r', lw = '2')
plt.scatter(m_1, xm_1, s=11, c='black', marker='o', zorder = 1)
plt.xlabel('m')
plt.ylabel('xm, мкм')
plt.grid(linewidth = 0.5)
plt.title(rf'График функции при $\nu$ = {nu_1} МГц')
plt.legend([f'k = {round(k_1, 2)} $\pm$ {round(sigma_k1, 2)} мкм'], fontsize=15)

plt.subplot(2, 2, 2)
plt.plot(m_2, np.polyval(np.polyfit(m_2, xm_2, 1), m_2), color = 'b', lw = '2')
plt.scatter(m_2, xm_2, s=11, c='black', marker='o', zorder = 1)
plt.xlabel('m')
plt.ylabel('xm, мкм')
plt.grid(linewidth = 0.5)
plt.title(rf'График функции при $\nu$ = {nu_2} МГц')
plt.legend([f'k = {round(k_2, 2)} $\pm$ {round(sigma_k2, 2)} мкм'], fontsize=15)

plt.subplot(2, 2, 3)
plt.plot(m_3, np.polyval(np.polyfit(m_3, xm_3, 1), m_3), color = 'm', lw = '2')
plt.scatter(m_3, xm_3, s=11, c='black', marker='o', zorder = 1)
plt.xlabel('m')
plt.ylabel('xm, мкм')
plt.grid(linewidth = 0.5)
plt.title(rf'График функции при $\nu$ = {nu_3} МГц')
plt.legend([f'k = {round(k_3, 2)} $\pm$ {round(sigma_k3, 2)} мкм'], fontsize=15)

plt.subplot(2, 2, 4)
plt.plot(m_4, np.polyval(np.polyfit(m_4, xm_4, 1), m_4), color = 'g', lw = '2')
plt.scatter(m_4, xm_4, s=11, c='black', marker='o', zorder = 1)
plt.xlabel('m')
plt.ylabel('xm, мкм')
plt.grid(linewidth = 0.5)
plt.title(rf'График функции при $\nu$ = {nu_4} МГц')
plt.legend([f'k = {round(k_4, 2)} $\pm$ {round(sigma_k4, 2)} мкм'], fontsize=15)

plt.subplots_adjust(hspace=0.3)
plt.savefig('График зависимости xm(m) при разных частотах.png')
plt.show()
