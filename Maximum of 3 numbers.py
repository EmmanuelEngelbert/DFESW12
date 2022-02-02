def maximumFunction(numbers):
    Max = 0 
    for i in numbers: 
        if i > Max: 
            Max = i 
    return Max

var1 = [] 

num1 = int(input("Type your first number "))
num2 = int(input("Type your second number "))
num3 = int(input("Type your third number "))

var1.extend([num1, num2, num3]) 

print(maximumFunction(var1))

