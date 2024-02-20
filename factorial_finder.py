#2.factorial finder
#factorial of 5 = 5*4*3*2*1 = 120 
#loops - using for loop

def factorial(number):
    result = 1
    for num in range(1, number+1):
        result *= num
    return result

value = int(input('enter a number'))
result = factorial(value)
print(f'The factorial of {value} is {result}')

# using recursion
# Recursion is a function that calls itself

def factorial(num):
    if num ==1:
        return 1
    else:
        return num * factorial(num-1)
    
num = int(input('enter a number'))
result = factorial(num)
print(f'The factorial of {num} is {result}')
