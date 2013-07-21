## Task 2
def dict2list(dct, keylist): 
    dlist=[]
    for x in range(len(keylist)):
        temp=[dct[x], keylist[x]]
        dlist.append(temp)
    return dlist

def list2dict(L, keylist): 
    dct={}
    for x in range(len(keylist)):
        dct[keylist[x]]= L[x]
    return dct  
 
## Task 3
def listrange2dict(L):
    """
    Input: a list
    Output: a dictionary that, for i = 0, 1, 2, . . . , len(L), maps i to L[i]

    You can use list2dict or write this from scratch
    """
    mydict={}
    for x in range(len(L)):
        mydict[x]= L[x]       
    return mydict
