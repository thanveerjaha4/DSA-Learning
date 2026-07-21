Binary Search
LeetCode 704
Difficulty: Easy


Problem:

Given a sorted array of integers nums and an integer target,
return the index of target if it exists in the array.
Otherwise, return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Explanation:
nums[4] = 9


Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1

Explanation:
2 does not exist in the array.


Approach:

Since the array is sorted, we use Binary Search.

We maintain two pointers:

left = 0
right = len(nums) - 1

Find the middle element:

mid = left + (right - left) // 2

If nums[mid] == target:
    Target found, return mid.

If nums[mid] < target:
    Target must be on the right side.
    Move left to mid + 1.

If nums[mid] > target:
    Target must be on the left side.
    Move right to mid - 1.

If the loop ends, target is not present.
Return -1.


Code:

class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1


Time Complexity: O(log n)

Space Complexity: O(1)


Key Takeaway:

Binary Search works on sorted arrays.

It eliminates half of the search space in every step,
making it much faster than Linear Search.
