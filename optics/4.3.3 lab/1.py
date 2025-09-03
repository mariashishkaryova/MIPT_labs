import numpy as np

sigma_L = 1 * 10 ** (-2)  # m
sigma_x = 1 * 10 ** (-3)  # m
lambd = 532 * 10 ** (-9)  # m

# сетка №1:
L1 = 141.5 * 10 ** (-2)  # m
mx1 = 2
x1 = np.array([151, 150, 150]) * 10 ** (-3)  # m
my1 = 2
y1 = np.array([152, 152, 151]) * 10 ** (-3)  # m

# сетка №2:
L2 = 142 * 10 ** (-2)  # m
mx2 = 2
x2 = np.array([149, 149, 150]) * 10 ** (-3)  # m
my2 = 2
y2 = np.array([151, 151, 150]) * 10 ** (-3)  # m

# сетка №3:
L3 = 141.5 * 10 ** (-2)  # m
mx3 = 5
x3 = np.array([151, 151, 150]) * 10 ** (-3)  # m
my3 = 5
y3 = np.array([151, 151, 151]) * 10 ** (-3)  # m

# сетка №4:
L4 = 141 * 10 ** (-2)  # m
mx4 = 5
x4 = np.array([151, 151, 150]) * 10 ** (-3)  # m
my4 = 5
y4 = np.array([151, 151, 151]) * 10 ** (-3)  # m

# сетка №5:
L5 = 144 * 10 ** (-2)  # m
mx5 = 8
x5 = np.array([122, 122, 122]) * 10 ** (-3)  # m
my5 = 8
y5 = np.array([123, 123, 123]) * 10 ** (-3)  # m

# сетка №6:
L6 = 144 * 10 ** (-2)  # m
mx6 = 8
x6 = np.array([122, 121, 122]) * 10 ** (-3)  # m
my6 = 8
y6 = np.array([123, 123, 122]) * 10 ** (-3)  # m

# Создадим списки для удобного доступа к переменным
x_lists = [x1, x2, x3, x4, x5, x6]
y_lists = [y1, y2, y3, y4, y5, y6]
L_values = [L1, L2, L3, L4, L5, L6]
mx_values = [mx1, mx2, mx3, mx4, mx5, mx6]
my_values = [my1, my2, my3, my4, my5, my6]

for i in range(6):
    # Получаем текущие значения
    current_x = x_lists[i]
    current_y = y_lists[i]
    current_L = L_values[i]
    current_mx = mx_values[i]

    # среднее x + y
    sred_delt = (np.sum(current_x) + np.sum(current_y)) / (len(current_x) + len(current_y))
    delta_x = np.zeros(len(current_x))
    delta_y = np.zeros(len(current_y))

    # отклонение от среднего x и y
    for j in range(len(current_x)):
        delta_x[j] = (current_x[j] - sred_delt) ** 2
    for j in range(len(current_y)):
        delta_y[j] = (current_y[j] - sred_delt) ** 2

    # погрешность sred_delt
    sigma_delt = ((1 / (len(current_x) + len(current_y) + 1)) * (np.sum(delta_x) + np.sum(delta_y))) ** 0.5
    error_delt = (sigma_x ** 2 + sigma_delt ** 2) ** 0.5

    # угол fi
    fi = sred_delt / current_L
    sigma_fi = fi * ((sigma_L / current_L) ** 2 + (error_delt / sred_delt) ** 2) ** 0.5

    # перевод в градусы
    fi_deg = np.degrees(fi) #рад
    sigma_fi_deg = np.degrees(sigma_fi) #рад

    # период решётки
    d = current_mx * lambd / np.sin(fi)
    sigma_d = d * ((sigma_fi / fi) ** 2) ** 0.5

    print(f'delta_x{i + 1} =', sred_delt * 100, '+/-', error_delt * 100, 'cm')
    print(f'fi{i + 1} =', fi_deg, '° +/-', sigma_fi_deg, '°')
    print(f'период d{i + 1} =', d * 10 ** 6, '+/-', sigma_d * 10 ** (6), 'mkm')
    print()