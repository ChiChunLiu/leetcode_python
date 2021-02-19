from q279_perfectSquares import *

sol = Solution()


def test_edge():
    assert sol.numSquares(1) == 1
    assert sol.numSquares(2) == 2
    assert sol.numSquares(3) == 3

def test1():
    assert sol.numSquares(12) == 3

def test2():
    assert sol.numSquares(13) == 2

sol.numSquares(12)