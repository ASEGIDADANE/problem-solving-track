class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = [[] for i in range(numCourses)]

        income = [0 for i in range(numCourses)]

        queue = deque()

        order = []

        for course,pre in prerequisites:
            graph[pre].append(course)
            income[course] += 1
        

        for i in range(numCourses):
            if income[i] == 0:
                queue.append(i)


        while queue:
            q = queue.popleft()
            order.append(q)

            for nab in graph[q]:
                income[nab] -= 1

                if income[nab] == 0:
                    queue.append(nab)
        
        if len(order) == numCourses:
            return order
        else:
            return []




        