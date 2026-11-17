import numpy as np

def pairwise_dist(A,B):
    """求所有点对之间的距离矩阵"""
    #扩维A(N,1,d),B(1,M,d)
    A_exp=A[:,np.newaxis,:] #(3,2)变(3,1,2)
    B_exp=B[np.newaxis,:,:] #(2,2)变(1,2,2),第0维
    diff=A_exp-B_exp    #shape(N,M,d)
    dist_sq=np.sum(diff**2,axis=-1)
    D=np.sqrt(dist_sq)  #shape(N,M)
    #A每一行找距离最小的B索引
    nearest_idx=np.argmin(D,axis=1)
    return D,nearest_idx

A = np.array([[0.20, -0.40],
              [0.80, 0.30],
              [-0.50, 0.70]])
B = np.array([[0.10, 0.20],
              [-0.60, -0.20]])
D,nearest_idx=pairwise_dist(A,B)
print("距离矩阵D=",D)
print("D.shape=",D.shape)
print("A每行对应的最近B索引=",nearest_idx)