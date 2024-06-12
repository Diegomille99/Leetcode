class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x<0 or (x!=0 and x%10==0):
            return False
        
        left=x
        right=0 

        while left>right:
            right*=10
            right+=left % 10
            left//=10
        return left==right or left==right//10   

