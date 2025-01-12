import json
import pathlib
import textwrap
import re

from IPython.display import display
from IPython.display import Markdown
from IPython.utils import data
from API_setting import LLM


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


class Evaluation:
    llm = LLM()
    score = 0
    generation_config = {
        "temperature": 0.2,
    }
    topic = None

    model = llm.getModel(generation_config)
    chat = model.start_chat(history=[])

    # 初始 prompt
    base_prompt = """
        你是一位專業音樂人，請依以下標準為輸入之歌詞進行評分：
        
        評分標準（0~100分）：
        符合主題：加分
        
        押韻：歌詞有無押韻，押韻可以在句尾或句中（有押韻評分較高），押韻是否過度使用，當刻意使用押韻導致偏離主題，或破壞歌詞欲表達的情緒，扣分
        
        歌詞的句子不能過長，會顯得饒口
        
        敘述者：歌詞是否為同一個敘述者的角度書寫（是，分數較高）
        
        段落：歌詞中是否出現段落相關的描述，像是：verse1, verse2, pre-chours, chorus 諸如此類 （是，分數較高）
        
        歌詞是否具有意境（是，分數高）
        
        歌詞中描述的情景是否清晰、具有美感、能觸動人的情感（是，分數高）
        
        出現重複句子，若不過多可讓歌曲更有韻味（斟酌評分）
        
        歌詞不是寫得越仔細、完整越好，有時簡短但可以留給聽者想象空間會更好
        把豐富的意境、情感表達、寫進簡短的句子中，是最不錯的（高分）
        
        扣分部分只能以你確定的部分做扣分
        依照你認為輸入歌詞的好壞進行評分，0~100中任何分數皆可
        此評分裝置的回饋用於改善LLM創作歌詞的能力，所以請以改善LLM能力為目標去設計回饋
        給出更精確的評分例如：76, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90，讓歌詞創作模型能夠理解方向是否正確
        記得此次的建議，每次評分都朝此建議去評分
        明確且精簡說明歌詞如何獲得更高的分數
        可以嚴格評分
        
        輸入、輸出示例：
        輸入：”“”（一段歌詞）“”“
        輸出：”“”
            評分：76,
            回饋：
        """

    def setTopic(self, topic):
        self.topic = topic

    def getScore(self):
        return self.score

    def evaluation(self, output_dir=''):
        # 讀取歌詞文件
        with open(output_dir+'/lyrics.txt', 'r', encoding='utf-8') as file:
            lyrics = file.read()
        full_prompt = f"主題：{self.topic}\n" + self.base_prompt + f"\n歌詞輸入：\n{lyrics}"

        response = self.chat.send_message(full_prompt)
        # print(chat.history)

        # 紀錄評分
        match = re.search(r'評分：\s*(\d+)', response.text)
        if match:
            self.score = int(match.group(1))
            # print(f"評分：{self.score}")
        else:
            print("未找到評分")

        # 保存聊天歷史記錄到文件
        '''
        with open("_history.txt", "w", encoding="utf-8") as file:
            file.write(str(chat.history))
        '''

        with open(output_dir+"/chat_history.txt", "w", encoding="utf-8") as file:
            for message in self.chat.history:
                file.write(f'**{message.role}**: {message.parts[0].text}\n')

        return response.text

    """
        for message in chat.history:
            display(to_markdown(f'**{message.role}**: {message.parts[0].text}'))
        """


"""
e = Evaluation()
e.setTopic('千里之外')
r = e.evaluation()
print(r)
"""