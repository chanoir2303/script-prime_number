x = int(input())
if x != 1:
    for n in range(2, x):
        if x % n == 0:
            print('This number is not prime')
            break
    else:
        print('This number is prime')
else:
    print('This number is not prime')



