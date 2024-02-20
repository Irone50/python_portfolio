#3.Random password generator
#have special characters or symbols, numbers ,letters
from random import choice

def generate_password(number):
    numbers = ['1','2','3','4','5','6','7','8','9']
    symbols = ['#','%','$','.','_','*','@']
    letters = ['a','b','c','d','e','f','g','h','A','B','C','D','E']
    chars = numbers + symbols + letters

    pwd = []
    for num in range(number):
        char = choice(chars)
        pwd.append(char)
    password = ''.join(pwd)
    return password

pwd = generate_password(10)
print(pwd)

#Assignment1 - using a for loop for string reverser
#Assignment2 = Research about recursion
#Assignment3 = research about string modules and refactor the code below to accomodate upper cases
#Assignment4 = prime finder
#Assignment5 = join leetcode.com