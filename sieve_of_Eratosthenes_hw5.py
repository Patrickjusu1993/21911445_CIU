#Sieve of Eratosthenes is simple, ancient algorithm for finding all prime numbers up to any given limit. 
#A python application that ask user for upper limit as n and use this ancient algorithm to print all available prime numbers from 2 to n.

#Patrick Jusu ID:21911445

n = int(input( "Enter upper limit of a range:"))
sieve = set(range(2, n+1))
while sieve:
    prime=min(sieve)
    print(prime, end="\t")
    sieve-=set(range(prime, n+1, prime))
    
print()
