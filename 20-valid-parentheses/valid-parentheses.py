class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1:
            return False
        temp = []
        for i in (s):
            if i in ["(","[", "{"]:
                temp.append(i)
            # elif i in [")", "]", "}"] and temp[-1] in ["(","[", "{"]:
            #     temp.pop()
            else:
                if not temp:          # <- important guard
                    return False
                elif (i == ")" and  temp[-1] == "("):
                    temp.pop()
                elif (i == "]" and  temp[-1] == "["):
                    temp.pop()
                elif (i == "}" and  temp[-1] == "{"):
                    temp.pop()
                else:
                    return False



        if len(temp) == 0:
            return True
        else:
            return False        