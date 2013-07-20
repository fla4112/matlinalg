# Please fill out this stencil and submit using the provided submission script.


## Problem 1
def my_filter(L, num): return [x for x in L if x%num != 0]
## Problem 2
def myLists(L): return [ L[0:x+1] for x in range(len(L)) if (L[x]>=0)]
## Problem 3
def myFunctionComposition(f, g): return { k:g[v] for (k,v) in f.items() }

## Problem 4
# Please only enter your numerical solution.

complex_addition_a = (5+3j)
complex_addition_b = (1j)
complex_addition_c = (-1 + .001j)
complex_addition_d = (.001 + 9j)

## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0
## Problem 6
def mySum(L): 
    current= 0
    for x in range(len(L)):
        current= current + L[x]
    return current 

## Problem 7
def myProduct(L):
    current= 1
    for x in range(len(L)):
        current= current * L[x]
    return current



## Problem 8
def myMin(L):
    current= L[0]
    for x in range(1, len(L)):
        if(L[x] < current):
            current= L[x]
    return current


## Problem 9
def myConcat(L):
    current= L[0]
    for x in range(1, len(L)):
        current += L[x]
    return current

## Problem 10
def myUnion(L):
    current= L[0]
    for x in range(1, len(L)):
        current= current | L[x]
    return current
