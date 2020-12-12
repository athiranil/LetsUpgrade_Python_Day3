mark = int(input("Enter the percentage of student: "))
if(mark>85):
    print('Grade : A+')
elif(mark<=85 and mark>80):
    print('Grade : A')
elif(mark>70 and mark<=80):
    print('Grade : B+')
elif(mark>60 and mark<=70):
    print('Grade : B')
elif(mark>40 and mark<=60):
    print('Grade : C+')
elif(mark<=40 and mark>=35  ):
    print('Grade : C')
else:
    print('Failed')
        
