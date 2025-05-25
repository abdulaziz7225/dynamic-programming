# Solution 1: Recursive approach
class Solution:
    def factorial(self, n):
        if n == 0:
            return 1
        return n * self.factorial(n - 1)

# Time Complexity: O(n)
# Space Complexity: O(n)


# Solution 2: Iterative approach
class Solution:
    def factorial(self, n):
        fac = 1
        for i in range(1, n + 1):
            fac *= i
        return fac

# Time Complexity: O(n)
# Space Complexity: O(1)
