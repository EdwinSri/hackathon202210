import numpy

"""
Command: prime_numbers
Return a list of all the prime numbers inferior or equal to n
"""
def prime_numbers(n):
    #https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return (numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]).tolist()


"""
Command: sum_prime_numbers
Return a sum of all the prime numbers inferior or equal to n
"""
def sum_prime_numbers(n):
    return sum(prime_numbers(n))
