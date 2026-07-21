Search Insert Position
LeetCode 35
Difficulty: Easy


Problem:

Given a sorted array of distinct integers and a target value,
return the index if the target is found.

If the target is not found, return the index where it would be
inserted in order.


Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Explanation:
Target 5 is present at index 2.


Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Explanation:
2 is not present.
It should be inserted at index 1.


Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

Explanation:
7 is greater than all elements.
So, it should be inserted at index 4.


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
    Target may be on the left side.
    Move right to mid - 1.

If the loop ends, the target was not found.

At this point, left represents the correct insertion position.
Return left.


Code:

class Solution:
    def searchInsert(self, nums, target):
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

        return left


Time Complexity: O(log n)

Space Complexity: O(1)


Key Takeaway:

Binary Search can be used not only to find a target,
but also to find the correct position where the target
should be inserted.

When the loop ends:

left = correct insertion position.
