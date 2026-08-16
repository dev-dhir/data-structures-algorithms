class Solution:
    def GCD(self, n1, n2):
        if n1 == 0:
            return n1
        if n2 == 0:
            return n2

        num = min(n1, n2)


        while num > 0:
            
            if n1 % num == 0 and n2 % num == 0:
                return num
            
            num -= 1

sol = Solution()
n1 = int(input("Enter No.: "))
n2 = int(input("Enter No.: "))
print(sol.GCD(n1, n2))
