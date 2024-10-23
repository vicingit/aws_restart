# prime_numbers.py

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    """Find all prime numbers in a given range."""
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes

def main():
    start, end = 1, 250
    primes = find_primes(start, end)

    # Display the prime numbers
    print("Prime numbers between 1 and 250:")
    for prime in primes:
        print(prime)

    # Save the results to a file
    with open("results.txt", "w") as file:
        for prime in primes:
            file.write(f"{prime}\n")

    print("Results saved to results.txt")

if __name__ == "__main__":
    main()
