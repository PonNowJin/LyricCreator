import os
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity
import torch
import numpy as np
from tqdm import tqdm 

DIR_PATH = 'SongAnalysis_m'
# DIR_PATH = 'Sample_songs'

# 抓出歌詞資料（歌名:歌詞）
def load_lyrics(dir) -> dict:
    lyrics = {}
    file_name = os.listdir(dir)
    try:
        file_name.remove('.DS_Store')
    except:
        pass
    for name in file_name:
        with open(os.path.join(dir, name), 'r') as f:
            lyrics[name] = f.read()
    return lyrics


# 使用pretrained embedding model
# 把歌詞做embedding
# model_name = 'sentence-transformers/all-MiniLM-L6-v2'
# model_name = 'sentence-transformers/paraphrase-mpnet-base-v2'

def embed_lyrics(lyrics):
    model_name = 'intfloat/multilingual-e5-large'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    inputs = tokenizer(lyrics, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        embeddings = model(**inputs).last_hidden_state.mean(dim=1)
    return embeddings
    

# 存embedding後的向量
def save_embeddings(embeddings, file_path):
    np.save(file_path, embeddings)
    

# 找最接近的10首歌
def find_similar_songs(input_lyric, embeddings_file, top_n=10):
    embeddings = np.load(embeddings_file, allow_pickle=True).item()
    input_embedding = embed_lyrics(input_lyric).numpy()
    similarities = {}
    for song, embedding in embeddings.items():
        similarity = cosine_similarity(input_embedding, embedding)
        similarities[song] = similarity
    sorted_songs = sorted(similarities.items(), key=lambda item: item[1], reverse=True)
    return sorted_songs[:top_n]


if __name__ == '__main__':
    lyrics_data = load_lyrics(DIR_PATH)
    print('Load Data Successfully')
    embeddings = {}
    for song, lyric in tqdm(lyrics_data.items(), desc="Embedding Lyrics", unit="song"):
        embeddings[song] = embed_lyrics(lyric).numpy()
        
    # save_embeddings(embeddings, 'Analysis_embeddings.npy')
    save_embeddings(embeddings, 'Multilingual-E5-large.npy')
    