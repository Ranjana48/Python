#method1:
a=5
b=9
print("before swap",a,b)
c=a
a=b
b=c
print("after swapping", a,b)


#method2:
num1 = input("Enter your first number")
num2 = input("Enter your second number")
print("before swapping", num1,num2)
num3 = num1
num1 = num2
num2 = num3
print("after swapping", num1, num2)

#method3:
a = input("enter value")
b = input("enter value")
print("before swapping",a,b)
#swap function
a,b = b,a
print("after swapping",a,b)