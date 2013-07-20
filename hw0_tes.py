# 1
L= [1,2,4,5,7,0]
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

from GF2 import one, zero
print(one+one+one+ zero)
print(one*one+ zero*one+zero*zero+one*one)
print((one+one+one)*(one+one+one+one))
