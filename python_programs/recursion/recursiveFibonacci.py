class Solution:
    def print_fibonacci(self, n):

        def fib(n):
            
            if n == 0:
                return 0
            if n == 1:
                return 1
            
            return fib(n-1) + fib(n-2)
        
        def printnum(i, n):
            if i > n - 1:
                return
            
            print(fib(i))

            printnum(i+1, n)

        printnum(0, n)




sol = Solution()
n = int(input("Enter No.: "))
sol.print_fibonacci(n)
      