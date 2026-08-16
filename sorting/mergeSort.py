class Solution:
    def merge_sort(self, nums):
        def merge(arr1, arr2): # function to merge two arrays
            i, j = 0, 0
            merged = []
            while i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
                    merged.append(arr1[i])
                    i += 1
                else:
                    merged.append(arr2[j])
                    j += 1
            merged.extend(arr1[i:])
            merged.extend(arr2[j:])
            return merged
                
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            return merge(mergeSort(left), mergeSort(right))

        result = mergeSort(nums)

        return result




sol = Solution()
nums = [5, 4, 2, 1, 3, 4]
print(sol.merge_sort(nums))
