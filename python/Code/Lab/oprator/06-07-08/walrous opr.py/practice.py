# walrus oprator or assignment expression oprator(:=)
# a = 10
# b = 20
# d = (e:=a+b)*(f:=a-b)
# print(d)
# print(e)
# print(f)

# a = (X:=10)
# print(a)

print((x:=10) if 40>30 else (y:=30))