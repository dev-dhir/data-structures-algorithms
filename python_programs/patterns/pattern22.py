class Solution:
    def pattern(self, N):

        size = 2 * N - 1

        for i in range(size):

            for j in range(size):

                top = i
                left = j
                right = size - 1 - j
                bottom = size - 1 - i

                layer = min(top, left, right, bottom)

                print(N - layer, end = " ")
            
            print()








        # # def printRow(n):
            
        # #     print(f"{n}" * N, end = "")
        # f = 0
        # for i in range(count):
        #     for j in range(count):
        #         if i <= 0+f-1 or j <= 0+f or i == count-1+f or j == count-1+f:
        #             print(N-f, end = " ")
        #         else:
        #             print("*", end = " ")

        #     f += 1
        #     print()

        #     # print(N, end = "")
            
        #     # if i < N-1:
        #     #     printRow(N-i)
        #     # else:
        #     #     printRow(N)

        #     # print(N, end = "")
        #     # print()

if __name__ == "__main__":
    sol = Solution()
    N = int(input("Enter No.: "))
    sol.pattern(N)