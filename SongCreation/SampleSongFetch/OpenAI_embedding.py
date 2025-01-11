import openai
from openai import OpenAI
import json
import numpy as np
from tqdm import tqdm
from Lyrics_embedding import load_lyrics


def embed_lyrics_with_openai(lyrics):
    response = openai.Embedding.create(
        input=lyrics,
        model='text-embedding-3-small'
    )
    embedding = response['data'][0]['embedding']
    return embedding

client = OpenAI()
def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

# 假设 lyrics_data 是一个包含歌曲名和歌词的字典
with open('Sample_songs.json') as f:
    lyrics_data = json.load(f)
embeddings = {}
for song, lyric in tqdm(lyrics_data.items(), desc="Embedding lyrics"):
    embeddings[song] = get_embedding(lyric)

# 保存嵌入到文件中
np.save('lyrics_embeddings_openai.npy', embeddings)
