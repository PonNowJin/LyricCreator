from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json
from Lyrics_embedding import *

def find_similar_songs(input_lyric, embeddings, top_n=10):
    input_embedding = embed_lyrics(input_lyric).numpy()
    similarities = {}
    for song, embedding in embeddings.items():
        similarity = cosine_similarity(input_embedding, embedding)
        similarities[song] = similarity
    sorted_songs = sorted(similarities.items(), key=lambda item: item[1], reverse=True)
    return sorted_songs[:top_n]

# Load embeddings
embeddings = np.load('Analysis_embeddings.npy', allow_pickle=True).item()

input_lyric = "小小胖腦"
similar_songs = find_similar_songs(input_lyric, embeddings)
print(similar_songs)

