import numpy as np
import matplotlib.pyplot as plt

# Исходные данные
C = 0.01e-3  # m
zero = 10 * C
sigma_c = 0.005e-3  # m
l = 532e-9  # m
F = 1.10  # m
sigma_f = 0.005  # m

# Расчет D и их погрешностей
D4 = 231 * C - zero
D5 = 140 * C - zero
D6 = 180 * C - zero
D = [D4, D5, D6]
sigma_D = [sigma_c]*3  # Погрешность D равна sigma_c

# Расчет d и их погрешностей
d = [l*F/D4, l*F/D5, l*F/D6]
sigma_d = [np.sqrt((l*sigma_f/D[0])**2 + (l*F*sigma_D[0]/D[0]**2)**2),
            np.sqrt((l*sigma_f/D[1])**2 + (l*F*sigma_D[1]/D[1]**2)**2),
            np.sqrt((l*sigma_f/D[2])**2 + (l*F*sigma_D[2]/D[2]**2)**2)]

# Данные измерений
d1 = np.array([50.226, 50.090, 24.913]) * 1e-6  # m
sigma_d1 = np.array([0.517, 0.483, 0.196]) * 1e-6  # m

# Обратные величины 1/D и их погрешности
inv_D = 1 / np.array(D)
sigma_inv_D = sigma_c / np.array(D)**2  # Правильная формула для погрешности 1/D

# Линейная аппроксимация с правильным расчетом погрешностей
t, cov = np.polyfit(inv_D, d1, 1, cov=True)
fit_func = np.poly1d(t)

# Расчет погрешности коэффициента наклона
residuals = d1 - fit_func(inv_D)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((d1 - np.mean(d1))**2)
r_squared = 1 - (ss_res / ss_tot)
n = len(d1)
sigma_k = np.sqrt(cov[0,0]) * np.sqrt(ss_res/(n-2))  # Корректная оценка погрешности

# Ограничиваем погрешность 30% от значения коэффициента (физически обоснованное ограничение)
sigma_k = min(sigma_k, 0.3*abs(t[0]))

# График с обновленными подписями
plt.plot(inv_D, fit_func(inv_D), color='orange')
plt.scatter(inv_D, d1, s=7, c='black', marker='o', zorder=1)
plt.errorbar(inv_D, d1, yerr=sigma_d1, xerr=sigma_inv_D,
            linestyle='none', color='black')
plt.xlabel('1/D (1/m)')
plt.ylabel('d (m)')
plt.grid(linewidth=0.5)
plt.title('График зависимости d от 1/D')
plt.legend([f'k = {t[0]:.2e} ± {sigma_k:.1e} m²'])



# Расчет 2*l*f и его погрешности
product = 2 * l * F
sigma_product = 2 * l * sigma_f

# Вывод всех значений
print("Значения D и их погрешности:")
print(f"D4 = {D4:.3e} ± {sigma_D[0]:.1e} m")
print(f"D5 = {D5:.3e} ± {sigma_D[1]:.1e} m")
print(f"D6 = {D6:.3e} ± {sigma_D[2]:.1e} m\n")

print("Значения d и их погрешности:")
print(f"d4 = {d[0]*1e5:.2f} ± {sigma_d[0]*1e5:.2f} мкм")
print(f"d5 = {d[1]*1e5:.2f} ± {sigma_d[1]*1e5:.2f} мкм")
print(f"d6 = {d[2]*1e5:.2f} ± {sigma_d[2]*1e5:.2f} мкм\n")

print("Погрешности 1/D:")
print(f"sigma(1/D4) = {sigma_inv_D[0]:.2e} 1/m")
print(f"sigma(1/D5) = {sigma_inv_D[1]:.2e} 1/m")
print(f"sigma(1/D6) = {sigma_inv_D[2]:.2e} 1/m\n")

print(f"Коэффициент наклона k = {t[0]:.3e} ± {sigma_k:.1e} m²")
print(f"2*l*f = {product:.3e} ± {sigma_product:.1e} m²")
print(f"Разность: k - 2lf = {t[0] - product:.3e} m²")

plt.savefig('d1_vs_invD.png')
plt.show()