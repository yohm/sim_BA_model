import networkx as nx
import powerlaw
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import json

g = nx.barabasi_albert_graph(2000, 5)

ks = [x[1] for x in g.degree()]
results = powerlaw.Fit(ks, xmin=20, discrete=True)
print(f'alpha: {results.power_law.alpha}, xmin: {results.power_law.xmin}')

figPDF = results.plot_pdf(color='b')
results.power_law.plot_pdf(ax=figPDF)
figPDF.set_ylabel("P(k)")
figPDF.set_xlabel(r"degree, k")
plt.savefig('pk.png')

with open('_output.json', 'w') as f:
    json.dump({"alpha": results.power_law.alpha}, f)

