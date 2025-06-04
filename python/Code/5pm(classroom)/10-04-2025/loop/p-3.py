# wap to find input is pallendrom or not


num = int(input("enter number: "))
num2 = num
rev =0
while num>0:
  last_digit = num%10
  rev = (rev*10) + last_digit
  num = num//10
  
  
if rev == num2:
  print(f'{rev} is palledrom number')  
else:
  print(f'{rev} is not palledrom number')


