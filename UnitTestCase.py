import unittest
from PrimeMethods import *

class TestPrimeFunction(unittest.TestCase):
    def test_Unit(self):
        self.assertEqual([2, 3, 5, 7], [x for x in range(1, 10) if prime_find_using_brute_force(x)])
        self.assertEqual([2, 3, 5, 7], [x for x in range(1, 10) if prime_find_using_optimized(x)])
        self.assertEqual([2, 3, 5, 7],  prime_find_using_sieve_of_eratosthenes(1, 10))
        self.assertEqual([2, 3, 5, 7],  prime_find_using_sieve_of_erato_optimized(1, 10))
        self.assertEqual([2, 3, 5, 7],  prime_find_using_segmented_sieve(1, 10))
        primeNumbers = prime_find_using_sieve_of_sundaram(10)
        primeNumbers = [prime for prime in primeNumbers if prime >= 1]
        self.assertEqual([2, 3, 5, 7],  primeNumbers)
        
if __name__ == "__main__":
    unittest.main()
