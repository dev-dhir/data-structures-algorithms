import math

class Solution:
    def divisors(self, n):
        divisors = []
        for i in range(1,math.isqrt(n) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n//i:
                    divisors.append(n//i)
                

        divisors.sort()
        print(divisors)
        print(type(divisors))



sol = Solution()
n = int(input("Enter No.: "))
sol.divisors(n)
