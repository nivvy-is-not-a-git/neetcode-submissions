class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def findCycle(node):
            if node in visited:
                return False
            if node in visiting:
                return True
            
            visiting.add(node)
            for subject in adjacency[node]:
                if findCycle(subject)==True:
                    return True
            visited.add(node)
            visiting.remove(node)
            return False
        adjacency = {}
        for i in range(numCourses):
            adjacency[i] = []
        for subject, prereq in prerequisites:
            adjacency[prereq].append(subject)
        visited = set()
        for subject in adjacency:
            visiting = set()
            if findCycle(subject)==True:
                return False
        return True


        
     
