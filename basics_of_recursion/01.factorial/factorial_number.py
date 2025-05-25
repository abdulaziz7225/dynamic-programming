"""
For a given number N, find whether it is a factorial number or not. A Factorial number is a number
which is equal to the factorial value of other numbers

https://www.geeksforgeeks.org/problems/factorial-number2446/1
"""


class Solution:
    def isFactorial(self, n):
        curr = 1
        i = 1
        while curr <= n:
            curr *= i
            if curr == n:
                return 1
            i += 1
        return 0

# Time Complexity: O(log(n))
# Space Complexity: O(1)
