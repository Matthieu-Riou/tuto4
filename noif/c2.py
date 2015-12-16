#! /usr/bin/env python

def isLower(a, b):
    ''' (number, number) -> Boolean

    Return True iif a is less than b.

    >>> isLower(4, 1)
    False
    >>> isLower(1, 1)
    False
    >>> isLower(0, 1)
    True
    >>> isLower(0, 0.1)
    True
    '''



if __name__ == '__main__':
    import doctest
    res = doctest.testmod()
    print res


