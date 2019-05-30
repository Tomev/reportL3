import matplotlib.pyplot as plt
import numpy as np
import scipy as stats

# Get paths to images
path = "./Badania 2/TR/"

#neon = path + "ar.txt"
neon = path + "l2kr"

# Get data form csv
f = open(neon, "r")

### Laser 1
#x = [48 ,133 ,	200 ,	310 ,	354 ,	595 ,	655 ,	808 ,	993]
### Laser 2
x = [9 ,	77 ,	188 ,	232 ,	472 ,	533 ,	686 ,	872 ,	962]
y = [627, 630, 633, 638, 640, 651, 653, 660, 669]

quadraticFit = np.polyfit(x, y, 2)

quadraticFit[0] = np.round(quadraticFit[0], decimals=6)
quadraticFit[1] = np.round(quadraticFit[1], decimals=6)
quadraticFit[2] = np.round(quadraticFit[2], decimals=6)

a = quadraticFit[0]
b = quadraticFit[1]
c = quadraticFit[2]

x = []
y = []

line = f.readline()

while line:
    i = float(line.split('  ')[0])
    x.append(a * i**2 + b * i + c)
    #x.append(float(line.split('  ')[0]))
    y.append(float(line.split('  ')[1]))
    line = f.readline()

print(x)
print(y)

f.close()

plt.plot(x, y)
plt.title("Widmo lampy Kryptonowej")
plt.ylabel('Natężenie światła')
plt.xlabel('Długość fali (nm)')
plt.savefig("./figs/f112.png")
plt.show()


