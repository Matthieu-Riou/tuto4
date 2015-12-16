#! /usr/bin/env python
# -*- coding: utf-8 -*-

''' 

    Question 1  -> Split
    Question 2  -> dual_primes
    Question 3  -> remove_odd_numbers
    Question 4  -> intersection
    Question 5a -> getIndiceOfMin
    Question 5b -> sortReverse

'''


def split(n):
    ''' (int) -> tuple of int

    This function takes a three-digit (max) integer as argument and returns a 
    tuple of those three digits.

    >>> split(123)
    (1, 2, 3)
    >>> split(203)
    (2, 0, 3)
    >>> split(3)
    (0, 0, 3)
    '''
    # Your code here



def pgcd(p, q):
    ''' (int, int) -> int

    Find and return the biggest common denominator of p and q.

    >>> pgcd(0, 3)
    3
    >>> pgcd(4, 6)
    2
    >>> pgcd(30, 4)
    2
    >>> pgcd(12, 18)
    6
    '''
    if p == 0:
        return q
    return pgcd(q % p, p)



def dual_primes(a, b):
    ''' (int, int) -> Boolean

    >>> dual_primes(27, 32)
    True
    >>> dual_primes(15, 25)
    False
    >>> dual_primes(21, 23)
    True
    '''
    # Your code here    




def remove_odd_numbers(l):
    ''' (list of int) -> NoneType

    >>> l = [0, 1, 2, 3, 4, 5] ; remove_odd_numbers(l) ; l
    [0, 2, 4]
    >>> l = [1, 2, 3, 3, 4, 5] ; remove_odd_numbers(l) ; l
    [2, 4]
    >>> l = [0, 1, 0, 1, 6, 9, 2] ; remove_odd_numbers(l) ; l
    [0, 0, 6, 2]
    '''
    # Your code here



def intersection(l1, l2):
    ''' (list of int, list of int) -> list of int

    Returns a list 


    >>> intersection([1, 2, 3], [1, 2, 3])
    [1, 2, 3]
    >>> intersection([1], [1, 2, 3])
    [1]
    >>> intersection([1, 2], [1, 2, 3])
    [1, 2]
    >>> intersection([1, 2, 3], [3])
    [3]
    '''
    # Your code here




def getIndiceOfMin(l, n):
    ''' (list of int, int) -> int

    Returns the indice of the smallest element among the n first elements of l.

    >>> getIndiceOfMin([9, 8, 2, 6, 5, 1], 4)
    2
    >>> getIndiceOfMin([9, 8, 2, 6, 5, 1], 5)
    2
    >>> getIndiceOfMin([9, 8, 2, 6, 5, 1], 6)
    5
    >>> getIndiceOfMin([9, 8, 2, 6, 5, 1], 7)
    5
    '''
    # Your code here



def sortReverse(l):
    ''' (list of int) -> list of int

    Sort l in decreasing order using the getIndiceOfMin() function.

    >>> l = [9, 8, 2, 6, 5, 1] ; sortReverse(l) ; l
    [9, 8, 6, 5, 2, 1]
    '''
    # Your code here




if __name__ == '__main__':
    import doctest
    res = doctest.testmod()
    print res


