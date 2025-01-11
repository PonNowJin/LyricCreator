import requests
from bs4 import BeautifulSoup
import re

songs = {}
song_url_basic = 'https://www.kkbox.com/tw/tc/song/'

def remove_tags(text):
  """移除指定的 HTML 標籤

  Args:
    text: 要處理的文字

  Returns:
    處理後的文字
  """

  pattern = re.compile(r'<br />|<p>')
  return re.sub(pattern, '', text)


# 從專輯抓歌曲
url = 'https://www.kkbox.com/tw/tc/playlist/GnN-ifVBBEMYgmqMlB'
response = requests.get(url)

if response.status_code == 200:
    print("請求成功")
    html_content = response.text
    
    soup = BeautifulSoup(html_content, 'html.parser')
    li_elements = soup.find_all('li')
    print(li_elements)
    for li in li_elements:
        button_div = li.find('div', class_='button')
        
        if button_div:
            preview_control = button_div.find('preview-control')
                
            if preview_control:
                data_id = preview_control.get('data-id')
                data_ga_label = preview_control.get('data-ga-label')
                songs[data_id] = data_ga_label
                print(f"data-id: {data_id}, data-ga-label: {data_ga_label}")
    
else:
    print(f"失敗: {response.status_code}")


# 進入歌曲頁面抓歌詞
ids = songs.keys()
for id in ids:
    song_url = song_url_basic + id
    response = requests.get(song_url)
    
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        p = soup.find_all('p')
        if len(p) > 1:
          lyric = p[1].text
          lyric = remove_tags(lyric)
        else:
          lyric = 'None'
          
        name = songs[id]
        try:
          with open('Sample_songs/'+name+'.txt', 'w', encoding='utf-8') as f:
              f.write(lyric)
        except:
          pass
        
    else:
        print(f"抓歌詞失敗: {response.status_code}")
