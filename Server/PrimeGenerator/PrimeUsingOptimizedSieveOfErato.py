
class PrimeUsingOptimizedSieveOfErato():
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