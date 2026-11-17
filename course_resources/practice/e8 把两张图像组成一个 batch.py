import numpy as np
#图像格式：(C,H,W)，batch批次[样本集]
a = np.array([[[0.20, -0.40], [0.70, 0.10]],
              [[0.30, 0.80], [-0.20, 0.50]],
              [[-0.10, 0.60], [0.40, -0.30]]])
b = a + 0.10

batch=np.stack([a,b],axis=0)    #stack在第0维拼接,表示图像编号
print("batch=",batch)
print("batch.shape=",batch.shape)   #(B,C,H,W)

blue_channel=batch[:,2,:,:] #C=2,第3行，即一张图里第3个数组
print("蓝色通道=",blue_channel)
print("蓝色通道shape=",blue_channel.shape)

batch_hwc=np.transpose(batch,(0,2,3,1)) #(B,C,H,W)到(B,H,W,C)换序
print("转为(B,H,W,C)后的batch=",batch_hwc)
print("转为(B,H,W,C)后的batch.shape=",batch_hwc.shape)