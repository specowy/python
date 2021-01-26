import time
from random import randint


def f1(long_list):
    print(" Metoda 1 ")
    start = time.time()
    for i in long_list:
        if i == -1:
            break
    end = time.time()
    print('czas:', end - start, 'sekund')


def f2(long_list):
    print(" Metoda 2 ")
    start = time.time()
    for i in range(1000000):
        if long_list[i] == -1:
            break
    end = time.time()
    print('czas:', end - start, 'sekund')


def f3(long_list):
    print(" Metoda 3 ")
    start = time.time()
    for i in range(1000000):
        if long_list[i] == -1:
            break
    end = time.time()
    print('czas: ', end - start, 'sekund')


if __name__ == '__main__':
    long_list = [randint(0, 3000) for element in range(1000000)]
    f1(long_list)
    f2(long_list)
    f3(long_list)
