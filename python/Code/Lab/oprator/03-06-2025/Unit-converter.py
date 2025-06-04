'''Unit Converter (Length, Weight, etc.)
Write a program to convert units like kilometers to miles or grams to kilograms using arithmetic operators. For instance:

1 kilometer = 0.621371 miles

1 kilogram = 1000 grams'''

unit = int(input('Enter amount of unit : '))
miles = float(unit * 0.621371)
print(f'miles : {miles:.2f}')
grams = unit*1000
print(f'grams : {grams:.2f}')
