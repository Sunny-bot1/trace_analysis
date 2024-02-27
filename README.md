# trace_analysis
大规模性能轨迹分析
## time_slice
时间片划分

```shell
# 处理进程（节点）特征，进行时间片划分与特征合并
# 参数：程序名称
# 输出路径：data/feature
python3 feature_time_split.py is.B.x

# 对data/feature中的数据进行向量化
# 输出路径：output/feature_vector
python3 w2v.py

# 处理边
# 参数：程序名称
# 输出路径：data/edge
python3 edge_time_split.py is.B.x
```