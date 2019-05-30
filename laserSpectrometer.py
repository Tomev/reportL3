import matplotlib.pyplot as plt
import glob
import numpy as np
from scipy import stats


# Get paths to images
path = "./Badania 2/TR/"

neon = path + "Ne.txt"

# Get xs values in wavelength
f = open(neon, "r")

x = []
y = []
### Laser 1
x = [48 ,133 ,	200 ,	310 ,	354 ,	595 ,	655 ,	808 ,	993]
### Laser 2
#x = [9 ,	77 ,	188 ,	232 ,	472 ,	533 ,	686 ,	872 ,	962]
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
    xVal = float(line.split('  ')[0])
    x.append(a * xVal**2 + b * xVal + c)
    line = f.readline()

f.close()

# Get files

print("Getting files")
#files = glob.glob(path + "l1t*")
files = glob.glob(path + "l2t*")
#files = ['l1t7i20', 'l1t7i325', 'l1t54i20', 'l1t54i325']
#files = ['l2t7i65', 'l2t35i65', 'l2t7i38', 'l2t35i38']

intensities = []
positions = []
temperatures = []

for file in files:
    y.clear()

    filePath = file
    fileName = file.split("TR\\")[1]

    #fileName = file
    #filePath = path + fileName

    print(filePath)

    temperature = fileName.split('t')[1].split('i')[0]
    intensity = fileName.split('i')[1]

    if int(intensity) != 65:
        continue

    #if float(intensity) < 100:
    #if float(intensity) != 56.0:
    #    continue

    temperatures.append(float(temperature))

    while float(intensity) > 100:
        intensity = str(int(intensity) / 10)

    f = open(filePath, "r")

    line = f.readline()

    yMax = 0
    yMaxIdx = 0
    idx = 0

    while line:
        currentY = float(line.split('  ')[1])
        y.append(currentY)

        if currentY > yMax:
            yMax = currentY
            yMaxIdx = idx

        idx += 1
        line = f.readline()

    f.close()

    intensities.append(float(intensity))
    positions.append(float(x[yMaxIdx]))

    '''
    T = "Laser 1. T = " + temperature + " (stopni C), i = " + intensity + " (mA)"

    plt.plot(x, y)
    plt.title(T)
    plt.ylabel('Natężenie światła')
    plt.xlabel('Natężenie prądu zasilającego laser (mA)')
    plt.savefig("figs/" + T + ".png")
    plt.show()
    '''


slope, intercept, r_value, p_value, std_err = stats.linregress(intensities, positions)
line = [slope * i + intercept for i in intensities]

#print("x_{"+ intensity +"}(T) = " + str(np.round(slope, decimals=2)) + "T + " + str(np.round(intercept, decimals=2)))
print(np.round(slope, decimals=2))
print(np.round(intercept, decimals=2))

print("Intensities:")
print(intensities)
print("Temperatures:")
print(temperatures)
print("Positions")
print(positions)

#plt.plot(intensities, positions, 'ro', intensities, line)
plt.plot(temperatures, positions, 'ro')
#plt.title("Laser 2. Zależność położenia linii w funkcji natężenia \n prądu zasilającego laser. T = 35 (stopni C)")
plt.title("Laser 2. Zależność położenia linii w funkcji temperatury. I = 65 (mA)")
plt.ylabel('Zmierzona długość fali (nm)')

plt.xlabel('Temperatura (stopnie C)')
#plt.xlabel('Natężenie prądu zasilającego laser (mA)')

plt.savefig("figs/f152.png")
plt.show()

#np.set_printoptions(suppress=True)

c = 3 * 10**8
n = 1.0003

positions.sort()
print(positions)

lambda1 = 10**(-9) * positions[1]
lambda2 = 10**(-9) * positions[3]

f1 = c / (n * lambda1)
f2 = c / (n *lambda2)

deltaF = abs(f2 - f1)

L = c / (2 * n * deltaF)

print("L_12")
print(np.round(L, decimals=6) * 10**6)

lambda1 = 10**(-9) * positions[3]
lambda2 = 10**(-9) * positions[5]

f1 = c / (n * lambda1)
f2 = c / (n *lambda2)

deltaF = abs(f2 - f1)

L = c / (2 * n * deltaF)

print("L_23")
print(np.round(L, decimals=6) * 10**6)
