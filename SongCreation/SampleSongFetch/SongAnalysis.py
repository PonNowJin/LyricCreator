import os
import re
import time
import json
import google.api_core.exceptions
import google.generativeai as genai
from API_setting import LLM
from Toolkit import *

#######################
# 用於分析歌詞，統整成標籤、一句話說明，存檔
# reset(): 重置歌名與歌詞
# getSongName(): 回傳目前歌名
# setLyrics(): 用於傳入欲分析的歌詞
# analysis(): 用於獲取分析後的資訊並存檔
#######################


class SongAnalysis:
    llm = LLM()
    lyrics = ''
    name = ''
    output_dir = 'SongAnalysis_m/'
    
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = llm.getModel(generation_config)

    prompt_content = [
    "input: 不要談什麼分離\n我不會因為這樣而哭泣\n那只是昨夜的一場夢而已\n不要說願不願意\n我不會因為這樣而在意\n那只是昨夜的一場遊戲\n\n那只是一場遊戲一場夢\n雖然你影子還出現我眼裡\n在我的歌聲中早已沒有你\n那只是一場遊戲一場夢\n不要把殘缺的愛留在這裡\n在兩個人的世界裡不該有你\n\n喔 為什麼道別離 又說什麼在一起\n如今雖然沒有你 我還是我自己\n說什麼此情永不渝 說什麼我愛你\n如今依然沒有你 我還是我自己\n\n那只是一場遊戲一場夢\n雖然你影子還出現我眼裡\n在我的歌聲中早已沒有你\n那只是一場遊戲一場夢\n不要把殘缺的愛留在這裡\n在兩個人的世界裡不該有你\n\n喔 為什麼道別離 又說什麼在一起\n如今雖然沒有你 我還是我自己\n說什麼此情永不渝 說什麼我愛你\n如今依然沒有你 我還是我自己\n\n為什麼道別離 又說什麼在一起\n如今雖然沒有你 我還是我自己\n說什麼此情永不渝 說什麼我愛你\n如今依然沒有你 我還是我自己\n\n你可以把這歌詞統整出一些標籤嗎？像是：憂傷、高興等等，也把這歌詞的情感主題濃縮的越短越好（一句話），其他不需要",
    "output: 歌詞標籤情感類： 憂傷、失落、堅強、決絕、無奈、釋懷意象類： 夢、遊戲、影子、殘缺、道別情境類： 分離、告別、過去、現在、自我情感主題濃縮一句話濃縮： 雖然心有不捨，但已決定放手，面對失戀，堅強地活出自己。",
    "input: 後視鏡裏的世界 越來越遠的道別\n你轉身向背 側臉還是很美\n我用眼光去追 竟聽見你的淚\n\n在車窗外面徘徊 是我錯失的機會\n你站的方位 跟我中間隔著淚\n街景一直在後退 你的崩潰在窗外零碎\n\n我一路向北 離開有你的季節\n你說你好累 已無法再愛上誰\n風在山路吹 過往的畫面全都是我不對\n細數慚愧 我傷你幾回\n\n後視鏡裏的世界 越來越遠的道別\n你轉身向背 側臉還是很美\n我用眼光去追 竟聽見你的淚\n\n在車窗外面徘徊 是我錯失的機會\n你站的方位 跟我中間隔著淚\n街景一直在後退 你的崩潰在窗外零碎\n\n我一路向北 離開有你的季節\n你說你好累 已無法再愛上誰\n風在山路吹 過往的畫面全都是我不對\n細數慚愧 我傷你幾回\n\n我一路向北 離開有你的季節\n方向盤周圍 迴轉著我的後悔\n我加速超越 卻甩不掉緊緊跟隨的傷悲\n細數慚愧 我傷你幾回\n停止狼狽 就讓錯純粹\n\n這個也要，但只要保留歌詞標籤與情感主題濃縮的分析即可，剩餘省略",
    "output: 歌詞標籤情感類： 傷心、後悔、失落、無奈、孤獨、決絕意象類： 後視鏡、道別、側臉、淚水、車窗、山路、方向盤情境類： 分手、離別、回憶、追憶、遠離情感主題濃縮一句話濃縮： 面對分手的現實，在遠去的車窗裡，看著對方孤獨的身影，滿心懊悔與傷痛，卻無力挽回。",
    "input: 那女人嘗試在皮膚紋上\n活在方格裡的男人和她\n忍著痛 掩蓋毛細孔\n無聲的故事 演奏著\n\n於是真實剩殘破的影子\n在各自的城市逐漸靜止\n轉身後 像一顆灰塵\n親密的擁有 光和熱\n\n愛不愛 無關了\n會習慣 合理的\n不快樂 愛～\n\n愛不愛 無關了\n會習慣 合理的 不快樂\n\n愛不愛 記不得\n漂亮的 偽裝成 另一個人\n\n忽然間\n想起在哪裡的你好不好\n\n好不好\n\n這個也要，但只要保留歌詞標籤與情感主題濃縮的分析即可，剩餘省略，簡要分析也不用，補充也不用",
    "output: 歌詞標籤情感類： 痛楚、空虛、麻木、懷疑、遺忘、掙扎意象類： 紋身、方格、毛細孔、影子、城市、灰塵情境類： 失去自我、偽裝、愛情變質、回憶情感主題濃縮一句話濃縮： 為了迎合他人，壓抑自我，在失去真實的過程中，愛情逐漸變質，最終只剩空虛和懷疑。",
    "input: 窗外的麻雀 在電線桿上多嘴\n妳說這一句 很有夏天的感覺\n手中的鉛筆 在紙上來來回回\n我用幾行字形容妳是我的誰\n\n秋刀魚 的滋味 貓跟妳都想了解\n初戀的香味就這樣被我們尋回\n那溫暖 的陽光 像剛摘的鮮豔草莓\n你說妳捨不得吃掉這一種感覺\n\n雨下整夜 我的愛溢出就像雨水\n院子落葉 跟我的思念厚厚一疊\n幾句是非 也無法將我的熱情冷卻\n妳出現在我詩的每一頁\n\n雨下整夜 我的愛溢出就像雨水\n窗台蝴蝶 像詩裡紛飛的美麗章節\n我接著寫 把永遠愛妳寫進詩的結尾\n妳是我唯一想要的了解\n\n雨下整夜 我的愛溢出就像雨水\n院子落葉 跟我的思念厚厚一疊\n幾句是非 也無法將我的熱情冷卻\n妳出現在我詩的每一頁\n\n那飽滿的稻穗 幸福了這個季節\n而妳的臉頰像田裡熟透的番茄\n妳突然 對我說 七里香的名字很美\n我此刻卻只想親吻妳倔強的嘴\n\n雨下整夜 我的愛溢出就像雨水\n院子落葉 跟我的思念厚厚一疊\n幾句是非 也無法將我的熱情冷卻\n妳出現在我詩的每一頁\n\n整夜 我的愛溢出就像雨水\n窗台蝴蝶 像詩裡紛飛的美麗章節\n我接著寫 把永遠愛妳寫進詩的結尾\n妳是我唯一想要的了解\n\n這個也要，但只要保留歌詞標籤與情感主題濃縮的分析即可，其他部分完全不需回答或分析",
    "output: 歌詞標籤情感類： 熱戀、甜蜜、思念、執著、幸福意象類： 麻雀、鉛筆、秋刀魚、陽光、草莓、雨、落葉、蝴蝶、稻穗、番茄、七里香情境類： 夏天、初戀、寫詩、雨夜、自然情感主題濃縮一句話濃縮： 將對戀人的愛意化為詩句，細膩描繪了熱戀中的甜蜜與幸福，表達了對戀人的深情與執著。",
    "input: 編曲:盧鈞右 Neon Lu\n\n傳說人間有命中注定\n只要遇對的人 他們就會被吸引\n\n傳說人類常常流淚\n開心 難過 感動的時候都會\n\n或許是被上天懲罰 我的心空空蕩蕩\n一眼瞬間 心臟竟開始撲通撲通 撲通的跳\n\n我看過 紅的綠的藍的黃的紫色的煙火\n看過太陽月亮 和世上最閃亮的星星\n看過你的笑容才發現 這是我最喜歡的人間煙火\n\n看懂愛情發酵瞬間 看懂幸福的相依\n原來我已明白什麼叫做愛情\n人間煙火 請照亮我的夜空\n\n或許是被上天懲罰 我的心空空蕩蕩\n一眼瞬間 心臟竟開始撲通撲通 撲通的跳\n\n我看過 紅的綠的藍的黃的紫色的煙火\n看過太陽月亮 和世上最閃亮的星星\n看過你的笑容才發現 這是我最喜歡的人間煙火\n\n看懂愛情發酵瞬間 看懂幸福的相依\n原來我已明白什麼叫做愛情\n人間煙火 請照亮我的夜空\n\n這個也要，但只要保留歌詞標籤與情感主題濃縮的分析即可，其他部分完全不需回答或分析，不需多加補充",
    "output: 歌詞標籤情感類： 愛情、幸福、悸動、驚喜、浪漫意象類： 命中注定、煙火、太陽、月亮、星星、笑容情境類： 初遇、心動、愛情啟蒙情感主題濃縮一句話濃縮： 一見鍾情，心動不已，在遇到心愛的人的那一刻，才真正理解了愛情的真諦，並對未來充滿了美好的期待。",
    "input: 夜 黑夜 寂寞的夜裡\n氣 生氣 對自己生氣\n軟弱的電話 又打 給你\n想 聽你 那邊的空氣\n有 什麼 精采的話題\n你還是溫柔 給我 婉轉 的距離\n我的聲音在笑 淚在飆 電話那頭的你可知道\n世界若是那麼大 為何我要忘你 無處逃\n我的聲音在笑 淚在飆 電話那頭的你可知道\n世界若是那麼小 為何我的真心 你聽不到\n\n夜 黑夜 寂寞的夜裡\n氣 生氣 對自己生氣\n軟弱的電話 又打 給你\n想 聽你 那邊的空氣\n有 什麼 精采的話題\n你還是溫柔 給我 婉轉 的距離\n我的聲音在笑 淚在飆 電話那頭的你可知道\n世界若是那麼大 為何我要忘你 無處逃\n我的聲音在笑 淚在飆 電話那頭的你可知道\n世界若是那麼小 為何我的真心 你聽不到\n聽不到聽不到我的執著\n撲通撲通 一直在跳\n直到你有一天能夠明暸\n我做得到 我做得到\n我的聲音在笑 淚在飆 電話那頭的你可知道\n世界若是那麼大 為何我要忘你 無處逃\n我的聲音在笑 淚在飆 電話那頭的你可知道\n世界若是那麼小 為何我的真心 你聽不到\n你聽不到～你聽不到～\n\n這個也要，但只要保留歌詞標籤與情感主題濃縮的分析即可，不需要簡要分析",
    "output: 歌詞標籤情感類： 孤獨、失落、矛盾、執著、愛慕意象類： 夜、電話、空氣、聲音、淚水情境類： 失戀、思念、自我懷疑情感主題濃縮一句話濃縮： 夜深人靜時，內心的孤獨與思念愈加強烈，明明想忘記對方，卻又忍不住撥通電話，在矛盾的情緒中掙扎，渴望對方能理解自己的真心。",
    "input: 每雙眼睛都是魚\n眼前滄海的一滴\n時光如夢盤旋成了鱗\n銀河泛起漣漪\n我像風在銀河間飛行\n經過如海的星星\n入光的森林\n躍天空的溪\n彎成淺笑的光影\n啦啦啦啦啦\n心兒留下投影\n投影一世界\n魚躍映出山頂\n從日月間\n到塵埃裡\n只願與愛\n同來同去\n每雙眼睛都是魚\n初見是無邊海域\n默念的聲音萬物驚奇\n星球是淚滴\n我像風在銀河間飛行\n穿越所有的散聚\n在時光盡頭\n細數著足跡\n那是無數我和你\n啦啦啦啦啦\n心兒留下投影\n投影一世界\n洩露天意\n啦啦啦啦\n啦啦啦啦啦啦\n明明是愛\n暗暗不語\n啦啦啦啦啦\n心兒留下投影\n投影一世界\n將天空微微捲起\n想和念\n從滄海浮現\n無盡的心\n幻化成鱗\n\n這個也要",
    "output: 歌詞標籤情感類： 愛情、思念、浪漫、哲學、宇宙觀意象類： 眼睛、魚、滄海、銀河、星星、風、森林、溪流、投影、日月、塵埃情境類： 宇宙、時空、相遇、分離、思念情感主題濃縮一句話濃縮： 將愛比喻為宇宙中的星塵，每雙眼睛都是一顆獨特的星球，彼此在時空中相遇、相知、相惜，最終在浩瀚宇宙中留下愛的印記。",
    "input: 編曲：王治平\n\n早已忘了想你的滋味是什麼\n因為每分每秒都被你佔據在心中\n你的一舉一動牽扯在我生活的隙縫\n誰能告訴我離開你的我會有多自由\n\n也曾想過躲進別人溫暖的懷中\n可是這麼一來就一點意義也沒有\n我的高尚情操一直不斷提醒著我\n離開你的我不論過多久還是會寂寞\n\n別對我小心翼翼\n別讓我看輕你\n跟著我勇敢的走下去\n別勸我回心轉意\n這不是廉價的愛情\n看著我對我說真愛我\n\n也曾想過躲進別人溫暖的懷中\n可是這麼一來就一點意義也沒有\n我的高尚情操一直不斷提醒著我\n離開你的我不論過多久還是會寂寞\n\n別對我小心翼翼\n別讓我看輕你\n跟著我勇敢的走下去\n別勸我回心轉意\n這不是廉價的愛情\n看著我對我說真愛我\n\n也曾想過躲進別人溫暖的懷中\n可是這麼一來就一點意義也沒有\n我的高尚情操一直不斷提醒著我\n離開你的我不論過多久還是會寂寞\n\n這個也要，但只要保留歌詞標籤與情感主題濃縮的分析即可，不需要簡要分析，完全不需要寫出其他的分析內容",
    "output: 歌詞標籤情感類： 愛情、執著、矛盾、掙扎、寂寞意象類： 懷中、高尚情操、溫暖情境類： 分手、掙扎、重新開始情感主題濃縮一句話濃縮： 雖然想忘記對方，但內心深處卻無法割捨這段感情，渴望對方能夠勇敢面對這段感情，並給予自己最真實的愛。",
    "input: 久未放晴的天空 依舊留著妳的笑容\n哭過 卻無法掩埋歉疚\n風箏在陰天擱淺 想念還在等待救援\n我拉著線 復習妳給的溫柔\n曝曬在一旁的寂寞 笑我給不起承諾\n怎麼會怎麼會 妳竟原諒了我\n\n我只能永遠讀著對白 讀著我給妳的傷害\n我原諒不了我 就請妳當作我已不在\n我睜開雙眼 看著空白 忘記妳對我的期待\n讀完了依賴 我很快就離開\n\n☆☆☆\n ☆☆\n  ☆\n久未放晴的天空 依舊留著妳的笑容\n哭過 卻無法掩埋歉疚\n風箏在陰天擱淺 想念還在等待救援\n我拉著線 復習妳給的溫柔\n曝曬在一旁的寂寞 笑我給不起承諾\n怎麼會怎麼會 妳竟原諒了我\n\n我只能永遠讀著對白 讀著我給妳的傷害\n我原諒不了我 就請妳當作我已不在\n我睜開雙眼 看著空白 忘記妳對我的期待\n讀完了依賴 我很快就\n我只能永遠讀著對白 讀著我給妳的傷害\n我原諒不了我 就請妳當作我已不在\n我睜開雙眼 看著空白 忘記妳對我的期待\n讀完了依賴 我很快就離開\n\n這個也要，但只要保留歌詞標籤與情感主題濃縮的分析即可，不需要簡要分析，完全不需要寫出其他的分析內容",
    "output: 歌詞標籤情感類： 愧疚、思念、孤獨、失落、自責意象類： 天空、笑容、風箏、陰天、寂寞情境類： 分手、回憶、自我懲罰情感主題濃縮一句話濃縮： 深深地後悔過去的過錯，無法原諒自己帶給對方的傷害，只能獨自承受思念的痛苦，並祈求對方能忘記自己，好讓自己能從這段感情中解脫。",
    "input: 舞鞋穿了洞裂了縫\n預備迎接一個夢\nOK繃遮住痛要把蒼白都填充\n勇氣惶恐 我要用哪一種 面對他\n一百零一分笑容\n等待的時空有點重重得時針走不動\n無影踪他始終不曾降臨生命中\n我好想懂 誰放我手心裡捧\n幸福啊 依然長長的人龍\n想踮起腳尖找尋愛遠遠的存在\n我來不及說聲嗨影子就從人海暈開\n才踮起腳尖的期待只怕被虧待\n我勾不著還微笑忍耐 Woo\n等你回過頭來\n哪天撲了空折了衷祈禱終於起作用\n一陣風吹來夢卻又敗在難溝通\n我終於懂 怎麼人們的臉孔\n想到愛 寂寞眼眶就轉紅\n想踮起腳尖找尋愛遠遠的存在\n我來不及說聲嗨影子就從人海暈開\n才踮起腳尖的期待只怕被虧待\n我勾不著還微笑忍耐 woo\n等你回過頭來\n你會回過頭來    woo\n回過頭來\n想踮起腳尖找尋愛遠遠的存在\n我來不及說聲嗨影子就從人海暈開\n才踮起腳尖的期待只怕被虧待\n我勾不著還微笑忍耐 Woo\n等你回過頭來\n\n這個也要，但只要保留歌詞標籤與情感主題濃縮的分析即可，不需要簡要分析，完全不需要寫出其他的分析內容",
    "output: 歌詞標籤情感類： 期待、緊張、孤獨、失落、希望意象類： 舞鞋、笑容、時鐘、影子、人海情境類： 等待、相遇、失落、堅持情感主題濃縮對愛的渴望與不確定性： 歌詞中描述了主角渴望愛情，但同時也害怕被拒絕，內心充滿了矛盾與不安。等待的焦慮與期待： 主角為了與心儀的人相遇所做的準備和等待，以及內心深處的緊張與期待。對未來的憧憬與堅持： 儘管面臨等待的煎熬和可能的失望，主角依然堅持著對愛的追求，希望能夠與心儀的人相遇。",
    "input: ",
    "output: ",
    ]
    
    prompt_modify = '這個也要，但只要保留歌詞標籤（幾個單詞）、情感主題濃縮的分析（一句話）即可，不需要簡要分析，完全不需要寫出其他的分析內容'
    
    def reset(self):
        self.name = ''
        self.lyrics = ''
        
    def getSongName(self) -> str:
        return self.name

    
    def setLyrics(self, file_path):
        if os.path.exists(file_path):
            match = re.search(r'/([^/]+)\.txt$', file_path)
            if match:
                self.name = match.group(1)
            else:
                print('err: 抓取歌曲名稱錯誤')
                
            with open(file_path, 'r', encoding='utf-8') as f:
                self.lyrics = f.read()
        else:
            print('err: 歌詞檔不存在, ', file_path)
            
        # print(self.name)
        # print(self.lyrics)
        return 
    
    
    # api 錯誤遞迴處理
    def make_api_request(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response
        except google.api_core.exceptions.ResourceExhausted as e:
            print(f"Encountered error: {e}")
            print("Retrying in 5 seconds...")
            time.sleep(5)
            return self.make_api_request(prompt)
        

    def analysis(self) -> bool:
        prompt = self.prompt_content[-2] + self.lyrics + self.prompt_modify
        # print(self.prompt_content)
        # response = self.model.generate_content(prompt)
        response = self.make_api_request(prompt)
        print(response)
        try:
            print(response.text)
        except:
            print('err')
            return False
        
        file_name = self.output_dir + self.name
        if save_to_file(file_name, response.text, 'w'):
            return True
        return False
    
        
        
if __name__ == '__main__':
    path = 'Sample_songs/'
    SA = SongAnalysis()
    # songs = os.listdir(path)
    songs = read_file_to_list('FailSongs.txt')
    fail_songs = []
    # print(songs)
    for song in songs:
        SA.reset()
        SA.setLyrics(path+song+'.txt')
        print(SA.getSongName())
        if not SA.analysis():
            fail_songs.append(SA.getSongName)
        time.sleep(1)

    