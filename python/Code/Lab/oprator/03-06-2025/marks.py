name = input("Enter student name : ")
sub1 = float(input("enter subject1 marks: ")) 
sub2 = float(input("enter subject2 marks: "))
total_marks = sub1+sub2
print(''' name :{}
      math : {}
      English : {}
      total marks : {}
      '''.format(name,sub1,sub2,total_marks))