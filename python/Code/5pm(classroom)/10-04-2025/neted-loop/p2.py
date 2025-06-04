# wap to generate prime numbers 2 to 40

num = int(input("enter any number: "))
for num in range(2,41):
  c=0
  for i in range(1,num+1):
    num = num%10
