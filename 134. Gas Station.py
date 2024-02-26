from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        gas_sum = 0
        result = 0

        for i in range(len(gas)):
            gas_sum += gas[i] - cost[i]
            if gas_sum < 0:
                gas_sum = 0
                result = i + 1
        return result


solution = Solution()
assert solution.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]) == 3
assert solution.canCompleteCircuit([2,3,4], [3,4,3]) == -1
assert solution.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1]) == 4

