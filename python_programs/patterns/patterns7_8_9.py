class Solution:
    def pattern(self, N):

        def printSpace(n):  # prints n spaces
            for i in range(n):
                print(" ", end = "")

        def printRow(n):    # prints n stars
            for i in range(n):
                print("*", end = "")
        

        for i in range(1, N+1):
            printSpace(N-i)
            printRow((2*i)-1)
            print()
            
        for i in range(N, 0, -1):
            printSpace(N-i)
            printRow((2*i)-1)
            print()

sol = Solution()
N = int(input("Enter No.: "))
sol.pattern(N)