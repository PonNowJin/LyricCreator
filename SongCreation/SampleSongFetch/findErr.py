import os
from Toolkit import *

#####################
#用於找出沒有分析成功的歌曲
#####################

"""
success = os.listdir('SongAnalysis_m')
all = os.listdir('Sample_songs')
all_name = []
for a in all:
    a = a[0:-4]
    all_name.append(a)

success_set = set(success)
all_name_set = set(all_name)

fall_set = all_name_set - success_set
print(fall_set)
print(len(fall_set))

result_string = "\n".join([item for item in fall_set])
save_to_file('FailSongs.txt', result_string)
"""


###################
# 用於標記歌名到分析中
###################

names = os.listdir('SongAnalysis_m')
for name in names:
    with open(os.path.join('SongAnalysis_m', name), 'a') as f:
        f.write('\r'+name)

