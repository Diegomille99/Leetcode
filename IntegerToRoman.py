class Solution:
    def intToRoman(self, num: int) -> str:
        book=['I', 'V', 'X', 'L', 'C', 'D', 'M']
        translate=[]
        x=num
        for i in range(0,6,2):
            d=book[i:i+3]
            x=num%10
            num=num//10
            if x==9 or x==4:
                translate.append(d[2]) if x==9 else translate.append(d[1])
                translate.append(d[0])
            elif x>=5:
                translate.append(d[0]*(x-5))
                translate.append(d[1])  
            else:
                translate.append(d[0]*(x)) 
        x=num%10
        translate.append("M"*x)
        translate.reverse()
        result = ''.join([item for item in translate if item != ''])
        return(result)
