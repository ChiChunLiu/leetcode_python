from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False] * N
        for i in range(N):
            for w in wordDict:
                w_length = len(w)
                if s[(i - w_length + 1):(i + 1)] == w and dp[i - w_length] and i - w_length + 1 > 0:
                    dp[i] = True
                elif s[(i - w_length + 1):(i + 1)] == w and i - w_length + 1 == 0:
                    dp[i] = True
        print(dp)
        return dp[-1]
        