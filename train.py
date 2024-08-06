import argparse
from graphlstm_vae_ad import GraphLSTM_VAE_AD
import pandas as pd
import numpy as np

parser = argparse.ArgumentParser(description="train")
parser.add_argument('-p', '--program', type=str, required=True, help='program')
parser.add_argument('-d', '--duration', type=str, required=True, help='duration')
parser.add_argument('-n', '--num', type=int, required=True, help='nodes num')

parser.add_argument('-g', '--gpu', type=int, default=0, help='gpu')
parser.add_argument('-s', '--seq', type=int, default=30, help='seq')
parser.add_argument('-l', '--lr', type=float, default=1e-3, help='lr')
parser.add_argument('-b', '--bsz', type=int, default=32, help='bsz')
parser.add_argument('-hd', '--hdim', type=int,default=8, help='hdim')
parser.add_argument('-e', '--epoch', type=int,default=1000, help='epoch')
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

print(process + "_" + duration
            + '_seq=' + str(args.seq)
            + '_lr=' + str(args.lr)
            + '_bsz=' + str(args.bsz)
            + '_hdim=' + str(args.hdim)
            + '_epoch=' + str(num_epochs))

# process = "lammps_48_normal"
# duration = "100ms_closed"
# node_num = 48
DATASET = "/root/MPI_profile/"+ process + "/" + duration + "/node_feature.csv"
TOPOLOGY = "/root/MPI_profile/"+ process + "/" + duration + "/graph_edge"

def edge_load(filename, len):
    edge_data = pd.read_csv(filename, header=0)
    edge_data = edge_data.groupby(['ts_id','src', 'dst']).agg({'commsize': 'sum'}).reset_index()
    edge_index_dict = {}
    edge_weight_dict = {}
    for ts_id, group in edge_data.groupby('ts_id'):
        edge_index = group[['src', 'dst']].values.T.tolist()  # Transpose to get shape (2, num_edges)
        edge_index_dict[ts_id] = edge_index

        edge_weight = group['commsize'].values.tolist()
        edge_weight_dict[ts_id] = edge_weight

    edge_index_list = []
    edge_weight_list = []
    for i in range(len):
        if i in edge_index_dict.keys():
            edge_index_list.append(edge_index_dict[i])
            edge_weight_list.append(edge_weight_dict[i])
        else:
            edge_index_list.append([[], []])
            edge_weight_list.append([])

    return edge_index_list, edge_weight_list


def data_load(filename): 
    data = pd.read_csv(filename, header=[0,1])
    data.columns.names = ['metric', 'host']
    tempm = data.stack()
    tempm = (tempm-tempm.mean())/(tempm.std())
    metric = tempm.unstack().swaplevel('metric','host',axis=1).stack().unstack()
    edge_index, edge_weight = edge_load(TOPOLOGY, len(metric))

    return metric, edge_index, edge_weight

print("loading data...")

metric, edge_index, edge_weight = data_load(DATASET)

model = GraphLSTM_VAE_AD(name=process + '_' + duration
                        + '_seq=' + str(args.seq)
                        + '_lr=' + str(args.lr)
                        + '_bsz=' + str(args.bsz)
                        + '_hdim=' + str(args.hdim)
                        + '_epoch=' + str(num_epochs) , 
                        kind='GCN', gpu=args.gpu,  sequence_length=args.seq, hidden_dim=args.hdim, batch_size=args.bsz, lr=args.lr, num_epochs=num_epochs)

print("training...")
model.fit(metric, node_num, edge_index, log_step=2, patience=20, step=10)

print("predicting...")
model.load(node_num, metric.shape[1])
scores_sum = []
scores_max = []
scores = []
outputs = []
scores, scores_sum, scores_max, outputs = model.predict(metric, node_num, edge_index, 1)

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


shuffle_scores = scores
shuffle_scores = shuffle_scores.T

plt.figure(figsize=(40, 10))

sns.heatmap(shuffle_scores, cmap='Blues', cbar=True)

plt.title('Heatmap of Scores', fontsize=12)
plt.xlabel('Trace Slices', fontsize=12)
plt.ylabel('Nodes', fontsize=12)

plt.savefig('/root/MPI_profile/train_log/' + process + "_" + duration
            + '_seq=' + str(args.seq)
            + '_lr=' + str(args.lr)
            + '_bsz=' + str(args.bsz)
            + '_hdim=' + str(args.hdim)
            + '_epoch=' + str(num_epochs) + '_score.png', bbox_inches='tight')
plt.show()



