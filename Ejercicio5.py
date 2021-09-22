'''Encontrar el menor valor de un conjunto de n números dados'''
number_numbers = int(input( "enter to numbers to list \n"))
list_numbers = []
less= 999999
for i in range (number_numbers):
    number = int(input(f"Enter to number {i + 1}\n"))
    list_numbers.append(number)
print ( list_numbers)
for number in list_numbers: 
    if number < less:
       less = number
print(f"To less number is {less}")
