# Given an array of strings, group anagrams together.
class Solution(object):
    def groupAnagrams(self, strs):
        # Prime Number Solution.
        primeTable = {
            'a': 2, 'b': 3, 'c': 5, 
            'd': 7, 'e': 11, 'f': 13, 'g': 17, 
            'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 41, 
            'm': 43, 'n': 47, 'o': 53, 'p': 59, 'q': 61, 'r': 67, 's': 71, 't': 73, 'u': 79, 
            'v': 83, 'w': 89, 'x': 97, 'y': 101, 'z': 103
        }
        anaHashTable = {}
        result = []
        
        for word in strs:
            key = 1
            for c in word:
                key *= primeTable[c.lower()]
            if key not in anaHashTable:
                anaHashTable[key] = [word]
            else:
                anaHashTable[key].append(word)
        for key in anaHashTable:
            result.append(anaHashTable[key])
        # The solution below is a bit buggy, however the idea should be correct.
#         def generateAnaHash(word):
#             hashtable = {}
#             for c in word:
#                 if c not in hashtable:
#                     hashtable[c] = 1
#                 else:
#                     hashtable[c] = hashtable[c] + 1
#             return hashtable
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
        
#         result = []
#         while(len(strs) > 0):
#             subRes = [strs[0]]
#             offset = 0
#             if(len(strs) > 1):
#                 for i in range(1, len(strs)):
#                     i -= offset
#                     offset = 0
#                     if(i == len(strs)):
#                         break
                    
#                     if generateAnaHash(strs[0]) == generateAnaHash(strs[i]):
#                         subRes.append(strs[i])
#                         del strs[i]
#                         offset = 1

#             strs.remove(strs[0])
            
#             result.append(subRes)
        return result
                
            