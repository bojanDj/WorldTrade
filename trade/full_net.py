import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt    

df = pd.read_csv('APIdata/data.csv')

for yeard in range(1990,2021,5):

	print(yeard)

	importC = df['Trade Flow'] == 'Export'
	dfImport = df[importC]

	year = dfImport['Year'] == yeard
	dfYear = dfImport[year]

	GD = nx.from_pandas_edgelist(dfYear, source = 'Reporter', target = 'Partner', edge_attr = 'Trade Value (US$)', create_using=nx.DiGraph())
	GD.is_directed()

	print("W degree:"+str(GD.degree(weight='Trade Value (US$)')))

	nx.write_gexf(GD,"Mreze/"+str(yeard)+".gexf")

print(GD.size())
print(GD.size('Trade Value (US$)'))

# import community as community_louvain
# partition = community_louvain.best_partition(G)

#nx.draw(GD, with_labels=True)
#plt.show()

#import pyvis

#from pyvis.network import Network


#net = Network(bgcolor='#222222', font_color='white')

#net.from_nx(GD)

#name = 'full_network.html'

#net.show(name)

import pydot
pos = nx.spring_layout(GD, k=2, iterations=100)
betCent = nx.betweenness_centrality(GD, normalized=True, endpoints=True)
node_color = [20000.0 * GD.degree(v) for v in GD]
node_size =  [v * 10000 for v in betCent.values()]
plt.figure(figsize=(20,20))
nx.draw_networkx(GD, pos=pos, with_labels=True,
                node_color=node_color,
                node_size=node_size)
#communities
# from networkx.algorithms import community
# communities = community.greedy_modularity_communities(GD)
# modularity_dict = {} # Create a blank dictionary
# for i,c in enumerate(communities): # Loop through the list of communities, keeping track of the number for the community
    # for name in c: # Loop through each person in a community
        # modularity_dict[name] = i # Create an entry in the dictionary for the person, where the value is which group they belong to.
        # print(name)
        # print(i)

# # Now you can add modularity information like we did the other metrics
# nx.set_node_attributes(G, modularity_dict, 'modularity')
#communities
print(nx.density(GD))
#from networkx.algorithms.centrality import *
#print(degree_centrality(GD))

#plt.axis('off') 
#plt.show()
