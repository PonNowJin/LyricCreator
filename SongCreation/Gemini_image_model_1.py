import os
import google.generativeai as genai
from API_setting import LLM

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini.

  See https://ai.google.dev/gemini-api/docs/prompting_with_media
  """
  file = genai.upload_file(path)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

# Create the model
generation_config = {
  "temperature": 2,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "application/json",
}

llm = LLM()
model = llm.getModel(generation_config, system_instruction="你是一位極具創意與哲理的藝術家")

prompt = '請先為照片找出一個主題(帶有詩意、一句話），再描述圖中的情景、感情、故事或心情，用繁體中文回答'

# TODO Make these files available on the local file system
# You may need to update the file paths
'''
files = [
  upload_to_gemini(os.path.join(ROOT_DIR, "SongCreation", "SampleImage", "1.jpeg"), mime_type="application/octet-stream"),
  upload_to_gemini(os.path.join(ROOT_DIR, "SongCreation", "SampleImage", "2.jpeg"), mime_type="application/octet-stream"),
  upload_to_gemini(os.path.join(ROOT_DIR, "SongCreation", "SampleImage", "3.jpeg"), mime_type="application/octet-stream"),
  upload_to_gemini(os.path.join(ROOT_DIR, "SongCreation", "SampleImage", "4.jpeg"), mime_type="application/octet-stream"),
  upload_to_gemini(os.path.join(ROOT_DIR, "SongCreation", "SampleImage", "5.jpeg"), mime_type="application/octet-stream"),
  upload_to_gemini(os.path.join(ROOT_DIR, "SongCreation", "SampleImage", "6.jpeg"), mime_type="application/octet-stream"),
  upload_to_gemini(os.path.join(ROOT_DIR, "SongCreation", "SampleImage", "7.jpeg"), mime_type="application/octet-stream"),
  upload_to_gemini(os.path.join(ROOT_DIR, "SongCreation", "SampleImage", "8.jpeg"), mime_type="application/octet-stream"),
  upload_to_gemini(os.path.join(ROOT_DIR, "SongCreation", "SampleImage", "9.jpeg"), mime_type="application/octet-stream"),
  upload_to_gemini(os.path.join(ROOT_DIR, "SongCreation", "SampleImage", "10.jpeg"), mime_type="application/octet-stream"),
  upload_to_gemini(os.path.join(ROOT_DIR, "SongCreation", "SampleImage", "11.jpeg"), mime_type="application/octet-stream"),
  upload_to_gemini(os.path.join(ROOT_DIR, "SongCreation", "SampleImage", "12.jpeg"), mime_type="application/octet-stream"),
  upload_to_gemini(os.path.join(ROOT_DIR, "SongCreation", "SampleImage", "13.jpeg"), mime_type="application/octet-stream"),
  upload_to_gemini(os.path.join(ROOT_DIR, "SongCreation", "SampleImage", "14.jpeg"), mime_type="application/octet-stream"),
  upload_to_gemini(os.path.join(ROOT_DIR, "SongCreation", "SampleImage", "15.jpeg"), mime_type="application/octet-stream"),
  upload_to_gemini(os.path.join(ROOT_DIR, "SongCreation", "SampleImage", "16.jpeg"), mime_type="application/octet-stream"),
  upload_to_gemini(os.path.join(ROOT_DIR, "SongCreation", "SampleImage", "17.jpeg"), mime_type="application/octet-stream"),
  upload_to_gemini(os.path.join(ROOT_DIR, "SongCreation", "SampleImage", "18.jpeg"), mime_type="application/octet-stream"),
  upload_to_gemini(os.path.join(ROOT_DIR, "SongCreation", "SampleImage", "19.jpeg"), mime_type="application/octet-stream"),
  upload_to_gemini(os.path.join(ROOT_DIR, "SongCreation", "SampleImage", "20.jpeg"), mime_type="application/octet-stream"),
]
'''

'''
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
    "```json\n{\"description\": \"透過破碎的鏡片，我們看到的不僅僅是女人美麗的面龐，而是多重的倒影，彷彿是她內心世界的映射。 城市的冰冷建築在背景中模糊，與她迷離的眼神形成對比，暗示著現代社會中，人們常常迷失在自我認知的迷宮裡，追尋著真實的自己。 照片以一種破碎的美感，呈現出現代人內心的複雜和多面性，以及在都市生活中對自我身份的探索與追尋。\" }\n\n```",
    ],
},
{
    "role": "user",
    "parts": [
    files[3],
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
    files[4],
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
    files[5],
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
    files[6],
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
    files[7],
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
    files[8],
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
    files[9],
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
    files[10],
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
    files[11],
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
    files[12],
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
    files[13],
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
    files[14],
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
    files[15],
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
    files[16],
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
    files[17],
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
    files[18],
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
    files[19],
    "請先為照片找出一個主題，再描述圖中的情景、感情、故事或心情，用繁體中文回答",
    ],
},
{
    "role": "model",
    "parts": [
    "```json\n{\"description\": \"照片主題是「等待」。  照片中，  一座   木製  的   長   椅   安靜  地   佇   立  在   樹蔭  下  ，  等待  着   人  們  的   到來   。  椅子  的  形  狀  优雅   ，   材質  古樸   ，   彷彿   見證  了   許   多  人   生   故事  ，  也   承載   着  许多   甜蜜  或   悲伤   的  回忆  。  画面   充满了  宁静   ，  让人   感受到   一種  靜  待  的   力量  ，  等待  着  ，   与  心   爱   的人  ，   在  這  裡   相遇  ，   享受   生活  的  美好   。  或許  ，   它   也  在   等待  着   ，  人們  在  忙碌  的  生活中   ，  找到  一個  角落  ，  放   下   包袱   ，   靜靜  地  思考   人生   ，   回味   生命   的  真  谛  。\"}\n\n\n\n\n```",
    ],
},
]
'''

chat_session = model.start_chat(history=[])
# chat_session.history.extend(history)

def send_message_with_image(image_path:str, text:str=''):
    if not image_path and not os.path.exists(image_path):
        print("send_message_with_image err: image_path錯誤")
        return 
    text = text + prompt
    image = upload_to_gemini(image_path)
    response = model.generate_content([image, text])

    return response.text


if __name__ == '__main__':
    path = '/Users/ponfu/Desktop/vs code/MusicCreation/SongCreation/SampleImage/IMG_4074.JPG'
    response = send_message_with_image(path)
    print(response)
