import numpy as np
A=np.array([
    [0.20, -0.50, 1.10, 0.40],
    [0.80, 0.30, -0.70, 0.60],
    [-0.40, 0.90, 0.10, -0.20]
])
print("A.ndim=",A.ndim) #二维数组
print("A.shape=",A.shape)   #(行，列)
print("A.size=",A.size) #数字个数

row1=A[1,:] #第二行
last2_col=A[:,-2:]  #最后两列
print("第2行：",row1)
print("第2行shape=",row1.shape)
print("最后2列：",last2_col)
print("最后2列shape=",last2_col.shape)

B=A.copy()  #新建副本
B[B<0]=0    #布尔掩码True就换
# mask=B<0
# B[mask]=0
print("数组B：",B)