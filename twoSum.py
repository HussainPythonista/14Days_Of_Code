nums = [3,3,11,15]
target = 6

def twoSum(nums):
    lookups={}
    for i in range(len(nums)):
        compliment=target-nums[i]
        if nums[i] in lookups:
            return [lookups[nums[i]],i]
        else:
            lookups[compliment]=i

print(twoSum(nums))