# trace_analysis

大规模MPI性能轨迹分析

## Requirements

```
Python              3.8.19
cuda                11.8
gensim              4.3.3
numpy               1.24.1
pandas              2.0.3
torch               2.1.0+cu118
torch_geometric     2.5.3
```
## Time Slice Generate

安装 [JSI_Toolkit:sx/timeslice](https://github.com/buaa-hipo/JSI-Toolkit/tree/sx/timeslice)

使用方法参考脚本 [generate_graph](./scripts/generate_graph.sh)

生成数据类似

```
MPI_profile
└── lammps_128_abnormal   程序名
    └── 100ms_closed      duration
        ├── graph         节点信息
        └── graph_edge    边信息

```

## Preprocess

```
python preprocess.py -p lammps_128_abnormal -d 100ms_closed -n 128
```

执行后生成向量化后的节点信息 node_feature.csv

```
MPI_profile
└── lammps_128_abnormal         程序名
    └── 100ms_closed            duration
        ├── graph               节点信息
        ├── graph_edge          边信息
        └── node_feature.csv    向量化后的节点信息

```

输入路径写死在preprocess.py里，记得修改

参数含义详见 preprocess.py

## Train

```
python train.py -p lammps_128_abnormal -d 100ms_closed -n 128 -b 128
```

训练好的模型会存在[checkpoints](./checkpoints/)里

输入路径写死在 train.py 里，记得修改

参数含义详见 train.py

## Predict

```
python predict.py -p lammps_128_normal -d 100ms_closed -n 128 -b 128
```

计算出的异常分数存在[./results/scores/](./results/scores/)

原始热力图存在[./results/heatmaps/](./results/heatmaps/)

输入路径写死在 predict.py 里，记得修改

参数含义详见 predict.py

## Analyze

```
python analyze.py -p lammps_128_normal -d 100ms_closed -n 128 -b 128
```

按照阈值过滤后的异常分数存在[./results/heatmaps_filter/](./results/heatmaps_filter/)

参数含义详见 analyze.py