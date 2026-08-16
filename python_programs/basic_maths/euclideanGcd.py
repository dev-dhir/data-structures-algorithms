class Solution:
    def gcd(self, a, b):
        a = abs(a)
        b = abs(b)
        while a > 0 and b > 0:
            if a > b:
                a %= b
            else:
                b %= a
            
        if a == 0:
            return b
        return a
    
sol = Solution()
a = int(input("Enter No.: "))
b = int(input("Enter No.: "))
print(sol.gcd(a, b))