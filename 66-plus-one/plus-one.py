class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        answer = []
        single_string = "".join(str(n) for n in digits)
        single_integer = int(single_string)
        single_integer +=1
        digitlist = [int(d)for d in str(single_integer)]
        return digitlist


   