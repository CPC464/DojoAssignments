print("Helloooooo World!")

name = "Thomas"
name = name.swapcase()
print("My name is", name)
name = name.upper()
print("My name is " + name)
name = name.lower()
print("My name is " + name)
print(name.isalpha())
print(name.isnumeric())

number = 45
number2 = "45" # Storing the number as a string in order to concatenate with +
print("The number is", number)
print("The number is " + number2)
print(number2.isalpha())
print(number2.isnumeric())

fave_food1 = "Sushi"
fave_food2 = "Veggies"
print("I love to eat {} and {}".format(fave_food1, fave_food2))
print(f"I love to eat {fave_food1} and {fave_food2}")


