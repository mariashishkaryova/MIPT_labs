import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

b = 27 * 10**(-5) #m

zero = 49 * 10**(-2) #m
n1 = np.arange(5, 0, -1)
x1 = np.array([49.5, 49.7, 49.8, 50.3, 50.9]) * 10**(-2) #m

z = np.array(x1) - np.array(zero) #m
s_z = 0.1 * 2**0.5 * 10**(-2)#m
print('z =', z * 100, 'cm')

lam = 5461 * 10**(-10) #m

ksi = (np.array(z) * (np.array(n1) + 1) * lam)**0.5
sigma_ksi = (s_z/np.array(z)) * np.array(ksi)
for i in range(len(ksi)):
    print(f'2 * ksi[{i}] =', 2 * ksi[i] * 10**6, '+/-', sigma_ksi[i] * 10**6, 'mkm')

fig1, ax1 = plt.subplots()
t1 = np.polyfit(2 * ksi * 10**6, n1, 1)
f1 = np.poly1d(t1)

b1 = [87*3 for _ in range(len(n1))] #mkm
b2 = [14 * 20 for _ in range(len(n1))] #mkm
print('b1 =', b1[0] * 10**(-3), 'mm')
print('b2 =', b2[0] * 10**(-3), 'mm')

plt.scatter(n1, 2 * ksi * 10**6, s = 20, c='black', marker='o', zorder = 1)
plt.errorbar(n1, 2 * ksi * 10**6, yerr=sigma_ksi * 10**6, linestyle='none', color='darkgreen')
plt.plot(n1, b1, linestyle='--', color='orange', label = 'b, измеренная винтом')
plt.plot(n1, b2, linestyle='--', color='red', label = 'b, измеренная микроскопом')
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
plt.xlabel('n')
plt.ylabel(r'2$\xi_{m}$, mkm')
plt.legend()
plt.title(r'график зависимости 2$\xi_{m}$ от n')
plt.savefig('ksi(n).png')
plt.show()



m = n1 + 1
# 2. Построение модели (линейная регрессия)
slope, intercept, r_value, p_value, std_err = stats.linregress(m, z)

# 3. Расчет ожидаемых значений
z_expected = slope * m + intercept

# 4. Расчет хи-квадрат
O_i = z
E_i = z_expected
chi_squared = np.sum((O_i - E_i)**2 / E_i)

# 5. Степени свободы
n = len(m)
degrees_of_freedom = n - 2

# 6. Сравнение с критическим значением
alpha = 0.05  # уровень значимости
critical_value = stats.chi2.ppf(1 - alpha, degrees_of_freedom)

# Вывод результатов
print(f"Коэффициент наклона (m): {slope}")
print(f"Свободный член (b): {intercept}")
print(f"Значение хи-квадрат: {chi_squared}")
print(f"Критическое значение хи-квадрат: {critical_value}")

if chi_squared > critical_value:
    print("Нулевая гипотеза отвергается: данные не могут быть апроксимированы прямой.")
else:
    print("Нулевая гипотеза не отвергается: данные могут быть апроксимированы прямой.")

# Визуализация
plt.scatter(m, z, s = 20, color='red', label='Экспериментальные точки')
plt.plot(m, z_expected, color='blue', label='Апроксимированная прямая')
plt.xlabel('m')
plt.ylabel('z')
plt.legend()
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
plt.savefig('z(m).png')
plt.show()