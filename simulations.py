from generateGraph import *
from evolutionDynamics import *

# set parameters
# number of nodes N, average degree k
# initial fraction of positive edges omega
# intial fraction of cooperators gamma
N = 100
k = 4
omega = 0.5
gamma = 0.1

maxIter = 1000
beta = 10
lmbd = 0.5

# graph = randomGraph(N,k,omega,gamma)
# evolutionwoSB(graph, maxIter, beta, lmbd)
# evolutionwSB_behavior(graph, maxIter, beta, lmbd)
# evolutionwSB_pure(graph, maxIter, beta, lmbd)

# graph_hub_C = randomGraph_hub_C(N,k,omega,gamma)
# evolutionwoSB(graph_hub_C, maxIter, beta, lmbd)
# evolutionwSB_behavior(graph_hub_C, maxIter, beta, lmbd)
# evolutionwSB_pure(graph_hub_C, maxIter, beta, lmbd)

graph_leaf_C = randomGraph_leaf_C(N,k,omega,gamma)
evolutionwoSB(graph_leaf_C, maxIter, beta, lmbd)
# evolutionwSB_behavior(graph_leaf_C, maxIter, beta, lmbd)
# evolutionwSB_pure(graph_leaf_C, maxIter, beta, lmbd)