import numpy as np
import matplotlib.pyplot as plt

# Данные
theta = np.deg2rad(list(range(0, 121, 10)))
sigm_theta = np.deg2rad(1)

N = np.array([812, 824, 720, 677, 661, 555, 522, 439, 392, 360, 330, 304, 280])
sigma_N = np.array([8, 7, 4, 8, 10, 10, 5, 5, 5, 4, 4, 3, 3])

# Вычисление величин
x = 1 - np.cos(theta)
y = 1 / N

# Погрешности
sigma_x = np.sin(theta) * sigm_theta
sigma_y = sigma_N / N**2

# Линейная аппроксимация
t = np.polyfit(x, y, 1)
f = np.poly1d(t)

# Построение графика
plt.figure(figsize=(10, 6))
plt.errorbar(x, y, xerr=sigma_x, yerr=sigma_y, fmt='o', capsize=3, markersize=2)
plt.plot(x, f(x), 'r-', label=f'y = ({t[0]:.4f} ± {np.sqrt(np.cov(x, y)[0,0]):.4f})x + ({t[1]:.4f} ± {np.sqrt(np.cov(x, y)[1,1]):.4f})')

plt.xlabel('1 - cos(θ)')
plt.ylabel('1/N')
plt.title('1/N = f(1 - cos(θ))')
plt.grid(True, alpha=0.3)
plt.legend()
plt.savefig('1N от (1 - cos(theta)).png')
plt.show()

# Нахождение N(0) и его погрешности
y_at_zero = f(0)  # 1/N при theta=0
N_at_zero = 1 / y_at_zero
sigma_N_at_zero = sigma_y[np.argmin(x)] * N_at_zero**2  # погрешность N(0)

# Нахождение N(90) и его погрешности
theta_90 = np.deg2rad(90)
x_90 = 1 - np.cos(theta_90)
y_90 = f(x_90)  # 1/N при theta=90
N_at_90 = 1 / y_90
sigma_N_at_90 = sigma_y[np.argmin(np.abs(theta - theta_90))] * N_at_90**2  # погрешность N(90)

# Вычисление энергии покоя и погрешности
E0 = 662  # кэВ
mc2 = E0 * (N_at_90 / (N_at_zero - N_at_90))
sigma_mc2 = mc2 * np.sqrt((sigma_N_at_90/N_at_90)**2 + ((sigma_N_at_zero + sigma_N_at_90)/(N_at_zero - N_at_90))**2)

# Вывод результатов
print("Коэффициенты линейной зависимости:")
print(f"k = {t[0]:.6f} ± {np.sqrt(np.cov(x, y)[0,0]):.6f}")
print(f"b = {t[1]:.6f} ± {np.sqrt(np.cov(x, y)[1,1]):.6f}")
print(f"Уравнение: y = ({t[0]:.4f} ± {np.sqrt(np.cov(x, y)[0,0]):.4f})x + ({t[1]:.4f} ± {np.sqrt(np.cov(x, y)[1,1]):.4f})")
print('\nРасчётные величины:')
print(f"N(θ=0°) = {N_at_zero:.1f} ± {sigma_N_at_zero:.1f}")
print(f"N(θ=90°) = {N_at_90:.1f} ± {sigma_N_at_90:.1f}")
print(f"\nmc² = {mc2:.1f} ± {sigma_mc2:.1f} кэВ")