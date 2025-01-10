class Solution:
    def mergeStringsAlternately(self, word1: structuredClone, word2: str) -> str:
        i,j = 0, 0

        res = []
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[2])
            i += 1
            j += 1
        res.append(word1[i:])
        res.append(word2[j:])

        return "".join(res)