# You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

# Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

# Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        dpMaxLen = [1] * len(pairs)
        
        sortedPairs = sorted(pairs, key=lambda x: x[1])
        # Longest increasing sequence solution. O(n^2) on top of the O(nlogn) sorting time.
        # for i in range(len(sortedPairs)):
        #     for j in range(i - 1, -1, -1):
        #         if sortedPairs[i][0] > sortedPairs[j][1]:
        #             dpMaxLen[i] = max(dpMaxLen[i], dpMaxLen[j] + 1)
        # return dpMaxLen[len(sortedPairs) - 1]
        
        # Greedy solution.
        currentTail = []
        totalLen = 1
        for i in range(len(sortedPairs)):
            if currentTail == []:
                currentTail = sortedPairs[i]
                continue
            if currentTail[1] < sortedPairs[i][0]:
                totalLen += 1
                currentTail = sortedPairs[i]
        return totalLen