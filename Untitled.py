#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import powerlaw


# In[8]:


plt.rcParams["figure.subplot.left"] = 0.22
plt.rcParams["figure.subplot.right"] = 0.95
plt.rcParams["figure.subplot.bottom"] = 0.20
plt.rcParams["figure.subplot.top"] = 0.95
plt.rcParams['font.family'] ='sans-serif'
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.major.width'] = 1.0
plt.rcParams['ytick.major.width'] = 1.0
plt.rcParams['axes.labelsize'] = 20
plt.rcParams['font.size'] = 14
plt.rcParams['axes.linewidth'] = 1.2


# In[9]:


g = nx.barabasi_albert_graph(50000, 5)

ks = [x[1] for x in g.degree()]
results = powerlaw.Fit(ks, discrete=True)
results2 = powerlaw.Fit(ks, xmin=10, discrete=True)
print(f'alpha: {results.power_law.alpha}, xmin: {results.power_law.xmin}')
print(f'alpha: {results2.power_law.alpha}, xmin: {results2.power_law.xmin}')
R, p = results.distribution_compare('power_law', 'lognormal')


# In[10]:


# figPDF = results.plot_pdf(color='b')
figPDF = results.power_law.plot_pdf(label=r"fit($\alpha$: %.2f, $x_{min}$: %d)" % (results.alpha, results.xmin)) 
figPDF.set_ylabel("P(k)")
figPDF.set_xlabel("k")

cdf = {z[0]:z[1] for z in zip(*powerlaw.cdf(ks))}
cdf_xmin = cdf[results.xmin]

bin_edges, prob = powerlaw.pdf(ks)
x = [ (bin_edges[i]+bin_edges[i+1])/2.0 for i in range(0, len(bin_edges)-1) ]
plt.plot(x, prob/(1.0-cdf_xmin), label="data")
plt.legend()
plt.savefig('pk.png')


# In[ ]:





# In[ ]:




