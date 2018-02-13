# Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

# However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

# You need to return the least number of intervals the CPU will take to finish all the given tasks.



class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # Find max tasks.
        countTable = collections.Counter(tasks)

        sortedValues = [(key, countTable[key]) for key in sorted(countTable, key = countTable.get, reverse=True)]
        
        maxOccurence = sortedValues[0][1] - 1
        totalSize = (maxOccurence) * (n + 1)
        
        totalIdleSlots = totalSize
        for i in range(len(sortedValues)):
            totalIdleSlots -= min(maxOccurence, sortedValues[i][1])
        
        return totalIdleSlots + len(tasks) if totalIdleSlots > 0 else len(tasks)