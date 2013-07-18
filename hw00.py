k= 'Bilbo'
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
out=[[x, y[x]] if x==k else 'NOT PRESENT' for y in dlist for x in y]
print(out)

k= 'Frodo'
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
out=[[x, y[x]] if x==k else 'NOT PRESENT' for y in dlist for x in y]
print(out)


def my_filter1(L):return [x*x for x in L]

#given list = [1,2,4,5,7] and num = 2, return [1,5,7].
l= [1,2,4,5,7]
num = 2
def my_filter(L, num):return [x for x in L if x%num != 0]
print(my_filter(l, num))

'''Task 23: Using range, write a comprehension whose value is a dictionary. The keys should be the integers
from 0 to 99 and the value corresponding to a key should be the square of the key.'''
out=[[x, x**2] for x in range(100)]
print(out)

d=['red', 'white','blue']
''' out={{k:d[k]} for k in range(len(d)) } curly brackets not working why? '''
out=[{k:d[k]} for k in range(len(d)) ]
print(out)

d = {0:1000.0, 3:990, 1:1200.50}
L = ['Larry', 'Curly', '', 'Moe']
out=[{L[k]: v} for (k,v) in d.items()]
print(out)

'''
Task 27: Dene a one-line procedure nextInts(L) specied as follows:
 input: list L of integers
 output: list of integers whose ith element is one more than the ith element of L
 example: input [1; 5; 7], output [2; 6; 8].
'''
def nextInts(L): return [x+1 for x in L]
print(nextInts([0,5,9]))

'''Task 28: Dene a one-line procedure cubes(L) specied as follows:
 input: list L of numbers
 output: list of numbers whose ith element is the cube of the ith element of L
 example: input [1; 2; 3], output [1; 8; 27].'''
def cubes(L): return [x**3 for x in L]
print(cubes([0,5,9]))

'''Task 29: Dene a one-line procedure dict2list(dct,keylist) with this spec:
 input: dictionary dct, list keylist consisting of the keys of dct
 output: list L such that L[i] = dct[keylist[i]] for i = 0; 1; 2; : : : ; len(keylist)  1
 example: input dct={'a':'A', 'b':'B', 'c':'C'} and keylist=['b','c','a'], output
['B', 'C', 'A']'''
def dict2list(dct, keylist): return [dct[x] for x in keylist]
dct={'a':'A', 'b':'B', 'c':'C'}
keylist=['b','c','a']
print(dict2list(dct, keylist))

'''
Task 30: Dene a one-line procedure list2dict(L, keylist) specied as follows:
 input: list L, list keylist of immutable items
 output: dictionary that maps keylist[i] to L[i] for i = 0; 1; 2; : : : ; len(L)  1
 example: input L=['A','B','C'] and keylist=['a','b','c'], output
{'a':'A', 'b':'B', 'c':'C'}
Hint: Use a comprehension that iterates over a zip or a range.
'''
def list2dict(L, keylist): return [{keylist[k]:L[k]} for k in range(len(L)) ]
L=['A','B','C']
keylist=['a','b','c']
print(list2dict(L, keylist))
