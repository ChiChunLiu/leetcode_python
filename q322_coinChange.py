from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        m[a] represents the minimal amount of coints needed for amount a.
        '''
        m = [0] + [float('inf')] * amount
        for a in range(1, amount + 1):
            m[a] = min([m[a - c] + 1 if a - c >= 0 else float('inf') for c in coins])

        print(m)
        if m[-1] == float('inf'):
            return -1
        else:
            return m[-1]