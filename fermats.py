from Crypto.PublicKey import RSA
import sympy

def factorize_n(n):
    # Using sympy's factorint method to factorize n
    factors = sympy.factorint(n)
    # Converting factors to a list of primes
    primes = list(factors.keys())
    if len(primes) != 2:
        raise ValueError("Factorization did not result in exactly two primes.")
    return primes[0], primes[1]

# Example modulus n (replace with your actual n)
n = 3233  # This is a small example; replace with the real n

try:
    p, q = factorize_n(n)
    print(f"p: {p}")
    print(f"q: {q}")

    # Validate using pycryptodome (Optional)
    key = RSA.construct((n, 65537, None, p, q))
    print("Validation successful.")
except Exception as e:
    print(f"Error: {e}")
