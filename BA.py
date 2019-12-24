import sys,json
import networkx as nx

if len(sys.argv) != 4:
    print(f"Usage: python {sys.argv[0]} <N> <m> <seed>", file=sys.stderr)
    raise Exception("invalid number of arguments")

g = nx.barabasi_albert_graph(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

import analyze_pk

alpha, xmin = analyze_pk.analyze_pk(g, 'pk.png')
with open('_output.json', 'w') as f:
    json.dump({"alpha": alpha, "x_min": xmin}, f)

