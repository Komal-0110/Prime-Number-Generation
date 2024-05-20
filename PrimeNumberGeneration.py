from PrimeMethods import * 


primeNumbers = [] # storing prime number in list
while True:
    print("Enter your choice for:")
    print("1. Find prime numbers using brute force approach.")
    print("2. Find prime numbers using optimized approach.")
    print("3. Find prime numbers using Sieve of Eratosthenes.")
    print("4. Find prime numbers using Optimized Sieve of Eratosthenes.")
    print("5. Find prime numbers using Segmented Sieve.")
    print("6. Find prime numbers using Sieve of sundaram.")
    print("7. Exit")

    try:
        # Getting choice from user
        choice = int(input("Enter your choice. "))
        if choice == 7:
            break
        # Getting numbers from user
        num1 = int(input("Enter the starting number of the range "))
        num2 = int(input("Enter the ending number of the range "))
    except ValueError:
        print("Incorrect value, please try again!")
        continue
    
    if(choice == 1):
        primeNumbers = [x for x in range(num1, num2+1) if prime_find_using_brute_force(x)]
        print(f"Prime numbers between {num1} and {num2} are: {primeNumbers}")
        primeNumbers.clear()
    elif(choice == 2):
        primeNumbers = [x for x in range(num1, num2+1) if prime_find_using_optimized(x)]
        print(f"Prime numbers between {num1} and {num2} are: {primeNumbers}")
        primeNumbers.clear()
    elif(choice == 3):
        print(f"Prime numbers between {num1} and {num2} are: {prime_find_using_sieve_of_eratosthenes(num1, num2)}")
    elif(choice == 4):
        print(f"Prime numbers between {num1} and {num2} are: {prime_find_using_sieve_of_erato_optimized(num1, num2)}")
    elif(choice == 5):
        print(f"Prime numbers between {num1} and {num2} are: {prime_find_using_segmented_sieve(num1, num2)}")
    elif(choice == 6):
        primeNumbers = prime_find_using_sieve_of_sundaram(num2)
        print('primeNumbers : ', primeNumbers)
        primeNumbers = [prime for prime in primeNumbers if prime >= num1]
        print(f"Prime numbers between {num1} and {num2} are: {primeNumbers}")
    else:
        print("Invalid choice. Please try again.")