#! /usr/bin/env python

def sumIsOdd(a, b):
    ''' (int, int) -> Boolean

    Returns True iif a+b is odd

    >>> sumIsOdd(1, 3)
    False
    >>> sumIsOdd(2, 3)
    True
    >>> sumIsOdd(1, 1)
    False
    >>> sumIsOdd(-1, 3)
    False
    >>> sumIsOdd(-1, -2)
    True
    '''











if __name__ == '__main__':
    import doctest
    res = doctest.testmod()
    print res


