from ast import List
import collections

# To find the redundant connection we can iterate through the list of edges
# and create the graph as we go along the list. For each node u,v in the list
# of edges if both u and v exist as nodes in the graph, then we can try and 
# form a path from u to v. 

# If the u -> v path already exists then adding another edge from u to v would 
# make our tree invalid.
