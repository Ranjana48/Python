# wap to find last digit of input number is divisible with 3 or not
digit = int(input('enter digit: '))
last_digit = digit%10
print('divisible') if last_digit%3==0 else print('not divisible')