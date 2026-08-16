class Solution:
    def countDigit(self, N):
        N = abs(N)

        count = 0

        if N == 0:
            return 1
        
        while N > 0:
            N //= 10
            count += 1

        print(count)
    
sol = Solution()
N = int(input("Enter No.: "))
print(sol.fountDigit(N))

