class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        mAp = {}

        if len(s1) > len(s2):
            return False


        for c in s1:
            freq[c] = freq.get(c, 0) + 1

        for i in range(len(s1)):
            mAp[s2[i]] = mAp.get(s2[i], 0) + 1

        if freq == mAp:
            return True

        l = 0

        for r in range(len(s1), len(s2)):
            mAp[s2[r]] = mAp.get(s2[r], 0) + 1

            mAp[s2[l]] -= 1
            if mAp[s2[l]] == 0:
                del mAp[s2[l]]
            
            l += 1

            if freq == mAp:
                return True
        return False


     


        # for l in range((len(s2) - len(s1) + 1)):
        #     map = {}
        #     for r in range(len(s1)):
        #         map[s2[l + r]] = map.get(s2[l + r], 0) + 1
        #     if map == freq:
        #         return True
        # return False
                

        