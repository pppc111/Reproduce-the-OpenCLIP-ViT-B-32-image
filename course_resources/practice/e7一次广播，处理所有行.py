import numpy as np
X = np.array([[0.80, -0.60, 0.70],
              [-0.40, 0.50, 0.20]])
scale = np.array([1.50, 0.50, -1.00])
bias = np.array([-0.10, 0.20, 0.30])

Y=X*scale+bias
print("Y=",Y)
print("Y.shape=",Y.shape)

# 广播对齐说明
# X.shape=(2,3)
# scale.shape=(3,)，bias.shape=(3,)
# numpy自动把 scale、bias 广播成 (2,3)，两行共用同一套缩放、偏移参数
# 每一行：[x0*scale0 + bias0, x1*scale1 + bias1, x2*scale2 + bias2]

#边界输入：X只有一行