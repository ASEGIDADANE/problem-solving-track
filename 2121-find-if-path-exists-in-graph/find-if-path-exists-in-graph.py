class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        visited = set()

        def dfs(vertex, visited):
            if vertex == destination:
                return True

            visited.add(vertex)

            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    
                    found = dfs(neighbour,visited)
                    if found:
                        return True

            return False
        return dfs(source,visited)

                 

        

        
        