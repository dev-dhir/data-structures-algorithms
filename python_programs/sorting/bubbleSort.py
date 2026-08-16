class Solution:
    def bubble_sort(self, nums):
        def pass_swap(sorted_index):  # sorted_index -> no. of indices sorted at the end of the array
            swaps = 0
            for i in range(len(nums) - sorted_index - 1):  
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swaps += 1
            return swaps  # returns the no. of swaps

        for i in range(0, len(nums)):
            if not pass_swap(i):
                return                      # already sorted, return early


        


sol = Solution()
nums = list(map(int, input("Enter Array: ").split()))
sol.bubble_sort(nums)
print(nums)