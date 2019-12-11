__author__ = """\n""".join(['Maksim Tsvetovat <maksim@tsvetovat.org',
                            'Drew Conway <drew.conway@nyu.edu>',
                            'Aric Hagberg <hagberg@lanl.gov>'])

from collections import defaultdict
import networkx as nx
import pandas as pd
from scipy.cluster import hierarchy
from scipy.spatial import distance
import matplotlib.pyplot as plt


def create_hc(G, t=1.0):
    """
    Creates hierarchical cluster of graph G from distance matrix
    Maksim Tsvetovat ->> Generalized HC pre- and post-processing to work on labelled graphs and return labelled clusters
    The threshold value is now parameterized; useful range should be determined experimentally with each dataset
    """

    """Modified from code by Drew Conway"""
    
    ## Create a shortest-path distance matrix, while preserving node labels
    # labels=list(G.nodes())  
    distances = hierarchy.complete(
            pd.DataFrame(dict(nx.all_pairs_shortest_path_length(G))).values)
    membership = hierarchy.fcluster(distances, t=t)
    # Create hierarchical cluster
    # Y=distance.squareform(distances)
    #Z=hierarchy.complete(Y)  # Creates HC using farthest point linkage
    
    
    # This partition selection is arbitrary, for illustrive purposes
    # membership=hierarchy.fcluster(Z,t=t)
    # Create collection of lists for blockmodel
    partition = defaultdict(list)
    for cluster_label, node in zip(membership, G.nodes()):
        partition[cluster_label].append(node)
    return list(partition.values())
