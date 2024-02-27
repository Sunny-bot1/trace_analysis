from gensim.models import Word2Vec
import pandas as pd
import os

dimension = 64

def process_csv(file_path):

    data = pd.read_csv(file_path, header=None)
    sentences = data.reset_index(drop=False).apply(lambda row: row.tolist(), axis=1).tolist()

    model = Word2Vec(sentences, vector_size=dimension, window=5, min_count=1, workers=4)

    def get_vector(row):
        vectors = [model.wv[str(num)] for num in row if str(num) in model.wv]
        if vectors:
            return sum(vectors) / len(vectors)  
        # else:
        #     return [0] * dimension  

    new_data = pd.DataFrame({'ts': None, 'id': data.iloc[:, 0], 'feature_vector': data.apply(get_vector, axis=1)})

    time_step = 0

    for index, row in new_data.iterrows():
        if row.isnull().all():
            time_step += 1
        else:
            new_data.at[index, 'ts'] = time_step

    new_data.dropna(axis=0, how='any', inplace=True)

    print(time_step)
    new_data.to_csv(os.path.join('output/feature_vector', file_name), header=True, index=False)


for file_name in os.listdir('data'):
    if file_name.endswith('.csv'):
        process_csv(os.path.join('data', file_name))