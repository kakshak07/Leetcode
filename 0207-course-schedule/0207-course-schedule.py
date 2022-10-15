from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        matrixList = defaultdict(list)
        
        for a,b in prerequisites:
            matrixList[a].append(b)
        for i in range(numCourses):
            if i not in matrixList:
                matrixList[i] = []
        visitedList = set()
        def traverse(matrixList, startPoint):
            if startPoint in visitedList:
                return False
            if len(matrixList[startPoint]) == 0:
                return True
            visitedList.add(startPoint)
            for i in matrixList[startPoint]:
                if not traverse(matrixList, i):
                    return False
                
            visitedList.remove(startPoint)
            matrixList[startPoint] = []
            return True
        for courses in range(numCourses):
            if not traverse(matrixList, courses):
                return False
        return True
            