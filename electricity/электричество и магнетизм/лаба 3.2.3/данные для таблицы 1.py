import numpy as np
import matplotlib.pyplot as plt

R = 3.91
R_1 = 953


C_1 = 22 * 10**(-9)
f_1 = 34.36 * 10**(3)
U_1 = 1.0067
E_1 = 0.178

L_1 = 1/(C_1 * (2 * 3.14 * f_1)**2)
Ro_1 = 1/(2 * 3.14 * f_1 * C_1)
Z_1 = U_1 * R_1/ E_1
Q_1 = Z_1* 2 * 3.14 * f_1 * C_1
Rsum_1 = 1 / (Z_1 * (2 * 3.14 * f_1 * C_1)**2)
Rsmax_1 = Ro_1 * 10**(-3)
Rl_1 = Rsum_1 - R - Rsmax_1
print('L_1 =', L_1, 'Гн')
print('Ro_1 =', Ro_1, 'Ом')
print('Z_1 =', Z_1, 'Ом')
print('Q_1 =', Q_1)
print('Rsum_1 =', Rsum_1, 'Ом')
print('Rsmax_1 =', Rsmax_1, 'Ом')
print('Rl_1 =', Rl_1, 'Ом')



C_2 = 33.1 * 10**(-9)
f_2 = 28.07 * 10**(3)
U_2 = 0.7014
E_2 = 0.179

L_2 = 1/(C_2 * (2 * 3.14 * f_2)**2)
Ro_2 = 1/(2 * 3.14 * f_2 * C_2)
Z_2 = U_2 * R_1/ E_2
Q_2 = Z_2* 2 * 3.14 * f_2 * C_2
Rsum_2 = 1 / (Z_2 * (2 * 3.14 * f_2 * C_2)**2)
Rsmax_2 = Ro_2 * 10**(-3)
Rl_2 = Rsum_2 - R - Rsmax_2
print('L_2 =', L_2, 'Гн')
print('Ro_2 =', Ro_2, 'Ом')
print('Z_2 =', Z_2, 'Ом')
print('Q_2 =', Q_2)
print('Rsum_2 =', Rsum_2, 'Ом')
print('Rsmax_2 =', Rsmax_2, 'Ом')
print('Rl_2 =', Rl_2, 'Ом')



C_3 = 47.9 * 10**(-9)
f_3 = 23.61 * 10**(3)
U_3 = 0.5082
E_3 = 0.179

L_3 = 1/(C_3 * (2 * 3.14 * f_3)**2)
Ro_3 = 1/(2 * 3.14 * f_3 * C_3)
Z_3 = U_3 * R_1/ E_3
Q_3 = Z_3* 2 * 3.14 * f_3 * C_3
Rsum_3 = 1 / (Z_3 * (2 * 3.14 * f_3 * C_3)**2)
Rsmax_3 = Ro_3 * 10**(-3)
Rl_3 = Rsum_3 - R - Rsmax_3
print('L_3 =', L_3, 'Гн')
print('Ro_3 =', Ro_3, 'Ом')
print('Z_3 =', Z_3, 'Ом')
print('Q_3 =', Q_3)
print('Rsum_3 =', Rsum_3, 'Ом')
print('Rsmax_3 =', Rsmax_3, 'Ом')
print('Rl_3 =', Rl_3, 'Ом')



C_4 = 57.4 * 10**(-9)
f_4 = 21.30 * 10**(3)
U_4 = 0.4215
E_4 = 0.180

L_4 = 1/(C_4 * (2 * 3.14 * f_4)**2)
Ro_4 = 1/(2 * 3.14 * f_4 * C_4)
Z_4 = U_4 * R_1/ E_4
Q_4 = Z_4* 2 * 3.14 * f_4 * C_4
Rsum_4 = 1 / (Z_4 * (2 * 3.14 * f_4 * C_4)**2)
Rsmax_4 = Ro_4 * 10**(-3)
Rl_4 = Rsum_4 - R - Rsmax_4
print('L_4 =', L_4, 'Гн')
print('Ro_4 =', Ro_4, 'Ом')
print('Z_4 =', Z_4, 'Ом')
print('Q_4 =', Q_4)
print('Rsum_4 =', Rsum_4, 'Ом')
print('Rsmax_4 =', Rsmax_4, 'Ом')
print('Rl_4 =', Rl_4, 'Ом')



C_5 = 66.7 * 10**(-9)
f_5 = 19.74 * 10**(3)
U_5 = 0.3659
E_5 = 0.180

