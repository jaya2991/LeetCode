/*Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

*/
void swap(int *a, int *b){
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}
void sortColors(int* nums, int numsSize) {
    int start = 0;
    int mid = 0;
    int end = numsSize - 1;
    while(mid <= end){
        switch(nums[mid]){
        case 0: swap(&nums[start], &nums[mid]);
                start++;
                mid++;
                break;
        case 1: mid++;
                break;
        case 2: swap(&nums[mid], &nums[end]);
                end--;
                break;
        }
        
    }
}
