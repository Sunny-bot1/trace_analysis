import json
import csv
import sys
import pandas as pd

arguments = sys.argv[1:]

inputfile = '/home/sx/NPB3.4.2/NPB3.4-MPI/bin/MPI_profile/' + arguments[0] + '/graph'
outputfile = 'data/edge/' + arguments[0] + '_edge.csv'

egde_fieldnames = ['name', 'cat', 'ph', 'ts', 'pid', 'tid']

#将JSON文件整理成dataframe格式
with open(inputfile, 'r') as file:
    data = json.load(file)

edge = []
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
        edge.append(row)



#开始切片
df = pd.DataFrame(edge)
df.to_csv(outputfile, mode='a', header=True, index=False)


# duration = 10000
# interval = 10000

# #获取interval开始时间列表
# def split_time_interval(start_time, end_time, interval):

#     current_time = start_time
#     time_interval = []

#     while current_time < end_time:
#         time_interval.append(current_time)
#         current_time += interval

#     return time_interval

# start = df.iloc[0]['ts']
# end = df.iloc[-1]['ts']

# #获取interval开始时间列表
# time_interval = split_time_interval(start, end, interval)

# df = df.fillna(0)

# #遍历每个interval
# for start_time in time_interval:
#     result = []
#     for index, row in df.iterrows():
#         time_s = row['ts']
#         time_e = row['ts'] + row['dur']
#         #事件按照时间筛选:三种情况
#         #开始时间在[start_time,start_time+duration]
#         #结束时间在[start_time,start_time+duration]
#         #开始时间<start_time且结束时间>start_time+duration
#         if (time_s >= start_time and time_s < start_time + duration) or (time_e >= start_time and time_e < start_time + duration) or (time_s < start_time and time_e >= start_time + duration):
#             result.append(dict(row))
    
#     result.append({col: '' for col in df.columns})

#     #merge by tid
#     result_df = pd.DataFrame(result)
#     merged_df = result_df.groupby('tid').agg(lambda x: ','.join(x.astype(str))).reset_index()
#     merged_df.to_csv(outputfile, mode='a', header=False, index=False)
