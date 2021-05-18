import networkx as nx
import matplotlib.pyplot as plt


def pyplot_path(n, x_list, y_list, dist_matrix, best_path):
    temp = dict()
    for i in range(n):
        temp[i] = (x_list[i], y_list[i])
    print(temp)
    labels = dict()
    for i in range(n):
        labels[best_path[i]] = best_path[i]
    # print(labels)
    graph = nx.from_numpy_matrix(dist_matrix)
    plt.figure()
    pathEdges = list(zip(best_path, best_path[1:]))
    print(pathEdges)

    nx.draw_networkx_nodes(graph, temp, node_color="b")
    nx.draw_networkx_labels(graph, temp, labels=labels, font_size=10, font_color='w', font_family='sans-serif', font_weight='normal', alpha=1.0, bbox=None, ax=None)
    # nx.draw_networkx_edges(graph,temp,edge_color='k')
    # nx.draw_networkx_nodes(graph,temp,nodelist=best_path,node_color="r")
    nx.draw_networkx_edges(graph, temp, edgelist=pathEdges, edge_color='r', width=4)
    plt.show()


def cost_vs_gen(cost, gen):
    plt.plot(gen, cost)
    plt.xlabel('Number of ants')
    plt.ylabel('Iterations taken')
    plt.show()
