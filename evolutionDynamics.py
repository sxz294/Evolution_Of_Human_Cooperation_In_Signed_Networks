import numpy as np
import random
import matplotlib.pyplot as plt

def getPayoff(node, edge, i, j, lmbd):
    # payoff matrix for positive relations, T>R>P>S
    R = 1
    S = -lmbd
    T = 1 + lmbd
    P = 0
    # print(edge)

    # when relation between i and j is negative, the payoff is also negative
    if node[i] and node[j]:
        return R * edge[i, j]
    elif node[i] and (not node[j]):
        return S * edge[i, j]
    elif (not node[i]) and node[j]:
        return T * edge[i, j]
    else:
        return P * edge[i, j]


def evolutionwoSB(graph, maxIter, beta, lmbd):
    nodes, edges = graph
    N = nodes.size
    k = np.sum(np.abs(edges)) * 2 // N
    taus = [0, 0.3, 0.6, 0.9]
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=False, figsize=(12,4))
    for tau in taus:
        node = nodes.copy()
        edge = edges.copy()
        fraction_nodes = []
        fraction_edges = []
        for _ in range(maxIter):
            # print(edge.shape)
            for i in range(node.size):
                # print(edge[i,:])
                neighbors_i = np.argwhere(edge[i] != 0)
                # print(neighbors_i)
                if neighbors_i.size == 0:
                    continue

                # with probability of tau to update relation
                a = np.random.uniform(0, 1)
                if a < tau:

                    j = np.random.choice(neighbors_i.flatten(),1)[0]

                    # calculate accumulated payoffs of i and j
                    fi = 0
                    fj = 0

                    # find neighbors of j
                    neighbors_j = np.argwhere(edge[j] != 0)
                    for ni in neighbors_i.flatten():
                        fi += getPayoff(node, edge, i, ni, lmbd)
                    for nj in neighbors_j.flatten():
                        fj += getPayoff(node, edge, j, nj, lmbd)

                    # # find common neighbors of i and j
                    # neighbors_j = np.argwhere(edge[j] != 0)
                    # for ni in neighbors_i.flatten():
                    #     for nj in neighbors_j.flatten():
                    #         if ni == nj:
                    #             fi += getPayoff(node, edge, i, ni, lmbd)
                    #             fj += getPayoff(node, edge, j, nj, lmbd)

                    # calculate the probability that i would adapt relation
                    p = 1.0 / (1 + np.exp(-beta*(fi-fj)))

                    # if relation between i and j is positive:
                    if edge[i,j] == 1:
                        # if i is cooperator and j is defector
                        if node[i] and (not node[j]):
                            # change relation to negative with p
                            b = np.random.uniform(0, 1)
                            if b < p:
                                edge[i,j] = -1
                                edge[j,i] = -1
                        # if both i and j are defectors
                        elif (not node[i]) and (not node[j]):
                            # change relation to negative
                            edge[i,j] = -1
                            edge[j,i] = -1
                    # else when the relation between i and j is negative:
                    else:
                        # if i is defector and j is cooperator
                        if (not node[i]) and node[j]:
                            # change relation to positive with p
                            b = np.random.uniform(0, 1)
                            if b < p:
                                edge[i,j] = 1
                                edge[j,i] = 1
                        elif node[i] and node[j]:
                            # change relation to positive
                            edge[i,j] = 1
                            edge[j,i] = 1
                # with probability of 1-tau to update behavior
                else:
                    # print(neighbors_i.shape)
                    j = np.random.choice(neighbors_i.flatten(), 1)[0]
                    # calculate accumulated payoffs of i and j
                    fi = 0
                    fj = 0

                    # find neighbors of j
                    neighbors_j = np.argwhere(edge[j] != 0)
                    for ni in neighbors_i.flatten():
                        fi += getPayoff(node, edge, i, ni, lmbd)
                    for nj in neighbors_j.flatten():
                        fj += getPayoff(node, edge, j, nj, lmbd)

                    # # find common neighbors of i and j
                    # neighbors_j = np.argwhere(edge[j] != 0)
                    # for ni in neighbors_i.flatten():
                    #     for nj in neighbors_j.flatten():
                    #         if ni == nj:
                    #             fi += getPayoff(node, edge, i, ni, lmbd)
                    #             fj += getPayoff(node, edge, j, nj, lmbd)

                    # calculate the probability that i would adapt strategy
                    p = 1.0 / (1 + np.exp(-beta * (fj - fi)))
                    # i learn j's strategy with p
                    b = np.random.uniform(0, 1)
                    if b < p:
                        node[i] = node[j]

