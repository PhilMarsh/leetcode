class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        start_index = 0
        current_gas = 0
        for index, (gas_amount, cost_amount) in enumerate(zip(gas, cost)):
            current_gas += gas_amount - cost_amount
            if current_gas < 0:
                start_index = index + 1
                current_gas = 0
        return start_index

