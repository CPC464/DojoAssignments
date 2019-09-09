for x in range(151):
    print(x)

for x in range(5,1001,5):
    print(x)

for x in range(1,101):
    if x % 5 == 0 and x % 10 !=0:
        print('Coding')
    elif x % 10 == 0:
        print('Dojo')
    else:
        print(x)
total = 1
for x in range(3,500000,2):
    total = total + x
print(total)

for x in range(2018,3,-4):
    print(x)

lowNum = 3
highNum = 17
mult = 3

if lowNum < mult:
    lowNum = mult
    print ("lowNum was less than mult. Changed to:", lowNum)

elif lowNum % mult !=0:   
    for y in range(lowNum,2*mult+1,1):
        print("y: ", y)
        if y % mult == 0:
            lowNum = y
            print ("lowNum was not divisible with mult. Changed to:", lowNum)

for x in range(lowNum,highNum+1,mult):
    print(x)
