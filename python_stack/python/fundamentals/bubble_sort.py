def bubble(myList):
    maxindex=len(myList)-1
    for j in range(maxindex,0,-1):
        print('Outerloop', j)
        for i in range (j):
            print('Innerloop', i+1)
            if myList[i]>myList[i+1]:
                myList[i], myList[i+1] = myList[i+1], myList[i]
            print(myList)
    return myList



x = [15,23,65,72,19,12,15]
print(bubble(x))
