"""
https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.convert_matrix.from_scipy_sparse_matrix.html
"""
import networkx as nx
import scipy.sparse
A = scipy.sparse.eye(2,2,1)
print(A)
G = nx.from_scipy_sparse_matrix(A)
G1 = nx.from_scipy_sparse_matrix(A, create_using=nx.DiGraph())
#print(G)
#adj = G1.adjacency_matrix().to_dense()
#print(adj)


A = scipy.sparse.csr_matrix([[1, 1], [1, 2]])
print('-'*20)
print(A)
print('-'*20)
G = nx.from_scipy_sparse_matrix(A, parallel_edges=True,
        create_using=nx.MultiGraph())
print(G)
