class Solution:
    def countFrequencies(self, nums):

        freq = {}

        for i in nums: 
            freq[i] = freq.get(i, 0) + 1

        # freqList = (list(map(list, (freq.items()))))
        freqList = [list(item) for item in freq.items()]

        return freqList

sol = Solution()
arr = list(map(int, input("Enter List: ").split()))
print(sol.countFrequencies(arr))