L_5 = 1/(C_5 * (2 * 3.14 * f_5)**2)
Ro_5 = 1/(2 * 3.14 * f_5 * C_5)
Z_5 = U_5 * R_1/ E_5
Q_5 = Z_5 * 2 * 3.14 * f_5 * C_5
Rsum_5 = 1 / (Z_5 * (2 * 3.14 * f_5 * C_5)**2)
Rsmax_5 = Ro_5 * 10**(-3)
Rl_5 = Rsum_5 - R - Rsmax_5
print('L_5 =', L_5, 'Гн')
print('Ro_5 =', Ro_5, 'Ом')
print('Z_5 =', Z_5, 'Ом')
print('Q_5 =', Q_5)
print('Rsum_5 =', Rsum_5, 'Ом')
print('Rsmax_5 =', Rsmax_5, 'Ом')
print('Rl_5 =', Rl_5, 'Ом')



C_6 = 82.1 * 10**(-9)
f_6 = 17.78 * 10**(3)
U_6 = 0.3025
E_6 = 0.180

L_6 = 1/(C_6 * (2 * 3.14 * f_6)**2)
Ro_6 = 1/(2 * 3.14 * f_6 * C_6)
Z_6 = U_6 * R_1/ E_6
Q_6 = Z_6 * 2 * 3.14 * f_6 * C_6
Rsum_6 = 1 / (Z_6 * (2 * 3.14 * f_6 * C_6)**2)
Rsmax_6 = Ro_6 * 10**(-3)
Rl_6 = Rsum_6 - R - Rsmax_6
print('L_6 =', L_6, 'Гн')
print('Ro_6 =', Ro_6, 'Ом')
print('Z_6 =', Z_6, 'Ом')
print('Q_6 =', Q_6)
print('Rsum_6 =', Rsum_6, 'Ом')
print('Rsmax_6 =', Rsmax_6, 'Ом')
print('Rl_6 =', Rl_6, 'Ом')



C_7 = 99.6 * 10**(-9)
f_7 = 16.12 * 10**(3)
U_7 = 0.2545
E_7 = 0.181

L_7 = 1/(C_7 * (2 * 3.14 * f_7)**2)
Ro_7 = 1/(2 * 3.14 * f_7 * C_7)
Z_7 = U_7 * R_1/ E_7
Q_7 = Z_6 * 2 * 3.14 * f_7 * C_7
Rsum_7 = 1 / (Z_7 * (2 * 3.14 * f_7 * C_7)**2)
Rsmax_7 = Ro_7 * 10**(-3)
Rl_7 = Rsum_7 - R - Rsmax_7
print('L_7 =', L_7, 'Гн')
print('Ro_7 =', Ro_7, 'Ом')
print('Z_7 =', Z_7, 'Ом')
print('Q_7 =', Q_7)
print('Rsum_7 =', Rsum_7, 'Ом')
print('Rsmax_7 =', Rsmax_7, 'Ом')
print('Rl_7 =', Rl_7, 'Ом')



L = [L_1, L_2, L_3, L_4, L_5, L_6, L_7]
L_sred = sum(L)/len(L)
L_sredkv = (sum((np.array(L) - L_sred)**2)/(len(L) - 1))**0.5
print("L среднее = ",L_sred)
print('L среднекв отклонение = ',L_sredkv)


RL = [Rl_1, Rl_2, Rl_4, Rl_5, Rl_6, Rl_7]
RL_sred = sum(RL)/len(RL)
RL_sredkv = (sum((np.array(RL) - RL_sred)**2)/(len(RL) - 1))**0.5
print("RL среднее = ", RL_sred)
print('RL среднекв отклонение = ', RL_sredkv)


F = [f_7, f_6, f_4, f_3, f_2, f_1]

X = [f_7 * 0.6, f_1 * 0.6]
Y = [RL_sred, RL_sred]

fig, ax = plt.subplots()

t = np.polyfit(F, RL, 1)
f = np.poly1d(t)

plt.plot(np.array(F) * 0.6, RL, color='green', marker='o', markersize=2, label='Rl(f)')
plt.plot(X, Y, color='purple', label='RL_sred')
plt.legend()
plt.xlabel('f * 0.6')
plt.ylabel('RL')
plt.title('зависимость RL(f)')
plt.grid(linewidth = 1)
plt.savefig('график зависимости RL(f).png')
plt.show()

print('I = ', E_2/R_1)
print('Ic = ', Q_2 * E_2/ R_1)


