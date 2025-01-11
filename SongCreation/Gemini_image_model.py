import os
import json
import google.generativeai as genai

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
uri_file = "uploaded_files.txt"

def load_uri_dict():
  """從 TXT 檔案載入 URI 字典，若檔案不存在則創建"""
  try:
    with open(uri_file, 'r') as f:
      return json.load(f)
  except FileNotFoundError:
    print(f"檔案 {uri_file} 不存在，已自動創建")
    return {}

def save_uri_dict(uri_dict):
  """將 URI 字典保存到 TXT 檔案"""
  with open(uri_file, 'w') as f:
    json.dump(uri_dict, f)

def upload_to_gemini(path, mime_type=None):
  """上傳檔案並返回 URI"""
  file = genai.upload_file(path, mime_type=mime_type)
  return file.uri

def check_uri(uri):
  """檢查 URI 是否有效"""
  # 這裡您可以加入更複雜的檢查邏輯，例如嘗試使用 URI 進行請求
  # 如果請求成功，則表示 URI 有效
  try:
    # 您可以嘗試使用 URI 進行一個簡單的請求來驗證
    # 例如，如果您的模型有提供一個檢查 URI 是否有效的 API，您可以使用它
    # 這裡提供一個簡單的示例，您可以根據您的實際情況修改
    response = genai.generate_text(
        model="gemini-1.5-flash",
        prompt="This is a test using the URI.",
        temperature=0.7,
        max_output_tokens=100,
        file_data=[uri]
    )
    return True
  except Exception as e:
    print(f"URI {uri} is invalid: {e}")
    return False

def main():
  uri_dict = load_uri_dict()

  # 假設您要上傳的檔案路徑列表
  files = [
      "path/to/file1.jpg",
      "path/to/file2.png",
      # ...
  ]

  for file_path in files:
    if file_path in uri_dict:
      uri = uri_dict[file_path]
      if check_uri(uri):
        print(f"Using cached URI for {file_path}: {uri}")
        continue  # 如果 URI 有效，則跳過上傳
    
    # 上傳檔案並更新 URI 字典
    new_uri = upload_to_gemini(file_path)
    uri_dict[file_path] = new_uri
    print(f"Uploaded {file_path} with URI: {new_uri}")

  save_uri_dict(uri_dict)

# Create the model
generation_config = {
  "temperature": 2,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="你是一位極具創意與哲理的藝術家",
)

