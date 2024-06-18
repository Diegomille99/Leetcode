class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return(True)
        a=list(s1)
        b=list(s2)
        map={}
        for i in range(len(a)):
            if a[i] not in map:
                map[a[i]]=1
            else:
                map[a[i]]+=1    
        for j in range (len(a)):
            if b[j] not in map:
                return (False)
            map[b[j]]-=1
            if map[b[j]]<0:
                return(False)
        remainder=0
        for key in map:
            remainder+=map[key]
        if remainder!=0:
            return(False)  
        count=0  
        for i in range(len(a)):
            if a[i]!=b[i]:
                count+=1
        return(count==2)          
