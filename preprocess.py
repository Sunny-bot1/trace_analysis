import json
import pandas as pd
import itertools
from gensim.models import Word2Vec
import argparse

parser = argparse.ArgumentParser(description="preprocess...")
parser.add_argument('-p', '--program', type=str, required=True, help='program')
parser.add_argument('-d', '--duration', type=str, required=True, help='duration')
parser.add_argument('-n', '--num', type=int, required=True, help='nodes num')

args = parser.parse_args()

program = args.program
duration = args.duration
num = args.num
dimension = 32

trace_file = "/root/MPI_profile/"+ program + "/" + duration + "/graph"
feature_merged_file ="/root/MPI_profile/"+ program + "/" + duration + "/graph_feature_merged.csv"

vec_input_path = "/root/MPI_profile/"+ program + "/" + duration + "/graph_feature_merged.csv"
vec_output_path = "/root/MPI_profile/"+ program + "/" + duration + "/node_feature.csv"

fieldnames = ['ts_id', 'tid', 'name', 'ts', 'dur', 'args_Data_type', 'args_Dest', 'args_Tag', 'args_Count',
            'args_Send_Count', 'args_Recv_Count', 'args_Comm', 'args_Request', 'args_Op', 'args_Root'
            , 'arg_pmu_0', 'arg_pmu_1', 'arg_pmu_2', 'arg_pmu_3']


print("load graph ...")

with open(trace_file, 'r') as file:
    trace_data = json.load(file)



feature = []
for item in trace_data['traceEvents']:
    if item['name'] == 'dep_flow_':
        break
    if 'dur' not in item:
        item['dur'] = 0
    if 'args' not in item:
        item['args'] = {}
    # print(item)
    if 'Data type' not in item['args']:
        item['args']['Data type'] = 0
    if 'Dest' not in item['args']:
        item['args']['Dest'] = 0
    if 'Tag' not in item['args']:
        item['args']['Tag'] = 0
    if 'Count' not in item['args']:
        item['args']['Count'] = 0
    if 'Comm' not in item['args']:
        item['args']['Comm'] = 0
    if 'Request' not in item['args']:
        item['args']['Request'] = 0
    if 'Op' not in item['args']:
        item['args']['Op'] = 0
    if 'Root' not in item['args']:
        item['args']['Root'] = 0
    if 'Backtrace' not in item['args']:
        item['args']['Backtrace'] = 0
    if 'Send Count' not in item['args']:
        item['args']['Send Count'] = 0
    if 'Recv Count' not in item['args']:
        item['args']['Recv Count'] = 0
    # print(item)
    row = {
        'ts_id': item['ts_id'],
        'tid': item['tid'],
        'name': item['name'],
        # 'cat': item['cat'],
        # 'ph': item['ph'],
        'ts': item['ts'],
        'dur': item['dur'],
        'args_Data_type': item['args']['Data type'],
        'args_Dest': item['args']['Dest'],
        'args_Tag': item['args']['Tag'],
        'args_Count': item['args']['Count'],
        'args_Send_Count': item['args']['Send Count'],
        'args_Recv_Count': item['args']['Recv Count'],
        'args_Comm': item['args']['Comm'],
        'args_Request': item['args']['Request'],
        'args_Op': item['args']['Op'],
        'args_Root': item['args']['Root'],
        # 'args_Backtrace': item['args']['Backtrace'],
        'arg_pmu_0': item['args']['PMU 0(PAPI_LD_INS) count'],
        'arg_pmu_1': item['args']['PMU 1(PAPI_L2_ICR) count'],
        'arg_pmu_2': item['args']['PMU 2(PAPI_BR_PRC) count'],
        'arg_pmu_3': item['args']['PMU 3(PAPI_L2_TCR) count'],
    }
    feature.append(row)
    # print(row)
    # writer.writerow(row)

print("merge events ...")

df_feature = pd.DataFrame(feature)
df_feature_merged = df_feature.groupby(['ts_id', 'tid']).agg(lambda x: ','.join(x.astype(str))).reset_index()

# print(df_feature_merged)
df_feature_merged.to_csv(feature_merged_file, header=True, index=False)

print("vectorizeing ...")

data = pd.read_csv(vec_input_path, header=0)
print(len(data))
# data = data.iloc[140:268973]
# print(len(data))



sentences = data.reset_index(drop=False).apply(lambda row: row.tolist(), axis=1).tolist()
model = Word2Vec(sentences, vector_size=dimension, window=5, min_count=1, workers=4)

def get_vector(row):
    vectors = [model.wv[str(num)] for num in row if str(num) in model.wv]
    if vectors:
        return sum(vectors) / len(vectors)  
    # else:
    #     return [0] * dimension  

vectors = [get_vector(row) for row in sentences]

df_vectors = pd.DataFrame(vectors, columns=[f'vector_{i}' for i in range(dimension)])
df_vectors = pd.concat([data.iloc[:, 0], data.iloc[:, 1], df_vectors], axis=1)

# print(df_vectors)

def filter_tid(group, tid):
    filtered = group[group['tid'] == tid]
    if filtered.empty:
        filtered = pd.DataFrame({'ts_id': group.name, 'tid': [tid]})
        for i in range(32):
           filtered[f'vector_{i}'] = [0]
    return filtered

results = []
for tid in range(num):
    df_vectors_i = df_vectors.groupby('ts_id').apply(filter_tid, tid)
    df_vectors_i = df_vectors_i.reset_index(drop=True)
    results.append(df_vectors_i.iloc[:, 2:])
    df_combined = pd.concat(results, axis=1)
    df_combined = df_combined.reset_index(drop=True)


# print(df_combined)

nodes = [f'node_{i}' for i in range(num)]
vectors = [f'vector_{i}' for i in range(dimension)]

repeated_nodes = list(itertools.repeat(node, dimension) for node in nodes)
repeated_vectors = list(itertools.repeat(vectors, num))

nodes = [item for sublist in repeated_nodes for item in sublist]
vectors = [item for sublist in repeated_vectors for item in sublist]

df_metric = pd.DataFrame(data=[nodes], columns=vectors)
# print(df_metric)

df_result = pd.concat([df_metric, df_combined], ignore_index=True)

# print(df_result)
df_result.to_csv(vec_output_path, header=True, index=False)


