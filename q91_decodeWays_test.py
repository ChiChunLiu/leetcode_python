from q91_decodeWays import *

sol = Solution()

def test1():
    assert sol.numDecodings("12") == 2

def test2():
    assert sol.numDecodings("226") == 3

def test3():
    assert sol.numDecodings("0") == 0

def test4():
    assert sol.numDecodings("06") == 0

def test5():
    assert sol.numDecodings("10") == 1
 

def test7():
    assert sol.numDecodings("210") == 1

def test6():
    assert sol.numDecodings("2101") == 1
 