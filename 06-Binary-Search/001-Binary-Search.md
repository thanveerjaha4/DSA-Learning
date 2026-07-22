# Binary Search
# LeetCode 704
# Difficulty: Easy


# Problem:
# Given a sorted array of integers nums and an integer target,
# return the index of target if it exists in the array.
#
# If target does not exist in the array, return -1.
#
# The solution should have O(log n) runtime complexity.


# Example 1:
# Input:
# nums = [-1,0,3,5,9,12]
# target = 9
#
# Output:
# 4
#
# Explanation:
# The target 9 exists at index 4.


# Example 2:
# Input:
# nums = [-1,0,3,5,9,12]
# target = 2
#
# Output:
# -1
#
# Explanation:
# The target 2 does not exist in the array.


# Approach 1: Brute Force (Linear Search)
#
# Check every element one by one.
# If the current element is equal to target,
# return its index.
#
# If the target is not found, return -1.


class Solution:
    def search_brute_force(self, nums, target):

        for i in range(len(nums)):

            if nums[i] == target:
                return i

        return -1


# Time Complexity:
# O(n)
#
# In the worst case, we check every element.
#
# Space Complexity:
# O(1)


# Approach 2: Optimized (Binary Search)
#
# Since the array is sorted, we can use Binary Search.
#
# Binary Search checks the middle element and eliminates
# half of the search space in every step.
#
# If nums[mid] == target:
#     Target is found.
#
# If nums[mid] < target:
#     Search the right half.
#
# If nums[mid] > target:
#     Search the left half.


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


# Time Complexity:
# O(log n)
#
# Binary Search eliminates half of the search space
# after every comparison.
#
# Space Complexity:
# O(1)
#
# Only left, right, and mid variables are used.


# Dry Run:
#
# nums = [-1,0,3,5,9,12]
# target = 9
#
# Step 1:
# left = 0
# right = 5
# mid = 2
# nums[mid] = 3
#
# 3 < 9
# Search right half.
#
# left = 3
#
# Step 2:
# left = 3
# right = 5
# mid = 4
# nums[mid] = 9
#
# 9 == 9
#
# Return 4.


# Key Takeaway:
#
# Binary Search is an efficient searching algorithm used
# on sorted arrays.
#
# Linear Search -> O(n)
# Binary Search -> O(log n)
#
# Instead of checking every element, Binary Search eliminates
# half of the search space in every step.
