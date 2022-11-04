import math;

def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(2*i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True];

#단일 숫자에 대한 소수판별 알고리즘.
def is_prime_number(x):
    if x <= 1 :
        return False;
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False;
    return True;