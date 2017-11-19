# Count the number of prime numbers less than a non-negative number, n.

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        totalPrimes = 0
        isPrime = [True] * n
        for i in range(2, n):
            if isPrime[i]:
                totalPrimes += 1
                j = 2
                while j * i < n:
                    isPrime[j * i] = False
                    j += 1

        return totalPrimes