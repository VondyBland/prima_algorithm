class PrimsMST:
    def find_min_spanning_tree(self, graph):
        num_points = len(graph)
        mst = set()
        selected = [False] * num_points
        selected[0] = True 

        while len(mst) < num_points - 1:
            min_weight = float('inf')
            u, v = -1, -1

            for i in range(num_points):
                if selected[i]:
                    for j in range(num_points):
                        if not selected[j] and graph[i][j] < min_weight:
                            min_weight = graph[i][j]
                            u, v = i, j

            if u != -1 and v != -1:
                mst.add((u, v, graph[u][v]))
                selected[v] = True

        return mst

