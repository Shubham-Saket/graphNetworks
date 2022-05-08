import networkx as nx
import pandas as pd


data = [('A','B','1'),("A","C",'2'),("C","D",'6'),("C","E",'4'),
        ("B","C",'3'),("F","D",'7'),("D","B",'5')]
df = pd.DataFrame(data=data,columns=['node1','node2','edge'])
graph = nx.from_pandas_edgelist(df=df, source='node1', target='node2', edge_attr='edge',create_using=nx.Graph())

total_nodes = len(graph.nodes)
is_seen = [False] * total_nodes

def depth_first_algo(graph,start_node='A'):
    print(start_node,end='--->')
    start_node_index = list(graph.nodes).index(start_node)
    if is_seen[start_node_index]:
        print('retracting from',start_node)
        return 0
    is_seen[start_node_index] = True
    node_neighbours = graph.neighbors(start_node)
    for neighbour in node_neighbours:
        print('neighbour:',neighbour)
        depth_first_algo(graph,start_node=neighbour)
depth_first_algo(graph)



