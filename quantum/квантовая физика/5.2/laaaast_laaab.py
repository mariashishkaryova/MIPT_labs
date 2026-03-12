import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Калибровка по пикам радия

N = [2541, 2030, 1866, 1637]
E = [7.6, 6.0, 5.2, 4.6]

fig, ax = plt.subplots()
t = np.polyfit(N, E, 1)
f = np.poly1d(t)
print(f)

# Построение графика
plt.scatter(N, E, color='m', marker='o', s = 10, linewidth = 1, alpha=1)
plt.plot(N, np.polyval(np.polyfit(N, E, 1), N), color='brown',linewidth = 1.5, alpha=1, label = f'E = {t[0]:.4f}*N + {t[1]:.4f}')
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('N', fontsize=12)
plt.ylabel('E, МэВ', fontsize=12)
plt.title('Калибровочный график \n Ei = f(Ni)', fontsize=14)
plt.legend()
plt.savefig('Калибровка.png')
plt.show()

#Спектр Радия
df = pd.read_excel('Радий.xlsx', header=None, skiprows=6)

# Извлечение данных из двух колонок (например, колонки 0 и 1)
N_rad = df[0].values  # Первая колонка
counts_rad = df[1].values  # Вторая колонка

E_rad = np.array(N_rad) * t[0] + t[1]
plt.plot(E_rad, counts_rad, color='m', linewidth = 0.5, alpha=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('E, МэВ', fontsize=12)
plt.ylabel('N', fontsize=12)
plt.title('Спкетр Радия', fontsize=14)
plt.savefig('Радий.png')
plt.show()

#Спектр 241Am + 230Th
df = pd.read_excel('Am+Th.xlsx', header=None, skiprows=6)

# Извлечение данных из двух колонок (например, колонки 0 и 1)
N_amth = df[0].values  # Первая колонка
counts_amth = df[1].values  # Вторая колонка

E_amth = np.array(N_amth) * t[0] + t[1]
plt.plot(E_amth, counts_amth,  color='m', linewidth = 0.5, alpha=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('E, МэВ', fontsize=12)
plt.ylabel('N', fontsize=12)
plt.title('Спкетр 241Am + 230Th', fontsize=14)
plt.savefig('241Am + 230Th.png')
plt.show()


#Спектр Плутония
df = pd.read_excel('Pu.xlsx', header=None, skiprows=6)

# Извлечение данных из двух колонок (например, колонки 0 и 1)
N_pu = df[0].values  # Первая колонка
counts_pu = df[1].values  # Вторая колонка

E_pu = np.array(N_pu) * t[0] + t[1]
plt.plot(E_pu, counts_pu,  color='m',linewidth = 0.5, alpha=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('E, МэВ', fontsize=12)
plt.ylabel('N', fontsize=12)
plt.title('Спкетр Плутония', fontsize=14)
plt.savefig('Плутоний.png')
plt.show()


#Спектр Урана
df = pd.read_excel('U.xlsx', header=None, skiprows=6)

# Извлечение данных из двух колонок (например, колонки 0 и 1)
N_u = df[0].values  # Первая колонка
counts_u = df[1].values  # Вторая колонка

E_u = np.array(N_u) * t[0] + t[1]
plt.plot(E_u, counts_u,  color='m',linewidth = 0.5, alpha=1)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('E, МэВ', fontsize=12)
plt.ylabel('N', fontsize=12)
plt.title('Спкетр Урана', fontsize=14)
plt.savefig('Уран.png')
plt.show()

def Rfl (Uo, delt):
    return delt / Uo

Uo_rad = sum(E_rad) / len(E_rad)
Uo_pu = sum(E_pu) / len(E_pu)
Uo_u = sum(E_u) / len(E_u)
Uo_amth= sum(E_amth) / len(E_amth)

R_rad = np.sqrt(sum(E_rad) / len(E_rad) * E_rad)
R_pu =  np.sqrt(sum(E_pu) / len(E_pu) * E_pu)
R_u =  np.sqrt(sum(E_u) / len(E_u) * E_u)
R_amth =  np.sqrt(sum(E_amth) / len(E_amth) * E_amth)



print('R_rad =', R_rad)
print('R_pu =', R_pu)
print('R_u =', R_u)
print('R_amth =', R_amth)





