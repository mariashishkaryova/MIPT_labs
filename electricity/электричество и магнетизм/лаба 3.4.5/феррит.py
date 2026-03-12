import matplotlib.pyplot as plt

B = [0.215, 0.2, 0.178, 0.166, 0.130, 0.1]
H = [13.8, 12.7, 10.3, 8.9, 8, 6.7]

fig, ax = plt.subplots()

plt.scatter(H, B, s=30, c='black', marker='d', zorder = 1)
ax.errorbar(H, B, xerr=0.3, yerr=0.003, linestyle='none', color='black')
plt.grid(linewidth = 0.5)
plt.xlabel('H, А.м')
plt.ylabel('B, Тл')
plt.title('Феррит')
plt.savefig('Феррит.png')
plt.show()