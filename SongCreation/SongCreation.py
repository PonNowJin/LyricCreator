import os
import json
import sys
from dotenv import load_dotenv
load_dotenv()

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
print('ROOT_DIR: ', ROOT_DIR)
sys.path.append(ROOT_DIR)
sys.path.append(os.path.join(ROOT_DIR, 'SongCreation'))

from Evaluation import Evaluation
from LyricsCreator import LyricsCreator_llm
from google.generativeai.types.generation_types import StopCandidateException
from Prompt_optimize import Prompt_OPT
# from Suno_api_3 import *        # 使用Suno_api_3
from SampleSongFetch.Lyrics_embedding import find_similar_songs
from Gemini_image_model_1 import send_message_with_image
from pathlib import Path
import warnings 
warnings.filterwarnings('ignore')

def SongCreation(topic:str='', CREATE_SONG=1, image:str=None, music_style:str=None, preprocessed:bool=False, CREATE_VIDEO:bool=False) -> bool:
    '''
    topic: 歌曲提示詞
    CREATE_SONG: 是否傳入suno api創造並存檔
    image: 圖片path
    music_style: 已指定的風格字串
    preprocessed: 是否已經經過預處理
    CREATE_VIDEO: 是否要生成影片
    '''
    try:
        os.chdir(ROOT_DIR)
        current_directory = Path.cwd()
        print("Current working directory:", current_directory)
        
        
        OUTPUT_DIR = os.path.join(ROOT_DIR, 'outputs')
        file_path = OUTPUT_DIR+'/lyrics.txt'
        print(file_path, flush=True)
        # 如果資料夾不存在，創建它
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

        # 如果檔案不存在，創建它
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as f:
                pass

        lyricsCreator_llm = LyricsCreator_llm()
        evaluation_llm = Evaluation()
        prompt_opt = Prompt_OPT()

        # LLM分析topic撰寫prompt
        # topic = """"""

        """
        with open('Story.txt', 'r') as f:
            topic = f.read()
        """

        if not image and not preprocessed:        
            if len(topic) <= 7:
                print('topic: ', topic)
                prompt_opt.setInputPrompt(topic)
                topic = prompt_opt.sendMsg()
                
        elif preprocessed:
            print('topic: ', topic)
        else:
            topic = str(send_message_with_image(image_path=image, text=topic))
            print(topic)

        # 找最相近n首歌做參考
        # sample_song = find_similar_songs(topic, 'SampleSongData/Analysis_embeddings.npy', 6)
        # sample_song = find_similar_songs(topic, 'SampleSongData/lyrics_embeddings.npy', 6)
        # sample_song = find_similar_songs(topic, 'SampleSongData/Songs_Multilingual-E5-large.npy')
        sample_song = find_similar_songs(topic, 'SampleSongData/Multilingual-E5-large.npy', 10) # good!
        selected_songs = [song[0] for song in sample_song]
        print(selected_songs)
        with open('SampleSongData/Sample_songs.json') as f:
            song_data = json.load(f)

        songs_str = '參考歌曲：\n'
        for selected in selected_songs:
            songs_str += f"歌名：{selected}\n{song_data[selected+'.txt']}\n\n"
            
        # print(songs_str)
        topic += '，先去思考參考歌曲的意境、想法，再去臨摹歌曲的筆法、敘事角度、歌詞長短，創造出一首新穎的歌曲'     


        lyricsCreator_llm.setInputPrompt(topic)
        lyricsCreator_llm.setRhyme([])
        evaluation_llm.setTopic(topic)

        evaluation = None
        # 做第一次歌詞、曲風生成
        try:
            lyricsCreator_llm.sendMsg(output_dir=OUTPUT_DIR, music_style=music_style)
            evaluation = evaluation_llm.evaluation(output_dir=OUTPUT_DIR)  # evaluation為評分和建議的text
            print(evaluation_llm.getScore())
        except StopCandidateException as e:
            print(f"安全政策異常:")

        # 做prompt的變異
        count = 0
        while evaluation_llm.score < 90:
            try:
                lyricsCreator_llm.sendMsg(output_dir=OUTPUT_DIR, evaluation=evaluation, music_style=music_style)
                evaluation = evaluation_llm.evaluation(output_dir=OUTPUT_DIR)
                print(evaluation_llm.getScore())
                count += 1
                # print(evaluation)
                if count >= 6 and evaluation_llm.getScore() >= 87: # 準備輸出mp3
                    break
            except StopCandidateException as e:
                print(f"安全政策異常:")
                continue
            except Exception as e:
                print(f"出現錯誤")
                continue
            
        '''
        if CREATE_SONG:
            print("創建歌曲...")
            create_and_download_songs()
            print("歌曲存檔完成")
            
        if CREATE_VIDEO:
            print("生成影片...")
            # video_create_func()...
            print("影片生成完成")
        '''
            
        return True
    
    except Exception as e:
        print('err from SongCreation.py: ', e)
        return False
        


if __name__ == '__main__':
    topic = 'title: 調查局'
    SongCreation(topic, CREATE_SONG=0, image=None, music_style=None, preprocessed=True)

