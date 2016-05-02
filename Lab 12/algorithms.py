# By: Lauren Tubbs and Jake Hennessy
# algorithms.py

# Obsevations on Linear vs. Binary searches:
#       On smaller lists (~50 items):
#           The difference is negligible between
#           between the two algorithms, only when the entire list is iterated
#           through is there any discrepancy
#           (twice as long for linear, in terms of 1/100,000 of a sec.)
#       On larger lists (10,000,000 item):
#           The linear search time becomes almost an entire second, whereas the
#           binary search time remains virtually unchanged.
#           (Binary: .00002 sec vs. Linear: ~0.72500 sec)

# Observations on insertion sort versus Python's sort:
#       Python's sort is about 2500 times faster than the insertion sort.

def readData(filename):
    infile = open(filename, "r")
    data = []
    for line in infile:
        lineList = line.split()
        for value in lineList:
            data.append(int(value))
    print(data)
    return data

def isInLinear(searchVal, values):
    foundPos = -1
    for i in range(len(values)):
        if searchVal == values[i]:
            foundPos = i
            return True
    return False
        
def isInBinary(searchVal, values):
    foundPos = -1
    low = 0
    high = len(values) - 1
    while foundPos == -1 and low <= high:
        mid = (low + high) // 2
        if searchVal == values[mid]:
            foundPos = mid
            return True
        elif searchVal > values[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False

def insertionSort(values):
    for i in range(1, len(values)):
        value = values[i]
        j = i-1
        while j >= 0 and values[j] > value:
            values[j+1] = values[j]
            j -= 1
        values[j+1] = value
    return values


def main():
    filename = input("Enter a filename: ")
    userVal = eval(input("Enter a search value: "))
    data = readData(filename)
    tf = isInLinear(userVal, data)
    print('Using a Linear Search:', end =' ')
    if tf == True:
        print("\tThe value is in the list.")
    elif tf == False:
        print("\tThe value is not in the list.")
    biTF = isInBinary(userVal, data)
    print('Using a Binary Search:', end =' ')
    if biTF == True:
        print("\tThe value is in the list.")
    elif biTF == False:
        print("\tThe value is not in the list.")

