import matplotlib.pyplot as plt
import numpy as np

#Градуировка
theta = [2600, 2328, 2300, 2297, 2277, 2266, 2240, 2219, 2206, 2178, 2159, 1887] #угол тетта, градус
lamda = [7032, 6217, 6164, 6143, 6096, 6074, 6030, 5976, 5945, 5882, 5852, 5331] #длина волны, Армстренг
sigm_theta = 0.5 #градусов, погрешность измерения угла тетта

fig1, ax1 = plt.subplots()
t = np.polyfit(theta, lamda, 1)
f = np.poly1d(t)

plt.scatter(theta, lamda, s = 10, c='black', marker='o', zorder = 1)
plt.errorbar(theta, lamda, xerr=0.5, linestyle='none', color='darkgreen')
plt.plot(theta, np.polyval(np.polyfit(theta, lamda, 1), theta), linestyle='-', color='orange')
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
plt.xlabel(r'$\theta$, $\circ$')
plt.ylabel(r'$\lambda$, $\AA$')
# Добавление легенды с уравнением прямой и коэффициентом наклона
slope = np.polyfit(theta, lamda, 1)[0]  # коэффициент наклона
equation = f'λ(θ) = {slope:.3f}·θ + {np.polyfit(theta, lamda, 1)[1]:.1f}'
plt.legend([f'{equation}\nk = {slope:.3f} Å/$\circ$'])
plt.title(r'градуировка монохроматора')
plt.savefig('градуировка монохроматора.png')
plt.show()
#уравнение прямой на графике выше - закон, по которому зная значения углов тетта можно найти длины волн лямбда,
#на которых в дальнейшем производили измерения.

print(f'λ(θ) = {slope:.3f}·θ + {np.polyfit(theta, lamda, 1)[1]:.1f}')


#Измерения
sigma_I = 0.001 #погрешность измерения силы тока I
sigma_V = 0.001 #погрешность измерения напряжения V

#Зная уравнение прямой лямда от угла тетта и значения углов, можно найти значения lamda{i} для i = 1,2,3,4,5. и погрешность всех лямда

theta1 = 2300
I1 = [0.506, 0.609, 0.636, 0.260, 0.022, 0.027]
V1 = [0.008, 0.760, 1.188, -0.244, -0.410, -0.655]

theta2 = 1500
I2 = [0.458, 0.506, 0.563, 0.428, 0.130, 0.027]
V2 = [0.008, 0.361, 1.323, -0.106, -0.504, -0.707]

theta3 = 2090
I3 = [0.568, 0.573, 0.608, 0.028, 0.060, 0.453]
V3 = [0.008, 0.0485, 0.0992, -0.977, -0.489, -0.159]

theta4 = 1900
I4 = [0.499, 0.543, 0.576, 0.030, 0.004, 0.316]
V4 = [0.008, 0.334, 0.736, -1.000, -0.720, -0.328]

theta5 = 1700
I5 = [0.481, 0.522, 0.548, 0.0054, 0.392, 0.005]
V5 = [0.008, 0.294, 0.0602, -0.589, -0.243, -0.749]


theta = [theta1, theta2, theta3, theta4, theta5]
lamda = [0]*5
for i in range(5):
    lamda[i] = int(t[0]) * theta[i] + t[1]
    print(f'lamda{i+1} = {lamda[i]}')

sigma_lamda = np.array(lamda) * (sigm_theta / np.array(theta))
print("sigm_l =", sigma_lamda)

I = [I1, I2, I3, I4, I5]
Isqrt = []  # Инициализируем пустой список

for i in range(5):  # 5 списков (I1-I5)
    temp_list = []
    for j in range(6):  # 6 элементов в каждом списке
        temp_list.append(np.sqrt(I[i][j]))  # Используем np.sqrt
    Isqrt.append(temp_list)
    print(f'Isqrt{i + 1} = {Isqrt[i]}')

sigma_Isqrt = []
for i in range(5):
    list_s = []
    for j in range(6):
        list_s.append(np.array(Isqrt[i][j]) * (sigma_I / (2 * np.array(Isqrt[i][j])**0.5)))
    sigma_Isqrt.append(list_s)

fig2, ax2 = plt.subplots()

plt.scatter(V1, Isqrt[0], s = 10, c='orange', marker='o', zorder = 1)
plt.errorbar(V1, Isqrt[0], xerr=sigma_V, yerr = sigma_Isqrt[0], linestyle='none', color='darkgreen')
plt.plot(V1, np.polyval(np.polyfit(V1, Isqrt[0], 1), V1), linestyle='-', color='orange', label = f'λ1 = {lamda[0]:.0f} Å')

plt.scatter(V2, Isqrt[1], s = 10, c='blue', marker='o', zorder = 1)
plt.errorbar(V2, Isqrt[1], xerr=sigma_V, yerr = sigma_Isqrt[1], linestyle='none', color='darkgreen')
plt.plot(V2, np.polyval(np.polyfit(V2, Isqrt[1], 1), V2), linestyle='-', color='blue', label = f'λ2 = {lamda[1]:.0f} Å')

