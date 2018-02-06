# Given a non-empty list of words, return the k most frequent elements.

# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        countDict = collections.Counter(words)
        countList = countDict.keys()
        countList.sort(key = lambda item: (-countDict[item], item))
        
        return countList[0:k]