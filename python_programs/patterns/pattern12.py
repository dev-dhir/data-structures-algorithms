class Solution:
    def pattern(self, N):

        def printSpaces(n):
            for i in range(n):
                print(" ", end = "")

        def printRow(n):
            for i in range(1, n+1):
                print(i, end = "")
        
        def printRevRow(n):
            for i in range(n, 0, -1):
                print(i, end = "")

        for i in range (1, N+1):
            printRow(i)
            printSpaces(2*(N-i))
            printRevRow(i)
            print("")


sol = Solution()
N = int(input("Enter No.: "))
sol.pattern(N)

