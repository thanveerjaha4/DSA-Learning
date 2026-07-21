Valid Perfect Square
LeetCode 367
Difficulty: Easy


Problem:

Given a positive integer num,
return True if num is a perfect square.

Otherwise, return False.

A perfect square is a number that can be written as
the product of an integer with itself.

For example:

16 = 4 × 4
25 = 5 × 5


Example 1:

Input: num = 16
Output: True

Explanation:
4 × 4 = 16


Example 2:

Input: num = 14
Output: False

Explanation:
There is no integer whose square is 14.


Approach:

We need to find if there is an integer x such that:

x × x = num

We can search for x using Binary Search.

The possible square root lies between:

1 and num

We maintain two pointers:

left = 1
right = num

Find the middle value:

mid = left + (right - left) // 2

Calculate:

square = mid × mid

If square == num:
    We found the perfect square.
    Return True.

If square < num:
    The square root must be larger.
    Move left to mid + 1.

If square > num:
    The square root must be smaller.
    Move right to mid - 1.

If the loop ends,
no integer square root exists.

Return False.


Code:

class Solution:
    def isPerfectSquare(self, num):
        left = 1
        right = num

        while left <= right:
            mid = left + (right - left) // 2

            square = mid * mid

            if square == num:
                return True

            elif square < num:
                left = mid + 1

            else:
                right = mid - 1

        return False


Time Complexity: O(log n)

Space Complexity: O(1)


Key Takeaway:

Binary Search can be used to search for an answer
inside a numerical range.

Here, instead of searching an array,
we search for the possible square root of num.

This is an important step toward learning:

Binary Search on Answer
