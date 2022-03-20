import jieba                # 分词
import numpy as np         # 矩阵运算
from matplotlib import pyplot as plt    # 绘图,数据可视化,用于直接显示统计图
from wordcloud import WordCloud         # 词云
from PIL import Image
from pymongo import MongoClient


client = MongoClient(host='127.0.0.1', port=27017)
col = client.hot.clo
result = col.find({}, {'_id': 0, 'introduce': 1})
temp = list()
for one in result:
    temp.append(one['introduce'].strip())
# print(''.join(temp))
# print(len(temp))
my_str = ''.join(temp)
client.close()



cut = jieba.cut(my_str)
string = ''.join(cut)
print(len(string))      # 17062词



img = Image.open('./static/images/2.png')       # 打开一个白底遮罩图
img_array = np.array(img)            # 将图片转换为数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="Hiragino Sans GB.ttc"
)
wc.generate_from_text(string)



# 绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')     # 是否显示坐标轴
# plt.show()      # 显示图片
plt.savefig('./static/images/word.png', dpi=500)











