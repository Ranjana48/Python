# n1 = 10 +20
# print(n1)

# num1 = 1
# num2 = 2
# print(num1+num2)


# x1 = 1.5+5
# print(x1)

# x2 = 1+2j + 5+4j
# print(x2)


# n4 = True+True
# print(n4)

# n5 = "full"+"stack"+"pthon"
# print(n5)

# n6 = [10,30,30] + [40,80,90]
# print(n6)


# wap to print marksheet enter name, two subject marks and calculate total marks

name = input("enter student name : ")
sub1 =  int(input(" enter subject1 marks : "))
sub2 = int (input("enter subject2 marks : "))
total_marks = float(((sub1+sub2)/200)*100)


print(f'''
      Name : {name}
      subject1 : {sub1}
      subkect2 : {sub2}
      Total - Marks : {total_marks}%
      ''')
