class Solution:
    def pattern(self, N):
        
        def printStars(n):
            print("*" * n, end = "")

        def printSpaces(n):
            print(" " * n, end = "")

        def upper_half():
            for i in range(N):
                printStars(N-i)
                printSpaces(i * 2)
                printStars(N-i)
                print()
        
        def lower_half():
            for i in range(N-1,-1, -1):
                printStars(N-i)
                printSpaces(i * 2)
                printStars(N-i)
                print()

        upper_half()
        lower_half()
            

sol = Solution()
N = int(input("Enter No.: "))
sol.pattern(N)
