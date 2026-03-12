import math
import numpy as np

R0 = 560
R = np.arange(24, 77, 4) #кОм

x1 = [213, 182, 154, 138, 124, 187, 164, 156, 146, 211, 194, 175, 194, 177]
x2 = [20, 22, 22, 25, 25, 44, 43, 46, 45, 73, 68, 66, 74, 69]

theta = [math.log(x1[i] / x2[i]) for i in range(len(x1))]
print('theta = ', theta)

R_cr = [((R[i] * 1000 + R0) / (1 + 4 * math.pi ** 2 / theta[i] ** 2) - R0) for i in range(len(R))]
print('R_cr =', np.array(R_cr) * 10**(-3) + 6, 'кОм')
print(len(R))

R_cr_sr = (sum(R_cr) * 10**(-3)) / len(R_cr)
print('Rkr =', R_cr_sr + 6)