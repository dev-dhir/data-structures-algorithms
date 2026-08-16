class Solution:
    def isArmstrong(self, n):
        if n == 0:
            return True
        num = n
        sum = 0
        count = 0
        count = len(str(n))
            
        while n > 0:
            digit = n % 10
            n //= 10
            sum += digit ** count
         
        return sum == num
        
if __name__ == "__main__":
    sol = Solution()
    n = int(input("Enter No.: "))
    print(sol.isArmstrong(n))