#Define the mathmatics
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Request two numbers from the user
print("Please input two numbers you wish to have added, subtracted, multiplied or divided")
number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))

#Ask what operation they wish to do
print("What operation do you want to accomplish?")
print("1. For Addition")
print("2. For Subtraction")
print("3. For Multiplication")
print("4. For Division")

#What is the choice?
choice = int(input("Please enter 1-4.  What is your choice?"))

#Perform the mathmatical operation
operations = {
    1: add,
    2: subtract,
    3: multiply,
    4: divide
}

#Define the number as a result
result = operations[choice](number1, number2)

#Display the results
print("This ends up being: ",result)
