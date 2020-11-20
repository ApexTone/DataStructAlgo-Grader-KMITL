class Graph:
    def __init__(self, vertices_lst):
        self.weight = dict()
        for src in vertices_lst:
            self.weight[src] = dict()
            for dest in vertices_lst:
                self.weight[src][dest] = 0

    def add_edge(self, start, end, weight=1, bidir=False):
        self.weight[start][end] = weight
        if bidir:
            self.weight[end][start] = weight

    def adj_matrix(self):
        print(f"    ", end="")
        for key, _ in self.weight.items():
            print(f"{key}  ", end="")
        print()
        for key, dictionary in self.weight.items():
            print(f"{key} : ", end="")

            for i, key in enumerate(dictionary):
                print(f"{dictionary[key]}", end="")
                if i < len(dictionary)-1:
                    print(", ", end="")
            print()


if __name__ == '__main__':
    pass