# -*- coding: utf-8 -*-
__author__ = 'p.olifer'


def main(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        return None

my_list = [1,2,3,4,5,6,7,8,9]

if __name__ == '__main__':
    print(main(my_list, 5))
    print(main(my_list, 10))

