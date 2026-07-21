First Bad Version
LeetCode 278
Difficulty: Easy


Problem:

You are a product manager and want to find out which version
caused all the following versions to be bad.

Once a version is bad, all versions after it are also bad.

Given n versions [1, 2, ..., n],
find the first bad version.

We use the provided API:

isBadVersion(version)

It returns True if the version is bad.
Otherwise, it returns False.


Example:

Input: n = 5, first bad version = 4
Output: 4

Explanation:

Version 1 -> Good
Version 2 -> Good
Version 3 -> Good
Version 4 -> Bad
Version 5 -> Bad

The first bad version is 4.


Approach:

The versions have a special pattern:

Good Good Good Bad Bad Bad

Because all bad versions come after the first bad version,
we can use Binary Search.

We maintain two pointers:

left = 1
right = n

Find the middle version:

mid = left + (right - left) // 2

If isBadVersion(mid) is True:
    mid could be the first bad version.
    Search on the left side for an earlier bad version.
    Move right to mid - 1.

If isBadVersion(mid) is False:
    The first bad version must be after mid.
    Move left to mid + 1.

When the loop ends,
left points to the first bad version.

Return left.


Code:

class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n

        while left <= right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                right = mid - 1

            else:
                left = mid + 1

        return left


Time Complexity: O(log n)

Space Complexity: O(1)


Key Takeaway:

This problem teaches an important Binary Search pattern.

We are not searching for an exact value.

Instead, we are finding the first position where
a condition becomes True.

Pattern:

False False False True True True

The answer is the first True position.
