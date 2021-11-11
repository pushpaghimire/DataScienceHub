import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx

# Process input file. There are two files we will need 1) airport mapping file and 2) route files
# airline to be processed 'AL2' # of rows in the input data file 2354
f_route = open('src/routes_v3.txt', "r", )
route_col = ['airline_cd', 'airline_id', 'src_airport_cd', 'src_airport_id', 'dstn_airport_cd', 'dstn_airport_id',
             'filler', 'stop_nbr', 'equipment_cd']
route = pd.read_csv(f_route, index_col=False, names=route_col, skipinitialspace='true')

f_airportmapping = open('src/AirportMapping.csv', "r")
airportmapping = pd.read_csv(f_airportmapping, index_col=False)

# 1) Filtering airline assigned to me [United Airways]
myroute = route.query('airline_cd == "AL2"')
# myroute=(route[route['airline_cd'] == 'AL2'].groupby(['airline_cd', 'src_airport_cd', 'dstn_airport_cd']).size().reset_index(name='count')).sort_index(ascending=False)

# 4) Generating top 20 hubs
# 5) Predicting the next hub Cleveland OH
# United is the airlines - Flights leaving mostly from Ohare, Houston, Denver, Newark and Washington = United Airways
myroute[['airline_cd', 'src_airport_cd', 'dstn_airport_cd']].groupby(['airline_cd', 'src_airport_cd']). \
    size().reset_index(name='count').sort_values(by='count', ascending=False).head(20)

#This code provides airport information from the mapping file in combination with the route file.
myroute.set_index('src_airport_cd').join(airportmapping.set_index('Code'))

# top 5 source airports that AL2 is leaving from #,'EWR', 'DEN', 'IAD'])]
top_5_airlines = airportmapping[airportmapping.Code.isin(['IAH', 'ORD'])]

# 2) Creating graph data structure. Take 10 airport from the top 2 hubs and union them for the graph.
graph1 = myroute[myroute.src_airport_cd.isin(top_5_airlines['Code'])].iloc[:10, [2, 4]]
graph2=(myroute[myroute.src_airport_cd.isin(['ORD'])].iloc[:10,[2,4]])
graph=pd.concat([graph1, graph2], axis=0)

airline_analysis = graph.groupby('src_airport_cd').size().reset_index(name='count').sort_values(by='count',ascending=False).head(9)
airline_analysis

# instantiate graph and populate the node from series airport 1. The loop below runs through the source records and creates edge records
G = nx.petersen_graph()

for i in range(0, len(graph)):
    G.add_edge(graph.iloc[i, 0], graph.iloc[i, 1])

# 3) This graph is used to generate graph characterstics
nx.draw(G, with_labels=True)
plt.show()

f_route.close()
f_airportmapping.close()
