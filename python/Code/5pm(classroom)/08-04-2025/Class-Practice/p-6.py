# wap to generate mathemetical table of input number. ex: inter 5 genrate the table for 5

n = int(input("Enter the value of table: "))
for i in range(1, 11):
  table = n*i
  print(f' table of {n} is: {table}')  