def pascalsTriangle(n):
    finalArray=[]
    for i in range(n):
        tempArray=[]
        for j in range(i+1):
            tempArray.append(1)
        finalArray.append(tempArray)
    print(finalArray)
        
n=5
pascalsTriangle(n)