# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

# Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dpIMinusOne = cost[1]
        dpIMinusTwo = cost[0]
        dpCurrent = 0
        for i in range(2, len(cost) + 1):
            costPrice = cost[i] if i < len(cost) else 0
            dpCurrent = min(dpIMinusOne + costPrice, dpIMinusTwo + costPrice)
            dpIMinusTwo = dpIMinusOne
            dpIMinusOne = dpCurrent
        return dpCurrent