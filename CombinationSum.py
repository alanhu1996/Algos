# Given a set of candidate numbers (C) (without duplicates) and a target number (T), 
# find all unique combinations in C where the candidate numbers sums to T.
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candidates.sort()
        def combinationSumHelper(candidates, target, path, index, result = []):
            for n in range(index, len(candidates)):
                if(target == candidates[n]):
                    result.append(path + [candidates[n]])
                    break
                if(target < candidates[n]):
                    break
                combinationSumHelper(candidates, target - candidates[n], path + [candidates[n]], n, result)
            return result
        return combinationSumHelper(candidates, target, [], 0)
                