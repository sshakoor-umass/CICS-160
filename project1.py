#Sheik Shakoor

def is_prime(n):
    if n <= 1:
        return False
    #divisible numbers in between 2 and "n"
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def are_relatively_prime(x, y):
    #number cant a factor bigger than itself
    smallest = min(x, y)

    #any shared factors?
    for i in range(2, smallest + 1):
        if x % i == 0 and y % i == 0:
            return False

    return True
def primes_up_to(n):
    primes = []

    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes
def prime_decomposition(n):
    factors = []
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1

    return factors
def decomp_check(n):
    factors = prime_decomposition(n)

    if len(factors) != 2:
        return False

    return factors[0] != factors[1]

if __name__ == '__main__':
    print(is_prime(10))  
    print(is_prime(17))
    print(are_relatively_prime(10, 17))
    print(are_relatively_prime(21, 10))
    print(primes_up_to(10))  
    print(primes_up_to(1))
    print(prime_decomposition(10))  
    print(prime_decomposition(24))  
    print(prime_decomposition(101))  