import os
##########################
#清除歌詞為空的歌曲
##########################

songs = os.listdir('Sample_songs')
for song in songs:
    with open('Sample_songs/'+song, 'r', encoding='utf-8') as f:
        lyrics = f.read()
    if lyrics == 'None':
        print('Sample_songs/',song,'為空，清除')
        # os.remove('Sample_songs/'+song)
        