# you are developing a simple geometric calculator. the user inputs are : length and width of a rectangle, and the program calculates and displays the perimeter and area. perimeter = (2*(length+width)) and area is (length * width)

length = float(input("Enter length of rectangle : "))
width = float(input("Enter width of rectangle : "))
Area = length*width
Perimeter = 2*(length+width)
print(f'''
      Length is : {length}
      Width is : {width}
      Area ia : {Area:.2f}
      Perimeter : {Perimeter:.2f}
      
      ''')
