import numpy as np
import matplotlib.pyplot as plt

#n = 2

F1 = [27.27, 27.37, 27.47, 27.57, 27.67, 27.77, 27.87, 27.97, 28.17, 28.27, 28.37, 28.47, 28.57, 28.67, 28.77, 28.87]
U1 = [0.430, 0.464, 0.502, 0.543, 0.586, 0.629, 0.666, 0.691, 0.690, 0.664, 0.626, 0.582, 0.537, 0.494, 0.453, 0.416]

#n = 7

F2 = [15.32, 15.42, 15.52, 15.62, 15.72, 15.82, 15.92, 16.02, 16.22, 16.32, 16.42, 16.52, 16.62, 16.72, 16.82, 16.92]
U2 = [0.172, 0.181, 0.192, 0.205, 0.217, 0.231, 0.243, 0.251, 0.250, 0.238, 0.221, 0.200, 0.179, 0.160, 0.142, 0.126]

fig, ax = plt.subplots()

t1 = np.polyfit(F1, U1, 1)
f1 = np.poly1d(t1)
t2 = np.polyfit(F2, U2, 1)
f2= np.poly1d(t2)

X = [0.95, 1.05]
Y = [1/(2)**0.5, 1/(2)**0.5]

plt.plot(np.array(F1)/28.07, np.array(U1)/(0.701), color='green', marker='o', markersize=2, label='C2 = 33.1 нФ')
plt.plot(np.array(F2)/16.12, np.array(U2)/(0.255), color='red', marker='o', markersize=2, label='C7 = 99.6 нФ')
plt.plot( X, Y, color='purple', label='1/sqrt2')
plt.legend()
plt.title('зависимость U(f) в относительных координатах')
plt.xlabel('f(x)/f(1)')
plt.ylabel('U(x)/U(1)')
plt.grid(linewidth = 1)
plt.savefig('график зависимости U(f) в относительных координатах.png')
plt.show()

