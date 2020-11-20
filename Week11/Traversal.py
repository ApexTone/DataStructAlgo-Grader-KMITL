# TODO: Draw Graph and Fix This


class Graph:
    def __init__(self, vertices_lst):
        self.weight = dict()
        for src in vertices_lst:
            self.weight[src] = []

    def add_edge(self, start, end, weight=1, bidir=False):
        if end not in self.weight[start]:
            self.weight[start].append(end)
        if bidir:
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

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)
        out = ""
        while len(queue) > 0:
            vertex = queue.pop(0)
            out += str(vertex) + ' '
            for item in self.weight[vertex]:
                if item not in visited:
                    queue.append(item)
                    visited.add(item)
            queue = sorted(queue, key=lambda x: ord(x))
        print(f"Breadth First Traversals : {out}")


    def dfs(self, start):
        visited = set()
        stack = [start]
        visited.add(start)
        out = ""
        while len(stack) > 0:
            vertex = stack.pop()
            out += str(vertex) + ' '
            for item in self.weight[vertex]:
                if item not in visited:
                    stack.append(item)
                    visited.add(item)
            stack = sorted(stack, key=lambda x: ord(x))
        print(f"Depth First Traversals : {out}")

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
        g.add_edge(src, dest, True)
    g.adj_matrix()
    g.dfs(vertex_lst[0])
    g.bfs(vertex_lst[0])

