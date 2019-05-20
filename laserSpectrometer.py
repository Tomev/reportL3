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

line = f.readline()

while line:
    x.append(float(line.split('  ')[0])*0.26 + 548.16)
    line = f.readline()

f.close()

# Get files

print("Getting files")
#files = glob.glob(path + "l1t7*")
files = glob.glob(path + "l1*")

#files = ['l1t7i20', 'l1t7i325', 'l1t54i20', 'l1t54i325']

intensities = []
positions = []
temperatures = []

for file in files:
    y.clear()

    filePath = file
    fileName = file.split("TR\\")[1]

    print(filePath)

    temperature = fileName.split('t')[1].split('i')[0]
    intensity = fileName.split('i')[1]

    #if float(intensity) < 100:
    if float(intensity) != 30.0:
        continue

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

    T = "Laser 1. T = " + temperature + ", i = " + intensity + " (mA)"

    plt.plot(x, y)
    plt.title(T)
    plt.ylabel('Natężenie światła')
    plt.xlabel('Natężenie zasilające (mA)')
    plt.savefig("figs/" + T + ".png")
    plt.show()


slope, intercept, r_value, p_value, std_err = stats.linregress(temperatures, positions)
line = [0.99 * i + 679.54 for i in temperatures]

print("x_{"+ temperature +"}(I_i) = " + str(np.round(slope, decimals=2)) + "I_i + " + str(np.round(intercept, decimals=2)))

plt.plot(temperatures, positions, 'ro', temperatures, line)
plt.title("Laser 1. Zależność położenia linii w funkcji temperatury. I = 30 (mA)")
plt.ylabel('Zmierzona długość fali (nm)')
plt.xlabel('Temperatura (stopnie C)')
plt.savefig("figs/iw.png")
plt.show()


