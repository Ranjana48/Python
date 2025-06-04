# you are designing a car rental system. The car charges a fixed rate per killometers driven and the  rate per kilometer. your program should calculate:

killometer = float(input("Enter number of killometers driven: "))
rate = float(input("rate per killometers: "))
total_cost = killometer*rate
print(f'''
      killomeres : {killometer} 
      rate : {rate}
      total rental cost : {total_cost:.2f}
      ''')