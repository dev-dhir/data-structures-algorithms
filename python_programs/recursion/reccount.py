class Solution:
    def count(self, N):
        
        def counter(count):
            if count == 0:
                return
            current = N - count + 1
            print(current)
            
            counter(count - 1)

        counter(N)

sol = Solution()
n = int(input("Enter No.: "))
sol.count(n)