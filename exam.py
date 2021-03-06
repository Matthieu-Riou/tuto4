#! /usr/bin/env python
# -*- coding: utf-8 -*-


def function(x, y):
    ''' (int, int) -> int

    Returns x * (y + 2)

    Retourne x * (y + 2)

    >>> function(3, 5)
    21
    >>> function(10, 2)
    40
    '''
    # Your code here



def function2(x, y):
    ''' (int, int) -> int

    Returns (x * (y + 2))² - x * (y + 2). Reuse previous function.

    Retourne (x * (y + 2))² - x * (y + 2). Réutilissez la fontion précédente.

    >>> function2(2,1)
    30
    >>> function2(3, 5)
    420
    >>> function2(10,2)
    1560
    >>> check_usage(function2, "function")
    True
    '''
    # Your code here



def nb_words(s):
    ''' (str) -> int

    Returns the number of words (separated by a space) in the sentence s.

    Retourne le nombre de mots (séparés par un espace) dans la phrase s.

    >>> nb_words("Ce code fonctionne bien.")
    4
    >>> nb_words("C'est un bien beau programme.")
    5
    '''
    # Your code here



def list_words(s):
    ''' (str) -> list of str

    Returns a list of the words (separated by a space) in the sentence s.

    Retourne une liste contenant les mots (séparés par un espace) de la phrase s.

    >>> list_words("Ce code fonctionne bien.")
    ['Ce', 'code', 'fonctionne', 'bien.']
    >>> list_words("C'est un bien beau programme.")
    ["C'est", 'un', 'bien', 'beau', 'programme.']
    '''
    # Your code here



def split_words_by_line(s):
    ''' (str) -> str

    Returns a string containing each word (separated by a space) of the 
    sentence s on a new line.

    Retourne une chaîne de caractères contenant chaque mot (séparés par 
    un espace) de la phrase s sur une nouvelle ligne.

    >>> split_words_by_line("Ce code fonctionne bien.")
    'Ce\\ncode\\nfonctionne\\nbien.'
    >>> print split_words_by_line("Cest un bien beau programme.")
    Cest
    un
    bien
    beau
    programme.
    '''
    # Your code here



def has_n_chars(s, c, n):
    ''' (str, str, int) -> Boolean

    Find and return if c appears at least n times in s.

    Calcule et retourne si c apparaît au moins n fois dans s.

    >>> has_n_chars("un serpent si souple", "s", 3)
    True
    >>> has_n_chars("l'attaque tant attendue", "t", 4)
    True
    >>> has_n_chars("veni vidi vici", "v", 5)
    False
    '''
    # Your code here



def is_palindrome(s):
    ''' (str) -> Boolean

    Find and return if s is a palindrome.

    Cacule et retourne si s est un palindrome.

    >>> is_palindrome("anna")
    True
    >>> is_palindrome("revolver")
    False
    >>> is_palindrome("ressasser")
    True
    >>> check_usage(is_palindrome, "is_palindrome")
    True
    '''
    # Your code here



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
    >>> check_usage(coprimes, "pgcd")
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



def get_indice_of_min(l, n):
    ''' (list of int, int) -> int

    Returns the indice of the smallest element among the n first elements of l.

    Retourne l'indice du plus petit élément parmi les n premiers éléments de l.

    >>> get_indice_of_min([9, 8, 2, 6, 5, 1], 4)
    2
    >>> get_indice_of_min([9, 8, 2, 6, 5, 1], 5)
    2
    >>> get_indice_of_min([9, 8, 2, 6, 5, 1], 6)
    5
    >>> get_indice_of_min([9, 8, 2, 6, 5, 1], 7)
    5
    '''
    # Your code here



def sort_reverse(l):
    ''' (list of int) -> list of int

    Sort l in decreasing order using the get_indice_of_min() function.

    Trie l dans l'ordre décroissant en utilisant la fonction get_indice_of_min().

    >>> l = [9, 8, 2, 6, 5, 1] ; sort_reverse(l) ; l
    [9, 8, 6, 5, 2, 1]
    >>> check_usage(sort_reverse, "get_indice_of_min")
    True
    '''
    # Your code here



if __name__ == '__main__':
    print "Use runtests to tests your functions : `python runtests.py`"
    print "Use `python runtests.py -h` for helps"


