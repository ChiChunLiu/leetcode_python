from typing import List
import copy

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        need to go from [0,0] to [m-1, n-1]
        You can only move either down or right at any point in time.
        '''
        m = len(grid)
        n = len(grid[0])
        ans = copy.deepcopy(grid)

        for i in range(1, m):
            ans[i][0] = ans[i-1][0] + grid[i][0]
        for j in range(1, n):
            ans[0][j] = ans[0][j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                ans[i][j] = min(ans[i - 1][j], ans[i][j - 1]) + grid[i][j]

        #print(ans)
        return ans[-1][-1]


