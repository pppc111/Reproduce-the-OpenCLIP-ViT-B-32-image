import numpy as np

def unit_vector(a):
    """把向量变成单位长度"""
    norm_a=np.linalg.norm(a)
    if np.isclose(norm_a,0):
        raise ValueError("不能对零向量归一化")
    return a/norm_a

a = np.array([-1.20, 0.40, 0.80])
u=unit_vector(a)
print("a.shape=",a.shape)
print("单位向量u=",u)
print("u.shape=",u.shape)
print(f"u的长度={np.linalg.norm(u):.2f}")
print("长度是否为1：",np.allclose(np.linalg.norm(u),1.0))
#边界输入：a=np.array([0,0,0]零向量异常