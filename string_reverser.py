#1.string reverser
#2.factorial finder
#3.random password generator
#4.prime finder
#5.number guessing game

#1.string reverser
#hello -> olleh

#using iteration - while loop
source = input('enter a word: ')
count = len(source) - 1
reversed_string = []

while count >= 0:
    char = source[count]
    reversed_string.append(char)
    count -= 1

output = ''.join(reversed_string)
print(output)

# using a one line code/Slicing
source = input('enter a word: ')
reversed_string = source[::-1]
print(reversed_string)
