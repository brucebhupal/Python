# Integer
age = 25  

# Float
salary = 4567.89  

# String
name = "Alice"  

# Boolean
is_active = True  

# List
fruits = ["apple", "banana", "cherry"]  

# Tuple
coordinates = (10, 20)  

# Dictionary
student = {"id": 101, "name": "Alice", "grade": "A"}  

# Set
unique_numbers = {1, 2, 3, 3, 2}
# Integer to String
num = 100
num_str = str(num)     # "100"

# String to Integer
text = "200"
text_num = int(text)   # 200

# Float to Integer
pi = 3.14
pi_int = int(pi)       # 3

# Integer to Float
marks = 95
marks_float = float(marks)  # 95.0

# List to Tuple
fruits = ["apple", "banana"]
fruits_tuple = tuple(fruits)   # ("apple", "banana")

# Tuple to List
coordinates = (10, 20)
coord_list = list(coordinates) # [10, 20]
# Simple Interest Calculation
P = float(input("Enter Principal amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time in years: "))

SI = (P * R * T) / 100
print("Simple Interest =", SI)
x = 10
y = 20

print("Before Swap: x =", x, " y =", y)

temp = x
x = y
y = temp

print("After Swap: x =", x, " y =", y)