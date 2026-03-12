import numpy as np
import matplotlib.pyplot as plt

#n = 2

F1 = np.array([27.27, 27.37, 27.47, 27.57, 27.67, 27.77, 27.87, 27.97, 28.17, 28.27, 28.37, 28.47, 28.57, 28.67, 28.77, 28.87])/(2)**0.5
U1 = np.array([0.430, 0.464, 0.502, 0.543, 0.586, 0.629, 0.666, 0.691, 0.690, 0.664, 0.626, 0.582, 0.537, 0.494, 0.453, 0.416])/(2)**0.5

F2 = np.array([15.32, 15.42, 15.52, 15.62, 15.72, 15.82, 15.92, 16.02, 16.22, 16.32, 16.42, 16.52, 16.62, 16.72, 16.82, 16.92])/(2)**0.5
U2 = np.array([0.172, 0.181, 0.192, 0.205, 0.217, 0.231, 0.243, 0.251, 0.250, 0.238, 0.221, 0.200, 0.179, 0.160, 0.142, 0.126])/(2)**0.5

fig, ax = plt.subplots()

t1 = np.polyfit(F1, U1, 1)
f1 = np.poly1d(t1)
t2 = np.polyfit(F2, U2, 1)
f2= np.poly1d(t2)

plt.plot(F1, U1 / 2 ** 0.5, color='green', marker='o', markersize=2, label='C2 = 33.1 нФ')
plt.plot(F2, U2 / 2 ** 0.5, color='red', marker='o', markersize=2, label='C7 = 99.6 нФ')
plt.legend()
plt.title('зависимость U(f)')
plt.xlabel('f, кГц')
plt.ylabel('U, В')
plt.grid(linewidth = 1)
plt.savefig('график зависимости U(f).png')
plt.show()

