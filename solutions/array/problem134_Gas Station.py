class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sumGas = sumCost = tank = start = 0
        for i in range(len(gas)):
            sumGas += gas[i]
            sumCost += cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1

        if sumGas < sumCost:
            return -1
        else:
            return start