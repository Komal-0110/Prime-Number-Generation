class PrimeUsingSieveErot():
    def prime_find_using_sieve_of_eratosthenes(num1, num2):
        if num1 < 2:
            num1 = 2
        prime = [True] * ((num2-num1) + 1)
        
        for p in range(2, (int(num2**0.5))+1):
            for i in range(max(p * p, (num1//p)*p), num2+1, p):
                if i >= num1:
                    prime[i - num1] = False
        # while p * p <= num2+1:
        #     if prime[p]:
        #         for i in range(p * p, num2 + 1, p):
        #             prime[i] = False
        
        #     p += 1
        # primes = []
        # for p in range((max(2, num1)), num2+1):
        #     if prime[p]:
        #         primes.append(p)
        return [num1 + i for i, is_prime in enumerate(prime) if is_prime]