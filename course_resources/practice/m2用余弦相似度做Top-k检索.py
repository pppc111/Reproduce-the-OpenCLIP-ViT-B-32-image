import numpy as np
def top_k_cosine(query,gallery,k):
    """检索相似度最高的前k个的下标和具体数值及对应ID"""
    norm_q=np.linalg.norm(query)
    if np.isclose(norm_q,0):
        raise ValueError("query不能为零向量")
    norm_g=np.linalg.norm(gallery,axis=1) #列数，每行向量模长
    dot=gallery@query
    cos_sim=dot/(norm_q*norm_g) #求相似度

    mask_zero=np.isclose(norm_g,0)  #掩码标记零向量
    cos_sim[mask_zero]=-np.inf      #零向量对应角度改成-np.inf(负无穷)，排序永远排在最末尾，不会选中
    valid_num=np.sum(~mask_zero)    #~按位取反，把不为0的相加
    if k<=0 or k>valid_num:
        raise ValueError("k必须是正整数，且不超过有效样本数")
    #稳定排序，从小到大，取最后k个相似度最高的
    idx_sorted=np.argsort(cos_sim,kind="stable")    #返回排序之后的下标索引，稳定排序
    topk_idx=idx_sorted[-k:]
    topk_idx=topk_idx[::-1]  #翻转，相似度由高到低
    topk_sim=cos_sim[topk_idx]
    return topk_idx,topk_sim

query = np.array([0.60, -0.80, 0.00])
gallery = np.array([[0.60, -0.80, 0.00],
                    [0.30, -0.40, 0.00],
                    [0.80, 0.60, 0.00],
                    [-0.60, 0.80, 0.00],
                    [0.00, 0.00, 0.00]])
ids = np.array(["img_a", "img_b", "img_c", "img_d", "img_zero"])
k=3
top_idx,top_sim=top_k_cosine(query,gallery,k)
print("top-k索引：",top_idx)
print("top-k相似度：",top_sim)
print("选中ID：",ids[top_idx])

#边界输入：k=0，k=有效样本数，query零向量