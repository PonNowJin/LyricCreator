import os
import google.generativeai as genai
from dotenv import load_dotenv
from google.generativeai.types import HarmCategory, HarmBlockThreshold

load_dotenv()

class LLM:
    API_KEY = os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=API_KEY)

    def __init__(self):
        pass

    def getModel(self, config=None, system_instruction=None, model_name='gemini-1.5-flash'):
        model = genai.GenerativeModel(
            model_name=model_name,
            generation_config=config,
            safety_settings={
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE
            },
            system_instruction = system_instruction,
        )
        return model
    

    def getEmbeddingContent(self, content, model='models/text-embedding-004', task_type='SEMANTIC_SIMILARITY', title=None):
        """
        task_type:
        RETRIEVAL_QUERY	指定指定文字是搜尋/擷取設定中的查詢。
        RETRIEVAL_DOCUMENT	指定文字是搜尋/擷取設定中的文件。使用這個工作類型需要 title。
        SEMANTIC_SIMILARITY	指定指定文字將用於語意文字相似度 (STS)。
        """
        
        result = genai.embed_content(
            model, content, task_type, title,
            safety_settings={
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH
            })
        
        return result
