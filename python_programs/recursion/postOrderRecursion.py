class Solution:
    def print_reverse(self, i, N):
        if i > N:
            return
        
        self.print_reverse(i + 1, N)

        print(i)
    
sol = Solution()
N = int(input("Enter No.: "))
sol.print_reverse(1, N)