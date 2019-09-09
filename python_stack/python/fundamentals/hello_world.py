print("Hello World")
x = "Hello Python"
print(x)
y = 42
print(y)

name = "Zen"
print("My name is", name)

name = "Zen"
print("My name is " + name)

number = 10
print("The number is", number)

print(f"The name is {name}, the number is {number}")

print("The name is {}, the number is {}".format(name, number))

#x = "hello world"
x = "hello "
print(x.title()) # Capitalizes the first letter
print(x.upper()) # Capitalizes entire string
print(x.count("o")) # Counts occurences of "o"
print(x.find("o")) # Returns indecx of first occurences of "o"
print(x.isalnum()) # Returns boolean whether string is all numbers     NB: does not seem to work now
print(x.isalpha()) # Returns boolean whether string is all alphabetic  NB: does not seem to work now

