from q322_coinChange import *

sol = Solution()

def test1():
    assert sol.coinChange(coins = [1,2,5], amount = 11)  == 3


def test2():
    assert sol.coinChange(coins = [2], amount = 3)  == -1


def test3():
    assert sol.coinChange(coins = [1], amount = 0)  == 0