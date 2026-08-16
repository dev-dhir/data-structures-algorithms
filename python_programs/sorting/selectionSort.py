class Solution:
    def selectionSort(self, nums):
        def rangeMin(arr, start):           
            i = start + 1
            min_index = start
            while i < len(arr):
                if arr[i] < arr[min_index]:
                    min_index = i
                i += 1
            return min_index
        
        for i in range(len(nums)):

            min_index = rangeMin(nums, i)

            nums[i], nums[min_index] = nums[min_index], nums[i]       

sol = Solution()
nums = list(map(int, input("Enter Array: ").split()))
sol.selectionSort(nums)
print(nums)