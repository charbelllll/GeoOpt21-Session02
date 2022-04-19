
#charbel baliss

#importing libraries and 'geometry' file
from flask import Flask
import ghhops_server as hs
import rhino3dm as rg
import geometry as geo

app = Flask(__name__)
hops = hs.Hops(app)

#creating the workflow
@hops.component(
    "/createSpiralGraph",
    name = "Create a Spiral Graph",
    inputs=[
    ],
    outputs=[
       hs.HopsPoint("Nodes","N","  Nodes list ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","E"," edges List ", hs.HopsParamAccess.LIST)
    ]
)
def createSpiralGraph():

    G = geo.createGridGraph()
    GW = geo.addRandomWeigths(G)

    nodes = geo.getNodes(GW)
    edges = geo.getEdges(GW) 

    return nodes, edges

if __name__== "__main__":
    app.run(debug=True)