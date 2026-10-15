class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        

        for word in strs:
            signature = [0] * 26
            for letter in word:
                index = ord(letter) - 97
                signature[index] += 1
            key = tuple(signature)    
            if key in hashMap:
                hashMap[key].append(word)
            else:
                hashMap[key] = [word]

        return list(hashMap.values())