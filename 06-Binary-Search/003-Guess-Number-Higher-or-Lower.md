Guess Number Higher or Lower
LeetCode 374
Difficulty: Easy


Problem:

We are playing a guessing game.

There is a number picked from 1 to n.

You need to guess the picked number.

If your guess is higher than the picked number,
the API returns -1.

If your guess is lower than the picked number,
the API returns 1.

If your guess is equal to the picked number,
the API returns 0.

Return the picked number.


Example 1:

Input: n = 10, pick = 6
Output: 6

Explanation:

guess(5) returns 1 because 5 is lower than 6.
guess(7) returns -1 because 7 is higher than 6.
guess(6) returns 0 because 6 is the picked number.


Approach:

The possible answer lies between 1 and n.

So, we use Binary Search.

We maintain two pointers:

left = 1
right = n

Find the middle number:

mid = left + (right - left) // 2

Call the guess API:

guess(mid)

If guess(mid) == 0:
    We found the picked number.
    Return mid.

If guess(mid) == 1:
    Our guess is lower than the picked number.
    Search on the right side.
    Move left to mid + 1.

If guess(mid) == -1:
    Our guess is higher than the picked number.
    Search on the left side.
    Move right to mid - 1.


Code:

class Solution:
    def guessNumber(self, n):
        left = 1
        right = n

        while left <= right:
            mid = left + (right - left) // 2

            result = guess(mid)

            if result == 0:
                return mid

            elif result == 1:
                left = mid + 1

            else:
                right = mid - 1


Time Complexity: O(log n)

Space Complexity: O(1)


Key Takeaway:

Binary Search does not always need to be applied directly
to an array.

Here, we apply Binary Search to a range of possible answers.

The search space is:

1 to n
