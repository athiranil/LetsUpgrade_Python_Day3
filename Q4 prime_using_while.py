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
