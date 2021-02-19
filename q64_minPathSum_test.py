from q64_minPathSum import *

sol = Solution()

def test1():
    assert sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]]) == 7


def test2():
    assert sol.minPathSum([[1,2,3],[4,5,6]]) == 12