# Write a program to check whether the last digit of a number entered by user is divisible by 3 or not
num = int(input('enter a number: '))
last_digit = num%10
if(last_digit % 3 == 0):
  print('divisible by three ')
else:
  print('not divisible by three')