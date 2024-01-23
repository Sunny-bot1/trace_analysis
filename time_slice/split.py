import pandas as pd

df = pd.read_csv('is_feature.csv')

duration = 10000
interval = 10000

def split_time_interval(start_time, end_time, interval):

    current_time = start_time
    time_interval = []

    while current_time < end_time:
        time_interval.append(current_time)
        current_time += interval

    return time_interval

start = df.iloc[0]['ts']
end = df.iloc[-1]['ts']
time_interval = split_time_interval(start, end, interval)

# print(time_interval)

# result = []

df = df.fillna(0)

for start_time in time_interval:
    result = []
    for index, row in df.iterrows():
        time_s = row['ts']
        time_e = row['ts'] + row['dur']
    
        if (time_s >= start_time and time_s < start_time + duration) or (time_e >= start_time and time_e < start_time + duration) or (time_s < start_time and time_e >= start_time + duration):
            result.append(dict(row))
    
    result.append({col: '' for col in df.columns})

    #merge by tid
    result_df = pd.DataFrame(result)
    merged_df = result_df.groupby('tid').agg(lambda x: ','.join(x.astype(str))).reset_index()
    merged_df.to_csv('is_feature_slice.csv', mode='a', header=False, index=False)



# result_df = pd.DataFrame(result)
# result_df.to_csv('output.csv', index=False)
