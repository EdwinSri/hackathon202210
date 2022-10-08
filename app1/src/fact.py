import math
""" 
#### factorial function example ### 
 fact n 
 n integer number
 commande_type fact
 args : n , positive integer 
 in  case of of negative return 0
"""

def factorielle(a):
    if a < 0:
        return 'undefined'
    return math.factorial(a)

def cmd_fact(n):
    return str(factorielle(n))
