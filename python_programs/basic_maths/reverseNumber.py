class Solution:
    def reverseNumber(self, n):
        rev = 0
        while n > 0:
           
            temp = n % 10
            n //= 10
            rev = rev * 10 + temp

        return rev
        

sol = Solution()
n = int(input("Enter No.: "))
print(sol.reverseNumber(n))