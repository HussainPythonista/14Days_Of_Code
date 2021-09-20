nums=[-1,-2]

def maximumSubArray(nums):
    maximum=nums[0]
    tempMax=nums[0]
    for i in range(1,len(nums)):
        tempMax=max(tempMax+nums[i],nums[i])
    
        maximum=max(maximum,tempMax)
    return (max(maximum,tempMax))
print(maximumSubArray(nums))