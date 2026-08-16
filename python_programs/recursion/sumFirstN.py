class Solution:
    def summation(self, N):
        
        if N < 0:
            return 0

        return N + self.summation(N - 1)

        # def adder(n, total):
        #     if n < 1:
        #         print(total)
        #         return
            
        #     adder(n-1, total + n)
            
        # adder(N, 0)
            



    
            
sol = Solution()
N = int(input("Enter No.: "))
print(sol.summation(N))
# print(sol.summation(N))