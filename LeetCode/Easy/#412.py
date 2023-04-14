# Fizz Buzz 2 ways in python

for n in range(1, 101):
    if n % 15 == 0:
        print('FizzBuzz')
    else:
        if n % 3 == 0:
            print('Fizz')
        else:
            if n % 5 == 0:
                print('Buzz')
            else:
                print(n)

for n in range(1, 101):
    if n % 15 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)
