class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Map = {}

        for letter in strs:
            signature = [0] * 26

            for char in letter:
                indexInSignature = ord(char) - 97
                signature[indexInSignature] += 1
            
            key = tuple(signature)
            if key not in Map:
                Map[key] = []
            Map[key].append(letter)
        
        return list(Map.values())
            
