'''Paycheck Calculation
Scenario:
You are building a payroll system. The program needs to calculate the total salary based on hourly wages and the number of hours worked, with overtime calculations:

Regular hourly wage: $15/hr.

Overtime wage: $22.5/hr (for hours worked beyond 40 hours in a week).

Exercise:
Write a Python program that calculates the total paycheck, factoring in regular hours and overtime.

Example Input:
hours_worked = 45, hourly_rate = 15

Expected Output:
Total Pay: $712.5'''

hours_worked=int(input("enter your working hors:"))
if hours_worked<=40:
  regular_wage = hours_worked*15
  print(regular_wage)
else:
  extra_hours_worked = hours_worked-40
  extra_wage = extra_hours_worked*(22.5)
  total_wage =  (40*15) + extra_wage
  print(total_wage)
  




    
    

  