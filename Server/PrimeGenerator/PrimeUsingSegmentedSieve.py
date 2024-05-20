import math
class PrimeUsingSegmentedSieve():
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

    def prime_find_using_segmented_sieve(num1, num2):
        limit = int(math.sqrt(num2)) + 1
        primes = PrimeUsingSegmentedSieve.simple_sieve(limit)
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