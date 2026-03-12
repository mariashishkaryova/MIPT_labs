import numpy as np
import matplotlib.pyplot as plt

T1 = 30
P_1 = (0.2*9.81)*np.array([188, 188, 188, 188, 188, 188]) #Па
deltaP_1 = P_1 - 9.8*(1.45*10**(-2))*995.6
sigmanat_1 = (deltaP_1*1.3*(10**(-3)))/4
print(T1, P_1, "Па",sigmanat_1*(10**(3)), "мН/м" )

t1 = np.polyfit(deltaP_1, sigmanat_1, 1)
f1 = np.poly1d(t1)



T2 = 35
P_2 = (0.2*9.81)*np.array([190, 190, 190, 190, 190, 190]) #Па
deltaP_2 = P_2 - 9.8*(1.45*10**(-2))*994
sigmanat_2 = (deltaP_2*1.3*(10**(-3)))/4
print(T2, P_2, "Па",sigmanat_2*(10**(3)), "мН/м" )

t2 = np.polyfit(deltaP_2, sigmanat_2, 1)
f2 = np.poly1d(t2)



T3 = 40
P_3 = (0.2*9.81)*np.array([188, 188, 188, 188, 188, 188]) #Па
deltaP_3 = P_3 - 9.8*(1.45*10**(-2))*992.2
sigmanat_3 = (deltaP_3*1.3*(10**(-3)))/4
print(T3, P_3, "Па",sigmanat_3*(10**(3)), "мН/м" )

t3 = np.polyfit(deltaP_3, sigmanat_3, 1)
f3 = np.poly1d(t3)



T4 = 45
P_4 = (0.2*9.81)*np.array([186.5, 186.5, 186.5, 186.5, 186.5, 186.5]) #Па
deltaP_4 = P_4 - 9.8*(1.45*10**(-2))*990.2
sigmanat_4 = (deltaP_4*1.3*(10**(-3)))/4
print(T4, P_4, "Па",sigmanat_4*(10**(3)), "мН/м" )

t4 = np.polyfit(deltaP_4, sigmanat_4, 1)
f4 = np.poly1d(t4)



T5 = 50
P_5 = (0.2*9.81)*np.array([186, 186, 186, 186, 186, 186]) #Па
deltaP_5 = P_5 - 9.8*(1.45*10**(-2))*988
sigmanat_5 = (deltaP_5*1.3*(10**(-3)))/4
print(T5, P_5, "Па",sigmanat_5*(10**(3)), "мН/м" )

t5= np.polyfit(deltaP_5, sigmanat_5, 1)
f5 = np.poly1d(t5)



T6 = 55
P_6 = (0.2*9.81)*np.array([184.5, 184.5, 184.5, 184.5, 184.5, 184.5]) #Па
deltaP_6 = P_6 - 9.8*(1.45*10**(-2))*985.7
sigmanat_6 = (deltaP_6*1.3*(10**(-3)))/4
print(T6, P_6, "Па",sigmanat_6*(10**(3)), "мН/м" )

t6 = np.polyfit(deltaP_6, sigmanat_6, 1)
f6 = np.poly1d(t6)




sigmanat = np.array([f1(0),f2(0), f3(0), f4(0),f5(0), f6(0)])
T = np.array([T1,T2, T3,T5, T4, T6])
sr_T = sum(T)/6
sr_sigmanat = sum(sigmanat)/6
sr_Tsigmanat = sum(T*sigmanat)/6
sr_T_kv = sum(T**2)/6
sr_kv_T = sr_T**2
sr_sigmanat_kv = sum(sigmanat**2)/6
sr_kv_sigmanat = sr_sigmanat**2
k = (sr_Tsigmanat - sr_T*sr_sigmanat)/(sr_T_kv - sr_kv_T)
sigma_angle = (1/(6**0.5))*(((sr_sigmanat_kv - sr_kv_sigmanat)/(sr_T_kv - sr_kv_T) - k**2)**0.5)
print(k, sigma_angle)


fig, ax = plt.subplots()

t = np.polyfit(T, sigmanat, 1)
f = np.poly1d(t)

plt.scatter(T, sigmanat, c="r", zorder = 1)
plt.plot(T, f(T),
         linestyle='-', alpha = 1,
         color = "black", ms=5, zorder = 0)
plt.grid(linewidth = 0.5)

plt.ylabel('sigmanat, Н/м', fontsize=10)
plt.xlabel('T, ℃', fontsize=10)
plt.savefig("График коэффициента поверхностного натяжения от температуры", dpi=600)

plt.show()


