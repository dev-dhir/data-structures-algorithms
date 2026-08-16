class Solution:
    def factorial(self, N):
        def fac(n):
            print(f"New call ; n = {n}")
            if n <= 1:
                return 1

            return n * fac(n-1)
        
        print(fac(N))
        
sol = Solution()
n = int(input("Enter No.: "))
sol.factorial(n)