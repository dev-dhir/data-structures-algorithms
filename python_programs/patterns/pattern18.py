class Solution:
    def pattern(self, N):


        def caesar(n):
            if n > 90:
                return caesar(n - 26)
            else:
                return n
            
        def printRow(n):   # prints a row
            f = 65 + N - n   # in the last row n = N
            while f <= 64 + N:
                print(chr(caesar(f)), end = " ")
                f += 1

        for i in range(N):
            printRow(i+1)
            print()


sol = Solution()
N = int(input("Enter No.: "))
sol.pattern(N)

