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
        g.add_edge(src, dest)
    g.adj_matrix()