#include<stdio.h>

int pass_and_swap(int arr[], int sorted_index, int size);

int main()
{
    int nums[100];
    int size;
    printf("Enter size: ");
    scanf("%d", &size);
    for(int i = 0; i < size; i++)
    {
        scanf("%d", &nums[i]);
    }

    for(int i = 0; i < size; i++)
    {
        int swaps = pass_and_swap(nums, i, size);
    }
    for(int i = 0; i < size; i++)
    {
        printf("%d ", nums[i]);
    }
}

int pass_and_swap(int arr[],int sorted_index, int size)
{
    int swaps = 0;
    for(int i = 0; i < size - sorted_index - 1; i++)
    {
        if (arr[i] > arr[i+1])
        {
            arr[i] = arr[i] + arr[i+1]; //swaps arr[i] and arr[i+1]
            arr[i+1] = arr[i] - arr[i+1];
            arr[i] = arr[i] - arr[i+1];
            swaps++;
        }
    }
    return swaps;
}
