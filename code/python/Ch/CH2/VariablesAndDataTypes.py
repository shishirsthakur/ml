a = 1 #integer
b = 5.22 #floating point number
c = "code" #double quotes for string
d = False #boolean variable
e = None #none type variable

# variable names can only start with alphabet/underscore
# and no white space or special characters allowed

# 1. Arithmetic operators: +, -, *, / etc.
# 2. Assignment operators: =, +=, -= etc.
# 3. Comparison operators: ==, >, >=, <, != etc.
# # 4. Logical operators: and, or, not.


# Arithmetic Operators
e = 7
f = 4
g = e + f
print(g)


# Assignment Operators
e = 4-2 # Assign 4-2 in e
print(e)
f = 6
# f += 3 # Increment the value of f y 3 and then assign it to f
g -= 3 # Decrement the value of g by 3 and then assign it to g
print(g)

# Comparison Operators

h = 5==5

print(h)


# Logical Operators

e = True or False

# Truth table of 'or'
print("True or False is ", True or False)
print("True or True is ", True or True)
print("False or True is ", False or True)
print("False or False is ", False or False)

# Truth table of 'and'
print("True and False is ", True and False)
print("True and True is ", True and True)
print("False and True is ", False and True)
print("False and False is ", False and False)

print(not(True))

b = str(a) #integer typecasted to float

t = type(b) #used to find out datatypes
print(t)
