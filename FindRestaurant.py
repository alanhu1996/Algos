# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

# You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.



class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        hashDict = {}
        
        for i in xrange(len(list1)):
            hashDict[list1[i]] = i
        
        minNum = -1
        result = []
        
        upperLoopBound = len(list2)
        for i in xrange(upperLoopBound):
            if list2[i] in hashDict:
                sumNum = hashDict[list2[i]] + i
                if sumNum < minNum or minNum == -1:
                    result = [list2[i]]
                    minNum = sumNum
                    upperLoopBound = minNum + 1
                elif sumNum == minNum:
                    result.append(list2[i])

            
        return result