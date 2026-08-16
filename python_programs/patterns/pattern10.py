class Solution:
    def pattern(self, N):
        
        def printRow(n):
            for i in range(n):
                print("*", end = "")

        for i in range(1, N):
            printRow(i)
            print("")

        for i in range(N,0,-1):
            printRow(i)
            print("")
    
sol = Solution()
N = int(input("Enter No.: "))
sol.pattern(N)