print("__Learning Strings__")
print('Single Strings')
print("Double Strings")
print("Manisha's first python programme")
print('We are learning single strings, and "double strings".')
print("String " + " concatenation ")
# storing string value in a variable:-
greetings = "Hello"
name = "Manisha"
# name = input("Enter your name here")

# using variable in a function :- if we want space, we can add empty "".
print(greetings + " " + name)

age = 27
print(age)
# re-bounding  age and changing datatype:-
# age = "27 years"
age_in_string = "27 years"

print(type(age))
# python cannot concatenate with integers , age var had int datatype.
print(name + " is " + age_in_string + " old ")
