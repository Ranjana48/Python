#WAP to genrate sum of 10 integers, input 10 integers from keyboard.

sum=0
for _ in range(10): # start = 0, stop=10, step=1
  num = int(input("Enter  number: "))
  sum = sum+num
 
print(f'sum is: {sum}')