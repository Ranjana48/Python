# Devlop Temprature conversion app: Celsius to Fahrenheit ==&gt; F = (C × 9/5) + 32. and 
# Fahrenheit to Celsius ==&gt; C = (F-32)x(5/9)

Temp = int(input("Enter Temprature in degree: "))
F = float((Temp * (9/5)) + 32)
C = float((F - 32) * (5/9))
print(f'''
      Temprature is: {Temp}deg converted into fahrenheit {F:.2f}oF
      Temprature is: {Temp} converted into Celsius {C:.2f}oC
       
      ''')