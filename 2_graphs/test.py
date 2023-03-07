from graph import Graph

import matplotlib.pyplot as plt

graph1 = Graph(10)

font = {'family': 'serif',
        'color':  'k',
        'weight': 'normal',
        'size': 16,
        'horizontalalignment' : 'center',
        'verticalalignment' : 'center'
        }
params = {
    'marker' : 'o',
    'color' : 'b'
}

graph1.add_node('object here')
graph1.add_edge(1, 10)

fig, ax = plt.subplots(figsize=(6, 6))
graph1.plot(ax, params, font)
plt.show()