class Solution:
    
    def pattern(self, N):
        # f = 0
        def printRow(n):
            # nonlocal f
            
            if n % 2 != 0: # n is odd
                f = 1 # set f to odd initially
            else:          # n is even
                f = 0 # set f to even initially
                     
            for i in range(n):

                if f%2 == 0: # f is even
                    print("0", end = "")
                else:        # f is odd
                    print("1", end = "")
                f += 1



        for i in range(1, N+1):
            printRow(i)
            print("")

sol = Solution()
N = int(input("Enter No.: "))
sol.pattern(N)
