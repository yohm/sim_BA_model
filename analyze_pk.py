import networkx as nx
import powerlaw
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def analyze_pk(g, figfile):
    ks = [x[1] for x in g.degree()]
    results = powerlaw.Fit(ks, discrete=True)

    figPDF = results.power_law.plot_pdf(label=r"fit($\alpha$: %.2f, $x_{min}$: %d)" % (results.alpha, results.xmin)) 
    figPDF.set_ylabel("P(k)")
    figPDF.set_xlabel("k")

    cdf = {z[0]:z[1] for z in zip(*powerlaw.cdf(ks))}
    cdf_xmin = cdf[results.xmin]

    bin_edges, prob = powerlaw.pdf(ks)
    x = [ (bin_edges[i]+bin_edges[i+1])/2.0 for i in range(0, len(bin_edges)-1) ]
    plt.plot(x, prob/(1.0-cdf_xmin), label="data")
    plt.legend()
    plt.savefig(figfile)

    return (results.power_law.alpha, results.power_law.xmin)
