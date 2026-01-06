class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        my_dict = {}
        
        for ch in ransomNote:
            if ch in my_dict:
                my_dict[ch] +=1
            else:
                my_dict[ch] = 1
        
        for ch2 in magazine:
            if ch2 in my_dict:
                my_dict[ch2] -=1
        
        for i,x in my_dict.items():
            if x>0:
                return False
   
        return True