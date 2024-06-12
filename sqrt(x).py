class Solution:
    def mySqrt(self,x:int):
        y=x
        e=1e-4 #tollerance 
        error=y*y-x
        
        if abs(error)<e:
            return y
        else:
            while abs(error)>e:
                y=y-(y*y-x)/(2*y) 
                error=y*y-x
        return round(y)     

