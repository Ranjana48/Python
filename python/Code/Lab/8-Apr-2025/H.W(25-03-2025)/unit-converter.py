# Write a program to convert units like kilometers to miles or grams to kilograms using arithmetic operators. For instance:1 kilometer = 0.621371 miles and 1 kilogram = 1000 grams

Units = float(input("Enter number of units"))
killometer = Units * 0.621371
grams = Units * 1000
print(f'''
      Enter Units are: {Units}
      converted into killometers are: {killometer}
      converted into grams are: {grams}
      ''')