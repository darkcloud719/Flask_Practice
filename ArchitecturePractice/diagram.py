from graphviz import Digraph

dot = Digraph(comment="Simple Architecture Diagram")

dot.node('A', 'Client')
dot.node('B', 'Web Server')
dot.node('C', 'Database Server')

# Define edges between nodes
dot.edge('A', 'B')  # Client -> Web Server
dot.edge('B', 'C')  # Web Server -> Database Server

# Render the diagram to a file
dot.render('architecture-diagram', format="png", view=True)
