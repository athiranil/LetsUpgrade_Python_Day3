for num in range (2, 1001):
    for i in range(2, (num//2 + 1)):
        if(num % i == 0):
            break
    else:
        print(num)
