import random


# def randInt(min=0, max=100   ):
def randInt(min=0, max=100  ):
    if min > max:
        print("Error: Min is greater than max, please try again")
        return
    if max < 0:
        print("Error: Max must be greater than zero, please try again")
        return
    num = random.random()*max + min
    num = round(num)
    return num

print(randInt())

# print("#")*50
# print(randInt(max=5))
# print(randInt(min=50))
# print(randInt(min=50,max=500))
# print(randInt(min=500,max=50))
# print(randInt(max=-10))