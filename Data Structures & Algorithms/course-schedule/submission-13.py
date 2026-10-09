class Solution:
    def traverse(self, node: int, adjacency: list[int], visiting, visited):
        
        if node not in adjacency:
            visiting.remove(node)
            return True
        for neighbour in adjacency[node]:
            if neighbour in visiting:
                return False
            elif neighbour in visited:
                continue
            else:
                visiting.add(neighbour)
                if (self.traverse(neighbour, adjacency, visiting, visited))==False:
                    return False
                else:
                    continue
        visited.add(node)
        visiting.remove(node)
        return True
            

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency = {}

        for prereq in prerequisites:
            if prereq[0] not in adjacency:
                adjacency[prereq[0]] = []
            adjacency[prereq[0]].append(prereq[1])
        visited=set()
        for vertex in adjacency:
            print("new vertex: ", vertex)
            visiting = set()
            visiting.add(vertex)
            if (self.traverse(vertex,adjacency, visiting, visited)==False):
                return False
        return True
        
     
