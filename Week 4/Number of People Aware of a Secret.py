class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        share = 0
        for day in range(2, n + 1):
            if day - delay >= 1:
                share += dp[day - delay]
            if day - forget >= 1:
                share -= dp[day - forget]
            share %= mod
            dp[day] = share
        return sum(dp[n - forget + 1: n + 1]) % mod