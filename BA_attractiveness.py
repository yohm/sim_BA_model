import networkx as nx
import powerlaw
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import json

def py_random_state(random_state_index):
    return nx.utils.py_random_state(random_state_index)

def _random_subset(seq, m, rng):
    """ Return m unique elements from seq.
    This differs from random.sample which can return repeated
    elements if seq holds repeated elements.
    Note: rng is a random.Random or numpy.random.RandomState instance.
    """
    targets = set()
    while len(targets) < m:
        x = rng.choice(seq)
        targets.add(x)
    return targets

@py_random_state(3)
def barabasi_albert_attractiveness(n, m, a, seed=None):
    if m < 1 or m >= n:
        raise nx.NetworkXError("Barabási–Albert network must have m >= 1"
                               " and m < n, m = %d, n = %d" % (m, n))

    G = nx.empty_graph(m)
    # Target nodes for new edges
    targets = list(range(m))
    # List of existing nodes, with nodes repeated once for each adjacent edge
    repeated_nodes = []
    # Start adding the other n-m nodes. The first node is m.
    source = m
    while source < n:
        # Add edges to m nodes from the source.
        G.add_edges_from(zip([source] * m, targets))
        # Add one node to the list for each new edge just created.
        repeated_nodes.extend(targets)
        # And the new node "source" has m edges to add to the list.
        repeated_nodes.extend([source] * m)
        # Now choose m unique nodes from the existing nodes
        # Pick uniformly from repeated_nodes (preferential attachment)
        targets = _random_subset(repeated_nodes, m, seed)
        source += 1
    return G

g = barabasi_albert_attractiveness(6, 3, 1)
print( g.edges() )

