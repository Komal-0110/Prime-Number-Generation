from .PrimeUsingBruteForce import PrimeUsingBruteForce
from .PrimeUsingOptimized import PrimeUsingOptimized
from .PrimeUsingSieveErot import PrimeUsingSieveErot
from .PrimeUsingOptimizedSieveOfErato import PrimeUsingOptimizedSieveOfErato
from .PrimeUsingSegmentedSieve import PrimeUsingSegmentedSieve
from .PrimeUsingSieveOfSundaram import PrimeUsingSieveOfSundaram

class PrimeGenerate():

    def prime_number_generator_by_choosing_algorithm(start_range, end_range, algorithm_choosen):
        if(algorithm_choosen == 1):
            primeNumbers = [x for x in range(start_range, end_range+1) if PrimeUsingBruteForce.prime_find_using_brute_force(x)]
            return primeNumbers
        elif(algorithm_choosen == 2):
            primeNumbers = [x for x in range(start_range, end_range+1) if PrimeUsingOptimized.prime_find_using_optimized(x)]
            return primeNumbers
        elif(algorithm_choosen == 3):
            primeNumbers = PrimeUsingSieveErot.prime_find_using_sieve_of_eratosthenes(start_range, end_range)
            return primeNumbers
        elif(algorithm_choosen == 4):
            primeNumbers = PrimeUsingOptimizedSieveOfErato.prime_find_using_sieve_of_erato_optimized(start_range, end_range)
            return primeNumbers
        elif(algorithm_choosen == 5):
            primeNumbers = PrimeUsingSegmentedSieve.prime_find_using_segmented_sieve(start_range, end_range)
            return primeNumbers
        elif(algorithm_choosen == 6):
            primeNumbers = PrimeUsingSieveOfSundaram.prime_find_using_sieve_of_sundaram(end_range)
            primeNumbers = [prime for prime in primeNumbers if prime >= start_range]
            return primeNumbers