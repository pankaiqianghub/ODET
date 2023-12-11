import numpy as np

# 设置随机种子以确保结果可复现
np.random.seed(0)

# 首先，我们定义三个关键点的位置和值
key_points = [(0, 1.01), (12, 0.97), (36, 0.93), (49, 0.83)]

# 根据这三个关键点，我们生成三段数值
values = []

# 第一部分：从1.01下降到0.97，下降速度越来越慢
for i in range(13):
    t = i / 12  # 当前步骤的归一化时间（0到1）
    weight = 1 - (t ** 2)  # 调整权重，让下降速度逐渐减慢
    value = key_points[0][1] - (key_points[0][1] - key_points[1][1]) * weight
    values.append(value)

# 第二部分：从0.97缓慢下降到0.93
values.extend(np.linspace(0.97, 0.93, 24))

# 第三部分：从0.93下降到0.83，下降速度越来越快
for i in range(13):
    t = i / 12  # 当前步骤的归一化时间（0到1）
    weight = t ** 2  # 调整权重，让下降速度逐渐加快
    value = key_points[2][1] - (key_points[2][1] - key_points[3][1]) * weight
    values.append(value)

print(values)
value = [1.01, 0.9951, 0.9911, 0.9873, 0.9844, 0.9814, 0.98, 0.9778, 0.9761, 0.9748, 0.9733,
         0.9715, 0.9705, 0.97, 0.9682608695652174, 0.9665217391304347, 0.9647826086956521, 0.9630434782608696, 0.961304347826087, 0.9595652173913043, 0.9578260869565217, 0.9560869565217391, 0.9543478260869566, 0.9526086956521739, 0.9508695652173913, 0.9491304347826087, 0.9473913043478261, 0.9456521739130435, 0.9439130434782609, 0.9421739130434783, 0.9404347826086957, 0.938695652173913, 0.9369565217391305, 0.9352173913043479, 0.9334782608695653, 0.9317391304347826, 0.93, 0.93, 0.9293055555555556, 0.9272222222222223, 0.9237500000000001, 0.918888888888889, 0.9126388888888889, 0.905, 0.8959722222222223, 0.8855555555555555, 0.87375, 0.8605555555555555, 0.8459722222222222, 0.83]