class Solution:
    def reverse(self, x: int) -> int:
        if x > ((2 ** 31) -1) or x < (-2 ** 31):
            return 0

        else : 
            temp = str(x)
            temp1 = temp[::-1]

            if "-"in temp1:
                temp1 = temp1.replace("-","")
                temp1 = "-" + temp1

            print (int(temp1))

            if int(temp1) > ((2 ** 31) -1) or int(temp1) < (-2 ** 31):
                return 0
            
            return int(temp1)
            

        