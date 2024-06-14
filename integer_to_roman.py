class Solution:
    def romanToInt(self, s: str) -> int:

        h={"I":1,
   "V":5,
   "X":10,
   "L":50,
   "C":100,
   "D":500,
   "M":1000}

        s=list(s)
        kernel=0
        n=0
        num=0
        for letter in s:
            type=h[letter]
            if type==kernel:
                n+=type
            elif type>kernel:
                num-=n
                kernel=type
                n=type
            else:
                num+=n
                kernel=type
                n=type
        num+=n
        return(num)
    

solution=Solution()

result=solution.romanToInt("III")

print(result)






