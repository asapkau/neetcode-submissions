class Solution:
    def encode(self, strs):
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s):
        res = []
        i = 0

        while i < len(s):
            j = i

            # Find the separator after the length
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # String starts after '#'
            start = j + 1
            end = start + length

            res.append(s[start:end])

            # Move to the next encoded string
            i = end

        return res