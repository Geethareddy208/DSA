def findcontentchildren(g,s):
    g.sort()
    s.sort()
    child=0
    cookies=0
    while child<len(g) and cookies<len(s):
        if s[cookies]>=g[child]:
            child+=1
        cookies+=1
    return child
g=[1,2,3]
s=[1,1]
print(findcontentchildren(g,s))