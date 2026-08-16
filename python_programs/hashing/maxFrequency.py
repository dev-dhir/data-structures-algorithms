class Solution:
    def maxFrequency(self, nums, k):

        def highestFreq(nums):

            freq = {}

            for i in nums: 
                freq[i] = freq.get(i, 0) + 1

            valueList = list(freq.values())

            return max(valueList)



sol = Solution()
# arr = list(map(int, input("Enter List: ").split()))
arr = [1, 2, 4, 8]
# k = int(input("Max Operations: "))
k = 2
print(sol.maxFrequency(arr, k))