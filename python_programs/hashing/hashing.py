class Solution:
    def hashing(self, text, check):
        hashArray = []
        hashArray = [0] * 256

        for letter in text:
            hashArray[ord(letter)] += 1

        print(hashArray[ord(check)])

sol = Solution()
text = input("Enter Text: ")
check = input("Enter Letter: ")
sol.hashing(text, check)
        


