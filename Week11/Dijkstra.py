class Graph:
    def __init__(self, vertices_lst):
        self.weight = dict()
        for src in vertices_lst:
            self.weight[src] = []

    def add_edge(self, start, end, weight=0, undirect=False):
        if [end, weight] not in self.weight[start]:
            self.weight[start].append([end, weight])
        if undirect:
            if [start, weight] not in self.weight[end]:
                self.weight[end].append([start, weight])

    def _min_distance(self, dist, visited):
        minimum = 9999999999999
        tmp = list(self.weight.keys())
        min_index = tmp[0]
        for vertex in self.weight:
            if dist[vertex][0] < minimum and vertex not in visited:
                minimum = dist[vertex][0]
                min_index = vertex
        return min_index

    def dijkstra(self, start):
        visited = set()
        dist = dict()
        for vertex in self.weight:
            dist[vertex] = [999999999999999999, start]
        dist[start] = [0, start]
        for key in self.weight:
            u = self._min_distance(dist, visited)
            visited.add(u)
            for pair in self.weight[u]:  # every vertex that connected to u
                v = pair[0]
                w = pair[1]
                if v not in visited and dist[v][0] > dist[u][0]+w:
                    dist[v][0] = dist[u][0]+w
                    dist[v][1] = u

        return dist

    def dijkstra_AB(self, src, dest):
        dist = self.dijkstra(src)
        if dist[dest][0] == 999999999999999999:
            print(f"Not have path : {src} to {dest}")
            return
        curr = dist[dest][1]
        out = f"{src} to {dest} : {src}"

        stack = []
        while curr != src:
            stack.append(curr)
            curr = dist[curr][1]
        while len(stack) > 0:
            out += "->"+stack.pop()
        out += "->"+dest
        print(out)

    def __str__(self):
        return str(self.weight)


if __name__ == '__main__':
    inp = input("Enter : ").split('/')
    starting = inp[0].split(',')
    query = inp[1].split(',')
    distinct_vertex = set()
    for lst in starting:
        src, _, dest = lst.split()
        distinct_vertex.add(src)
        distinct_vertex.add(dest)
    for lst in query:
        src, dest = lst.split()
        distinct_vertex.add(src)
        distinct_vertex.add(dest)
    vertex_lst = list(distinct_vertex)
    vertex_lst = sorted(vertex_lst)

    g = Graph(vertex_lst)
    for lst in starting:
        src, weight, dest = lst.split()
        weight = int(weight)
        g.add_edge(src, dest, weight)

    query = inp[1].split(',')
    for line in query:
        pair = line.split()
        src, dest = pair[0], pair[1]
        g.dijkstra_AB(src, dest)
