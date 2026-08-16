class Solution:
    def maxFrequency(self, nums):

        freq = {}

        for i in nums: 
            freq[i] = freq.get(i, 0) + 1

        maxValue = max(freq.values())
        keyList = []
        for key, value in freq.items():
            if value == maxValue:
                keyList.append(key)

        return min(keyList)

sol = Solution()
arr = list(map(int, input("Enter List: ").split()))
print(sol.maxFrequency(arr))