from diagrams import Diagram
from diagrams.azure.network import LoadBalancers
from diagrams.azure.compute import VM
from diagrams.azure.database import SQLDatabases

with Diagram("Azure Architecutre", show=True):

    lb = LoadBalancers("Azure Load Balancer")

    vm1 = VM("VM 1")
    vm2 = VM("VM 2")

    db = SQLDatabases("SQL Database")

    lb >> [vm1, vm2] >> db