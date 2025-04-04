import matplotlib.pyplot as plt
import numpy as np

betha = [170, 160, 120, 105, 90, 75, 60, 45, 15, 0] #угол
h1 = np.array([10, 10, 9, 6, 6.5, 4.5, 2.5, 1.5, 6.5, 7.5]) * 0.2 #V
h2 = np.array([5.5, 5.5, 5.5, 5.6, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5]) * 0.2 #V
h3 = np.array([8.5, 7, 3, 3, 5.5, 6, 4.5, 4, 9, 12.5]) * 0.2 #V
h4 = np.array([21.5, 23.5, 26, 20.5, 17.5, 13.5, 11.5, 9.5, 14, 17.5]) * 0.2 #V

s_betha = 0.1
sig_h = 0.01 * 0.2 #V

delta = np.array(h1) / np.array(h2)
s_d = delta * ((sig_h/np.array(h1))**2 + (sig_h/np.array(h2))**2)**0.5

v1 = 2 * np.array(delta)**0.5 / (1 + np.array(delta))
s_v1 = v1 * s_d/np.array(delta)

v = (np.array(h4) - np.array(h3)) / (np.array(h4) + np.array(h3))
s_v = v * ((sig_h/np.array(h4))**2 + (sig_h/np.array(h3))**2)**0.5

v3 = np.array(v) / np.array(v1)
s_v3 = v3 * 10**(-1) * ((s_v/np.array(v))**2 + (s_v1/np.array(s_v1))**2)**0.5

fig1, ax1 = plt.subplots()
t1 = np.polyfit(v3, betha, 1)
f1 = np.poly1d(t1)

plt.scatter(betha, v3, s = 15, c='black', marker='o', zorder = 1)
plt.errorbar(betha, v3, yerr = s_v3, xerr = s_betha, linestyle='none', color='darkgreen')
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
plt.xlabel(r'$\beta$')
plt.ylabel('v3')
plt.title(r'график зависимости v3 от $\beta$')
plt.savefig('v3(betha).png')
plt.show()

x = np.array([10, 11, 75, 77.4, 79, 80.5, 82, 73, 70, 60, 55, 41, 28, 13, 9, 8]) * 10**(-2) #m
H1 = np.array([7.5 for _ in range(len(x))]) * 0.2 #V
H2 = np.array([5.5, 4.5, 8.5, 6.5, 3.5, 6.5, 6.5, 5, 6.5, 7, 10, 10.5, 6, 5.5, 2.5, 9.5]) * 0.2 #V
H3 = np.array([10, 6.5, 6.5, 7, 8.5, 7, 8, 7.5, 9, 14.5, 15.5, 15.5, 14, 7.5, 7, 11.5]) * 0.2 #V
H4 = np.array([26.5, 18, 18.5, 21, 25.5, 20.5, 19, 17.5, 17.5, 16.5, 18.5, 19.5, 14.5, 19, 14, 23.5]) * 0.2 #V

s_x = 0.1 * 10**(-2) #m

Delta = np.array(H1) / np.array(H2)
s_D = Delta * ((sig_h/np.array(H1))**2 + (sig_h/np.array(H2))**2)**0.5

V1 = 2 * np.array(Delta)**0.5 / (1 + np.array(Delta))
s_V1 = V1 * s_D/np.array(Delta)

V = (np.array(H4) - np.array(H3)) / (np.array(H4) + np.array(H3))
s_V = V * ((sig_h/np.array(H4))**2 + (sig_h/np.array(H3))**2)**0.5

V2 = np.array(V) / np.array(V1)
s_V2 = V2 * 10**(-1) * ((s_V/np.array(V))**2 + (s_V1/np.array(s_V1))**2)**0.5

fig2, ax2 = plt.subplots()
t2 = np.polyfit(V2, x * 10**2, 1)
f2 = np.poly1d(t2)

plt.scatter(x * 10**2, V2, s = 15, c='black', marker='o', zorder = 1)
plt.errorbar(x * 10**2, V2, yerr = s_V2, xerr = s_x * 10**2, linestyle='none', color='darkgreen')
#plt.plot(x * 10**2, V2, linestyle='--', color='orange')
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
plt.xlabel(r'x, cm')
plt.ylabel('v2')
plt.title(r'график зависимости v2 от x')
plt.savefig('v2(x).png')
plt.show()


L = 0.5 * (79 - 11) * 10**(-2) #m
s_L = 0.2 * 10**(-2)
c = 3 * 10**8 #m/c
print('L =', L, 'm')

d_nu = c/(2*L)
s_d_nu = d_nu * s_L/ L
print('d_nu =', d_nu * 10**(-8), 'pm', s_d_nu * 10**(-8), 'Hz')

l12 = 8 * 10**(-2)
s_l12 = 0.2 * 10**(-2)
D_F = 0.26 * c / l12
s_D_F = D_F * s_l12/ l12
print('2D_F =', 2 * D_F * 10**(-8), 'pm', s_D_F * 10**(-8), 'Hz')

N = 1 + 2 * D_F / d_nu
print('N =', N)
