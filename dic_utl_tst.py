dct=[1,2,3,4]
k=['a','b','c','d']
def dict2list(dct, keylist): 
    dlist=[]
    for x in range(len(keylist)):
        temp=[dct[x], keylist[x]]
        dlist.append(temp)
    return dlist
print(dict2list(dct, k))        
     

def list2dict(L, keylist): 
    dct={}
    for x in range(len(keylist)):
        dct[keylist[x]]= L[x]
    return dct  
print(list2dict(dct, k)) 
 
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
 
lst=['apple', 'banana', 'mango']
print(listrange2dict(lst))       
