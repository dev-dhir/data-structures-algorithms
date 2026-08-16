class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        def is_pali(text, i, j):


            if i >= j:
                return True

            if not("A" <= text[i] <= "Z" or "a" <= text[i] <= "z" or "0" <= text[i] <= "9"):
                return is_pali(text, i + 1, j)
            if not("A" <= text[j] <= "Z" or "a" <= text[j] <= "z" or "0" <= text[j] <= "9"):
                return is_pali(text, i, j - 1)
         
            if text[i] != text[j]: 
                if abs(ord(text[i]) - ord(text[j])) != 32: 
                    return False
                elif ("A" <= text[i] <= "Z" or "a" <= text[i] <= "z") and ("A" <= text[j] <= "Z" or "a" <= text[j] <= "z"):
                    return is_pali(text, i + 1, j - 1)
                else:
                    return False

                    
            
            return is_pali(text, i + 1, j - 1)

        return is_pali(s, 0, n - 1)
    
sol = Solution()
s = "0P"
print(sol.isPalindrome(s))