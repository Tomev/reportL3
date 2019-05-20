import numpy as np
from math import sqrt, ceil
import sys
import matplotlib.pyplot as plt
import glob
from scipy import stats

# Get paths to images
path = "./Badania 1/"
csvs = glob.glob(path + "*.csv")

l1ActionT = []
l1ActionI = []
l2ActionT = []
l2ActionI = []

l1Slope = []
l1SlopeT = []
l1Intercept = []
l2Slope = []
l2SlopeT = []
l2Intercept = []

# For each data file
for csv in csvs:

    T = 0

    temp = ""
    laserNum = ""

    # Check if it's first laser or second and get
    if csv.__contains__('x'):
        temperature_str = csv.split('x')[1]
        temperature_str = temperature_str.split('.csv')[0]
        temperature = np.round((int(temperature_str) - 1167.25) / 12.88, decimals=1)
        T = "Laser 1. T = " + str(temperature)
        l1ActionT.append(temperature)
        laserNum = "1"
        temp = str(temperature)
    else:
        temperature_str = csv.split("\\t")
        temperature_str = temperature_str[len(temperature_str) - 1]
        temperature_str = temperature_str.split('.csv')[0]
        T = "Laser 2. T = " + temperature_str
        l2ActionT.append(float(temperature_str))
        temp = temperature_str
        laserNum = "2"

    #print("Loading data for " + T)

    # Get data form csv
    f = open(csv, "r")

    x_str = f.readline().split(',')
    x = []
    for single_x in x_str:
        x.append(float(single_x))

    y_str = f.readline().split(',')
    y = []
    for single_y in y_str:
        y.append(float(single_y))

    for i in range(len(x)):
        x[i] *= 0.1
        y[i] *= 0.01

    x = [x[0] - 0.5] + x
    y = [0] + y

    # plt.errorbar(E, v_avg, xerr=u_E, yerr=u_v, fmt='o')
    plt.plot(x, y)
    plt.title(T)
    plt.ylabel('Natężenie światła (mA)')
    plt.xlabel('Natężenie zasilające (mA)')
    plt.savefig("d:/figs/" + T + ".png")
    plt.show()

    # print("Looking for laser action point")

    laserActionI = 0
    laserActionIndex = 0

    for i in range(1, len(y)):
        if y[i] - y[i-1] > 0.05:
            # print(x[i])
            laserActionI = x[i]
            laserActionIndex = i
            break

    if T.__contains__("Laser 2"):
        l2ActionI.append(laserActionI)
    else:
        l1ActionI.append(laserActionI)

    # print("After action plot")

    afterActionX = [x[i] for i in range(laserActionIndex, len(x))]
    afterActionY = [y[i] for i in range(laserActionIndex, len(y))]

    slope, intercept, r_value, p_value, std_err = stats.linregress(afterActionX, afterActionY)
    line = [slope * i + intercept for i in afterActionX]

    if T.__contains__("Laser 2"):
        l2Slope.append(slope)
        l2SlopeT.append(float(temp))
        l2Intercept.append(intercept)
    else:
        if slope > 2:
            l1Slope.append(slope)
            l1SlopeT.append(float(temp))
            l1Intercept.append(intercept)

    print("L_" + laserNum + "^{" + temp + "}(I_i) = " + str(np.round(slope, decimals=2)) + "I_i + " + str(np.round(intercept, decimals=2)))

    plt.plot(afterActionX, afterActionY, 'ro', afterActionX, line)
    plt.title(T + ", po akcji")
    plt.ylabel('Natężenie światła (mA)')
    plt.xlabel('Natężenie zasilające (mA)')
    plt.savefig("d:/figs/" + T + ", po akcji.png")
    plt.show()

'''
print(l1ActionT)
print(l1ActionI)
print(l2ActionT)
print(l2ActionI)
'''

slope, intercept, r_value, p_value, std_err = stats.linregress(l1ActionT, l1ActionI)
line = [slope * i + intercept for i in l1ActionT]

print("a = " + str(slope) + ", b = " + str(intercept))

plt.plot(l1ActionT, l1ActionI, 'ro', l1ActionT, line)
plt.title("Laser 1. Akcja Laserowa")
plt.ylabel('Natężenie zasilające (mA)')
plt.xlabel('Temperatura (stopnie C)')
plt.savefig("d:/figs/Laser1Action.png")
plt.show()

slope, intercept, r_value, p_value, std_err = stats.linregress(l2ActionT, l2ActionI)
line = [slope * i + intercept for i in l2ActionT]

print("a = " + str(slope) + ", b = " + str(intercept))

plt.plot(l2ActionT, l2ActionI, 'ro', l2ActionT, line)
plt.title("Laser 2. Akcja Laserowa")
plt.ylabel('Natężenie zasilające (mA)')
plt.xlabel('Temperatura (stopnie C)')
plt.savefig("d:/figs/Laser2Action.png")
plt.show()

slope, intercept, r_value, p_value, std_err = stats.linregress(l1SlopeT, l1Slope)
line = [slope * i + intercept for i in l1SlopeT]

print("a_1(T) = " + str(slope) + "T + " + str(intercept))

plt.plot(l1SlopeT, l1Slope, 'ro', l1SlopeT, line)
plt.title("Laser 1. Współczynnik kierunkowy jako funkcja temperatury")
plt.ylabel('a (mA / stopnie C)')
plt.xlabel('Temperatura (stopnie C)')
plt.savefig("d:/figs/a1T.png")
plt.show()

print(str(np.round(sum(l1Slope) / len(l1Slope), decimals=2)) + " + " + str(np.round(sum(l1Intercept) / len(l1Intercept), decimals=2)))

slope, intercept, r_value, p_value, std_err = stats.linregress(l2SlopeT, l2Slope)
line = [slope * i + intercept for i in l2SlopeT]

print("a_2(T) = " + str(slope) + "T + " + str(intercept))

plt.plot(l2SlopeT, l2Slope, 'ro', l2SlopeT, line)
plt.title("Laser 2. Współczynnik kierunkowy jako funkcja temperatury")
plt.ylabel('a (mA / stopnie C)')
plt.xlabel('Temperatura (stopnie C)')
plt.savefig("d:/figs/a2T.png")
plt.show()

print(str(np.round(sum(l2Slope) / len(l2Slope), decimals=2)) + " + " + str(np.round(sum(l2Intercept) / len(l2Intercept), decimals=2)))

print('Finished.')
