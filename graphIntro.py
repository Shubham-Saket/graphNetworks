import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

data = [('A','B','1'),("A","C",'2'),("C","D",'6'),("C","E",'4'),
        ("B","C",'3'),("F","D",'7'),("D","B",'5')]
df = pd.DataFrame(data=data,columns=['node1','node2','edge'])
graph = nx.from_pandas_edgelist(df=df, source='node1', target='node2', edge_attr='edge',create_using=nx.Graph())
pos = nx.spring_layout(graph, k=5)
nx.draw(graph, pos, with_labels=True)
labels = {edge_attribute: graph.edges[edge_attribute]['edge'] for edge_attribute in graph.edges}
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
plt.show()