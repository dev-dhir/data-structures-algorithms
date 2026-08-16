class Solution:
    def reverse(self, arr: list, N: int) -> None:
        def rev(arr, i, j):
            if i >= j:
                return
            
            
            arr[i], arr[j] = arr[j], arr[i]


            rev(arr, i + 1, j - 1 )

        rev(arr, 0, N-1)
        
        return arr

sol = Solution()
arr = [1,2,3,4,5]
print(sol.reverse(arr, len(arr)))