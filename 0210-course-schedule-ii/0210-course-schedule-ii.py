class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        matrixList = defaultdict(list)
        
        for a,b in prerequisites:
            matrixList[a].append(b)
        for i in range(numCourses):
            if i not in matrixList:
                matrixList[i] = []
        visitedSet = set()
        cycleSet = set()
        output = []
        
        def traverse(courseNumber):
            if courseNumber in cycleSet:
                return False
            if courseNumber in visitedSet:
                return True
            cycleSet.add(courseNumber)
            for cor in matrixList[courseNumber]:
                if not traverse(cor):
                    return False
            cycleSet.remove(courseNumber)
            visitedSet.add(courseNumber)
            output.append(courseNumber)
            return True
        for i in range(numCourses):
            if not traverse(i):
                return []
        return output
        
        
        
        