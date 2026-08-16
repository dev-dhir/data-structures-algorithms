class Solution:
    def insertion_sort(self, nums):
        def insert_element(arr, key):          #takes the last element of an array and inserts it to its correct position
            temp = arr[key]
            shifts = 0
            insert_pos = key
            while insert_pos > 0 and arr[insert_pos - 1] > temp:
                arr[insert_pos] = arr[insert_pos - 1]
                insert_pos -= 1
                shifts += 1

            arr[insert_pos] = temp
            return shifts
            


        is_sorted = True
        for i in range(1, len(nums)):
            if insert_element(nums, i) != 0:
                is_sorted = False
        return is_sorted




sol = Solution()
nums = list(map(int, input("Enter Array: ").split()))
is_sorted = sol.insertion_sort(nums)
print(nums)
print(f"Was the array already sorted? {is_sorted}")