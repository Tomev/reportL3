import numpy as np
from math import sqrt, ceil
import matplotlib.pyplot as plt
import glob

# Get paths to
path = "d:/Dysk Google/Studia\Fizyka/reSemestr IV/Pracownia fizyczna dla zaawansowanych A/Optyka/L3/Badania 1/"
csvs = glob.glob(path + "*.csv")

# For each data file
for csv in csvs:

    T = 0

    # Check if it's first laser or second and get
    if csv.__contains__('x'):
        temperature_str = csv.split('x')[1]
        temperature_str = temperature_str.split('.csv')[0]
        T = "Laser 1. x = " + temperature_str
        #T = "Laser 1. T = " + str(12.88 * int(temperature_str) / + 1167.25)
    else:
        temperature_str = csv.split("\\t")
        temperature_str = temperature_str[len(temperature_str) - 1]
        temperature_str = temperature_str.split('.csv')[0]
        T = "Laser 2. T = " + temperature_str

    print("Loading data for " + T)

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

print('Finished.')


