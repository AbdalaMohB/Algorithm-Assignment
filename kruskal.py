class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # To add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # A utility function to find set of an element i
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):

        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x

        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[y] = x
            rank[x] += 1

    # make an MST using Kruskal's algorithm
    def KruskalMST(self):
        result = []
        i = 0
        e = 0
        # Sort all the edges
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])

        parent = []
        rank = []

        # create V subsets
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:

            # Pick the smallest edge and increment the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimumCost = 0
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("MST ", minimumCost)

g = Graph(5)
g.addEdge(0, 1, 11)
g.addEdge(0, 2, 66)
g.addEdge(0, 3, 7)
g.addEdge(1, 3, 0)
g.addEdge(2, 3, 1)
g.KruskalMST()
