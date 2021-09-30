def nextGreaterElements(nums1,nums2):

    #This one is Simple approach 
    #Stack is useing for track the greater Element
    #Eample:Array=[3,5,2,1,6]
    # In Stack I append 3 then I teration will Continue
    #Now nextNumber is 5 in this case 5 is Greater than 3 so I pop() and Store the value in dictionary
    #Now Num is 2 and There is no element in stack so i simply add in stack
    #Now Num is 1 so 1 is less than 2 so i simply append in a stack 
    #Now the value is 6 and 6 is Greater than 1 and 2 so i pop() both and added to the dictionary
    
    # Stack is for Sttoring the Values : 
    stack=[]
    #dictionary i'm using for to track the next Greater of Current Element
    nextGreater={}
    for i in range(len(nums2)):

        #While Loop will run if the Given Condition is True
        #It will pop() less value and Added To the Dictionary
        while  stack and stack[-1]<nums2[i] :
            #Pop and Added To the Dictionary
            nextGreater[stack.pop()]=nums2[i]
        stack.append(nums2[i])
    result=[]
    #This Loop is for to track the num1 values are present in num2
    for i in range(len(nums1)):
        #if num1 value in dictionary It will simply add into the result
        if nums1[i] in nextGreater:
            result.append(nextGreater[nums1[i]])
        else:
            #else -1
            result.append(-1)
    print(result)
nums1=[4,1,2]
nums2=[1,3,4,2]
print(nextGreaterElements(nums1,nums2))