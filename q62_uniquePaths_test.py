from q62_uniquePaths import *

sol = Solution()

def test1():
    assert sol.uniquePaths(7, 3)  == 28

def test2():
    assert sol.uniquePaths(3, 3)  == 6

def test3():
    assert sol.uniquePaths(3, 2)  == 3

