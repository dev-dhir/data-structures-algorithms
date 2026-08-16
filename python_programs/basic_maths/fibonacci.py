class Solution:
    def print_fibonacci(self, n):
        prev = 0
        current = 1

        for i in range(n):
            print(prev)
            temp = prev
            prev = current
            current += temp

sol = Solution()
n = int(input("Enter No.: "))
sol.print_fibonacci(n)
      