import math
# Finding prime number method 1
def prime_find_using_brute_force(num):
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if(num%i == 0):
                return False
        return True

 # Finding prime number method 2
def prime_find_using_optimized(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if(num%i == 0):
                return False
        return True
    
# Finding prime number method 3
def prime_find_using_sieve_of_eratosthenes(num1, num2):
    if num1 < 2:
        num1 = 2
    prime = [True] * ((num2-num1) + 1)
    
    for p in range(2, (int(num2**0.5))+1):
        for i in range(max(p * p, (num1//p)*p), num2+1, p):
            if i >= num1:
                prime[i - num1] = False
    return [num1 + i for i, is_prime in enumerate(prime) if is_prime]

# Finding prime number method 4
def prime_find_using_sieve_of_erato_optimized(num1, num2):
    if num1 < 2:
        num1 = 2
    is_prime = [True] * (num2+1)
    
    is_prime[0], is_prime[1] = False, False

    for p in range(2, (int(num2**0.5))+1):
        if is_prime:
            for i in range(p * p, num2 +1, p):
                is_prime[i] = False

    prime_number = [x for x in range(num1, num2+1) if is_prime[x]]
    return prime_number

def simple_sieve(limit):
    primes = []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for num in range(2, int(math.sqrt(limit)) + 1):
        if sieve[num]:
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    for num in range(2, limit + 1):
        if sieve[num]:
            primes.append(num)
    return primes

# Finding prime number method 5
def prime_find_using_segmented_sieve(num1, num2):
    limit = int(math.sqrt(num2)) + 1
    primes = simple_sieve(limit)
    segmented_primes = []
    if num1 < 2:
        num1 = 2
    sieve_size = num2 - num1 + 1
    sieve = [True] * sieve_size
    for prime in primes:
        start = max(prime * prime, (num1 + prime - 1) // prime * prime)
        for multiple in range(start, num2 + 1, prime):
            sieve[multiple - num1] = False

    for i in range(sieve_size):
        if sieve[i]:
            segmented_primes.append(i + num1)   
    return segmented_primes

# Finding prime number method 6
def prime_find_using_sieve_of_sundaram(n):
    n = (n - 1) // 2
    marked = [False] * (n + 1)
    for i in range(1, (n // 2) + 1):
        j = i
        while (i + j + 2 * i * j) <= n:
            marked[i + j + 2 * i * j] = True
            j += 1
    primes = [2]
    for i in range(1, n + 1):
        if not marked[i]:
            primes.append(2 * i + 1)
    
    return primes