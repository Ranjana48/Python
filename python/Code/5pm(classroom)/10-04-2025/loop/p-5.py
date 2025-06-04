# wap to convert decimal integer to hexa decimal integer


num = int(input("Enter any number"))
h = ""
while num>0:
  last_digit = num%16
  if last_digit>=0 and last_digit<=9:
    h = h+str(last_digit)
  elif last_digit==10:
    h=h+"a"
  elif last_digit==11:
    h = h + "b"
  elif last_digit==12:
    h = h + "c"
  elif last_digit==13:
    h = h + "d"
  elif last_digit == 14:
    h = h+"e"
  elif last_digit==15:
    h = h+"f"
    
  num = num%10
    
print("0X"+h[::-1])    
 
    
  