import numpy as np

def angle_deg(a,b):
    """计算两个向量的夹角"""
    norm_a=np.linalg.norm(a)
    norm_b=np.linalg.norm(b)
    #零向量判断
    if np.isclose(norm_a,0) or np.isclose(norm_b,0):
        raise ValueError("输入不能是零向量")
    cos_theta=(a@b)/(norm_a*norm_b)     #求余弦
    cos_theta=np.clip(cos_theta,-1,1)   #裁剪到[-1,1]范围
    theta_rad=np.arccos(cos_theta)      #反余弦函数求弧度
    theta_deg=np.degrees(theta_rad)     #弧度转角度
    return theta_deg

a = np.array([1.00, -1.00])
b = np.array([1.00, 0.00])
res=angle_deg(a,b)
print(f"a,b向量的夹角为{res:.4f}度")
#边界输入：angle_deg(np.array([0,0]), np.array([1,2]))会抛异常