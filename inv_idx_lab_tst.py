from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0, len(review_options)-1)]
print(movie_review("Alien"))

## Task 4    
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    inv_idx=dict()
    for i, j in enumerate(strlist):
        inv_idx[i]= j
    return inv_idx

def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    results=[]
    for q in query:        
        for key, value in inverseIndex.items():                   
            if q in value:
                if key not in results:
                    results.append(key)
    return results

def andSearch(inverseIndex, query):
    results=[]
    for key, value in inverseIndex.items():  
        for i in range(len(query)):
            if query[i] not in value:
                # print(key,":NO")
                break
            if i==len(query)-1:
                print(value)
                results.append(key)
    return results

        
# lst1=["See it!", "A gem!", "Ideological claptrap!"]
# print([ {i:j} for i,j in enumerate(lst1)])
# print(makeInverseIndex(lst1))

def diction(infile):
    f=open(infile)
    lst=[]
    for line in f:
        # linelst= line.split()
        # for l in linelst:
        lst.append(line)
    return makeInverseIndex(lst)
        
mydict= diction('stories_small.txt')
print(type(mydict))
# print(mydict.keys())
# print(mydict.items())
#result= orSearch(mydict,["busy", "World"])
#print(len(result), ": ", sorted(result))
#result= orSearch(mydict,["World"])
#print(len(result), ": ", sorted(result))
result= andSearch(mydict,["Bosnian", "war-crimes", tribunal])
print(sorted(result))
