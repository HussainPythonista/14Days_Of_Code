nums1 = [3,0,0,0]
m = 1
nums2 = [2,5,6]
n = 3

def mergeSortedArray(num1,num2,m,n):
    aPointer=m-1
    bPointer=(m+n)-1
    numsPointer=n-1
    while aPointer>=0 and numsPointer>=0:
        if num1[aPointer]<=num2[numsPointer]:
            num1[bPointer]=nums2[numsPointer]
            numsPointer-=1
        elif num1[aPointer]>num2[numsPointer]:
            num1[bPointer]=num1[aPointer]
            
            aPointer-=1
        bPointer-=1
    while numsPointer>=0:
        num1[bPointer]=num2[numsPointer]
        numsPointer-=1
        bPointer-=1
    print(num1)
mergeSortedArray(nums1,nums2,m,n)