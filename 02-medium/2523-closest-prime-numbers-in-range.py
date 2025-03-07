import math


class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        def sieveOfEratosthenes(limit):
            primes = [True] * (limit + 1)
            primes[0] = primes[1] = False

            for p in range(2, int(math.sqrt(limit)) + 1):
                if primes[p]:
                    for multiple in range(p * p, limit + 1, p):
                        primes[multiple] = False

            return [num for num, is_prime in enumerate(primes) if is_prime]

        def segmentedSieve(left, right):
            if left < 2:
                left = 2

            limit = int(math.sqrt(right))
            primes = sieveOfEratosthenes(limit)

            isPrimeRange = [True] * (right - left + 1)

            for prime in primes:
                start = max(prime * prime, left + (prime - left % prime) % prime)
                for multiple in range(start, right + 1, prime):
                    isPrimeRange[multiple - left] = False

            return [
                num for i, num in enumerate(range(left, right + 1)) if isPrimeRange[i]
            ]

        primeNums = segmentedSieve(left, right)
        if len(primeNums) < 2:
            return [-1, -1]

        minDiff = 1_000_000
        idx = -1
        for i in range(1, len(primeNums)):
            if primeNums[i] - primeNums[i - 1] < minDiff:
                minDiff = primeNums[i] - primeNums[i - 1]
                idx = i

        return [primeNums[idx - 1], primeNums[idx]]


if __name__ == "__main__":
    s = Solution()
    print(s.closestPrimes(10, 19))
    print(s.closestPrimes(4, 6))


class TLESolution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        primeNums = []

        def checkPrime(n: int):
            if n < 2:
                return False
            for i in range(2, math.isqrt(n) + 1):  # Correct loop range
                if n % i == 0:
                    return False
            return True

        for i in range(left, right + 1):
            if checkPrime(i):
                primeNums.append(i)

        if len(primeNums) == 1:
            return [-1, -1]

        minDiff = 1_000_000
        idx = -1
        for i in range(1, len(primeNums)):
            if primeNums[i] - primeNums[i - 1] < minDiff:
                minDiff = primeNums[i] - primeNums[i - 1]
                idx = i

        return [primeNums[idx - 1], primeNums[idx]]
