# wap to input 10 numbers and find maximum value and minimum value


for i in range(10):
 num = int(input("Enter numbers:"))
 if i == 0:
   max_value=num
   min_value=num

 elif num>max_value:
   max_value=num
   
 elif num<min_value:
   min_value=num
   
   
print(f'max value is: {max_value}')  
print(f'min vALUE is: {min_value}') 