# WAP to find simple intrest

Principal_Amount = float(input ('Enter your principle amount : '))
Time = int(input("Enter time in month : "))
Rate = float(input("Enter rate : "))
Simple_Interset = (Principal_Amount*Rate*Time)/100
print(f'''
      Amount : {Principal_Amount}
      Rate : {Rate}
      Time : {Time}
      SI : {Simple_Interset}
      
      ''')
