import matplotlib.pyplot as plt
import networkx as nx

from utils.networkx import preprocess_input_and_run_fruchterman_reingold
from utils.testing import count_edge_crossings

def run_and_plot_graph_analysis(edges):

    g = nx.Graph()
    for u, v in edges:
        g.add_edge(u, v)

    plt.figure(figsize=(10, 10))
    pos, time_took = preprocess_input_and_run_fruchterman_reingold(g)
    crossings_count = count_edge_crossings(g,pos)
                
    nx.draw(
                g,
                pos,
                with_labels=True,
                node_color='lightblue',
                node_size=500,
                font_size=16,
                font_weight='bold'
            )
    plt.title("Tempo de execução do fruchterman_reingold: {:.4f} segundos, número de cruzamentos: {}".format(time_took, crossings_count))
    plt.axis('equal')
    plt.show()