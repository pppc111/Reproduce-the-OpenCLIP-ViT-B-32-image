import numpy as np
p = np.array([-0.50, 1.20, 2.00])
q = np.array([0.80, -0.40, 1.10])

pq=p-q  #坐标差向量
euclid=np.sqrt(np.sum(pq**2))   #欧氏距离：坐标差的平方和开方
manhattan=np.sum(np.abs(pq))    #曼哈顿距离：坐标差绝对值之和

print("p-q=",pq)
print("p-q.shape=",pq.shape)
print(f"欧氏距离={euclid:.6f}")
print(f"曼哈顿距离={manhattan:.6f}")
#边界输入：两点重合 p==q，距离都是0