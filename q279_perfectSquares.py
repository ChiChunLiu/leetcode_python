class Solution:
    def numSquares(self, n: int) -> int:
        if n in [1, 2, 3]:
            return n
        else:
            ans = [0] * (n + 1)
            ans[1] = 1
            ans[2] = 2
            ans[3] = 3
            for i in range(4, n + 1):
                ans[i] = min(ans[i - j**2] + 1 for j in range(1, int(i**0.5) + 1))
                
                #j = 1
                #while j**2 <= i:
                #    ans[i] = min(ans[i], ans[i - j**2] + 1)
                #    j += 1

            return ans[n]


