class Graph:
    def __init__(self,no_of_vertices):
        self.no_of_vertices = no_of_vertices
        self.adjaceny_list = [[] for i in range(no_of_vertices)]
        self.adjaceny_matrix = [[0] * no_of_vertices for i in range(no_of_vertices)]

    def adjaceny_list_repr(self,u,v):
        self.adjaceny_list[u].append(v)
        self.adjaceny_list[v].append(u)
        return self.adjaceny_list

    def print_adjacency_list(self):
        for vertex,neighbor in enumerate(self.adjaceny_list):
            print(f"{vertex}: {neighbor}")

    def adjaceny_matrix_repr(self,u,v):
        self.adjaceny_matrix[u][v] = 1
        self.adjaceny_matrix[v][u] = 1
        return  self.adjaceny_matrix

    def print_adjacency_matrix(self):
        for row in self.adjaceny_matrix:
            print(*(x for x in row))

def main():
    g = Graph(5)
    g.adjaceny_list_repr(0,1)
    g.adjaceny_list_repr(1,2)
    g.adjaceny_list_repr(1,3)
    g.adjaceny_list_repr(2,3)
    g.adjaceny_list_repr(2,4)
    g.print_adjacency_list()
    print("===Adjacency Matrix===")
    g.adjaceny_matrix_repr(0,1)
    g.adjaceny_matrix_repr(1,2)
    g.adjaceny_matrix_repr(1,3)
    g.adjaceny_matrix_repr(2,3)
    g.adjaceny_matrix_repr(2,4)
    g.print_adjacency_matrix()

if __name__ == "__main__":
    main()


    