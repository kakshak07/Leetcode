from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        names = {}
        graph = defaultdict(set)
        
        for acc in accounts:
            nam = acc[0]
            for i in acc[1:]:
                graph[i].add(acc[1])
                graph[acc[1]].add(i)
                names[i] = nam
                
        comps, seen, ans, i = defaultdict(list), set(), [], 0
        
        def traverse(node,i):
            # print(seen)
            seen.add(node)
            comps[i].append(node)
            for a in graph[node]:
                if a not in seen:
                    traverse(a,i)
        for k in graph:
            if k not in seen:
                traverse(k,i)
                i += 1
        w = []
        for i in comps:
            k = [names[comps[i][0]]]+sorted(comps[i])
            w.append(k)
        return w
        # print(comps)
            
        