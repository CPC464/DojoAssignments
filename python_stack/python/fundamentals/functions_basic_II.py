
# # Countdown
# def countdown(num):
#     output = []
#     for i in range(num,-1,-1):
#         print(i)
#         output.append(i)
#     return output

# # print(countdown(5))

# # Print and return
# def print_and_return(a,b):
#     print(a)
#     return b

# print(print_and_return(3,9))

# First Plus Length
def first_plus_length(a):
    print(a)
    print("length is:",len(a))
    output = a[0] + len(a)
    return output

print(first_plus_length([6,2,3,4,5,6,7,10]))

# Values Greater than Second
# def vgts(mylist,y):
#     if len(mylist) < 2:
#         return False
#     output = []    
#     for value in mylist:
#         print(value)
#         if value > y:
#             output.append(value)
#     print("The output has", len(output), "values")
#     return output

# print(vgts([1],4))


# # This length, that value

# def myfunc(x,y):
#     output = []
#     for i in range(x):
#         output.append(y)
#     return output

# print(myfunc(10,3))
