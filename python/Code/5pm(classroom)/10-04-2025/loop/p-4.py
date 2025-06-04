#wap to convert decimal integet to binary integer


num = int(input("enter decimal integer number: "))
b = ""

while num>0:
  r = num%2
  b = b+str(r)
  num = num//2
  
print("0b"+b[::-1])  