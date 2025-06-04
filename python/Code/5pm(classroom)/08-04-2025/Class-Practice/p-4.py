# wap to genrate sum of the follonung series: 1^2+2^2+3^2+4^2+5^2......+n^2

n = int(input("input value of n: "))
sum = 0
for num  in range(1,n+1):
  print(f'{num}-->{num**2}')
  sum = sum + (num**2)
  
print(f'sum of n numbers square is: {sum} ')
