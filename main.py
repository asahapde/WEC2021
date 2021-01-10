import osmnx as ox
import networkx as nx
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

# Import CSV
df = pd.read_csv('911Calls.csv')
df.head()

# Drop Empty Columns
df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
df.head()

# Adding minute and hour columns
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Minute'] = df['timeStamp'].apply(lambda time:time.minute)
df.head()

# Sorting by hour & minute
df.sort_values(by=['Hour','Minute'], inplace=True)
df.head()

# Removing all extra rows
df.dropna(axis=0,how='all',inplace=True)

# Adding alert type
df['Alert Type'] = df['title'].apply(lambda name: name.split(':')[0])


# Add Dictionary of Services

f1 = {
    'id':1,
    'lat':40.0137071,
    'lng':-75.3965480,
    'latTo':40.0137071,
    'lngTo':-75.3965480,
    'ready':0
}
f2 = {
    'id':2,
    'lat':40.0251013,
    'lng':-75.4490013,
    'latTo':40.0251013,
    'lngTo':-75.4490013,
    'ready':0
}
h1 = {
    'id':1,
    'lat':40.0514920,
    'lng':-75.3965480,
    'latTo':40.0514920,
    'lngTo':-75.3965480,
    'ready':0
}
h2 = {
    'id':2,
    'lat':40.0329254,
    'lng':-75.2750179,
    'latTo':40.0329254,
    'lngTo':-75.2750179,
    'ready':0
} 

# Speeds of Vehicles
fSpeed = 50 # Fire Truck Speed
hSpeed = 60/60 # Ambulance Speed

# Setup Map
north, east, south, west = 40.10, -75.2422, 40.00, -75.5077
G = ox.graph_from_bbox(north, south, east, west, network_type = 'drive', simplify=True)


# orig = ox.get_nearest_node(G, (f1['lat'],f1['lng']))
# route = nx.shortest_path(G, orig, 136012883)
# fig, ax = ox.plot_graph_route(G, route, show=False, close=False)

# route_map = ox.plot_route_folium(G, route)
# route_map

dest = ox.get_nearest_node(G, (40.135788,-75.5076694))


route1 = ox.shortest_path(G, 254777437, dest, weight='length')
route2 = ox.shortest_path(G, 136012883, dest, weight='length')
route3 = ox.shortest_path(G, 136148333, dest, weight='length')

fig, ax = ox.plot_graph(G, node_size=0, show=False, close=False)
ax.scatter(-75.3965480, 40.0137071, c='green', alpha=1, zorder=9)

plt.show()

# Loop through every Call
# for i in df.index:
#     newLat = df.at[i,'lat']
#     newLng = df.at[i,'lng']
#     emer = df.at[i,'Alert Type']

#     dest = ox.get_nearest_node(G, (newLat,newLng))
#     route1 = ox.shortest_path(G, 254777437, dest, weight='travel_time')

#     print(route1)

