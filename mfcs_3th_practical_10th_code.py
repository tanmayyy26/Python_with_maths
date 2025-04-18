import matplotlib.pyplot as plt
import networkx as nx

# Define a relation and create a directed graph
relation = [(1, 2), (2, 3), (3, 1)]  
G = nx.DiGraph(relation)  

# SDraw the graph
plt.figure(figsize=(6, 6))
pos = nx.spring_layout(G) 
nx.draw(G, pos, with_labels=True, node_color="blue", node_size=1000, font_size=15, font_weight="bold", edge_color="black")

# Display the graph
plt.title("Graph Representation")
plt.show()