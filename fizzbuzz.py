def fizz_buzz(counter):
    for i in xrange(counter):
        mod_5 = i % 5
        mod_3 = i % 3
        if mod_3 == 0 and mod_5 == 0:
            print('FizzBuzz')
        elif mod_3 == 0:
            print('Fizz')
        elif mod_5 == 0:
            print('Buzz')
        else:
            print(i)
