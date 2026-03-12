import matplotlib.pyplot as plt
import numpy as np

a = 41 * 10**(-6) #В/цельсий   постоянная термопары
Troom = 20 #цельсий   комнатная температура

print('ПУНКТ 1 \n')
#1 АЧТ
Tabb_p = 1090 #цельсий   пирометром

Vabb = 42.59 * 10**(-3) #В  термопара
Tabb_t = (Vabb / a) - Troom

s_Troom = 0.5 #цельсий
s_Vabb = 0.005 * 10**(-3) #В
s_Tabb_t = Tabb_t * ((s_Vabb / Vabb)**2 + (s_Troom / Troom)**2)**0.5

print('Температура АЧТ, измеренная пирометром, =', Tabb_p, 'град цельсия')
print('Температура АЧТ, измеренная термопарой, =', Tabb_t, '+/-', s_Tabb_t, 'град цельсия')


print('ПУНКТ 2 \n')
#2 Кольца
Tk1 = 807 #цельсий
Tk2 = 809 #цельсий
#данные взяты у соседей, трубка с кольцами не нагрелась
print('Температура колец равна', Tk1, 'и', Tk2, 'град цельсия')

print('ПУНКТ 3 \n')
#3 Закон Стефана - Больцмана
T_p_ya = np.arange(900, 1901, 100, dtype=float) #цельсий
#T_th = (np.array([5, 4.2, 3.85, 3.45, 2.91, 2.58, 2.13, 1.79, 1.78, 1.47, 1.54])*10**(-3) / a) - Troom #цельсий
I = [0.5, 0.52, 0.57, 0.62, 0.78, 0.80, 0.81, 0.82, 0.88, 0.99, 1.06] #А
V = [1.57, 1.73, 2.16, 2.72, 4.54, 4.74, 4.93, 5.08, 5.86, 7.38, 8.40] #В

print('Яркостная температура нити =', np.array(T_p_ya) + 273, 'K')

#из лабника:
Et = [0.081, 0.105, 0.119, 0.133, 0.144, 0.164, 0.179, 0.195, 0.209, 0.223, 0.236]

S = 5 #см^2

W = np.array(V) * np.array(I)
s_W = np.array(W) * ( (0.05 / np.array(I))**2 + (0.01 / np.array(V))**2 )**2
print('W =', W, 'Вт')
print('погрешность W =', s_W, 'Вт')

sigma = np.array(W) / (np.array(Et) * S * (np.array(T_p_ya) + 273)**4)
s_sigma = np.array(sigma) * ( (0.05 / np.array(I))**2 + (0.01 / np.array(V))**2 + (1 / np.array(T_p_ya))**2 + (s_W / np.array(W))**2 )**0.5
print('постоянная Стефана - Больцмана =', sigma, 'Вт/ см^2 * K^4')
print('погрешность пост стеф больцм =', s_sigma, 'Вт/ см^2 * K^4')

# Логарифмирование данных
lnW = np.log(W)
lnT_ya = np.log((np.array(T_p_ya ) + 273))

fig, ax = plt.subplots()
t = np.polyfit(lnT_ya, lnW, 1)
f = np.poly1d(t)

# Построение графика
plt.scatter(lnT_ya, lnW, color='salmon', marker='*', s = 50,linewidth = 2, alpha=0.7)
plt.plot(lnT_ya, np.polyval(np.polyfit(lnT_ya, lnW, 1), lnT_ya), color='mediumpurple',linewidth = 3, alpha=0.5, label = f'n = {t[0]:.4f}')

# Добавление сетки и оформление
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('ln(T)', fontsize=12)
plt.ylabel('ln(W)', fontsize=12)
plt.title('Логарифмическая зависимость мощности от температуры\nlnW = f(lnT)', fontsize=14)
plt.legend()
plt.savefig('Логарифмическая зависимость.png')
plt.show()
print('коэффициент наклона k =', f)


kB = 1.380649e-23  # постоянная Больцмана, Дж/К
c = 299792458      # скорость света, м/с

h = ((2 * np.pi**5 * kB**4) / (15 * c**2 * sigma * 1e-4))**(1/3)

# Погрешность постоянной Планка
s_h = (1/3) * h * (s_sigma / sigma)

print('Постоянная Планка =', h, 'Дж·с')
print('Погрешность постоянной Планка =', s_h, 'Дж·с')


print('ПУНКТ 4 \n')
#4 Неоновая лампа
T_neon_p = 1.09 * 10**(-3) / a - Troom

print('яркостная температура неона = 848 град цельсия')
print('температура нити, вычесленная при помощи термопары =', T_neon_p, 'град цельсия')
