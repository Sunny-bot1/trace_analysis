import argparse
from graphlstm_vae_ad import GraphLSTM_VAE_AD
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

parser = argparse.ArgumentParser(description="train")
parser.add_argument('-p', '--program', type=str, required=True, help='program')
parser.add_argument('-d', '--duration', type=str, required=True, help='duration')
parser.add_argument('-n', '--num', type=int, required=True, help='nodes num')
parser.add_argument('-per', '--percent', type=float, default=0.5, help='percent')
parser.add_argument('-i', '--num_inter', type=int, default=2, help='num_inter')
parser.add_argument('-delay', '--delay', type=int,default=5, help='delay')

parser.add_argument('-g', '--gpu', type=int, default=0, help='gpu')
parser.add_argument('-s', '--seq', type=int, default=30, help='seq')
parser.add_argument('-l', '--lr', type=float, default=1e-3, help='lr')
parser.add_argument('-b', '--bsz', type=int, default=32, help='bsz')
parser.add_argument('-hd', '--hdim', type=int,default=8, help='hdim')
parser.add_argument('-e', '--epoch', type=int,default=200, help='epoch')
parser.add_argument('-mode', '--mode', type=int,default=0, help='mode')

args = parser.parse_args()

process = args.program
duration = args.duration
node_num = args.num

gpu = args.gpu
seq = args.seq
lr = args.lr
bsz = args.bsz
hdim = args.hdim
num_epochs=args.epoch

percent = args.percent
mode = args.mode
delay = args.delay

is_static = ""
if mode == 1:
    is_static = "_static"

print(process + "_" + duration
            + '_seq=' + str(args.seq)
            + '_lr=' + str(args.lr)
            + '_bsz=' + str(args.bsz)
            + '_hdim=' + str(args.hdim)
            + '_epoch=' + str(num_epochs))

print("loading scores...")
scores = np.load('./results/scores/' + process + "_" + duration+ is_static
            + '_delay=' + str(delay)
            + '_seq=' + str(args.seq)
            + '_lr=' + str(args.lr)
            + '_bsz=' + str(args.bsz)
            + '_hdim=' + str(args.hdim)
            + '_epoch=' + str(num_epochs) + '_score.npy')


print("caculating distribution..")
def generate_intervals(start, end, num_intervals):
    interval_width = (end - start) / (num_intervals) 
    
    intervals = []
    
    intervals.append((-np.inf, start))
    
    for i in range(num_intervals):
        interval_start = start + i * interval_width
        interval_end = interval_start + interval_width
        intervals.append((interval_start, interval_end))
    
    intervals.append((end, np.inf))
    
    return intervals

def count_elements_in_intervals(array, intervals):
    counts = []
    for interval in intervals:
        count = np.sum((array >= interval[0]) & (array < interval[1]))
        counts.append(count)
    return counts

array = scores
min_value = np.min(array)
max_value = np.max(array)
num_intervals = args.num_inter

mean = np.mean(array)
print("期望:", mean)

# 计算方差
variance = np.var(array)
print("方差:", variance)

std_dev = np.std(array)
print("标准差:", std_dev)

# 生成平均划分的区间，并包含开区间
intervals = generate_intervals(min_value, max_value, num_intervals)
counts = count_elements_in_intervals(array, intervals)

for interval, count in zip(intervals, counts):
    print(f"interval {interval}: {count} ")


from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch


print("printing heatmap after filtering...")
t0 = mean + 1 * std_dev
t1 = mean + 2 * std_dev
t2 = mean + 3 * std_dev
array = array.T

# indices = []  
# for i, row in enumerate(array):  # enumerate函数用于获取索引和值  
#     for j, value in enumerate(row):  
#         if value > t2:  
#             indices.append((i, j))  
# # print(indices)

# filename = './results/indices/lammps_1024_abnormal_inject_indices.txt'  
  
# # 使用with语句打开文件，确保文件正确关闭  
# with open(filename, 'w') as file:  
#     # 遍历indices列表  
#     for index in indices:  
#         file.write(f'{index[0]} {index[1]}\n')  

