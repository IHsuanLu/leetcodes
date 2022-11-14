from cmath import sqrt


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # 0 and 1 are not prime
        is_prime = [False, False] + [True] * (n - 2)
        
        for i in range(2, int(sqrt(n)) + 1):
            if is_prime[i]:
                # since the number lower than i * i are already marked in the previous runs
                # more pythonic: primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
                multiplier = i
                while i * multiplier < n:
                    is_prime[i * multiplier] = False
                    multiplier += 1
    
        print(is_prime)
        return sum(is_prime)