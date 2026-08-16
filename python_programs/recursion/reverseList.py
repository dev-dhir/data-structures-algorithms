class Solution:
    def reverse(self, arr: list, N: int) -> None:
        def rev(arr, n):
            if n <= 1: # n = 5
                return
            
            temp = arr.pop(n - 2)  # The last element is already in its final position.
            arr.append(temp)       # Move the second-last element to the end.

            rev(arr, n-1)

        rev(arr, N)
        
        print(arr)

sol = Solution()
arr = [1,2,3,4,5]
sol.reverse(arr, len(arr))