#Creating a unit converter

#Weight
#Length
#Temperature
#Currency

def weight_converter():
    #kg, g
    value = float(input('Enter a value'))
    original_unit = int(input('Original: enter 1 for (kg) or 2 for (g) for the value'))
    final_unit = int(input('Final: enter 1 for (kg) or 2 for (g) for the value'))

    if original_unit == 1:
        if final_unit == 1:
            print(f'{value}kg is equivalent to {value}kg')
        elif final_unit == 2:
            result = value*1000
            print(f'{value}kg is equivalent to {result}g')
        else: 
            print('please enter a valid unit')

    elif original_unit == 2:
        if final_unit == 1:
            result = value/1000
            print(f'{value}g is equivalent to {result}kg')
        elif final_unit == 2:
            print(f'{value}g is equivalent to {value}g')
        else: 
            print('please enter a valid unit')

    else:
        print('please enter a valid number')

def length_converter():
    pass

def temperature_converter():
    pass

def currency_converter():
    pass

while True:
    print('This is a unit converter')

    print('press (1) to convert weight')
    print('press (2) to convert length')
    print('press (3) to convert Temperature')
    print('press (4) to convert currency')
    print('press (5) to exit the program')

    value = int(input('Enter: '))

    if value == 1:
        weight_converter()
    elif value == 2:
        length_converter()
    elif value == 3:
        temperature_converter
    elif value == 4:
        currency_converter()
    elif value == 5:
        print('exiting program')
        break