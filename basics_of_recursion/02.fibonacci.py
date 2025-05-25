# Solution 1: Recursive approach
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)

# Time Complexity: O(2 ^ n)
# Space Complexity: O(n)


# Solution 2: Iterative approach with storing
class Solution:
    def fib(self, n: int) -> int:
        fib_seq = [0, 1]
        for i in range(2, n + 1):
            fib_seq.append(fib_seq[-2] + fib_seq[-1])
        return fib_seq[n]

# Time Complexity: O(n)
# Space Complexity: O(n)


# Solution 3: Iterative approach without storing
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        prev, curr = 0, 1
        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr
        return curr

# Time Complexity: O(n)
# Space Complexity: O(1)
