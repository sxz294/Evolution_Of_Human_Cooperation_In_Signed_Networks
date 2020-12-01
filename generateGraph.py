import numpy as np
import random

def randomGraph(N,k,omega,gamma):
    # initialize nodes of size N
    # randomly select gamma fraction to be cooperators (1), others as defectors (0)
    nodes = np.zeros(N)
    randomlist_node = random.sample(range(0, N), int(N * gamma))
    nodes[randomlist_node] = 1

    # initialize adjacent matrix of size (N,N)
    edges = [[0 for _ in range(N)] for _ in range(N)]

    # form all the possible edges
    coord = []
    for i in range(N):
        for j in range(i + 1, N):
            coord.append((i, j))

    # randomly select from N(N-1)/2 possible edges to form N*k/2 edges, s.t. the average degree will be k
    randomlist_edge = random.sample(coord, int(N * k // 2))
    # print(randomlist_edge)
    # within the edges, randomly select omega of them to be positive edges (1)
    # set the others to be negative edges (-1)
    randomlist_positive_edges = random.sample(randomlist_edge, int(N * k * omega // 2))
    # print(randomlist_positive_edges)
    for coins in randomlist_edge:
        if coins in randomlist_positive_edges:
            edges[coins[0]][coins[1]] = 1
            edges[coins[1]][coins[0]] = 1
        else:
            edges[coins[0]][coins[1]] = -1
            edges[coins[1]][coins[0]] = -1

    edges = np.asarray(edges)
    # print(edges[:20,:20])
    f = np.sum(nodes) / nodes.size
    print(f)
    print(np.sum(np.abs(edges)))
    print(np.sum(edges))
    return (nodes,edges)

def randomGraph_hub_C(N,k,omega,gamma):

    # initialize adjacent matrix of size (N,N)
    edges = [[0 for _ in range(N)] for _ in range(N)]

    # form all the possible edges
    coord = []
    for i in range(N):
        for j in range(i + 1, N):
            coord.append((i, j))

    # randomly select from N(N-1)/2 possible edges to form N*k/2 edges, s.t. the average degree will be k
    randomlist_edge = random.sample(coord, int(N * k // 2))
    # print(randomlist_edge)
    # within the edges, randomly select omega of them to be positive edges (1)
    # set the others to be negative edges (-1)
    randomlist_positive_edges = random.sample(randomlist_edge, int(N * k * omega // 2))
    # print(randomlist_positive_edges)
    for coins in randomlist_edge:
        if coins in randomlist_positive_edges:
            edges[coins[0]][coins[1]] = 1
            edges[coins[1]][coins[0]] = 1
        else:
            edges[coins[0]][coins[1]] = -1
            edges[coins[1]][coins[0]] = -1

    edges = np.asarray(edges)
    # print(edges[:20,:20])

    sort_degree = np.argsort(np.sum(np.abs(edges),axis=0))
    # print(sort_degree)
    hub_degree = sort_degree[int(N-N * gamma):]
    # initialize nodes of size N
    # randomly select gamma fraction to be cooperators (1), others as defectors (0)
    nodes = np.zeros(N)
    nodes[hub_degree] = 1

    f = np.sum(nodes) / nodes.size
    print(f)
    print(np.sum(np.abs(edges)))
    print(np.sum(edges))
    return (nodes,edges)

def randomGraph_leaf_C(N,k,omega,gamma):

    # initialize adjacent matrix of size (N,N)
    edges = [[0 for _ in range(N)] for _ in range(N)]

    # form all the possible edges
    coord = []
    for i in range(N):
        for j in range(i + 1, N):
            coord.append((i, j))

    # randomly select from N(N-1)/2 possible edges to form N*k/2 edges, s.t. the average degree will be k
    randomlist_edge = random.sample(coord, int(N * k // 2))
    # print(randomlist_edge)
    # within the edges, randomly select omega of them to be positive edges (1)
    # set the others to be negative edges (-1)
    randomlist_positive_edges = random.sample(randomlist_edge, int(N * k * omega // 2))
    # print(randomlist_positive_edges)
    for coins in randomlist_edge:
        if coins in randomlist_positive_edges:
            edges[coins[0]][coins[1]] = 1
            edges[coins[1]][coins[0]] = 1
        else:
            edges[coins[0]][coins[1]] = -1
            edges[coins[1]][coins[0]] = -1

    edges = np.asarray(edges)
    # print(edges[:20,:20])

    sort_degree = np.argsort(np.sum(np.abs(edges),axis=0))
    # print(sort_degree)
    hub_degree = sort_degree[:int(N * gamma)]
    # initialize nodes of size N
    # randomly select gamma fraction to be cooperators (1), others as defectors (0)
    nodes = np.zeros(N)
    nodes[hub_degree] = 1

    f = np.sum(nodes) / nodes.size
    print(f)
    print(np.sum(np.abs(edges)))
    print(np.sum(edges))
    return (nodes,edges)
