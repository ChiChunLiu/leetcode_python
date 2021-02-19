from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        table = {}
        for i, n in enumerate(nums):
            complement_num = target - n
            if complement_num not in table:
                table[complement_num] = i
            else:
                return [table[complement_num], i]

        return None, None