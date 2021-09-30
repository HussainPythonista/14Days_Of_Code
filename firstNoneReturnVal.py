s="dddccdbba"
def repeatVal(s):
    repeatedVal={}
    for i in range(len(s)):
        if s[i] not in repeatedVal:
            repeatedVal[s[i]]=1
        else:
            repeatedVal[s[i]]+=1
    for j in range(len(s)):
        if repeatedVal[s[j]]==1:
            return j
    print(repeatedVal)
print(repeatVal(s))