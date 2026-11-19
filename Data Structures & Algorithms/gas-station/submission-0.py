class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        netl = []
        for g, c in zip(gas, cost):
            net = g - c
            netl.append(net)

        if sum(netl) < 0:
            return -1
        start = 0
        tank = 0

        for i in range(len(netl)):
            tank += netl[i]

            if tank < 0:
                start = i + 1
                tank = 0

        return start


        

