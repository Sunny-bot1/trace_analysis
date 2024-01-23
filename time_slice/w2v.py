from gensim.models import Word2Vec
import pandas as pd

dimension = 64

data = pd.read_csv('is_feature_merge.csv')
sentences = data.reset_index(drop=False).apply(lambda row: row.tolist(), axis=1).tolist()
# print(sentences[0])

model = Word2Vec(sentences, vector_size=dimension, window=5, min_count=1, workers=4)
# print("word:",model.wv.index_to_key)

def get_vector(row):
    vectors = [model.wv[str(num)] for num in row if str(num) in model.wv]
    if vectors:
        return sum(vectors) / len(vectors)  
    else:
        return [0] * dimension  

data['feature_vector'] = data.apply(get_vector, axis=1)
data.to_csv('is_vector.csv', header=True, index=False)

# print(data['feature_vector'])