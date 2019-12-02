import math

class Module:
    def __init__(self, setMass):
        self.mass = setMass

def getFuelForModule(module):
    fuel = module.mass/3
    fuel = truncate(fuel)
    fuel -= 2
    print("Amount of fuel:", fuel)
    return fuel

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def readDataFile():
    path = "E:\\programmering\\adventOfCode2019\\d1\\d1_data.txt"
    return open(path, "r")
    
fuelSum = 0
fileData = readDataFile()
for x in fileData:
    
    fuelSum += getFuelForModule(Module(int(x)))

print(fuelSum)