import matplotlib.pyplot as plt


# Get paths to images
path = "./Badania 2/TR/"

neon = path + "l2he"

# Get data form csv
f = open(neon, "r")

x = []
y = []

line = f.readline()

while line:
    x.append(float(line.split('  ')[0])*0.26 + 579.88)
    #x.append(float(line.split('  ')[0]))
    y.append(float(line.split('  ')[1]))
    line = f.readline()

print(x)
print(y)

f.close()

plt.plot(x, y)
plt.title("Widmo lampy Helowej")
plt.ylabel('Natężenie')
plt.xlabel('Długość fali (nm)')
plt.savefig("./figs/He.png")
plt.show()
