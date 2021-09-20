def nextGreaterElements(nums1,nums2):
    stack = []
    d = {}

    for e in nums2:
        
        while(stack and e > stack[-1]):
            c = stack.pop()
            d[c] = e
        
        stack.append(e)
    result=[]
    for i in nums1:
        if d[nums1[i]]:
            result.append(nums1[i])
        else:
            result.append(-1)
    print(result)
    #return [d.get(e, -1) for e in nums1]
nums1=[4,1,2]
nums2=[1,3,4,2]
print(nextGreaterElements(nums1,nums2))