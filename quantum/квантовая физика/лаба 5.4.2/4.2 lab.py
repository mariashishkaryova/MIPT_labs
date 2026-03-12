import numpy as np
import matplotlib.pyplot as plt

#до калибровки
I = [0.2, 0.4, 0.6, 0.8, 0.9, 1.0, 1.05, 1.2, 1.4, 1.6, 1.8, 2.0, 2.1, 2.15, 2.20, 2.25, 2.3, 2.4, 2.45, 2.5, 2.55, 2.6, 2.65, 2.7, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 3.9, 4.0, 4.2, 4.3, 4.5, 4.8, 5.0] #А
N_Nf = [-0.00016, 0.03, 0.1898, 0.1498, 0.1298, 0.3897, 0.3797, 1.0195, 1.9493, 3.4080, 4.9584, 5.7282, 6.8578, 7.7876, 7.0278, 8.0975, 8.4474, 7.7376, 8.4174, 7.9275, 7.8676, 7.8376, 7.5876, 7.7076, 6.9578, 6.4980, 4.8284, 2.9790, 1.6893, 1.1795, 1.0695, 2.3991, 2.9690, 1.3095, 1.1595, 2.0692, 1.9093] #1/c

#калибровка
p = [48.3, 48.3, 96.6, 144.9, 193.2, 217.3, 241.5, 253.6, 289.8, 338.1, 386.4, 434.7, 483.0, 507.1, 519.2, 531.3, 543.3, 555.4, 579.6, 591.6, 603.7, 615.8, 627.9, 639.9, 652.0, 676.1, 724.4, 772.7, 821.0, 869.3, 917.6, 941.8, 965.9, 1014.2, 1038.4, 1086.7, 1159.1] #кэВ / c

#энергетический спектр
T = [2.3, 9.0, 20.1, 35.3, 44.3, 54.2, 59.4, 76.4, 101.7, 129.6, 159.9, 192.1, 208.9, 217.5, 226.1, 234.9, 243.7, 261.7, 270.8, 279.9, 289.2, 298.5, 307.9, 317.4, 336.5, 375.5, 415.4, 456.1, 497.4, 539.3, 560.5, 581.8, 624.7, 646.3, 689.8, 755.7, 800.1] #кэВ

#график Ферми
mkFermi = [0.0000, 181.9290, 249.7895, 144.1403, 112.4466, 166.3611, 152.6247,
    204.6932, 224.6038, 243.1066, 245.7168, 225.4945, 229.3178, 235.8937,
    216.4953, 224.6851, 222.0457, 199.3696, 201.6102, 189.8156, 183.5619,
    177.9522, 170.1599, 166.7581, 158.0280, 130.7312, 182.2942, 73.3648,
    50.7082, 39.0702, 35.7826, 51.5954, 53.3461, 34.1992, 30.0600, 36.4516, 32.9347]

error_I = [0.01 * abs(val) for val in I]
error_N_Nf = [0.05 * abs(val) for val in N_Nf]
error_p = [0.01 * val for val in p]
error_T = [0.01 * val for val in T]
error_mkFermi = [0.05 * abs(val) for val in mkFermi]


fig1, ax1 = plt.subplots()
t1 = np.polyfit(I, N_Nf, 1)
f1 = np.poly1d(t1)

plt.scatter(I, N_Nf, s = 7, c='orange', marker='o', zorder = 1)
plt.errorbar(I, N_Nf, xerr=error_I, yerr = error_N_Nf, linestyle='none', color='purple')
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
plt.xlabel(r'I, A')
plt.ylabel(r'N - Nf, 1/c')
plt.title(r'Спектр $\beta$ распада')
plt.savefig('Спектр распада.png')
plt.show()


fig2, ax2 = plt.subplots()
t2 = np.polyfit(p, N_Nf, 1)
f2 = np.poly1d(t2)

plt.scatter(p, N_Nf, s = 7, c='orange', marker='o', zorder = 1)
plt.errorbar(p, N_Nf, xerr=error_p, yerr = error_N_Nf, linestyle='none', color='darkgreen')
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
plt.xlabel(r'p, кэВ/c')
plt.ylabel(r'N - Nf, 1/c')
plt.title(r'калибровка')
plt.savefig('Калибровка.png')
plt.show()


fig3, ax3 = plt.subplots()
t3 = np.polyfit(T, N_Nf, 1)
f3 = np.poly1d(t3)

plt.scatter(T, N_Nf, s = 7, c='orange', marker='o', zorder = 1)
plt.errorbar(T, N_Nf, xerr=error_T, yerr = error_N_Nf, linestyle='none', color='black')
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
plt.xlabel(r'T, кэВ')
plt.ylabel(r'N - Nf, 1/c')
plt.title(r'энергетический спектр')
plt.savefig('энергетический спектр.png')
plt.show()


fig4, ax4 = plt.subplots()
T_filtered = []
mkFermi_filtered = []
for i in range(len(T)):
    if 159 <= T[i] <= 545 and T[i] != 415.4:
        T_filtered.append(T[i])
        mkFermi_filtered.append(mkFermi[i])

t4 = np.polyfit(T_filtered, mkFermi_filtered, 1)
f4 = np.poly1d(t4)
errors = np.sqrt(abs(np.cov(abs(np.array(T_filtered)), abs(np.array(mkFermi_filtered)))))

plt.scatter(T, mkFermi, s = 7, c='orange', marker='o', zorder = 1)
T_line = np.linspace(min(T_filtered), max(T_filtered), 100)
plt.plot(T_line, f4(T_line), 'r-', linewidth=1, label=f'y = ({t4[0]:.3f}±{errors[0,0] * 10**(-4):.3f})x + ({t4[1]:.3f}±{errors[1,1] * 10**(-1):.3f})')
plt.errorbar(T, mkFermi, xerr=error_T, yerr = error_mkFermi, linestyle='none', color='darkblue')
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
plt.xlabel(r'T, кэВ')
plt.ylabel(r'mkFermi')
plt.legend()
plt.title(r'график Ферми')
plt.savefig('график Ферми.png')
plt.show()

E_max = - t4[1] / t4[0]
err_E = E_max * ((errors[0,0] * 10**(-4) / t4[0])**2 + (errors[1,1] * 10**(-1) / t4[1])**2)**0.5

print('E_max =', E_max, '+/-', err_E, 'кэВ')