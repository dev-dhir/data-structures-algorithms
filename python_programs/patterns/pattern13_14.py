class Solution:
    
    def pattern(self, N):
        f = 1
        def printRow(n):
            nonlocal f
            f = 65
            for i in range(n):
                print(chr(f), end = " ")
                f += 1

        for i in range(1, N+1):
            printRow(i)
            print("")

sol = Solution()
N = int(input("Enter No.: "))
sol.pattern(N)