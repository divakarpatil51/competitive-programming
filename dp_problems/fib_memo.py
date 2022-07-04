from  functools import lru_cache
class Solution:
    def fib(self, n: int) -> int:
        if n < 0:
            return 0
        if n == 0 or n == 1:
            return n
        return self.calc_fib(n)

    @lru_cache
    def calc_fib(self, curr, var="first"):
        print(curr, var)
        if curr in [1, 0]:
            return curr

        return self.calc_fib(curr - 1, "first") + self.calc_fib(curr - 2, "sec")

Solution().fib(3)