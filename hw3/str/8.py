def longestLength(words):
    res=max(words,key=len)
    print("length is ", len(res))
 
a = ["one", "two", "third", "four"]
longestLength(a)