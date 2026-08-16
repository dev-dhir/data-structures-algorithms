class Solution:
    def merge_sort(self, nums):
        def merge(arr, low, mid, high):
            left = low
            right = mid + 1
            merged = []
            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    merged.append(arr[left])
                    left += 1
                else:
                    merged.append(arr[right])
                    right += 1
            merged.extend(arr[left:mid + 1])
            merged.extend(arr[right:])

            arr = merged
                
        def mergeSort(arr, low, high):
            if len(arr) <= 1:
                return arr
            
            mid = low + high // 2

            mergeSort(arr, low, mid)

            mergeSort(arr, mid + 1, high)


            merge(arr, low, mid, high )

        result = mergeSort(nums)

        return result




sol = Solution()
nums = [5, 4, 2, 1, 3, 4]
print(sol.merge_sort(nums))
