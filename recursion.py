# -*- coding: utf-8 -*-
__author__ = 'p.olifer'


def hello(x):
    if x == 0:
        return
    else:
        print('Hello World!')
        hello(x-1)

def summa(x):
    if x == 0:
        return 0
    else:
        return x + summa(x-1)

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)


if __name__ == '__main__':
    # hello(4)
    # print(summa(4))
    # print(factorial(6))
    print(fibonacci(40))
