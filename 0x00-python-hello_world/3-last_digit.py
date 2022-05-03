#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if abs(int(str(number)[-1])) > 5:
    statement = "greater than 5"
if abs(int(str(number)[-1])) == 0:
    statement = "0"
if abs(int(str(number)[-1])) < 6 and abs(int(str(number)[-1])) > 0:
    statement = "less than 6 and not 0"
if str(number)[0] == "-":
    print("Last digit of {} is -{} and is {}".format(str(number), \
                                                    str(number)[-1], statement))
else:
    print("Last digit of {} is {} and is {}".format(str(number), \
                                                    str(number)[-1], statement))
