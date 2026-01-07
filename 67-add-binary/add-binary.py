class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a)-1, len(b)-1
        result = []
        carry = 0
        while i >= 0 or j >= 0 or carry:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0

            s = x+y +carry

            if s == 3:
                value = 1
                carry = 1
            elif s == 2:
                value = 0
                carry = 1
            elif s == 1:
                value = 1
                carry = 0
            elif s == 0:
                value = 0
                carry = 0

            result.append(str(value))

            i -=1
            j-=1
        
        result.reverse()
        return "".join(result)

        
        