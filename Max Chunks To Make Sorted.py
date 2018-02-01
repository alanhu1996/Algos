# Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

# What is the most number of chunks we could have made?

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        chunkCount = 0
        maxInChunk = 0
        for i in range(len(arr)):
            maxInChunk = max(maxInChunk, arr[i])
            if i == maxInChunk:
                chunkCount += 1
        return chunkCount