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
    tuple of those three digits.premier entre eux

    Cette fonction prend un entier de maximum trois chiffres en paramètre, et
    retourne un tuple contenant chacun de ces trois chiffres.

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

    Calcule et retourne le plus grand dénominateur commun de p et q.

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



def coprimes(a, b):
    ''' (int, int) -> Boolean

    Find and return if a and b are coprimes.

    Calcule et retourne si a et b sont premiers entre eux.

    >>> coprimes(27, 32)
    True
    >>> coprimes(15, 25)
    False
    >>> coprimes(21, 23)
    True
    '''
    # Your code here    




def remove_odd_numbers(l):
    ''' (list of int) -> NoneType

    Remove all the odd numbers from the list l.
    
    Supprime tous les nombres impairs de la liste l.

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

    Returns the list containing the elements that are in both lists l1 and l2.

    Retourne la liste contenant les éléments qui sont présents dans les deux listes l1 et l2.


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

    Retourne l'indice du plus petit élément parmi les n premiers éléments de l.

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

    Trie l dans l'ordre décroissant en utilisant la fonction getIndiceOfMin().

    >>> l = [9, 8, 2, 6, 5, 1] ; sortReverse(l) ; l
    [9, 8, 6, 5, 2, 1]
    '''
    # Your code here




if __name__ == '__main__':
    print "Use runtests to tests your functions : `python runtests.py`"
    print "Use `python runtests.py -h` for helps"


