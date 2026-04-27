class Solution:
    def isCyclic(self, V, edges):
        adj=[[] for i in range(V)]
        indeg=[0]*V
        for u,v in edges:
            adj[u].append(v)
            indeg[v]+=1
        q=[]
        for i in range(V):
            if indeg[i]==0:
                q.append(i)
        c=0
        while q:
            node=q.pop()
            c+=1
            for neig in adj[node]:
                indeg[neig]-=1
                if indeg[neig]==0:
                    q.append(neig)
        return c!=V
    
    
    
                
       