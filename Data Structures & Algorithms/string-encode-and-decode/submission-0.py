class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output+=(str(len(s))+'#'+s)
        return output

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            length = int(s[i:j])
            w = s[j+1:j+length+1]
            output.append(w)
            i = j+1+length
        return output