# 定义区间
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib.patches import Patch, Circle, Rectangle

# 假设你已经计算了mean, std_dev, array
# 并且将array转置了: array = array.T

# 定义区间
def categorize(value):
    if value <= t0:
        return 0  # 白色
    elif t0 < value <= t1:
        return 1  # 浅灰色
    elif t1 < value <= t2:
        return 2  # 浅蓝色
    else:
        return 3  # 红色

# 应用区间分类
categorized_arr = np.vectorize(categorize)(array)

# 定义自定义颜色映射
# colors = ["white", "lightgrey", "lightblue", "red"]

mycolors='Paired'
colors_map = plt.get_cmap(mycolors)(range(20))

colors = ["white", "lightblue", colors_map[6], colors_map[5]]

cmap = ListedColormap(colors)
# 绘制热力图
plt.figure(figsize=(10, 4))
sns.heatmap(categorized_arr, cmap=cmap, cbar=False)

# 在红色点上绘制红圈
ax = plt.gca()

# for i in range(categorized_arr.shape[0]):
#     for j in range(categorized_arr.shape[1]):
#         if categorized_arr[i, j] == 1:  # 分类为蓝色的点
#             circle = Circle((j + 0.5, i + 0.5), radius=0.5, edgecolor=colors[1], facecolor=colors[1], linewidth=2)
#             ax.add_patch(circle)


for i in range(categorized_arr.shape[0]):
    for j in range(categorized_arr.shape[1]):
        if categorized_arr[i, j] == 2:  # 分类为橙色的点
            rect = Rectangle((j - 0.25, i), 1.5, 1, edgecolor=colors[2], facecolor=colors[2])
            ax.add_patch(rect)


for i in range(categorized_arr.shape[0]):
    for j in range(categorized_arr.shape[1]):
        if categorized_arr[i, j] == 3:  # 分类为红色的点
            # 绘制红圈，半径和线宽可以根据需要调整
            rect = Rectangle((j - 0.25, i), 1.5, 1, edgecolor=colors[3], facecolor=colors[3])
            ax.add_patch(rect)        

# (-\infty, \mu+\sigma], (\mu+\sigma,\mu+2\sigma], (\mu+2\sigma, \mu+3\sigma], (\mu+3\sigma, \infty)

# # 添加图例
# legend_elements = [Patch(facecolor='white', edgecolor='black', label='<= t0'),
#                    Patch(facecolor='lightblue', edgecolor='black', label='t0 < x <= t1'),
#                    Patch(facecolor=colors[6], edgecolor=colors[6], label='t1 < x <= t2'),
#                    Patch(facecolor=colors[5], edgecolor=colors[5], label='> t2', linewidth=2)]

legend_elements = [
    Patch(facecolor='white', edgecolor='black', label=r'$(-\infty, \mu+\sigma]$'),
    Patch(facecolor='lightblue', edgecolor='black', label=r'$(\mu+\sigma,\mu+2\sigma]$'),
    Patch(facecolor=colors[2], edgecolor='black', label=r'$(\mu+2\sigma, \mu+3\sigma]$'),
    Patch(facecolor=colors[3], edgecolor='black', label=r'$(\mu+3\sigma, +\infty)$', linewidth=2)
]

plt.legend(handles=legend_elements, bbox_to_anchor=(0.5, -0.20), loc='upper center', ncol=4, frameon=False, fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.yticks(rotation=0)
# 设置标题和标签
# plt.title('Heatmap of Scores', fontsize=12)
plt.xlabel('Trace Slices', fontsize=12)
plt.ylabel('Nodes', fontsize=12)

# 保存图像
plt.savefig('./results/heatmaps_filter/' + process + "_" + duration + is_static
            + '_delay=' + str(delay)
            + '_seq=' + str(args.seq)
            + '_lr=' + str(args.lr)
            + '_bsz=' + str(args.bsz)
            + '_hdim=' + str(args.hdim)
            + '_epoch=' + str(num_epochs) + '_interval_score.png', bbox_inches='tight')

# 显示图像
plt.show()



