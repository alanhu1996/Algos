# Given a digit string, return all possible letter combinations that the number could represent.
class Solution(object):
    def letterCombinations(self, digits):
        
            
        """
        :type digits: str
        :rtype: List[str]
        """
        letterList = {"1": "*", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        useDigs = []
        for i in digits:
            useDigs.append(letterList[i])
            
        def generateCombinations(prefix, letterList, digPointer, result = []):
            if(len(prefix) == len(digits)):
                result.append(prefix)
                return result
            else:
                for i in letterList[digits[digPointer]]:
                    generateCombinations(prefix + i, letterList, digPointer + 1, result)
            return result
        
        return [] if digits == "" else generateCombinations("", letterList, 0, [])


    # One line python computation. Faster runtime than the above recursive solution.
    def letterCombinations2(self, digits):
        letterList = {"1": "*", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        useDigs = []
        for i in digits:
            useDigs.append(letterList[i])
        return [] if digits == "" else reduce(lambda acc, digs: [x + y for x in acc for y in digs], useDigs, [""])
        