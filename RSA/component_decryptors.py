import math

def isqrt(n):
    """Compute the integer square root of a number."""
    if n < 0:
        raise ValueError("Square root not defined for negative numbers")

    x = n
    y = (x + 1) // 2

    while y < x:
        x = y
        y = (x + n // x) // 2

    return x

def find_close_primes(N):
    """Find primes p and q where p*q = N and p and q are close to each other."""
    
    # Get an integer approximation of the square root of N
    approx_sqrt = isqrt(N)
    
    # Start from the approximated square root and search downwards for p and q
    for i in range(approx_sqrt, 1, -1):
        if N % i == 0:
            return i, N // i
    raise ValueError("Primes not found")

N = 15972193516711703087975582449793504899982274258760381909057914913499126400701433190829877310243699018526708836900867372490402854810661545464340802243237717845901675273164067733547340908544986777415862909880483844764971811594335411631581716596903273403413215383814687587225835341467243820523153721094354243810241012878394079431273089869736979808786425443568649955308808312873768015381849609595593775592239287925487722235813534656970918248030849488151451863029475041432293482494580883639848217518053758401094744542047964886269002853104067452346093869377068552518372694489915597106650532929798202293577261029092718156767  # replace with your value of N

p, q = find_close_primes(N)
print(f"p = {p}")
print(f"q = {q}")
