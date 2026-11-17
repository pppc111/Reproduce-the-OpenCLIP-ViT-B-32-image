import numpy as np
a = np.array([0.80, -0.60, 0.70])
b = np.array([-0.20, 0.90, 0.40])

mul_elem=a*b    #逐元素相乘
dot_val=a@b     #点乘/内积
print("a*b=",mul_elem)
print("a*b.shape=",mul_elem.shape)  #一维个数3 (3,)
print(f"a@b={dot_val:.2f}")         #浮点数精度
print("a@b.shape=",dot_val.shape)   #空元组，不是数组

len_a=np.sqrt(np.sum(a**2))
len_b=np.sqrt(np.sum(b**2))
print(f"a的欧式长度为{len_a:.6f}")
print(f"b的欧式长度为{len_b:.6f}")
#print("b的欧式长度为 %.6f" % len_b)

norm_a=np.linalg.norm(a)
norm_b=np.linalg.norm(b)
print("norm(a)=%.6f"%norm_a)
print("norm(b)=%.6f"%norm_b)