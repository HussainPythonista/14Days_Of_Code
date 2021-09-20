from collections import defaultdict
def nextGreaterElements(nums1,nums2):
    
    lookups = defaultdict(list)

    for i in range(len(nums2)):
        lookups[nums2[i]]=i
    i=0
    stack=[]
    while i<len(nums1):
        index=lookups[nums1[i]]
        for nextGreater in range(index,len(nums2)):
            if nums1[i]<nums2[nextGreater]:
                stack.append(nums2[nextGreater])
                break
        else:
            stack.append(-1)
        i+=1
    return stack
nums1=[4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElements(nums1,nums2))

    
