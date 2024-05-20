
class PrimeUsingSieveOfSundaram():
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