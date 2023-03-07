from random import randint
import matplotlib.pyplot as plt
import numpy as np

# Class for graph
# written in the spirit of dict of lists stroage type

class Graph:

    # storage of vertex data :
    # index of vertex -> some object 
    verteces = []

    # dict for graph edges
    # key : index of vertex
    # value : list of adjecent indeces
    edges = {}

    # number of verteces in graph
    N = 0

    # graph initializer
    
    # if N is not provided empty graph is created
    # else random graph is generated, where each edge
    # has 50 % chance to appear
    # by deafault we store in each vertex its index number
    def __init__(self, N = None):

        self.edges = {}

        if N == None:
            self.N = 0
            self.verteces = []
            return

        self.verteces = list(range(N))

        for i in range(N):
            self.edges[i] = []

        for i in range(N):
            for k in range(i, N):
                if randint(0, 1):
                    self.edges[i].append(k)
                    self.edges[k].append(i)

        self.N = N

    # get info from node index
    def __getitem__(self, index):
        return self.verteces[index]
    
    def __len__(self):
        return self.N

    # add vertex to existing graph
    # info is an information stored in vertex
    def add_vertex(self, info):
        self.verteces.append(info)
        self.edges[self.N] = []
        self.N = self.N + 1

    # add edge between two existing verteces
    def add_edge(self, i, j):
        assert i < self.N, 'first vertex is not present in graph'
        assert j < self.N, 'second vertex is not present in graph'

        self.edges[i].append(j)
        self.edges[j].append(i)

    # plot function for graph
    # graph is plotted as equally distrubed over circle points with lines coresponding to edges
    # axes : matplotlib axes to which plot a graph
    # param_dict : parameter dictionary for lines plot (see ex. in jupiter notebook)
    # font_dict : parameter dictionary for text labels of nodes (see ex. in jupiter notebook)
    def plot(self, axes, param_dict, font_dict, acsent_nodes=None):

        assert self.N > 0 , 'Graph is empty'

        d_alpha = 2 * np.pi / self.N

        # plot edges and verteces
        for node in self.edges.keys():
            # if edges are present
            alpha = d_alpha * node
            if self.edges[node]:

                for neigh in self.edges[node]:
                    if neigh > node:
                        beta = neigh * d_alpha
                        axes.plot([np.cos(beta), np.cos(alpha)],
                                   [np.sin(beta), np.sin(alpha)],
                                    **param_dict)

            else:
                axes.plot(np.cos(alpha), np.sin(alpha),
                           **param_dict)
                
        if acsent_nodes != None:
            alpha = d_alpha * np.array(acsent_nodes)
            axes.plot(np.cos(alpha), np.sin(alpha),
                           color='k', marker='o', linestyle='',
                           markersize=18, label='selected_nodes')

        # plot node labels
        for node in self.edges.keys():
            alpha = d_alpha * node

            margin_step = 0.05 + font_dict['size'] * 0.0025

            axes.text( (1 + margin_step) * np.cos(alpha),
                       (1 + margin_step) * np.sin(alpha), 
                      '{}'.format(node),
                      fontdict = font_dict)
            
        bd = 1 + 0.1 + font_dict['size'] * 0.0025
        axes.set_xlim([-bd, bd])
        axes.set_ylim([-bd, bd])