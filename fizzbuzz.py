for i in range(1,101):
    if (i % 3 == 0):
        if (i % 5 == 0):
            print('FizzBizz')
        else:
            print('Fizz')
    elif(i % 5 == 0):
        print('Bizz')
    else:
        print(i)