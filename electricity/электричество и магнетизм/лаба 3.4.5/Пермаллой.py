import matplotlib.pyplot as plt

B = [0.131, 0.120, 0.09, 0.07, 0.05, 0.04, 0.027, 0.023]
H = [31.1, 28.9, 24.2, 22.2, 20, 19.9, 18.5, 17.7]

fig, ax = plt.subplots()

plt.scatter(H, B, s=30, c='black', marker='d', zorder = 1)
ax.errorbar(H, B, xerr=0.3, yerr=0.003, linestyle='none', color='black')
plt.grid(linewidth = 0.5)
plt.xlabel('H, А.м')
plt.ylabel('B, Тл')
plt.title('Пермаллой')
plt.savefig('Пермаллой.png')
plt.show()