plt.scatter(V3, Isqrt[2], s = 10, c='red', marker='o', zorder = 1)
plt.errorbar(V3, Isqrt[2], xerr=sigma_V, yerr = sigma_Isqrt[2], linestyle='none', color='darkgreen')
plt.plot(V3, np.polyval(np.polyfit(V3, Isqrt[2], 1), V3), linestyle='-', color='red', label = f'λ3 = {lamda[2]:.0f} Å')

plt.scatter(V4, Isqrt[3], s = 10, c='green', marker='o', zorder = 1)
plt.errorbar(V4, Isqrt[3], xerr=sigma_V, yerr = sigma_Isqrt[3], linestyle='none', color='darkgreen')
plt.plot(V4, np.polyval(np.polyfit(V4, Isqrt[3], 1), V4), linestyle='-', color='green', label = f'λ4 = {lamda[3]:.0f} Å')

plt.scatter(V5, Isqrt[4], s = 10, c='pink', marker='o', zorder = 1)
plt.errorbar(V5, Isqrt[4], xerr=sigma_V, yerr = sigma_Isqrt[4], linestyle='none', color='darkgreen')
plt.plot(V5, np.polyval(np.polyfit(V5, Isqrt[4], 1), V5), linestyle='-', color='pink', label = f'λ5 = {lamda[4]:.0f} Å')

plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
plt.xlabel(r'V, В')
plt.ylabel(r'√I, √A')
plt.legend()
plt.title(r'Зависимость фототока от напряжения')
plt.savefig('√I(V).png')
plt.show()


V = [V1, V2, V3, V4, V5]

V0 = []
sigm_V0 = []

for i in range(5):
    # Аппроксимируем прямую с получением ковариационной матрицы
    coeffs, cov = np.polyfit(V[i], Isqrt[i - 1], 1, cov=True)
    k, b = coeffs

    # Извлекаем дисперсии коэффициентов из ковариационной матрицы
    sigm_k_sq = cov[0, 0]
    sigm_b_sq = cov[1, 1]
    cov_kb = cov[0, 1]  # ковариация между k и b

    # Погрешность V0 по формуле распространения ошибок
    sigm_v_zero = np.sqrt(sigm_b_sq / k ** 2 +
                          b ** 2 * sigm_k_sq / k ** 4 -
                          2 * b * cov_kb / k ** 3)

    # Находим точку пересечения с осью V (y=0)
    v_zero = -b / k

    V0.append(v_zero)
    sigm_V0.append(sigm_v_zero)

print("V0 = ", V0)
print('sigma V0 =', sigm_V0)

#print(lamda)
c = 3 * 10**8
w = [2 * 3.14 * c / (lamda[i] * 10**(-10)) for i in range(len(lamda))]
print('w =', np.array(w) / 10**15, '*10^15 рад/с')
sigm_w = np.array(w) * ((sigma_lamda / np.array(lamda)))
print('sigm_w =', sigm_w)

coeffs = np.polyfit(np.array(w) / 10**15, V0, 1)
slope, intercept = coeffs

# Форматируем уравнение для отображения в легенде
equation = f'y = {slope:.3f} * 10^15 x {intercept:.3f}'

# Создаем маску для исключения второй точки
mask = np.ones(len(w), dtype=bool)
mask[2] = False  # исключаем вторую точку (индекс 1)

# Применяем маску ко всем массивам
filtered_w = np.array(w)[mask] / 10**15
filtered_V0 = np.array(V0)[mask]
filtered_sigm_w = np.array(sigm_w)[mask] / 10**15
filtered_sigm_V0 = np.array(sigm_V0)[mask]

# Строим график
plt.scatter(filtered_w, filtered_V0, s=10, c='black', marker='o', zorder=1, label='Экспериментальные точки')
plt.errorbar(filtered_w, filtered_V0, xerr=filtered_sigm_w, yerr=filtered_sigm_V0, linestyle='none', color='b')
plt.plot(np.array(w) / 10**15, np.polyval(np.polyfit(np.array(w) / 10**15, V0, 1), np.array(w) / 10**15), linestyle='-', color='green', label=equation)
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
plt.ylabel(r'V0, В')
plt.xlabel(r'$\omega$, *10^15 рад/с')
plt.legend()
plt.title(r'Зависимость V0 от частоты $\omega$')
plt.savefig('V0(w).png')
plt.show()

# Расчет погрешности коэффициента наклона
residuals = V0 - (slope * (np.array(w) / 10**15) + intercept)
mse = np.sum(residuals**2) / (len(V0) - 2)
x_data = np.array(w) / 10**15
x_mean = np.mean(x_data)
sxx = np.sum((x_data - x_mean)**2)
sigma_slope = np.sqrt(mse / sxx)

print(f'Коэффициент наклона: {slope:.6f} ± {sigma_slope:.6f}')
print(f'Относительная погрешность наклона: {abs(sigma_slope/slope)*100:.2f}%')

h = slope * 1.6
s_h = h * sigma_slope/slope
print('h =', h, '+/-', s_h)

A = 1.6 * 10**(-19) * np.array(V0) - h * 10**(-34) * np.array(w)
s_A = A * ((np.array(sigm_w) / np.array(w))**2 + (np.array(sigm_V0) / np.array(V0))**2)**0.5
A_sr = sum(A) / len(A)
s_A_sr = sum(s_A) / len(A)
print("W =", A, "+/-", s_A)
