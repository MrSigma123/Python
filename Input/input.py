# to input a stream we simply use input function
input("Enter the value here: ")

# the above input only takes the input stream, but doesn't store it

# you can combine print and input functions with concatenation operator
print("Hello " + input("What is your name? "))

# in python you can use special kind of strings called f-strings
# f string is a literal string, prefixed with 'f', which contains 
# expressions inside braces

# in the following code the value variable value will be placed
# instead {value}
value = 1
print(f"Here is the value variable value is {value}")
