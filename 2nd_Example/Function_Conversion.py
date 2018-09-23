'''
Converting currenices
Miles and Kilometers
Kilograms and Pounds
Celsius and Fahrenheit

'''
def print_menu():
    print('1. British Pounds to US Dollars')
    print('2. British Pounds to Euros')
    print('3. British Pounds to Yens')
    
def Pounds_Dollars():
        Pounds = float(input('Enter Pounds: '))
        Dollars = Pounds * 1.28
        print('Amount in Dollars is: ',round(Dollars,2))

def Pounds_Euros():
        Pounds = float(input('Enter Pounds: '))
        Euros = Pounds * 1.19
        print('Amount in Euros is: ',round(Euros,2))

def Pounds_Yens():
        Pounds = float(input('Enter Pounds: '))
        Yen = Pounds * 139.79
        print('Amount in Yens is:',round(Yen,2)) 
    


def main():
    print_menu()
    choice = input('Which conversion would you like to do? ')

    if choice == '1':
        Pounds_Dollars()
    if choice == '2':
        Pounds_Euros()
    if choice == '3':
        Pounds_Yens()

main()

   
