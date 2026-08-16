class Solution:
    
    def pattern(self, N):
        def printRow(n):
            f = 65 + (n-1)
            for i in range(n):
                print(chr(f), end = "")

        for i in range(1, N+1):
            printRow(i)
            print("")

sol = Solution()
N = int(input("Enter No.: "))
sol.pattern(N)