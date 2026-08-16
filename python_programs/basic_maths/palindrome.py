class Solution:
    def isPalindrome(self, n):
        original = n
        rev = 0
        while n > 0:
           
            digit = n % 10
            n //= 10
            rev = rev * 10 + digit


        return original == rev
        

sol = Solution()
n = int(input("Enter No.: "))
print(sol.isPalindrome(n))