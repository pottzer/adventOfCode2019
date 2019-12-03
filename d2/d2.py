import math

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def readDataFile():
    path = "E:\\programmering\\adventOfCode2019\\d2\\d2_data.txt"
    return open(path, "r")

def opCodeOneAction(listPosition, dataList):
    result = dataList[listPosition+1] + dataList[listPosition+2]
    dataList[listPosition+3] = result
    return dataList
    

def opCodeTwoAction(listPosition):
    result = dataList[listPosition+1] * dataList[listPosition+2]
    dataList[listPosition+3] = result
    return dataList

def opCodeController(listValue, listPosition, dataList):
        if(listValue == 1):
            return opCodeOneAction(listPosition, dataList)
        elif(listValue == 2):
            print(2)
        elif(listValue == 99):
            print("End program")
            return 'end'
        else:
            print("Other opcode found error")
            return

testList = [1,0,0,3,99]

# Setting the realdata
for row in readDataFile():
    dataList = row.split(',')
    
dataList = map(int, dataList)
positionInList = 0

#defining which list to use
listUsed = testList
for listValue in listUsed:
        print(listValue)
        result = opCodeController(listValue, positionInList, listUsed)
        print result
        if(result == 'end'):
            break
        positionInList += 1


    




