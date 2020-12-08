from generateGraph import *
from evolutionDynamics import *
import matplotlib.pyplot as plt

# set parameters
# number of nodes N, average degree k
# initial fraction of positive edges omega
# intial fraction of cooperators gamma
N = 100
k = 4
omega = 0.5
gamma = 0.5

maxIter = 100
beta = 10
lmbd = 0.5

graph = randomGraph(N,k,omega,gamma)

p_node = np.zeros((10,10))
p_edge = np.zeros((10,10))
for i in range(10):
    # p_node[i,:], p_edge[i,:] = evolutionwoSB(graph, maxIter, beta, lmbd)
    p_node[i, :], p_edge[i, :] = evolutionwSB_behavior(graph, maxIter, beta, lmbd)
    # p_node[i, :], p_edge[i, :] = evolutionwSB_pure(graph, maxIter, beta, lmbd)
# Multiple box plots on one Axes
f, (ax1, ax2) = plt.subplots(1, 2, sharey=False, figsize=(12,4))
ax1.boxplot(p_node)
ax1.set_xticklabels(['0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9'])
ax2.boxplot(p_edge)
ax2.set_xticklabels(['0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9'])
ax1.set_title("Fraction of cooperators with different taus in the steady state")
ax1.set_ylabel("Fraction of cooperators")
ax1.set_xlabel("Tau")
ax2.set_title("Fraction of positive relations with different taus in the steady state")
ax2.set_ylabel("Fraction of positive relations")
ax2.set_xlabel("Tau")
plt.show()

# evolutionwoSB(graph, maxIter, beta, lmbd)
# evolutionwSB_behavior(graph, maxIter, beta, lmbd)
# evolutionwSB_pure(graph, maxIter, beta, lmbd)

# graph_hub_C = randomGraph_hub_C(N,k,omega,gamma)
# evolutionwoSB(graph_hub_C, maxIter, beta, lmbd)
# evolutionwSB_behavior(graph_hub_C, maxIter, beta, lmbd)
# evolutionwSB_pure(graph_hub_C, maxIter, beta, lmbd)

# graph_leaf_C = randomGraph_leaf_C(N,k,omega,gamma)
# evolutionwoSB(graph_leaf_C, maxIter, beta, lmbd)
# evolutionwSB_behavior(graph_leaf_C, maxIter, beta, lmbd)
# evolutionwSB_pure(graph_leaf_C, maxIter, beta, lmbd)