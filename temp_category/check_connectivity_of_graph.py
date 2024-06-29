def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]


def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1


def initialize_union_find(n):
    parent = [i for i in range(n)]
    rank = [0] * n
    return parent, rank


def union_find_example():
    n = 5
    parent, rank = initialize_union_find(n)

    print("parent", parent)
    print("rank", rank)

    edges = [(0, 1), (1, 2), (3, 4)]
    for u, v in edges:
        union(parent, rank, u, v)

    print("--------------")
    print("parent", parent)
    print("rank", rank)

    queries = [(0, 2), (0, 3), (3, 4)]
    results = [(u, v, find(parent, u) == find(parent, v)) for u, v in queries]

    for u, v, connected in results:
        print(f"Nodes {u} and {v} are {'connected' if connected else 'not connected'}")

union_find_example()
