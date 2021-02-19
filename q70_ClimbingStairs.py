class Solution:
    def climbStairs(self, n: int) -> int:
        
        tot = [1, 2]
        if n == 1:
            return tot[0]
        elif n == 2:
            return tot[1]
        else:
            for i in range(3, n+1):
                sum = tot[0] + tot[1]
                tot = [tot[1], sum]
            return sum


sol = Solution()

def test_edge_1():
    assert sol.climbStairs(1) == 1

def test_edge_2():
    assert sol.climbStairs(2) == 2

def test_3():
    assert sol.climbStairs(3) == 3
