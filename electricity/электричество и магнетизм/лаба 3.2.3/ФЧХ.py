import numpy as np
import matplotlib.pyplot as plt

#n = 2

F1 = [27.27, 27.37, 27.47, 27.57, 27.67, 27.77, 27.87, 27.97, 28.17, 28.27, 28.37, 28.47, 28.57, 28.67, 28.77, 28.87]
fi1 = [-3.5, -3.3, -3, -2.5, -2.3, -2, -1.5, -1, -0.2, 0.4, 0.8, 1, 1.3, 1.5, 1.8, 2]

#n = 7

F2 = [15.32, 15.42, 15.52, 15.62, 15.72, 15.82, 15.92, 16.02, 16.22, 16.32, 16.42, 16.52, 16.62, 16.72, 16.82, 16.92]
fi2 = [-7.3, -7, -6.5, -6, -5.8, -5.3, -4.5, -3.5, -2, -1.3, -0.3, 0.4, 1, 1.5, 2, 2.3]

fig, ax = plt.subplots()

t1 = np.polyfit(F1, fi1, 1)
f1 = np.poly1d(t1)
t2 = np.polyfit(F2, fi2, 1)
f2= np.poly1d(t2)

X1 = [0.95, 1.05]
Y1 = [3.14/4, 3.14/4]

X2 = [0.95, 1.05]
Y2 = [-1/4, -1/4]

plt.plot(np.array(F1)/28.07, np.array(fi1)/3.14, color='green', marker='o', markersize=2, label='C2 = 33.1 нФ')
plt.plot(np.array(F2)/16.12, np.array(fi2)/3.14, color='red', marker='o', markersize=2, label='C7 = 99.6 нФ')
plt.plot( X1, Y1, color='purple', label='pi/4')
plt.plot( X2, Y2, color='purple', label='-pi/4')
plt.legend()
plt.title('зависимость fi(f) в относительных координатах')
plt.xlabel('f(x)/f(1)')
plt.ylabel('fi/pi')
plt.grid(linewidth = 1)
plt.savefig('график зависимости fi(f) в относительных координатах.png')
plt.show()

