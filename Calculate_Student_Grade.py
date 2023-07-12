def GradeCalulator(marks):
    if marks > 100 or marks < 0:
      return 'Invalid Input please range 0 to 100'
    elif marks >= 90 and marks<=100 :
        return 'A+'
    elif marks >= 80 and marks < 90 :
        return 'A'
    elif marks >= 70 and marks < 80 :
       return 'B'
    elif marks >= 60 and marks < 70 :
       return 'C'
    elif marks >= 50 and marks < 60:
        return 'D'
    else:
        return 'F'


marks = float(input('Enter the Student marks '))
grade = GradeCalulator(marks)
print('The Grade of the Student is '+ grade +' having marks are '+ str(marks))
