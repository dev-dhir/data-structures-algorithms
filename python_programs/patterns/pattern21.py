class Solution:
    def pattern(self, N):
        
        def printStars(n):
            print("*" * n, end = "")

        def printSpaces(n):
            print(" " * n, end = "")

        if N == 1:
            printStars(1)
            return
        
        for i in range(1, N+1):
            
            printStars(1)
            
            if i == 1 or i == N:
                printStars(N-2)
            else:
                printSpaces(N-2)

            printStars(1)
            print()


sol = Solution()
N = int(input("Enter No.: "))
sol.pattern(N)












# class Solution:
#     # Function to print hollow square pattern
#     def pattern21(self, n):
#         # Outer loop for rows
#         for i in range(n):
#             # Inner loop for columns
#             for j in range(n):
#                 # Print star if it's a border cell
#                 if i == 0 or j == 0 or i == n - 1 or j == n - 1:
#                     print("*", end="")
#                 # Print space otherwise
#                 else:
#                     print(" ", end="")
#             # Move to next line after each row
#             print()


# if __name__ == "__main__":
#     # Create solution object
#     sol = Solution()
#     # Define N
#     N = 1
#     # Call pattern function
#     sol.pattern21(N)
