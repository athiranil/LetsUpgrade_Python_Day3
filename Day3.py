#question 1
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
    
#Question 2
for num in range (2, 1001):
    for i in range(2, (num//2 + 1)):
        if(num % i == 0):
            break
    else:
        print(num)
        
#Question 3
for i in range(1,11):
    for j in range(1,11):
        print(i,"X",j,"=",i*j,sep="")
    print()

#Question 4        
number = int(input('Please enter a number: '))
num = 2
while num<=number:
    i=2
    flag=True
    while(i<=num//2):
        if(num % i == 0):
            flag=False
            i+=1
            break
        i+=1
    if(flag):
        print(num)
    num+=1
