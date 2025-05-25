"""
Given a number n, return an array containing the first n Fibonacci numbers.

https://www.geeksforgeeks.org/problems/print-first-n-fibonacci-numbers1002/1
"""


class Solution:
    def fibonacciNumbers(self, n):
        result = []
        curr, next = 0, 1
        for _ in range(n):
            result.append(curr)
            curr, next = next, curr + next
        return result

# Time Complexity: O(n)
# Space Complexity: O(n)
