def smallest_prime_factor(valor):
    """Returns the smallest prime number that is a divisor of x"""
    # Start checking with 2, then move up one by one
    numero = 2
    while numero < valor:
        if valor!=numero and valor % numero == 0:
            return numero

print(smallest_prime_factor(12)) # should be 2
print(smallest_prime_factor(15)) # should be 3