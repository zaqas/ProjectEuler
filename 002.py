import math

def checkSquare(item):
    new_item = int(math.sqrt(item))
    iSquare = new_item * new_item
    if iSquare == item:
        return iSquare

def isFibo():
    myList= [i for i in range(4000000) if i is not None] # Removes None from list
    fibo = []
    for item in myList:
        if checkSquare(5*item**2+4):
            if(item%2 == 0):
                fibo.append(item)
        elif checkSquare(5*item**2-4):
            if (item % 2 == 0):
                fibo.append(item)
        else:
            pass
    print(sum(fibo))


isFibo()
