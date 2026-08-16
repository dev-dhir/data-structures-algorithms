class Solution:
    def printName(self, name, n):
        
        def print_name(n):
            if n <= 0:
                return
            
            print(name, end = " ")
            print_name(n-1)

        print_name(n)

sol = Solution()
name = "Dev"
n = int(input("Enter No.: "))
sol.printName(name, n)