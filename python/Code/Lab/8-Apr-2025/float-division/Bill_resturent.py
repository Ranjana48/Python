# you are building a resturent bill calculator.The user inputs the cost of the meal, the tip percentage,and any applicable taxes. Your program should: Add the tip and tax to the cost of the meal. Calculate the total amount to pay.meal_cost: The cost of the meal. tip_percentage: The percentage to tip. tax_percentage: The tax percentage. The total bill (meal cost + tip + tax).

meal_cost = int(input('Enter your one time meal cost: '))
tip_percentage = float(input("Enter tip percentage: "))
tax_percentage = float(input("Enter the tax percentage: "))
tip = meal_cost * tip_percentage
tax = meal_cost * tax_percentage
total_Bill = meal_cost+tip+tax
print(f'''
      Meal-cost is: {meal_cost} 
      Tip-Percentage is: {tip_percentage} and Tip-Cost is: {tip:.2f}
      Tax-Percentage is: {tax_percentage} and Tax-Cost is: {tax:.2f}
      Total - Bill is : {total_Bill:.2f}
      ''')