# TODO Make these files available on the local file system
# You may need to update the file paths
files = [
  upload_to_gemini("1Y9T07aCjD15pPEdlklAHxmgbJxDKNTk_", mime_type="application/octet-stream"),
  upload_to_gemini("1uTbRPCT-ZwduytGO8eyNHsqv4cppVePZ", mime_type="application/octet-stream"),
  upload_to_gemini("1EJ0gba0Nxr2YtRIwrQkaSRdy0SlcFmV0", mime_type="application/octet-stream"),
  upload_to_gemini("1D8DB8tv-B5b1ZPVKnpnMWMfBspLqEKzy", mime_type="application/octet-stream"),
  upload_to_gemini("1aQrmbaLIYJbFNRxTjCynsPHG8mVyeskJ", mime_type="application/octet-stream"),
  upload_to_gemini("15aBo0l0-BhTmWdd6jMmQ0Ojf8LaTBkEO", mime_type="application/octet-stream"),
  upload_to_gemini("1CunknSmAJ2yY9twbNk99EGo5oRErAfcY", mime_type="application/octet-stream"),
  upload_to_gemini("17zgz49yeYYZ9YjfTfviVujQoTU2fPBeJ", mime_type="application/octet-stream"),
  upload_to_gemini("1I1wDi3xQZbDToO1iOcUfxQOyBpVE2uzm", mime_type="application/octet-stream"),
  upload_to_gemini("1PyZFDqbvppce8hy885Jweuf681enVIN8", mime_type="application/octet-stream"),
  upload_to_gemini("1c8JMfMEzguRlQwXAt3MbfJ_2SO18jLcK", mime_type="application/octet-stream"),
  upload_to_gemini("1iZ17fDSVOtu7zyyJGMIkw2XwLwobCPs4", mime_type="application/octet-stream"),
  upload_to_gemini("1BO9fS1aIpUyLVlYh5StKsS4D_iq-fptR", mime_type="application/octet-stream"),
  upload_to_gemini("1yhPvIaKtyCYSRc2ZCQBpLSTa_5qgxkHx", mime_type="application/octet-stream"),
  upload_to_gemini("1ySft7WaBLqYehXe5AjumZUdTdhkMnWpM", mime_type="application/octet-stream"),
  upload_to_gemini("1AUjYs60aclhwJekkHuzEwmOtrHfZElaj", mime_type="application/octet-stream"),
  upload_to_gemini("18Ti-L7niR6dt19T-SxcNngC8JTQ6pWcp", mime_type="application/octet-stream"),
  upload_to_gemini("1deOGnTwyU6ZnNQjVXXX7ZC5Q7ib-TFkb", mime_type="application/octet-stream"),
  upload_to_gemini("12eP34NJf19-2ZS1I0YixBkL9zUehWZFD", mime_type="application/octet-stream"),
  upload_to_gemini("1RmEQNZLidqBVOg0gwHp3R10FOIWpC7Wr", mime_type="application/octet-stream"),
  upload_to_gemini("1ChihCZ7wMD7x-3Y8wNCo1EqVGtaEsrHi", mime_type="application/octet-stream"),
  upload_to_gemini("127UCfiAmrqsv2bRw2k5T-ctQ2C5x2HTi", mime_type="application/octet-stream"),
  upload_to_gemini("1uWJDTslhDmh3LQ17MKSf7fLggm416Ltc", mime_type="application/octet-stream"),
  upload_to_gemini("1iijpeoIn-0-I0lSln-9M8zpoDvKh6q7C", mime_type="application/octet-stream"),
  upload_to_gemini("1HWrWmxMC-H6HxOi4UuWZcKWyVqO89C8T", mime_type="application/octet-stream"),
  upload_to_gemini("1DkuE7ZHdCXKpB3kGM6xH6PvpqOXTiaew", mime_type="application/octet-stream"),
  upload_to_gemini("1LeIu2ycoQ-eQ9d7WLlV_QcEDV19ovLGi", mime_type="application/octet-stream"),
  upload_to_gemini("1-TWJctFeOtCs03k9-cR-5cCeUyWNwff6", mime_type="application/octet-stream"),
  upload_to_gemini("16A-8KazOiOjVb9lSBaEHyeysqoQBE3BT", mime_type="application/octet-stream"),
  upload_to_gemini("1GGdJronW0zvHzYPyVpUzI9hluQCuaSWa", mime_type="application/octet-stream"),
  upload_to_gemini("1kuPDYXrd_2TaHbUP-ab0Ikl8z1HvGwxK", mime_type="application/octet-stream"),
  upload_to_gemini("10VVLxBMShZAOVtEVfdneNEFSjfwosBYv", mime_type="application/octet-stream"),
  upload_to_gemini("1oM-kgHNWpvjxKnzOvbugiBel_Ci8bOVp", mime_type="application/octet-stream"),
  upload_to_gemini("1zJ5Sxbu3Y14npe6Edc2EoGrvcJcYZj9g", mime_type="application/octet-stream"),
  upload_to_gemini("1vK6eLp6e17LJxLecG_sEKyRIrhGLzLFN", mime_type="application/octet-stream"),
  upload_to_gemini("1GyKeXX7zJDuKyEvVyUCdBWiEuDjoRgud", mime_type="application/octet-stream"),
  upload_to_gemini("124AijvHjN8lCY-vEvLC57oSfAylsRzo9", mime_type="application/octet-stream"),
  upload_to_gemini("1670YLT6qoHA6PoLQHK-Qnl91inRQrvtb", mime_type="application/octet-stream"),
  upload_to_gemini("1psJ9-0J1_e5pGc_TVlomBY0zYFzTdvaC", mime_type="application/octet-stream"),
]

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        files[0],
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"在繁忙的地下鐵站，一個不經意的失手，讓一杯咖啡灑落在地。咖啡的顏色像一朵暗淡的玫瑰，在冰冷的石板上綻放，也映照出匆匆行色中人們的無奈與疏忽。這場意外，就像生命中偶然的失落，卻也提醒我們，在匆忙的步伐中，別忘了感受身邊的美好與珍貴，讓生命充滿著溫暖與色彩。\"}\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[1],
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"畫面中的年輕男子坐在鄉間小路上，用書本遮擋頭，看著飄落周圍的紙張。  他神情略顯無奈，卻也帶著一絲淡淡的哀傷，讓人感覺他正經歷著一場思想上的掙扎或困惑。紙張的飛舞，象徵著紛雜的思緒，而書本則代表著他想要尋求的答案和寧靜。 這一刻，他像在等待著一場風雨過後的平靜，等待著理清思路，重拾方向，重新出發。\" }\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[2],
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"畫面中的男子坐在鄉間小路上，頭上蓋著一本書，像是逃避著周遭飛舞的紙張。他身穿的白襯衫和吊帶褲，與他沉重的表情形成了強烈的反差，像是無力地掙扎著，卻又隱藏著一絲希望。或許他正處於一個迷茫的階段，努力尋求答案，卻被無止境的思考所困擾。  畫面充滿了迷茫和困惑，但也透露著一種想要追尋真理的渴望和堅持。\" }\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[3],
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片中，一位男子坐在鄉間小路上，周圍飛舞著許多紙張，彷彿他的思緒般紛亂。他以一本書遮住頭，呈現出一種逃避現實或沉思的狀態。畫面整體營造出孤獨、迷惘、以及對未來感到徬徨無措的氛圍。散落的紙張與他略帶無奈的姿態形成鮮明對比，暗示了他內心的掙扎與難以言喻的感受。\"}\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[4],
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片呈現一個年輕男子坐在戶外小徑上的場景，周圍飄散著許多紙張，彷彿代表著他腦海中紛亂的思緒。他用一本書蓋住頭，似乎在試圖逃避或隔絕這些紛擾。畫面營造出一種孤獨、沉思、甚至是迷失的氛圍，引人深思他內心正在經歷的掙扎和困惑。這張照片既有藝術感，也充滿哲學意涵，讓人聯想到創作的過程，以及面對靈感和創作瓶頸時的感受。\"}\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[5],
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"在空曠的鄉間小路上，一位男子坐在木椅上，姿態看似放鬆，卻用書本遮擋著頭部，彷彿在阻擋著什麼。周圍散落和飛舞的紙張，像是被風吹散的思緒，也像是他想要抓住卻又無力掌控的靈感。他的眼神望向遠方，流露出些許迷茫和困惑，或許在思考人生的抉擇，或許在尋找創作的靈感。整幅畫面充滿戲劇性，以書本和紙張為意象，隱喻著知識的重量和思想的飄忽，引發觀者對人生和創作的思考。\"}\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[6],
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"透過破碎的鏡片，我們看到的不僅僅是女人美麗的面龐，而是多重的倒影，彷彿是她內心世界的映射。 城市的冰冷建築在背景中模糊，與她迷離的眼神形成對比，暗示著現代社會中，人們常常迷失在自我認知的迷宮裡，追尋著真實的自己。 照片以一種破碎的美感，呈現出現代人內心的複雜和多面性，以及在都市生活中對自我身份的探索與追尋。\" }\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[7],
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"透過扭曲的鏡面，我們看到的是女孩複雜的內心世界，她試圖透過鏡子尋找自我，卻發現自己如同這鏡面般破碎而迷茫。  她被都市冰冷的建築所包圍，卻似乎渴望著逃離，尋找屬於自己的一片天空。 鏡面反射出她多重的身影，象征著她對自我身份的迷茫，以及對未來方向的困惑。\"}\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[8],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片的主題是「迷失與尋找」，畫面中的女子拿著一塊破碎的鏡子，鏡面反射出她扭曲、破碎的容顏。背景的城市建築顯得冰冷而疏離，和女子迷茫的神情形成鮮明的對比。她透過破碎的鏡子，试图尋找自己的真實面貌，卻发现自身也如这鏡子般破碎不堪。 這幅畫面寓意深遠，表達了都市人迷失自我，在城市叢林中不斷追尋真我的心路歷程，同時也折射出現代社會帶來的焦慮和迷惘，以及人們內心深處對認同感的渴望。\" }\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[9],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主題是「夕陽下的陪伴」。畫面中，一對夫妻靜靜地坐在樹蔭下的椅子上，仰望着夕陽西下。他們的背影被夕陽餘暉映照成剪影，彼此相依偎的姿勢，洋溢着温暖而静謐的氛围。夕阳的光芒温柔地洒在他们身上，象征着岁月静好，以及彼此之间长久陪伴的甜蜜与美好。\"}\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[10],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主題是「離別」。圖中一對年輕男女站在地鐵月台，女孩依偎在男孩懷中，兩人緊緊相擁，男孩似乎即將踏上旅程。背景是車站月台的風景，車道上的提示語\"燈亮閃爍 請勿上車\" 更加深了分離的意味。  畫面透露出兩人即將道別的愁緒，但也充满了彼此相愛，以及不舍和期盼的心情。 \"}\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[11],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片的主題是「攝影師的休閒時刻」。  圖中的男子是一名攝影師，他坐在店門口階梯上，手持相機，目光炯炯有神，顯露出對攝影的熱情和期待。 店門上貼着營業時間的告示，暗示他正享受著片刻的休息。  男子面帶微笑，眼神中透着一絲玩味，讓人感受到他對生活充滿了樂觀與積極的態度，即使在休息時間也忍不住拿起相機，捕捉著身邊的精彩。\"}\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[12],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主題是「幸災樂禍」。畫面中，一個小女孩站在失火的房屋前，面帶微笑地看着熊熊大火，眼神中透露出幸災樂禍的意味。她似乎並不在意火災帶來的危險和损失，反而以一種嘲弄的口吻看着眼前的災難。 照片傳遞出一種對於不幸事件的冷漠和無動於衷的感受，令人反思人們對於他人苦難的態度，以及潛藏在内心深处的陰暗面。\" }\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[13],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主題是「惡作劇的快感」。照片中，一個小女孩站在燃燒的房屋前，露出狡黠的微笑，眼神中帶著一絲得意。背景的房屋正在被大火吞噬，消防員正在努力滅火，但小女孩似乎對這場災難漠不關心，反而表現出一種玩味和興奮的情緒，讓人猜測她可能是这场火灾的始作俑者，正享受着惡作劇帶來的快感。\"}\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[14],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片的主題是「孩子與動物的純真」。  画面中，一个小男孩站在一匹白馬面前，雙眼充滿着好奇和喜悦。他微笑着，低下頭，仿佛在和白馬进行着无声的交流。白马也低垂着头，似乎在温柔地注视着这个天真的小男孩。 整幅画面充满了童真和溫馨，突显了孩子和动物之间纯真无邪的互動，令人想起美好的童真時代，以及大自然带来的简单快乐。\"}\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[15],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片的主題是「貓咪的聚會」。  這張照片裡的貓咪們，看起來就像在開一場盛大的貓咪聚會，牠們或坐或站，神態各異，有的慵懶地晒着太陽，有的互相依偎着，有的好奇地打量着周圍的环境，有的則面帶警惕地注视着鏡頭。 整幅画面充满了可愛和生氣，充满了歡樂和温暖，讓人感受到貓咪們的生活簡單而充實，也感受到貓咪之間的默契和互相陪伴。\"}\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        "如果我說那張照片主題是「凝視」呢？",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片的主題是「凝視」。 照片中的每隻貓咪都直勾勾地凝视着前方，眼神堅定而深邃，彷彿各自有着自己的思考，又像是在觀察著這個世界，每一雙眼睛都充满了故事。牠們看似靜止不動，卻充滿著靜默的力量，帶給觀者一種神秘而難以言喻的氛圍。  照片帶給觀者思考：究竟貓咪們在凝視著什麼？牠們的眼中是否充滿著智慧和秘密？照片以簡潔的構圖和貓咪們一致的眼神，成功地營造出「凝視」的主題，引發觀者的好奇心和深思。\"}\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[16],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片的主題是「雨中沉思」。 雨滴落在透明的雨傘上，泛起陣陣涟漪。 畫面模糊的背景是茂密的樹林，給人一種靜谧安逸的感受。雨滴透過雨傘，在傘面上形成一個個圓形的光點，如同人生中闪耀的回憶或憧憬。照片以雨傘作為一種媒介，將人與自然緊密地聯繫在一起。\"}\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[17],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主題是「不服輸的倔強」。 圖中的嬰兒握緊小拳頭，眼神坚定，表情严肃，彷彿正在跟什麼人或事較劲。 他的小嘴緊抿着，好像在说：“我就不！”  这幅照片  幽默地表現了婴儿在面对挑战时的坚定和不服输的精神。\"}\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[18],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片的主題是「視角」。  一張手握著水晶球的照片，球中倒映著建築物的倒影，如同將真實世界縮小至掌心一般。  而模糊的背景则是真实的建築物，与球中倒影形成了鮮明的对比。  這張照片带給观者一种奇妙的感受，讓人思考視角的变化是如何影響我们对世界的理解。 也暗示了：真實世界可以通過不同的方式呈現， 即使再大的世界，也能握在手中。\"}\n\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        "用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"這張照片的主題是「視角」。  一張手握著水晶球的照片，球中倒映著建築物的倒影，如同將真實世界縮小至掌心一般。  而模糊的背景则是真实的建築物，与球中倒影形成了鮮明的对比。  這張照片带給观者一种奇妙的感受，讓人思考視角的变化是如何影響我们对世界的理解。 也暗示了：真實世界可以通過不同的方式呈現， 即使再大的世界，也能握在手中。\"}\n\n\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[19],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主題是「企鵝的親密互動」。  畫面中，两只小企鵝站在雪地上，一隻企鵝親昵地依偎在另一隻企鵝身旁，牠們柔軟的絨毛在雪地里格外顯眼，呈現出一种温馨而可爱的画面。照片捕捉了企鵝之間的親密互动，展现出牠們之間的感情，  以及在严酷的环境中，互相依赖、互相支持的温暖，令人感受到生命在极地環境中的顽强与美丽。\"}\n\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        "如果我說照片的主題是「依偎」呢？",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片的主題是「依偎」。  兩隻小企鵝在冰天雪地中依偎在一起，一隻企鵝將頭靠在另一隻企鵝的身上，呈現出非常親密、溫暖的畫面。 牠們柔軟的絨毛在雪地中格外顯眼，彷彿在寒冷的環境中彼此給予對方慰藉，體現出在逆境中彼此扶持的温暖和愛意。 照片也傳達出生命堅強、勇敢面对困难的寓意，  讓人聯想到親情和友情的力量，  以及生命在自然環境中  互相扶持  和  互相依存 的美好與溫馨。\" }\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[20],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片的主題是「老舊建築的寂靜」。  照片捕捉到一座老舊建築的背面，斑駁的牆面、凌亂的管道，以及泛黄的牆體，透露着歲月的痕跡。  水泥建築物上的窗戶泛著光，像是這座建築物曾有過的輝煌歷史。 夕陽斜照，建築物被籠罩在一片橙色的光影中，也透露出一種滄桑和寂靜。  這張照片充滿了懷舊和憂鬱的氣氛，让人联想起过去，思考时间的流逝以及歲月的无情。\" }\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[21],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主題是「空中旅行的日常」。 照片展示了機艙內的景象，乘客坐在座位上，頭頂是置物櫃，座椅背後貼著機上服務的宣傳。畫面透露出一種平靜和日常感，让人想起飞机起飞前，乘客们怀着各自的心情等待着旅途的開始。\"}\n\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[22],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主題是「午后的甜蜜」。  照片裡，一杯 Godiva 巧克力飲料靜靜地躺在車上的杯架中，   吸管插入杯中， 像是等待著主人隨時可以享受它的甜蜜。   咖啡的顏色和香气仿佛瀰漫在空氣中，   讓人忍不住想  親嘗一口它的濃郁與香醇。  这幅照片  散發出一種愜意的氛圍，讓人聯想到   午后阳光灑落在車上的時候，   獨自享受一杯咖啡的甜蜜和舒適。\" }\n\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[23],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片的主題是「水鄉風情」。 照片展现了一條寧靜的運河，水波清澈，岸边是充滿著綠意的建築物。  一艘小船緩緩地在運河中航行， 船上的人們歡声笑語，  盡情享受着運河的美景。 一隻白鷺站在路燈上， 靜靜地欣賞著水上的風光。   整個畫面透露出一種輕鬆、寧靜的氣氛，  讓人感受到城市中的宁靜之美，   以及生活中的慢步調和閒適。\" }\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[24],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主題是「好奇」。 照片中的小熊猫站在木樁上，一雙圓滾滾的眼睛直勾勾地盯着鏡頭，嘴巴微張，表情好奇， 彷彿正在觀察著周圍的環境，也充滿了對攝影師的探索和詢問。 小熊猫的姿态充满着灵动，让人感受到牠  天真、可愛  以及對世界充满好奇  的天性。\" }\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[25],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主題是「田園鄉村鐵道」。  照片中有一條筆直的鐵軌蜿蜒在广阔的鄉村田野中。 鐵軌两旁的綠色草地、黃色稻田和白雲，  展現出  寧靜、祥和、自然的景觀，   讓人  感受  鄉村  生活  的  慢步調，   以及  心靈  的  平靜   。照片  仿佛   帶  人們  回味  兒時   在   鄉村  中   漫遊  的   美好  回憶，  或是  想像  一段   放鬆   、  自由  的   旅行   。\"}\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        "句子不完整\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主題是「田園鄉村鐵道」。 照片中有一條筆直的鐵軌蜿蜒在广阔的鄉村田野中。 鐵軌两旁是充滿著綠意的草地、黃色的稻田和白雲，  展現出  寧靜、祥和、自然的景觀，   讓人  感受  鄉村  生活  的  慢步調，   以及  心靈  的  平靜。  道路  一旁   還  可以  看見   一個  白  色的   房子   。   整个画面透露出一種輕鬆、宁靜的氣氛，  让人感受到城市中的宁靜之美，   以及  生活中的慢步調和閒適。\" }\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        "去想想看，鐵道的盡頭通往何方？\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主題是「田園鄉村鐵道」。 照片中有一條筆直的鐵軌蜿蜒在广阔的鄉村田野中。 鐵軌两旁是充滿著綠意的草地、黃色的稻田和白雲，  展現出  寧靜、祥和、自然的景觀，   讓人  感受  鄉村  生活  的  慢步調，   以及  心靈  的  平靜。   照片  仿佛   帶  人們  回味  兒時   在   鄉村  中   漫遊  的   美好  回憶，  或是  想像  一段   放鬆   、  自由  的   旅行   。   鐵道  的   尽头   消失   在   遠  處  的  山  林   之中   ，  让人  不免  想要  知道  它  會   通往   何方  ，  以及   前方  的  风景  。  也许  那裡  藏   着  一段   奇妙   的   旅程   ，  或   是  另一个  与  众   不同的   世界   。\"}\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[26],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主題是「豹」或「動物園」。 照片中有一隻  豹子   在   籠子   裡   。牠   的眼神   锐利   ，   彷彿  隨時  準備  要  出擊   。   笼子   外  ，  是一   片   绿色的  树木   ，  可以   想像  牠   在   野外  ，  生活  在   茂密   的   森林   之中   。  然而  现在  牠   卻  被  關  在   籠子   裡   ，  眼神   中   透露   出   一种   悲伤  和   无奈  。照片   反映   了   野生  動物   在   人类  文明   下  ，   面临  的   困境  ，  以及   动物  园   对  野生  動物   的   保護   和   展覽  的   冲突   。\"}\n\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        "如果我說主題是「伺機而動」呢？\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主題是「伺機而動」。 照片中的  豹  被   关  在   笼子   裡   ，  牠  虽然  身处  笼中  ，   眼神   却   锐利  ，   警觉   地  观察  着  周围   的   环境   。   牠  紧贴  木   桩   ，  随时  准备  要  跃   出   去   。  从  牠   的表情   中   ，  我们   不難   感受   到   牠  想要  摆脱  束缚  ，  回到   大自然   的   渴望   。   这  也   让我们   不得不  思考  人类   與   野生  動物   之间  ，  如何   和平   共存   的問題   。\"}\n\n\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        "輸出的句子詞與詞之間不要有空白\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主題是「伺機而動」。照片中的豹被关在笼子裡，牠虽然身处笼中，眼神却锐利，警觉地观察着周围的環境。牠紧贴木桩，随时准备要跃出去。从牠的表情中，我们不難感受到牠想要摆脱束缚，回到大自然的渴望。这也讓我們不得不思考人類與野生動物之间，如何和平共存的的問題。\"}\n\n\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[27],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主题是「牆上的艺术」。   图片中是一张悬挂在墙上的   艺术   作品。   画面中   的人物   以   抽象   的   形式   呈现   ，   背景   则   充满了   朦胧  和   梦幻   的   色彩   ，  給   人   一种  飘渺   的   感觉   。  画面  的   周围   有一  条  黑色的  边  ，  也  增加了  作品  的   层次  和   立体   感   。   透过  这  张  照片   ，  我们   不难  想像   这  是   一件  充满了   艺术  气息   的作品   ，   以及   作者  想  通过   这  张  画  所   表达  的   理念   。   或许  它   在  诉说着   爱情   、  梦幻   ，  或者   是对   生活   的   思考   。   总  之   ，  这  是一  件   耐  人  寻味   ，   让人  想要  不断  探索  和   思考  的   艺术   作品   。\"}\n\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        "詞和詞之間不要空白\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主题是「墙上的艺术」。图片中是一张悬挂在墙上的艺术作品。画面中的人物以抽象的形式呈现，背景则充满了朦胧和梦幻的色彩，给人一种飘渺的感觉。画面的周围有一条黑色的边，也增加了作品的层次和立体感。透过这张照片，我们不难想像这是  一件充满了艺术气息的作品，以及作者想通过  这  张  画  所表达  的   理念  。或许它在诉说着爱情、梦幻，或者是对生活的思考。总之，这是一  件   耐  人  寻味，让人想要不断探索和思考的艺术作品。\"}\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[28],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主题是「日本文化」。  图片中是一个日本女性穿  着   传统   服饰和服的宣传海报。   她   优雅  、  美丽  的   脸庞   以及   华  麗  的   和服  ，  让人   感受到   日本  的   传统   文化   的   魅力  ，  以及   大和   民族   的   美感  。   同时  ，  海报  上   还  印  着   一些  日语  ，  这  也   更加   强调   了  海报  的   日本  元素。\"}\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        "如果我說主題是「美，在大街上」會不會更好？",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主题是「美，在大街上」。图片中是一张日本女性穿着传统服饰和服的宣传海报，   她   优雅  、  美丽  的   脸庞   以及   华  麗  的   和服  ，   让人   感受到   日本  的   传统   文化   的   魅力  ，   以及   大和   民族   的   美感  。   画面  上  的   她  眼神   深邃  ，  仿佛  正在  欣赏  街  上  的   景色   ，  或   是   回味   过往  的   时光  。   照片   所  展现   的   是   一种   古典  与   现代   交織  的   美感   ，  让人   感受   到  ，  美   无处   不在   ，   即使   是在   繁华   的   都市   街头  。   同時  ，  海报  上   还  印  着   一些  日语  ，  也  更加   强调   了  海报  的   日本  元素  ，  以及  日本  文化   的   獨特  之處   。\"}\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[29],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主題是「衛生習慣」。照片中，是一張放滿  洗碗精   和   海绵   的   洗手台   。畫面   顯得   凌亂   、  脏污   ，   看起來   像是   有人   急着   洗   東西  ，   卻  又  忘記   將   洗   东西  的   东西  放   好   。   照片   反映  了   生活  中  ，  人們  經常  会   遇到   的   小  困擾   ，   以及   在   匆忙  中   難  免  会   忽略   的   細節  。  这  也   提醒   我們  要  注重   卫生   习惯  ，   保持   整洁   的  环境  ，   讓   生活  更加   美好   。\"}\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        "如果主題是「難過」呢？從菜瓜布看出難過的神情",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主题是「难過」。  画面中， 一  个   菜瓜布   被   遺忘   在   洗手台上，  它  像  一个   伤心   的   小   孩  一样   ，  孤独  地   躺   着   。   上面   附   着  的   泡沫   ，  仿佛  是  牠  的眼泪   ，  一  点   一  点   地   滑  落   。   这   也  讓我們  联想  到   这  只   菜瓜布  ，   可能  曾經   被   主人   經常   使用   ，   為  主人   清洗  碗  盘   ，   付出   辛劳  。   然而  现在  ，   它   卻   被  主人   遗弃  ，   躺在   冰冷  的   洗手台上   ，  感受   着   孤單  和   失落。\"}\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[30],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主題是「驚訝」。   照片   中   是一個   女生   ，  她  張  著   嘴巴   ，   眼睛   睁大   ，  驚訝   地   看着   鏡頭   。   我們   不難   想像   她  或許  正  在   遇到   一件  意   外   的事情  ，  或是  看到   令  她   感到  不可思议   的   景象  ，   表情   中   透露   着   浓   濃   的   驚奇   和   好奇   。\"}\n\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[31],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主题是「城市彩虹」。  照片中是一道   出现在   城市   高楼   和   樹木   之间   的   彩虹  。   彩虹   的颜色   鲜艳  、   美丽  ，  却  又  带着   一种  梦幻   的   感觉  ，  仿佛  是  从   现实   世界   中   跳跃   出来  的   奇幻   景象  。  照片  所  展现   的   是   一种   大自然   的   奇妙   ，  以及   人类   生活   与   自然   融合   的   美好   。\"}\n\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[32],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主題是「獨處」。  照片中，一個人  正  在   電腦   前  喝  著  湯  ，  屏幕  上   放  着   一   部   電視   劇  ，   畫面   中   是   兩  位  演員   開心   的  笑容   。   但是  ，   照片  裡   的   主人  ，   卻   是   独自  一人   ，  独自   享受  着   簡單   的  美食  ，   安靜  地   觀賞  着   電視   劇   。這  种  情景   給   人  一種  孤独  而   宁静   的   感受   。\"}\n\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[33],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主題是「歡樂」。   照片  中   是一   个   穿着   色彩  鲜艳   的  服装  ，   戴  着   红   色   假  发   的   小  丑  ，   他   正   用   手   捂   着  嘴巴   ，  大声   喊叫   着  ，   脸上   露出  着   夸张  的   笑容   。   从  他   的  表情   中  ，  我們  可以  感受到   他   的  热情   、   活潑  ，  以及   想要  将  歡乐   带给   大家  的   心情  。   这  种  欢乐  和  热情   的   氛围   ，  让人   情不自禁   地   想要  加入  到   他   的  快乐   中  ，  一起  感受  生活  的  美好  。\"}\n\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[34],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主題是「希望」。  画面   中   是一  个   身   穿   帽  衫  的   人  ，  站在  高  处   ，   面向  远   方   的  城市  ，   手   中   握   着   一支  燃   烧   着   的   火   柴   ，   在   夕阳   的   照耀  下   ，  火  柴   的光   芒  ，  如同  一颗  闪烁  的   星   星   ，  在   夜   空  中   闪耀  。   这  张   照片  充满了  希望   和   梦想   的   味道   ，  让人  联想到  在  艰难  的  困境   中  ，  依然  坚持  着   追求   自己  的   梦想  ，   也  仿佛   在   说  着  ，   只要   怀  抱   着   希望  ，  生命   总   會   有   光明   的   未来   。\"}\n\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[35],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主题是「自我探索」。画面中，一个男人的剪影站在海边，   夕陽   的   余晖   洒  在  他   的   身上   。   更   令人  驚嘆  的  是  ，   他的  身體   是  透明  的  ，  裡面   卻   映  照  出  另  一個   自己  ，   同樣   站在   海   邊   ，  面对   着   远   方   的   日   落  。   這   個   畫面   如同   一面  镜子   ，  映照  出   人   内心   的  挣扎   和  矛盾   ，  或许   代表   着  ，   人   生   的   道路  上   ，  我们  會  不斷  地   遇到   选择   ，  也會  在   不断   的  选择   中   ，  探索   和   認識   自己   的   內   心   。\"}\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[36],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主題是「夕陽下的音樂」。  畫面中，一位女孩坐在海邊，   背對   着   鏡頭   ，  手中   抱   着   吉他   ，   低頭   專注   地   彈奏   着   。  她的   身旁   放   着   一杯   咖啡  ，  夕陽  餘晖   洒   在   她   的  身上  ，  海  面   波光   粼   粼   。  這  個   畫面   散發   出   一種  寧静   、   舒適   的  氣氛   ，  让人   联想到   在   傍晚   的   海边  ，   享受  着  悠闲   的  时光   ，   聆听  着   音乐   ，   感受   着   生活   的   美好   。\"}\n\n\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[37],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主題是「等待」。  照片中，  一座   木製  的   長   椅   安靜  地   佇   立  在   樹蔭  下  ，  等待  着   人  們  的   到來   。  椅子  的  形  狀  优雅   ，   材質  古樸   ，   彷彿   見證  了   許   多  人   生   故事  ，  也   承載   着  许多   甜蜜  或   悲伤   的  回忆  。  画面   充满了  宁静   ，  让人   感受到   一種  靜  待  的   力量  ，  等待  着  ，   与  心   爱   的人  ，   在  這  裡   相遇  ，   享受   生活  的  美好   。  或許  ，   它   也  在   等待  着   ，  人們  在  忙碌  的  生活中   ，  找到  一個  角落  ，  放   下   包袱   ，   靜靜  地  思考   人生   ，   回味   生命   的  真  谛  。\"}\n\n\n\n\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[38],
        "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"description\": \"照片主题是「害羞」。照片中，  一位   女生   对着   镜头   ，   表情   显得   有些   害羞   和  不自然。    她的  眼睛   看着   镜头   ，   嘴唇  微  张   ，   手  則   放在   腿上，   像是   有些   局促  ，   不知   所   措   。   她  穿  着   一   件   浅蓝  色   的  上  衣   ，   肩  部   略   显   露  出  ，  散  发   着  一种   清純  和   甜美  的   气息  。   照片  让人   聯想到  一個  青涩  、  害羞  的  女孩  ，  在   面对   镜头  時  的   心情   ，   以及   少女  的   純   真   和   美好  。\"}\n\n\n```",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)