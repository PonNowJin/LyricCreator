import os
import json

"""
load Sample_songs into json
"""
songs = os.listdir('Sample_songs')
songs.remove('.DS_Store')
song_dict = {}
for song in songs:
    with open(os.path.join('Sample_songs', song), 'r') as f:
        print(song)
        song_dict[song] = f.read()
        
print(song_dict)

"""
json_string = json.dumps(song_dict)
with open("Sample_songs.json", "w") as outfile:
    outfile.write(json_string)
"""

with open("Sample_songs.json", "w", encoding="utf-8") as outfile:
    json.dump(song_dict, outfile, ensure_ascii=False, indent=4)
