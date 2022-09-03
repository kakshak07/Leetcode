class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        dict1 = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                dist = abs(bombs[i][0] - bombs[j][0])**2 + abs(bombs[i][1] - bombs[j][1])**2
                if dist <= bombs[i][2]**2:
                    dict1[i].append(j)
        print(dict1)
        def dfs(node):
            visited.add(node)

            for child in dict1[node]:
                if child not in visited:
                    dfs(child)

        max_val = 0

        for i in range(len(bombs)):
            visited = set()
            dfs(i)
            max_val = max(max_val, len(visited))

        return max_val
#         dict1 = defaultdict(list)
#         for a,b,c in bombs:
#             for d,e,f in bombs:
#                 distance = (a-d)**2 + (b-e)**2
#                 if distance<=c**2:
#                     dict1[(a,b,c)].append((d,e,f))
#         print(dict1)
                    
#         def dfs(i, list_set):
#             print(list_set,i)
#             list_set.add(i)
#             for cords in dict1[i]:
#                 if cords not in list_set:
#                     dfs(cords, list_set)
#         max_bomb = 1
#         for i in bombs:
#             print(i)
#             list_set = set()
#             dfs((i[0], i[1], i[2]), list_set)
#             max_bomb = max(max_bomb, len(list_set))
#         return max_bomb
            
