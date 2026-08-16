class Solution:
    def pattern(self, N):
        def printRow(n): #prints a row of alphabets in ascening order
            f = 65 #ascii for A
            for i in range(n):   # runs n times
                print(chr(f + i), end = "")

        for i in range(N,0,-1):
            printRow(i)
            print("")
    
sol = Solution()
N = int(input("Enter No.: "))
sol.pattern(N)