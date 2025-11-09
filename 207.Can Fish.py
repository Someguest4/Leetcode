from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prequisites_map = defaultdict(list)
        for p in prerequisites:
            prequisites_map[p[0]].append(p[1])
        print(prequisites_map)

        visited = set()

        def search_chain(course, visiting):
            if course in visiting:
                return False

            if course in visited:
                return True

            visiting.add(course)

            dependecies = prequisites_map[course]
            for dependecy in dependecies:
                if not search_chain(dependecy, visiting):
                    return False

            visited.add(course)
            visiting.remove(course)
            return True

        for pair in prerequisites:
            course = pair[0]
            visiting = set()
            if not search_chain(course, visiting):
                return False

        return True


print(Solution().canFinish(5, [[1,4],[2,4],[3,1],[3,2]])) # True
print(Solution().canFinish(2, [[1,0],[0,1]])) # False
print(Solution().canFinish(3, [[0,1],[0,2],[1,2]])) # True


