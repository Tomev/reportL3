import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


np.set_printoptions(suppress=True)

x = [9 ,	77 ,	188 ,	232 ,	472 ,	533 ,	686 ,	872 ,	962]
y = [627, 630, 633, 638, 640, 651, 653, 660, 669]

# x = [1, 2, 3, 4, 5, 6, 7]
# y = [1, 4, 9, 16, 25, 36, 49]

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
line = [slope * i + intercept for i in x]

print(str(slope) + "(fn) + " + str(intercept) )

quadraticFit = np.polyfit(x, y, 2)

quadraticFit[0] = np.round(quadraticFit[0], decimals=6)
quadraticFit[1] = np.round(quadraticFit[1], decimals=6)
quadraticFit[2] = np.round(quadraticFit[2], decimals=6)

print(quadraticFit)

a = quadraticFit[0]
b = quadraticFit[1]
c = quadraticFit[2]

lambdal = [np.round(slope * i + intercept) for i in x]
lambdaq = [np.round(a * i**2 + b * i + c) for i in x]

print(lambdal)
print(lambdaq)

el = 0
eq = 0

for i in range(len(lambdaq)):
    el += abs(y[i] - lambdal[i])
    eq += abs(y[i] - lambdaq[i])


print("el = " + str(el))
print("eq = " + str(eq))

plt.plot(x, y, 'ro', x, line)
plt.title("Simple Plot of KH")
plt.ylabel('Długość fali')
plt.xlabel('Fotodioda')
plt.savefig("figs/SimplePlot.png")
plt.show()
