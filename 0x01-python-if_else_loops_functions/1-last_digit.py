#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    negativeNum = int(str(number)[-1]) * -1
    print('Last digit of ' + str(number) + ' is ' + str(negativeNum) +
          ' and is less than 6 and not 0')
else:
    if int(str(number)[-1]) > 5:
        print('Last digit of ' + str(number) + ' is ' + str(number)[-1] +
              ' and is greater than 5')
    elif int(str(number)[-1]) < 6 and int(str(number)[-1]) != 0:
        print('Last digit of ' + str(number) + ' is ' + str(number)[-1] +
              ' and is less than 6 and not 0')
    else:
        print('Last digit of ' + str(number) + ' is ' +
              str(number)[-1] + ' and is 0')
