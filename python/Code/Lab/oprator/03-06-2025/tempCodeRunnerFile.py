''' creat a programs that calculate the BMI(body mass index) of a person.'''
w = float(input('enter weight in kilograms : '))
h = float(input('enter height in meters : '))
BMI = w / (h**2)
print(f'your BMI is : {BMI:.2f}')