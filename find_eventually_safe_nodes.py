


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        
        rev = [[] for _ in range(n)]
        outdeg = [0] * n
        
        
        for u in range(n):
            outdeg[u] = len(graph[u])
            for v in graph[u]:
                rev[v].append(u)
        
        
        q = deque()
        for i in range(n):
            if outdeg[i] == 0:
                q.append(i)
        
        res = []
        
       
        while q:
            node = q.popleft()
            res.append(node)
            
            for neig in rev[node]:
                outdeg[neig] -= 1
                if outdeg[neig] == 0:
                    q.append(neig)
        
        return sorted(res)