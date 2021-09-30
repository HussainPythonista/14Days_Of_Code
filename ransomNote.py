a="bg"
b="efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"

def canConstruct(a,b):#This One take O(nm)
    dummy=b
    dummyLen=len(a)
    i=0
    j=0
    while i<dummyLen:
        for j in range(len(b)):
            if a[i]==b[j]:

                print(a[i],b[j])
                b=b.replace(b[j],"",1)
                i+=1
                break
        else:
                return False
    return True
        

       


print(canConstruct(a,b))
