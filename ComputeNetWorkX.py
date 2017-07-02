import networkx as nx

G = nx.read_edgelist("/home/amitd92/solr/server/solr/IndexedNews/edges.txt", create_using=nx.DiGraph())
pr = nx.pagerank(G, alpha=0.85, personalization=None, max_iter=30, tol=1e-06, nstart=None, weight='weight', dangling=None)

target = open("/home/amitd92/solr/server/solr/IndexedNews/data/external_pageRankFile.txt",'w+')
for key in pr.keys():
    target.write("/home/amitd92/solr/NYTimesData/NYTimesDownloadData/"+key+"="+str(pr[key]))
    target.write("\n")


