class Solution:
    def pattern(self, N):
        def printStars(n):
            print("*" * n, end = "")

        def printSpaces(n):
            print(" " * n, end = "")

        def printLine(i):
                printStars(i)
                printSpaces(2 * (N-i))
                printStars(i)
                print()

        def upper_half():
            for i in range(1, N+1):
                printLine(i)

        def lower_half():
            for i in range(N-1, 0, -1):
                printLine(i)


        upper_half()
        lower_half()

sol = Solution()
N = int(input("Enter No.: "))
sol.pattern(N)