# wap to calculate grade based on avrage marks....  input name three subject marks and then calculate avrage
name = input('enter name: ')
sub1 = int(input('enter math marks: '))
sub2 = int(input('enter science marks: '))
sub3 = int(input('enter english marks: '))
avg = (sub1+sub2+sub3)/3
print('A+') if avg>=90 else print('A') if avg>=70 and avg<90 else print('B+') if avg>=50 and avg<70 else print('B') if avg>=40 and avg<50 else print('C')