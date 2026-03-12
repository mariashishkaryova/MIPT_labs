import matplotlib.pyplot as plt

B = [1.284, 1.235, 1.136, 1.087, 0.889, 0.790, 0.692, 0.494]
H = [211, 187.5, 164, 152, 117, 87.9, 76.2, 58.6]

fig, ax = plt.subplots()

plt.scatter(H, B, s=30, c='black', marker='d', zorder = 1)
ax.errorbar(H, B, xerr=3, yerr=0.05, linestyle='none', color='black')
plt.grid(linewidth = 0.5)
plt.xlabel('H, А.м')
plt.ylabel('B, Тл')
plt.title('Кремнистое железо')
plt.savefig('Кремнистое железо.png')
plt.show()