#wap to check number is armstrong or not

sum = 0
num = input("Enter number: ")
lenth_num = len(num)
print(lenth_num)
num = int(num)
num1 = num
while num>0:
    last_digit = num % 10
    sum = sum+(last_digit**lenth_num)
    num = num//10
if num1 == sum:
   print(f'{sum} is armstrong number')
else:
  print(f'{sum} is not armstrong number')   
    
    
