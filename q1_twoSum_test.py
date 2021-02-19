from q1_twoSum import *

sol = Solution()

def test1():
    assert sol.twoSum([2,7,11,15], 9)  == [0,1]


def test2():
    assert sol.twoSum([3,2,4], 6) == [1,6]


def test2():
    assert sol.twoSum([3,3], 6) == [0,1]