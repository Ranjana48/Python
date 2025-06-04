#wap to input 10 numbers and count even numbers and odd numbers

count = 0
count2 = 0
for _ in range(10):
 num = int(input("Enter integer number: "))
 if num%2==0:
   count = count+1
 else:
   count2 = count2+1
print(f'Even numbers: {count}')   
print(f'Odd numbers: {count2} ')