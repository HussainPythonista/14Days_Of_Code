a=[61,24,20,58,95,53,17,32,45,85,70,20,83,62,35,89,5,95,12,86,58,77,30,64,46,13,5,92,67,40,20,38,31,18,89,85,7,30,67,34,62,35,47,98,3,41,53,26,66,40,54,44,57,46,70,60,4,63,82,42,65,59,17,98,29,72,1,96,82,66,98,6,92,31,43,81,88,60,10,55,66,82,0,79,11,81]
b=[5,25,4,39,57,49,93,79,7,8,49,89,2,7,73,88,45,15,34,92,84,38,85,34,16,6,99,0,2,36,68,52,73,50,77,44,61,48]
#a=[1,2,2,1]
#b=[2,2]

def count(nums):
    frequency={}
    for i in range(len(nums)):
        if nums[i] in frequency:
            frequency[nums[i]]+=1
        else:
            frequency[nums[i]]=1
    return frequency

def intersectionOfArray(a,b):
    frequency1=count(a)
    frequency2=count(b)
    workingWith=[]
    for key,values in frequency1.items():
        if key in frequency2:

            workingWith.append([key,(min(frequency2[key],values))])
    print(workingWith)
    finalAnswer=[]
    for multiply in range(len(workingWith)):

        strVal=str(workingWith[multiply][0])
        
        multiply=workingWith[multiply][1]
        val=[]
        for i in range(multiply):
            val.append(int(strVal)) 
        finalAnswer+=val
    return(finalAnswer)
    

intersectionOfArray(a,b)

a={0:"a",1:"b"}
for i in a:
    print(i)
d={0,1,2}
for i in d:
    print(d.add(i))