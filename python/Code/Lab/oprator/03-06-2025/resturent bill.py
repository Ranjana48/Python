'''
You are building a restaurant bill calculator.
The user inputs the cost of the meal, the tip percentage,
and any applicable taxes. Your program should:
Add the tip and tax to the cost of the meal.
Calculate the total amount to pay.
meal_cost: The cost of the meal.
tip_percentage: The percentage to tip.
tax_percentage: The tax percentage.
The total bill (meal cost + tip + tax).
'''

meal_cost = float(input('The cost of the meal : '))
tip_percentage = float(input('The percentage to tip : '))
tax_percentage = float(input('The tax percentage : '))
tip = meal_cost*(tip_percentage/100)
tax = meal_cost*(tax_percentage/100)
total_bill = meal_cost+tip+tax
print(f'''
      The cost of the meal : {meal_cost}
      The percentage of the tip : {tip_percentage}
      The percentage of the tax : {tax_percentage}
      The amount of the tip is : {tip}
      The amount of the tax is : {tax}
      Total bill of meal of : {total_bill}
      ''')