"""
Given a positive integer N. Calculate the Fibonacci series till the number N. If N is a part of the series,
include N as well

https://www.geeksforgeeks.org/problems/fibonacci-to-n0811/1
"""


class Solution:
    def nFibonacci(self, n):
        result = []
        curr, next = 0, 1
        while curr <= n:
            result.append(curr)
            curr, next = next, curr + next
        return result

# Time Complexity: O(log(n))
# Space Complexity: O(log(n))
