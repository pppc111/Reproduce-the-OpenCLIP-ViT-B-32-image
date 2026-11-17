import numpy as np
def angles_to(query,X):
    """批量计算夹角"""
    norm_q=np.linalg.norm(query)
    if np.isclose(norm_q,0):
        raise ValueError("query不能为零向量")
    norm_X=np.linalg.norm(X,axis=1) #列数，每行向量模长
    dot=X@query
    cos_theta=dot/(norm_q*norm_X)
    cos_theta=np.clip(cos_theta,-1,1)
    theta_rad=np.arccos(cos_theta)
    theta_deg=np.degrees(theta_rad)
    mask_zero=np.isclose(norm_X,0)  #掩码标记零向量
    theta_deg[mask_zero]=np.nan     #零向量对应角度改成np.nan(Not a Number)
    return theta_deg

query = np.array([0.60, -0.80, 0.00])
X = np.array([[0.30, -0.40, 0.00],
              [-0.60, 0.80, 0.00],
              [0.80, 0.60, 0.00],
              [0.00, 0.00, 0.00]])
angles=angles_to(query,X)
print("angles:",angles)
print("angles.shape:",angles.shape)

#输入边界：query为零向量，X里有零向量