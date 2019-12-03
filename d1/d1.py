import math

def getFuelForModuleStarOne(module):
    fuel = module.mass/3
    fuel = truncate(fuel)
    fuel -= 2
    print("Amount of fuel:", fuel)
    return fuel

def getFuelForModuleStarTwo(originalFuel):
    fuel = originalFuel/3
    fuel = truncate(fuel)
    fuel -= 2
    print("Amount of fuel:", fuel)
    if(fuel > 0):
        fuel += getFuelForModuleStarTwo(fuel)
    else:
        fuel = 0
        return fuel
    print("totalFuelAmount:", fuel)
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
    #fuelSum += getFuelForModuleStarOne(int(x))
    fuelSum += getFuelForModuleStarTwo(int(x))

#fuelSum += getFuelForModuleStarTwo(1969)
print(fuelSum)