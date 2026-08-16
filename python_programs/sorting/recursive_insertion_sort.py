class Solution:
    def insertion_sort(self, nums):
        def shift_and_place(i, key):          #takes the last element of an array and inserts it to its correct position
            if i >= 0 and nums[i] > key:
                nums[i+1] = nums[i]
                shift_and_place(i-1, key)
            else:
                nums[i+1] = key

        def insert(index):
            if index >= len(nums):
                return
            key = nums[index]
            shift_and_place(index - 1, key)
            insert(index + 1)

        insert(1)




sol = Solution()
nums = list(map(int, input("Enter Array: ").split()))
sol.insertion_sort(nums)
print(nums)
