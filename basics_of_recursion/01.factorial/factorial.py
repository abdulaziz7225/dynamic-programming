"""
Given a positive integer, n. Find the factorial of n.

https://www.geeksforgeeks.org/problems/factorial5739/1
"""


class Solution:
    def factorial(self, n):
        fac = 1
        for i in range(1, n + 1):
            fac *= i
        return fac

# Time Complexity: O(n)
# Space Complexity: O(1)
