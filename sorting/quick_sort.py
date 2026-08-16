class Solution:
    def quick_sort(self, nums):
        def partition(l, h):
            if l >= h:
                return
            pivot_index = l
            pivot = nums[l]
            left = l + 1
            right = h
            while left <= right:
                while left <= right and nums[left] <= pivot:
                    left += 1
                while left <= right and nums[right] > pivot:
                    right -= 1
                if  left < right:
                    nums[left], nums[right] = nums[right], nums[left]
            
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            partition(l, right - 1)
            partition(right + 1, h)
                
            
        partition(0, len(nums) - 1)



sol = Solution()
nums = [8, 3, 5, 1, 9, 2] # list(map(int, input("Enter Array ").split()))
sol.quick_sort(nums)
print(nums)