#             find the cooperators and positive relations fraction in the network:
            f_node = np.sum(node)/N
            f_edge = (float)(np.sum(edge)//4 + N*k//4) / (N*k // 2)
            fraction_nodes.append(f_node)
            fraction_edges.append(f_edge)

            # print(f)
        ax1.plot(np.arange(0,maxIter),fraction_nodes, label='tau = %s'%tau)
        ax2.plot(np.arange(0,maxIter),fraction_edges, label='tau = %s'%tau)
    ax1.set_xlim(0, maxIter)
    ax1.set_ylim(0, 1.1)
    ax2.set_xlim(0, maxIter)
    ax2.set_ylim(0, 1.1)
    ax1.legend()
    ax2.legend()
    ax1.set_title("Evolution of cooperators in the random network")
    ax1.set_ylabel("Fraction of cooperators")
    ax1.set_xlabel("Iteration")
    ax2.set_title("Evolution of positive relations in the random network")
    ax2.set_ylabel("Fraction of positive relations")
    ax2.set_xlabel("Iteration")
    plt.show()

def evolutionwSB_behavior(graph, maxIter, beta, lmbd):
    nodes, edges = graph
    N = nodes.size
    k = np.sum(np.abs(edges)) * 2 // N
    taus = [0, 0.3, 0.6, 0.9]
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=False, figsize=(12,4))
    for tau in taus:
        node = nodes.copy()
        edge = edges.copy()
        fraction_nodes = []
        fraction_edges = []
        for _ in range(maxIter):
            for i in range(node.size):
                neighbors_i = np.argwhere(edge[i] != 0)
                if neighbors_i.size == 0:
                    continue

                # adapt relation with probability tau
                a = np.random.uniform(0, 1)
                if a < tau:

                    j = np.random.choice(neighbors_i.flatten(), 1)[0]

                    # calculate accumulated payoffs of i and j
                    fi = 0
                    fj = 0

                    # find neighbors of j
                    neighbors_j = np.argwhere(edge[j] != 0)
                    for ni in neighbors_i.flatten():
                        fi += getPayoff(node, edge, i, ni, lmbd)
                    for nj in neighbors_j.flatten():
                        fj += getPayoff(node, edge, j, nj, lmbd)

                    # calculate the probability that i would adapt relation
                    p = 1.0 / (1 + np.exp(-beta * (fi - fj)))

                    # if relation between i and j is positive:
                    if edge[i, j] == 1:
                        # if i is cooperator and j is defector
                        if node[i] and (not node[j]):
                            # change relation to negative with p
                            b = np.random.uniform(0, 1)
                            if b < p:
                                edge[i, j] = -1
                                edge[j, i] = -1
                        # if both i and j are defectors
                        elif (not node[i]) and (not node[j]):
                            # change relation to negative
                            edge[i, j] = -1
                            edge[j, i] = -1
                    # else when the relation between i and j is negative:
                    else:
                        # if i is defector and j is cooperator
                        if (not node[i]) and node[j]:
                            # change relation to positive with p
                            b = np.random.uniform(0, 1)
                            if b < p:
                                edge[i, j] = 1
                                edge[j, i] = 1
                        elif node[i] and node[j]:
                            # change relation to positive
                            edge[i, j] = 1
                            edge[j, i] = 1
                # with 1-tau probability, i will adapt strategy
                else:
                    j = np.random.choice(neighbors_i.flatten(), 1)[0]
                    # print(i,j,edge[i][j])
                    # calculate accumulated payoffs of i and j
                    fi = 0
                    fj = 0

                    # find neighbors of j
                    neighbors_j = np.argwhere(edge[j] != 0)
                    for ni in neighbors_i.flatten():
                        fi += getPayoff(node, edge, i, ni, lmbd)
                    for nj in neighbors_j.flatten():
                        fj += getPayoff(node, edge, j, nj, lmbd)

                    # calculate the probability that i would adapt relation
                    p = 1.0 / (1 + np.exp(-beta * (fj - fi)))
                    # print(i, j, p)
                    if edge[i, j] == 1:
                        # i learn j's strategy with p
                        b = np.random.uniform(0, 1)
                        if b < p:
                            node[i] = node[j]
                    else:
                        # i learn j's opposite strategy
                        b = np.random.uniform(0, 1)
                        if b < p:
                            node[i] = 1 - node[j]


