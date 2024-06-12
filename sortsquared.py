nums=[k for k in range(-49,67)]

solution=[0]*len(nums)

left=0
right=len(nums)-1

i=0
while left<right:
    if abs(nums[right])>=abs(nums[left]):
        solution[len(nums)-1-i]=nums[right]**2
        right-=1
    else:
        solution[len(nums)-1-i]=nums[left]**2
        left+=1
    i+=1
    print(solution)
print(solution)            