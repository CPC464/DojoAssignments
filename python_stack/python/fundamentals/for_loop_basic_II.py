import math

# Biggie size

# def biggie(mylist):
#     for i in range(0,len(mylist),1):
#         if mylist[i] >0:
#             mylist.pop(i)
#             mylist.insert(i,"big")
#     return mylist

# x = [-1,0,4,5,-2,10]
# print(biggie(x))

# Count positives

# def positives(mylist):
#     count =0
#     length = len(mylist)
#     for i in range(0,length,1):
#         if mylist[i] >0:
#             count +=1
#         mylist.pop(length-1)
#         mylist.insert(length-1,count)
#     return mylist

# x = [-1,0,4,5,-2,10]
# print(positives(x))


# def sumtotal(mylist):
#     tot = 0
#     for x in mylist:
#         tot += x
#     return tot

# x = [-1,0,4,5,-2,10]
# print(sumtotal(x))


# def aver(mylist):
#     tot = 0
#     length = len(mylist)
#     for x in mylist:
#         tot += x
#     return tot/length

# x = [-1,0,4,5,-2,10]
# x = [1,2,3,4]
# print(aver(x))

# def leng(mylist):
#     length = len(mylist)
#     return length
# x = []
# # x = [-1,0,4,5,-2,10]
# # x = [1,2,3,4]
# print(leng(x))

# def minimum(mylist):
#     if len(mylist)==0:
#         return false
#     m = mylist[0]
#     for x in mylist:
#         if x < m:
#             m = x
#     return m

# # x = [-1,0,4,5,-2,10]
# # x = [-10,0,4,5,-2,10]
# x = [7,0,4,5,-2,10,-8]
# print(minimum(x))

# def maximum(mylist):
#     if len(mylist)==0:
#         return false
#     m = mylist[0]
#     for x in mylist:
#         if x > m:
#             m = x
#     return m

# # x = [-1,0,4,5,-2,10]
# # x = [-10,0,4,5,-2,10]
# x = [7,0,4,5,-2,10,-8]
# print(maximum(x))

def ultimate(myList):
    minimum = myList[0]
    maximum = myList[0]
    length = len(myList)
    sumTotal = 0
    for x in myList:
        sumTotal += x
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    average = sumTotal/length
    return {'sumTotal':sumTotal, 'average':average, 'minimum':minimum, 'maximum':maximum, 'length': length}

x = [37,2,1,-9]
# x = [7,0,4,5,-2,10,-8]
print(ultimate(x))

def reverse(myList):
    length = len(myList)
    swaps = math.floor(length/2)
    print("swaps: ",swaps)
    for i in range(0,swaps,1):
        myList[i], myList[length-1-i] = myList[length-1-i], myList[i]  # Found method here: https://pythontips.com/2013/07/28/in-place-value-swapping/
    return myList

myinput = [1,2,3,4,5,6,7,8,9,10,11]
print(reverse(myinput))


