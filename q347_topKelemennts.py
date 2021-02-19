from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for t in range(1, target + 1):
            current_sum = 0
            for n in nums:
                if t - n >= 0:
                    current_sum += dp[t - n]
            dp[t] = current_sum
        return dp[-1]