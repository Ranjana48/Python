# BMI(Body Mass Index): create a program that calculates the Body Mass Index(BMI) of a person. you will need to : Take weight in killometers(kg) and height in meters(m) use the formula: BMI = weight/height^2

weight = float(input("Enter Person Weight in killometers: "))
height = float(input("Enter Person height in meters: "))
BMI =  (weight/height)**2
print(f'BMI of Person is: {BMI:.2f}')