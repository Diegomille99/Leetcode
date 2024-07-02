class Solution:
    def reverse(self, x: int) -> int:

        reverse=0
        bound=2**31-1
        negative=x<0
        if negative:
            x=-x
            bound+=1
        while  x!=0:

            if reverse >bound/10:
                return 0

            digit=x%10
            reverse=reverse*10+digit
            x-=digit
            x=x//10    

        if negative:
            return 0-reverse
        return reverse
                
