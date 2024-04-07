class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        answer = []
        visited, cycle = set(), set()
        dependencies = {node : [] for node in range(numCourses)}
        for course, pre in prerequisites:
            dependencies[course].append(pre)
        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            cycle.add(node)
            for dep in dependencies[node]:
                if dfs(dep) == False:
                    return False
            cycle.remove(node)
            visited.add(node)
            answer.append(node)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return answer