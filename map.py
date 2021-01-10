import osmnx as ox
import networkx as nx
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt

north, east, south, west = 40.10, -75.2422, 40.00, -75.5077
G = ox.graph_from_bbox(north, south, east, west, network_type = 'drive', simplify=True)

#Fire Station #1
#254777437
#(40.0137071, -75.3961213)

#Fire Station #panad2
#136012883
#(40.0251013, -75.4490013)
#Hospital #1
# 136148333
# (40.0514920, -75.3965480)

#Hospital #2
# 5673550491
# (40.0329254, -75.2750179)

#To get the shortest path between 2 points on the map
#route = nx.shortest_path(G, originalPosition, Destination)
route = nx.shortest_path(G, 254777437, 136012883)

fig, ax = ox.plot_graph(G, show=False, close=False)

#To draw the route, use the following line
fig, ax = ox.plot_graph_route(G, route, show=False, close=False)

#To draw a dot on the map, Use the following line. Long and Lat are reversed for dot drawing.
#ax.scatter(-75.25, 40.01, c='red', alpha=1, zorder=9)
ax.scatter(-75.25, 40.01, c='red', alpha=1, zorder=9)

plt.show()