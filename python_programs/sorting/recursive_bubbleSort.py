class Solution:
    def bubble_sort(self, nums):
        if len(nums) <= 1:
            return
        
        def compare_and_swap(index, limit):  # compares the element at index with the next element and swaps if needed up for <limit> valid elementxs
            swaps = 0
            if nums[index] < nums[index - 1]:
                nums[index], nums[index - 1] = nums[index - 1], nums[index]
                swaps += compare_and_swap(index + 1, limit) if index + 1 < limit else 0   # limit = len(nums) - sorted_index
            return swaps

        # for sorted_index in range(len(nums) + 1):
        #     compare_and_swap(1, len(nums) - sorted_index)
        def bubbleSort(sorted_index):
            if sorted_index >= len(nums) - 1:
                return
            
            if not compare_and_swap(1, len(nums) - sorted_index):
                exit
            bubbleSort(sorted_index + 1)

        bubbleSort(0)



sol = Solution()
nums = [5, 3, 2, 4, 1]
sol.bubble_sort(nums)
print(nums)            


