class Solution:
    def check_palindrome(self, text):
        n = len(text)
        def is_pali(text, i, j):
            if i >= j:
                return True
            
            if text[i] != text[j]:  
                return False
            
            return is_pali(text, i + 1, j - 1)

        return is_pali(text, 0, n - 1)

sol = Solution()
text = "blerp"
print(sol.check_palindrome(text))
