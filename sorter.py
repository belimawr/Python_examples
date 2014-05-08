'''Array sorter

Implements the Bubble Sort algortith
and its improved version'''

import random

'''A random array to tests '''
_a = []
for _i in xrange(20):
    _a.append(random.randint(-50, 50))


def bubble_sort(array):
    '''Sorts the array using the normal version of Buble Sort'''
    n = len(array)
    while True:
        swapped = False
        for i in xrange(1, n):
            if(array[i - 1] > array[i]):
                tmp = array[i - 1]
                array[i - 1] = array[i]
                array[i] = tmp
                swapped = True
        n -= 1
        if(not swapped):
            break
    return array


def improved_bubble_sort(array):
    '''Sorts the array using an improved version of Bubble Sort'''
    n = len(array)
    while True:
        newn = 0
        for i in xrange(1, n):
            if(array[i - 1] > array[i]):
                newn = i
                tmp = array[i - 1]
                array[i - 1] = array[i]
                array[i] = tmp
        n = newn
        if(n == 0):
            break