#             find the cooperators and positive relations fraction in the network:
            f_node = np.sum(node)/N
            f_edge = (float)(np.sum(edge)//4 + N*k//4) / (N*k // 2)
            fraction_nodes.append(f_node)
            fraction_edges.append(f_edge)

            # print(f)
        ax1.plot(np.arange(0,maxIter),fraction_nodes, label='tau = %s'%tau)
        ax2.plot(np.arange(0,maxIter),fraction_edges, label='tau = %s'%tau)
    ax1.set_xlim(0, maxIter)
    ax1.set_ylim(0, 1.1)
    ax2.set_xlim(0, maxIter)
    ax2.set_ylim(0, 1.1)
    ax1.legend()
    ax2.legend()
    ax1.set_title("Evolution of cooperators in the random network")
    ax1.set_ylabel("Fraction of cooperators")
    ax1.set_xlabel("Iteration")
    ax2.set_title("Evolution of positive relations in the random network")
    ax2.set_ylabel("Fraction of positive relations")
    ax2.set_xlabel("Iteration")
    plt.show()

def evolutionwSB_pure(graph, maxIter, beta, lmbd):
    nodes, edges = graph
    N = nodes.size
    k = np.sum(np.abs(edges))*2//N
    taus = [0, 0.3, 0.6, 0.9]
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=False, figsize=(12,4))
    for tau in taus:
        node = nodes.copy()
        edge = edges.copy()
        fraction_nodes = []
        fraction_edges = []
        for _ in range(maxIter):
            for i in range(node.size):
                neighbors_i = np.argwhere(edge[i] != 0)
                if neighbors_i.size == 0:
                    continue

                # adapt relation with probability tau
                a = np.random.uniform(0, 1)
                if a < tau:

                    j = np.random.choice(neighbors_i.flatten(),1)[0]
                    # print(i, j, edge[i][j])
                    # calculate accumulated payoffs of i and j
                    fi = 0
                    fj = 0

                    # find neighbors of j
                    neighbors_j = np.argwhere(edge[j] != 0)
                    for ni in neighbors_i.flatten():
                        fi += getPayoff(node, edge, i, ni, lmbd)
                    for nj in neighbors_j.flatten():
                        fj += getPayoff(node, edge, j, nj, lmbd)

                    # calculate the probability that i would adapt relation
                    p = 1.0 / (1 + np.exp(-beta*(fi-fj)))
                    # print(i,j,p)

                    # if relation between i and j is positive:
                    if edge[i, j] == 1:
                        # if i is cooperator and j is defector
                        if node[i] and (not node[j]):
                            # change relation to negative with p
                            b = np.random.uniform(0, 1)
                            if b < p:
                                edge[i, j] = -1
                                edge[j, i] = -1

                    # else when the relation between i and j is negative:
                    else:
                        # if both defector and j are cooperators
                        if node[i] and node[j]:
                            # change relation to positive
                            edge[i, j] = 1
                            edge[j, i] = 1
                # with 1-tau probability, i will adapt strategy
                else:
                    j = np.random.choice(neighbors_i.flatten(), 1)[0]
                    # print(i,j,edge[i][j])
                    # calculate accumulated payoffs of i and j
                    fi = 0
                    fj = 0

                    # find neighbors of j
                    neighbors_j = np.argwhere(edge[j] != 0)
                    for ni in neighbors_i.flatten():
                        fi += getPayoff(node, edge, i, ni, lmbd)
                    for nj in neighbors_j.flatten():
                        fj += getPayoff(node, edge, j, nj, lmbd)

                    # calculate the probability that i would adapt relation
                    p = 1.0 / (1 + np.exp(-beta * (fj - fi)))
                    # print(i, j, p)
                    if edge[i, j] == 1:
                        # i learn j's strategy with p
                        b = np.random.uniform(0, 1)
                        if b < p:
                            node[i] = node[j]
                    else:
                        # i learn j's opposite strategy
                        b = np.random.uniform(0, 1)
                        if b < p:
                            node[i] = 1-node[j]


#             find the cooperators and positive relations fraction in the network:
            f_node = np.sum(node)/N
            f_edge = (float)(np.sum(edge)//4 + N*k//4) / (N*k // 2)
            fraction_nodes.append(f_node)
            fraction_edges.append(f_edge)

            # print(f)
        ax1.plot(np.arange(0,maxIter),fraction_nodes, label='tau = %s'%tau)
        ax2.plot(np.arange(0,maxIter),fraction_edges, label='tau = %s'%tau)
    ax1.set_xlim(0, maxIter)
    ax1.set_ylim(0, 1.1)
    ax2.set_xlim(0, maxIter)
    ax2.set_ylim(0, 1.1)
    ax1.legend()
    ax2.legend()
    ax1.set_title("Evolution of cooperators in the random network")
    ax1.set_ylabel("Fraction of cooperators")
    ax1.set_xlabel("Iteration")
    ax2.set_title("Evolution of positive relations in the random network")
    ax2.set_ylabel("Fraction of positive relations")
    ax2.set_xlabel("Iteration")
    plt.show()