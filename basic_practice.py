# TASK 1: 
# Declare variables
num1 = 10  # an integer
num2 = 3.14  # a float
name = "Corina"  # a string

# Print values and types
print("num1 value:", num1, "Type:", type(num1))
print("num2 value:", num2, "Type:", type(num2))
print("name value:", name, "Type:", type(name))


# TASK 2:
# Prompting the user to enter their age
age = int(input("Please enter your age: "))

# Checking the age and printing the corresponding message
if age < 18:
    print("You are a minor.")
elif age >= 18 and age <= 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


# TASK3:
def check_number(num):
    if num > 0:
        print("Positive number.")
    elif num < 0:
        print("Negative number.")
    else:
        print("Zero.")

# Test the function with different integer values
check_number(5)  # Output: Positive number.
check_number(-2)  # Output: Negative number.
check_number(0)  # Output: Zero.


# TASK 4: 
for i in range(0, 21, 2):
    print(i)


# TASK 5:
def calculate_circle_area(radius):
    # Constants
    pi = 3.14
    
    # Calculate area
    area = pi * (radius ** 2)
    
    return area

# Call the function with different  of radius
radii = [2.5, 3.0, 5.2]
for radius in radii:
    area = calculate_circle_area(radius)
    print(f"The area of a circle with radius {radius} is {area:.2f}.")

