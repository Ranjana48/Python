# wap to revers input number

revers = 0
num = int(input("enter numbers: "))
while num>0:
 last_num = num % 10
 revers = (revers*10)+last_num
 num = num//10
print(revers)
