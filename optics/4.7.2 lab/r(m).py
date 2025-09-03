import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


#измерение №1
r1 = [8, 29, 41, 50, 58, 64, 70, 76, 80] #mm

#измерение №2
r2 = [9, 30, 43, 51, 59, 65, 71, 76, 81] #mm

#измерение №3
r3 = [9, 30, 42, 51, 59, 65, 71, 76, 80] #mm

#измерение №4
r4 = [8, 30, 41, 51, 58, 65, 70, 76, 81] #mm

s_r = 1 #mm

r = (np.array(r1) + np.array(r2) + np.array(r3) + np.array(r4))/4

sigma_r = [0]*len(r)

for i in range(len(r)):
    sigma_r[i] = ((1/4) * ((r1[i] - r[i])**2 + (r2[i] - r[i])**2 + (r3[i] - r[i])**2 + (r4[i] - r[i])**2))**0.5

error_r = (np.array(s_r)**2 + np.array(sigma_r)**2)**0.5

for i in range(len(r)):
    print(f'r{i} =', r[i], '+/-', error_r[i], 'mm')

m = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Вычисляем r^2 и его погрешность
r_squared = r ** 2
error_r_squared = 2 * r * error_r  # Погрешность r^2

# Линейная регрессия
slope, intercept, r_value, p_value, std_err = linregress(m, r_squared)

# Создаем переменную для коэффициента наклона
slope_value = slope

# Определяем значения для линейной зависимости
m_fit = np.linspace(min(m), max(m), 100)
r_squared_fit = slope_value * m_fit + intercept

# Отображаем линейную зависимость на графике
plt.plot(m_fit, r_squared_fit, color='red', label=f'k = {slope_value:.2f} ± {std_err:.2f} $mm^2$')
# Построение графика
plt.errorbar(m, r_squared, yerr=error_r_squared, fmt='o', capsize=7, markersize=4)
# Настройки графика
plt.xlabel('m')
plt.ylabel(r'$r^2$, $mm^2$')
plt.title(r'График зависимости $r^2$(m)')
plt.legend()
plt.grid()
plt.savefig('График зависимости r^2(m).png')
plt.show()

# Выводим коэффициент наклона
print(f'Коэффициент наклона прямой: {slope_value:.2f} ± {std_err:.2f} mm^2')


lamda = 632.8 * 10**(-9) #m
l = 3 * 10**(-2) #m
s_l = 0.5 * 10**(-2) #m
L = 75 * 10**(-2) #m
s_L = 1 * 10**(-2) #m
n0 = 2.29

n0_ne = lamda * (n0 * L)**2 / (l * slope * 10**(-6))
sigma_n0_ne = n0_ne * ((s_l/l)**2 + (s_L/L)**2 + (std_err/slope)**2)**0.5
print(f' n0 - ne = {n0_ne} ± {sigma_n0_ne}')
