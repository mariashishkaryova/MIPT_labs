import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#Фон
t = 5 * 60 #sec
nf = 3929
nf_sec = nf / t

#Начальное
t0 = 20 #sec
n0 = 102317
n0_sec = n0 / t0 - nf_sec

#Свинец
l1 = [4.97, 9.77, 14.67, 19.87, 24.67, 29.57, 33.97, 38.77] #mm
n1 = [85281, 48291, 36189, 25819, 18673, 13300, 9683, 7133]
t1 = [30, 30, 40, 50, 60, 70, 80, 90]
n1_sec = np.array(n1) / np.array(t1) - nf_sec

#Аллюминий
l2 = [19.9, 39.9, 60, 80.1, 99.8, 119.9, 140.2, 159.8] #mm
n2 = [33527, 22422, 14568, 9747, 9826, 8421, 8806, 6038]
t2 = [10, 10, 10, 10, 15, 20, 30, 30]
n2_sec = np.array(n2) / np.array(t2) - nf_sec

#Чугун
l3 = [10, 20.2, 30.4, 40.4, 50.4, 60.6, 70.8, 80.9] #mm
n3 = [169647, 94517, 53435, 30776, 17834, 10300, 6277, 3902]
t3 = [60]*8
n3_sec = np.array(n3) / np.array(t3) - nf_sec

sigma_t = 1 #sec

sigma_l = 0.05
sigma_n1 = []*8
sigma_n2 = []*8
sigma_n3 = []*8

for i in range(len(n1)):
    sigma1 = n1_sec[i] * ((sigma_t / t1[i])**2 + (1 /n1_sec[i]))**0.5
    sigma_n1.append(sigma1)

    sigma2 = n2_sec[i] * ((sigma_t / t2[i])**2 + (1 / n2_sec[i]))**0.5
    sigma_n2.append(sigma2)

    sigma3 = n3_sec[i] * ((sigma_t / t3[i])**2 + (1 / n3_sec[i]))**0.5
    sigma_n3.append(sigma3)

sigma_n0 = n0_sec * ((sigma_t / t0) ** 2 + (1 / n0_sec)) ** 0.5
sigma_nf = n0_sec * ((sigma_t / t0) ** 2 + (1 / nf_sec)) ** 0.5

# Свинец
y1 = np.log(n0_sec / n1_sec)
sigma_y1 = [y1[i] * ((sigma_n1[i] / n1_sec[i])**2 + (sigma_n0 / n0_sec)**2)**0.5 for i in range(len(sigma_n1))]

fig1, ax1 = plt.subplots()
slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(l1, y1)
f1 = np.poly1d([slope1, intercept1])

plt.scatter(l1, y1, s=7, c='orange', marker='o', zorder=1, label='Экспериментальные точки')
plt.errorbar(l1, y1, xerr=sigma_l, yerr=sigma_y1, linestyle='none', color='purple')
plt.plot(l1, f1(l1), color='red', linewidth=1, label=f'y = ({slope1:.4f} ± {std_err1:.4f})x + ({intercept1:.4f})')
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
plt.xlabel(r'l, mm')
plt.ylabel(r'ln(N0/N)')
plt.title(r'Свинец')
plt.legend()
plt.savefig('Свинец.png')
plt.show()

# Алюминий
y2 = np.log(n0_sec / n2_sec)
sigma_y2 = [y2[i] * ((sigma_n2[i] / n2_sec[i])**2 + (sigma_n0 / n0_sec)**2)**0.5 for i in range(len(sigma_n2))]

fig2, ax2 = plt.subplots()
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(l2, y2)
f2 = np.poly1d([slope2, intercept2])

plt.scatter(l2, y2, s=7, c='orange', marker='o', zorder=1, label='Экспериментальные точки')
plt.errorbar(l2, y2, xerr=sigma_l, yerr=sigma_y2, linestyle='none', color='darkgreen')
plt.plot(l2, f2(l2), color='red', linewidth=1, label=f'y = ({slope2:.4f} ± {std_err2:.4f})x + ({intercept2:.4f})')
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
plt.xlabel(r'l, mm')
plt.ylabel(r'ln(N0/N)')
plt.title(r'Алюминий')
plt.legend()
plt.savefig('Алюминий.png')
plt.show()

# Чугун
y3 = np.log(n0_sec / n3_sec)
sigma_y3 = [y3[i] * ((sigma_n3[i] / n3_sec[i])**2 + (sigma_n0 / n0_sec)**2)**0.5 for i in range(len(sigma_n3))]

fig3, ax3 = plt.subplots()
slope3, intercept3, r_value3, p_value3, std_err3 = stats.linregress(l3, y3)
f3 = np.poly1d([slope3, intercept3])

plt.scatter(l3, y3, s=7, c='orange', marker='o', zorder=1, label='Экспериментальные точки')
plt.errorbar(l3, y3, xerr=sigma_l, yerr=sigma_y3, linestyle='none', color='black')
plt.plot(l3, f3(l3), color='red', linewidth=1, label=f'y = ({slope3:.4f} ± {std_err3:.4f})x + ({intercept3:.4f})')
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
plt.xlabel(r'l, mm')
plt.ylabel(r'ln(N0/N)')
plt.title(r'Железо')
plt.legend()
plt.savefig('Чугун.png')
plt.show()

print('N0 =', n0_sec, '+/-', sigma_n0)
print('Nf =', f'{nf_sec:.0f}')
print('n1_sec =', n1_sec)
print('sigma_n1 =', sigma_n1)
print('n2_sec =', n2_sec)
print('sigma_n2 =', sigma_n2)
print('n3_sec =', n3_sec)
print('sigma_n3 =', sigma_n3)
