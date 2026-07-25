class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for i in strs:
            fingerPrint = [0] * 26

            for char in i:
                index = ord(char) - ord('a')
                fingerPrint[index] += 1
            key = tuple(fingerPrint)
            if key in hashMap:
                hashMap[key].append(i)
            else:
                hashMap[key] = [i]
        
        return list(hashMap.values())

                