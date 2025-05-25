"""
You are given an array A of integers of length N. You need to calculate factorial of each number.
The answer can be very large, so print it modulo 10^9 + 7.

https://www.geeksforgeeks.org/problems/large-factorial4721/1
"""


class Solution:
    def factorial(self, arr, n):
        max_val = max(arr)
        fac = [1]
        mod = 10**9 + 7

        for i in range(1, max_val + 1):
            fac.append((fac[-1] * i) % mod)

        return [fac[elem] for elem in arr]

# Time Complexity: O(max(arr) * n)
# Space Complexity: O(max(arr))
