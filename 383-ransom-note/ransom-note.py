class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        res = {}
        
        for s in ransomNote:
            if s in res:
                res[s] +=1
            else:
                res[s] = 1
        
        for p in magazine:
            if p in res:
                res[p]-=1

        for i,x in res.items():
            if x>0:
                return False
        
        return True

                
        