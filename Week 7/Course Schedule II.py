from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == numCourses else []