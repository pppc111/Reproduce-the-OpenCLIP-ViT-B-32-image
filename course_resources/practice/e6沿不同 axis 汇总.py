import numpy as np
A = np.array([[0.20, -0.50, 1.10],
              [0.80, 0.40, -0.30]])

sum0=A.sum(axis=0)  #沿轴0(行)方向求和——按列求和
print("A.sum(axis=0)=",sum0)
print("A.sum(axis=0)的shape=",sum0.shape)

mean1=A.mean(axis=1)  #沿轴1(列)方向求平均——按行求平均
print("A.mean(axis=1)=",mean1)
print("A.mean(axis=1)的shape=",mean1.shape)

max_all=A.max() #整个数组最大值
print("整个数组最大值=",max_all)

#边界输入：一维数组(只有axis=0，axis=1报错)，全0数组