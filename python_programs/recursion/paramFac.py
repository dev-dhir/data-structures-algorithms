# Factorial using parametric recursion
class Solution:
    def factorial(self, N):
        def fact(n, fac):
            if n < 1:
                print(fac)
                return
            
            fact(n - 1, n * fac)

        fact(N, 1)
sol = Solution()
N = int(input("Enter No>: "))
sol.factorial(N)
            

