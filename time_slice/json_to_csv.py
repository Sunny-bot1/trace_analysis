import json
import csv

fieldnames = ['name', 'cat', 'ph', 'ts', 'dur', 'pid', 'tid', 'args_Data_type', 'args_Dest', 'args_Tag', 'args_Count',
            'args_Comm', 'args_Request', 'args_Op', 'args_Root', 'args_Backtrace']

egde_fieldnames = ['name', 'cat', 'ph', 'ts', 'pid', 'tid']


with open('data/is.B.x/graph1', 'r') as file:
    data = json.load(file)
# print(data['traceEvents'])

featrue_file_path = 'is_feature.csv'
edge_file_path = 'is_edge.csv'

with open(featrue_file_path, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in data['traceEvents']:
        if item['name'] == 'dep_flow_':
            break
        if 'dur' not in item:
            item['dur'] = None
        if 'args' not in item:
            item['args'] = {}
        # print(item)
        if 'Data type' not in item['args']:
            item['args']['Data type'] = None
        if 'Dest' not in item['args']:
            item['args']['Dest'] = None
        if 'Tag' not in item['args']:
            item['args']['Tag'] = None
        if 'Count' not in item['args']:
            item['args']['Count'] = None
        if 'Comm' not in item['args']:
            item['args']['Comm'] = None
        if 'Request' not in item['args']:
            item['args']['Request'] = None
        if 'Op' not in item['args']:
            item['args']['Op'] = None
        if 'Root' not in item['args']:
            item['args']['Root'] = None
        if 'Backtrace' not in item['args']:
            item['args']['Backtrace'] = None
        # print(item)
        row = {
            'name': item['name'],
            'cat': item['cat'],
            'ph': item['ph'],
            'ts': item['ts'],
            'dur': item['dur'],
            'pid': item['pid'],
            'tid': item['tid'],
            'args_Data_type': item['args']['Data type'],
            'args_Dest': item['args']['Dest'],
            'args_Tag': item['args']['Tag'],
            'args_Count': item['args']['Count'],
            'args_Comm': item['args']['Comm'],
            'args_Request': item['args']['Request'],
            'args_Op': item['args']['Op'],
            'args_Root': item['args']['Root'],
            'args_Backtrace': item['args']['Backtrace']
        }
        # print(row)
        writer.writerow(row)


with open(edge_file_path, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=egde_fieldnames)
    writer.writeheader()
    for item in data['traceEvents']:
        if item['name'] == 'dep_flow_':
            row = {
                'name': item['name'],
                'cat': item['cat'],
                'ph': item['ph'],
                'ts': item['ts'],
                'pid': item['pid'],
                'tid': item['tid'],
            }
            # print(row)
            writer.writerow(row)