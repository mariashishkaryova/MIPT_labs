import matplotlib.pyplot as plt
import numpy as np

Vpr = 12 #V, пробоя

Vn1 = 2.19 #V
Vkat1 = [0.58, 1.05, 1.19, 1.24, 1.27, 1.30, 1.34, 1.37,
        1.43, 1.49, 1.56, 1.64, 1.74, 1.7, 1.82, 1.87,
        2.15, 3, 4.05, 5.03, 6.03, 7.07, 8.04, 9.07, 10, 11.6] #V

Van1 = [0.1, 11.8, 30.7, 39.3, 45.2, 49.8, 54.3, 56.9, 62.5,
       65.7, 66.9, 65.0, 62.8, 64.7, 54.3, 52.7, 36.8, 14.8,
       8.6, 6.5, 5.7, 5.5, 5.9, 6.7, 9.5, 12.6] #mV


Vn2 = 2.51 #v
Vkat2 = [11.6, 9.97, 9.05, 8, 7, 6, 5.06,
         4.53, 4.03, 3.53, 3.04, 2.53, 2, 1.79,
         1.62, 1.42, 1.71, 1.503, 1.2, 1.07, 0.84, 0.58, 0.41] #V

Van2 = [50.1, 37, 27.8, 24, 22.9, 23.7, 27.4, 33.6, 39.7,
        49.3, 66.6, 98.8, 148, 161, 157.2, 132.1, 163.1, 145.4,
        76.4, 39.9, 5.39, 0.29, 0.11] #mV


fig, ax = plt.subplots()

plt.scatter(Vkat1, Van1, color='salmon', marker='*', s = 20, label = 'Vн = 2.19В')
plt.scatter(Vkat2, Van2, color='mediumpurple', marker='p', s = 25, label = 'Vн = 2.51В')
plt.title('ВАХ тиратрона')
plt.xlabel('V катода, В')
plt.ylabel('V анода, мВ')
plt.legend()
plt.grid(True)

plt.savefig('ВАХ титратрона.png')
plt.show()


fig2, ax2 = plt.subplots()

# Вычисляем ln(Van1/Vkat1), преобразуя mV в V для Van1
ln_ratio1 = [ -1 * np.log((van/1000)/vkat) if vkat != 0 and van != 0 else 0 for van, vkat in zip(Van1, Vkat1)]

# Вычисляем ln(Van2/Vkat2), преобразуя mV в V для Van2
ln_ratio2 = [ -1 * np.log((van/1000)/vkat) if vkat != 0 and van != 0 else 0 for van, vkat in zip(Van2, Vkat2)]

plt.scatter(Vkat1, ln_ratio1, color='salmon', marker='*', s = 20, label = 'Vн = 2.19В')
plt.scatter(Vkat2, ln_ratio2, color='mediumpurple', marker='p', s = 25, label = 'Vн = 2.51В')
plt.title('w(V)')
plt.xlabel('Vкат, В')
plt.ylabel('ln(Van/Vkat)')
plt.legend()
plt.grid(True)

plt.savefig('ln_Van_Vkat_зависимость.png')
plt.show()

Emax = 1.6 * 10**(-19) * 1.71
Emin = 1.6 * 10**(-19) * 7.0
h = 6.6 * 10**(-34)
me = 9.1 * 10**(-31)

l = 10**(8) * (h * 2.23) / (32 * me * (Emin - Emax))**0.5 #Aнг
print('l = ', l)

U0 = (4 * Emax / 5 - 9 * Emin / 5) / (1.6 * 10**(-19))
print('U0 = ', U0)

