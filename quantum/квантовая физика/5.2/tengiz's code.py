import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

elements = ['$Ra$', '$U$', '$Pu$', '$Am + Th$']
E_alpha = [4869.0, 5550.0, 6085.0, 7746.9]  # кэВ

# Периоды полураспада в секундах
T_half = [
    1580 * 365.25 * 24 * 3600,
    3.75 * 24 * 3600,
    3.25 * 60,
    1.58e-4
]
log_T = np.log10(T_half)
inv_sqrt_E = 1 / np.sqrt(E_alpha)


def linear_func(x, a, b):
    return a * x + b

popt, pcov = curve_fit(linear_func, inv_sqrt_E, log_T)
a, b = popt

E_smooth = np.linspace(min(E_alpha), max(E_alpha), 100)
inv_sqrt_E_smooth = 1 / np.sqrt(E_smooth)
log_T_smooth = linear_func(inv_sqrt_E_smooth, a, b)

plt.figure(figsize=(10, 6))
plt.scatter(inv_sqrt_E, log_T, color='brown',marker='o', s = 15, linewidth = 1, label='Экспериментальные точки')

plt.plot(inv_sqrt_E_smooth, log_T_smooth, color='mediumpurple',linewidth = 1.5, alpha=1,
         label=f'Аппроксимация: lg(T) = {a:.2f}/√E + {b:.2f}')

plt.xlabel('1/√E (кэВ$^{-1/2}$)', fontsize=12)
plt.ylabel('lg(T$_{1/2}$), с', fontsize=12)
plt.title('Закон Гейгера-Неттола', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
for i, elem in enumerate(elements):
    plt.annotate(elem, (inv_sqrt_E[i], log_T[i]),
                 xytext=(5, 5), textcoords='offset points',
                 fontsize=10, ha='left')

plt.tight_layout()
plt.savefig('Закон Г-Н.png')
plt.show()

print("Энергия α-частицы и соответствующие значения:")
print("Элемент | E (кэВ) | 1/√E (кэВ^-0.5) | lg(T1/2)")
for i in range(len(elements)):
    print(f"{elements[i]:12} | {E_alpha[i]:6.1f} | {inv_sqrt_E[i]:8.6f} | {log_T[i]:6.2f}")

print(f"\nПараметры аппроксимации: a = {a:.4f}, b = {b:.4f}")
