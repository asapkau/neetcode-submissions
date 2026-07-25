class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        

        for word in strs:
            key = [0]*26
            for letter in word:
                indexToUpdate = ord(letter) - ord("a")
                key[indexToUpdate] += 1
            key = tuple(key)

            if key not in hashMap:
                hashMap[key] = []
            hashMap[key].append(word)
        return list(hashMap.values())