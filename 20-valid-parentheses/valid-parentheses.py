class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        if len(s) == 0:
            return True
        
        for i in s:
            if i in ["[", "(", "{"]:
                temp.append(i)
            elif i == "]" and temp and temp[-1] == "[":
                temp.pop()
            elif i == "}" and temp and temp[-1] == "{":
                temp.pop()
            elif i == ")" and temp and temp[-1] == "(":
                temp.pop()
            else:
                return False
        
        return len(temp) == 0
