
class PrimeUsingBruteForce():
    def prime_find_using_brute_force(num):
        if num < 2:
            return False
        else:
            for i in range(2, num):
                if(num%i == 0):
                    return False
            return True