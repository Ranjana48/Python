# wap to find prime number is not


#method-1:
num = int(input("enter number: "))
count = 0
for i in range(1,num+1):
  if num%i==0:
    count=count+1
    
if count ==2:
  print(f'{num} is prime')  
else:
  print(f'{num} is not prime') 
   
  