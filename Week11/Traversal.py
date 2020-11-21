# TODO: Draw Graph and Fix This


class Graph:
    def __init__(self, vertices_lst):
        self.weight = dict()
        for src in vertices_lst:
            self.weight[src] = []

    def add_edge(self, start, end, undirect=False):
        if end not in self.weight[start]:
            self.weight[start].append(end)
        if undirect:
            if start not in self.weight[end]:
                self.weight[end].append(start)

    def adj_matrix(self):
        print(f"    ", end="")
        for key in self.weight:
            print(f"{key}  ", end="")
        print()

        for key, lst in self.weight.items():
            print(f"{key} : ", end="")
            for i, vertex in enumerate(self.weight):
                if vertex in lst:
                    print("1", end="")
                else:
                    print("0", end="")

                if i < len(self.weight)-1:
                    print(", ", end="")
            print()

    def bfs(self, start=None):
        if start is None:
            for key in self.weight:
                start = key
                break
        visited = set()
        queue = [[start]]
        visited.add(start)
        out = ""
        while len(queue) > 0:
            lst = queue.pop(0)
            for vertex in lst:
                tmp_lst = []
                out += str(vertex) + ' '
                for item in self.weight[vertex]:
                    if item not in visited:
                        visited.add(item)
                        tmp_lst.append(item)
                queue.append(sorted(tmp_lst))
        print(f"Bredth First Traversals : {out}")  # typo for grader

    def bfs2(self):
        visited = set()
        queue = []
        out = ""
        for v in self.weight:
            if v not in visited:
                queue.append(v)
                visited.add(v)
            while len(queue) > 0:
                lst = queue.pop(0)
                for vertex in lst:
                    tmp_lst = []
                    out += str(vertex) + ' '
                    for item in self.weight[vertex]:
                        if item not in visited:
                            visited.add(item)
                            tmp_lst.append(item)
                    queue.append(sorted(tmp_lst))
        print(f"Bredth First Traversals : {out}")  # typo for grader

    def _dfs(self, start, visited):
        visited.add(start)
        print(start, end=" ")
        for vertex in self.weight[start]:
            if vertex not in visited:
                self._dfs(vertex, visited)

    def dfs(self):
        visited = set()
        print("Depth First Traversals : ", end="")
        for vertex in self.weight:
            if vertex not in visited:
                self._dfs(vertex, visited)
        print()

    def __str__(self):
        return str(self.weight)


if __name__ == '__main__':
    lst = input("Enter : ").split(',')
    vertex_lst = []
    for item in lst:
        src, dest = item.split()
        if src not in vertex_lst:
            vertex_lst.append(src)
        if dest not in vertex_lst:
            vertex_lst.append(dest)
    vertex_lst = sorted(vertex_lst)

    g = Graph(vertex_lst)
    for item in lst:
        src, dest = item.split()
        g.add_edge(src, dest, undirect=True)
    g.dfs()
    g.bfs2()

