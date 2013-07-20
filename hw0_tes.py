from GF2 import one, zero
print(one*one+zero)

# 1
L= [1,2,4,5,7]
num= 2
def my_filter(L, num): return [x for x in L if x%num != 0]
print(my_filter(L, num))

def myLists(L): return [ L[0:x+1] for x in range(len(L)) if (L[x]>=0)]
print(myLists(L))

print([ L[0:x+1] for x in range(len(L)) if (L[x]>=0)])

'''
Problem 3: my function composition(f,g) input: two functions f and g, 
represented as dictionaries, such that g o f exists. 
output: dictionary that represents a function g o f . 
example: given f = {0:'a', 1:'b'} and g = {'a':'apple', 'b':'banana'}, 
return {0:'apple', 1:'banana'}
'''
f = {0:'a', 1:'b'}
g = {'a':'apple', 'b':'banana'}

print({ k:g[v] for (k,v) in f.items() })

print(one+one+one+ zero)
print(one*one+ zero*one+zero*zero+one*one)
print((one+one+one)*(one+one+one+one))

def mySum(L): 
    current= 0
    for x in range(len(L)):
        current= current + L[x]
    return current   
print(mySum(L ))

def myProduct(L):
    current= 1
    for x in range(len(L)):
        current= current * L[x]
    return current
print(myProduct(L))

def myMin(L):
    current= L[0]
    for x in range(1, len(L)):
        if(L[x] < current):
            current= L[x]
    return current
print (myMin(L))

words=['hello', 'world', 'hi']
def myConcat(L):
    current= L[0]
    for x in range(1, len(L)):
        current += L[x]
    return current
print(myConcat(words))

def myUnion(L):
    current= L[0]
    for x in range(1, len(L)):
        current= current | L[x]
    return current
st = [ set([0, 1]), set([1, 2]) , set([2, 3]), set([10, 'f']) ]
print(myUnion(st))
