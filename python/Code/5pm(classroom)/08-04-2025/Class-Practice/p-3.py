# wap to genrate square sereies: 1 4 9 16.......


num2 = 1
for _ in range(1,11):
  num = int(input("Enter number: "))
  num2 = num**num
  
print(f'square value is: {num2}')  