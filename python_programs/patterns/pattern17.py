class Solution:
    def pattern(self, N):

        def printSpaces(n):
            for i in range(n):
                print(" ", end = "")

        def printRow(n):
            f = 65
            for i in range(1,(n*2)):
                print(chr(f), end = "")
                if i<n:
                    f += 1
                else:
                    f -= 1
            print()

        for i in range(1, N+1):
            printSpaces(N-i)
            printRow(i)

sol = Solution()
N = int(input("Enter No.: "))
sol.pattern(N)
