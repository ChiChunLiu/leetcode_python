from q300_longestIncreasingSubsequence import *

sol = Solution()

def test1():
    assert sol.lengthOfLIS([0,1,0,3,2,3])  == 4

def test2():
    assert sol.lengthOfLIS([10,9,2,5,3,7,101,18])  == 4

def test3():
    assert sol.lengthOfLIS([7,7,7,7,7,7,7])  == 1

def test4():
    assert sol.lengthOfLIS([1,3,6,7,9,4,10,5,6])  == 6
