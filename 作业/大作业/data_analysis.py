import json
import pandas as pd
import paddlehub as hub
import matplotlib.pyplot as plt
import datetime
import re
import os
from wordcloud import WordCloud

os.environ['CUDA_VISIBLE_DEVICES'] = '0'


# 情感打分
def rating(processing_data):
    data_content_list = [item['content'] for item in processing_data]
    senta = hub.Module(name='senta_bilstm')
    results = senta.sentiment_classify(texts=data_content_list, use_gpu=True, batch_size=1)
    wanted_results = []
    for k, result in enumerate(results):
        temp = {
            'sentiment_key': result['sentiment_key'],
            'positive_probs': result['positive_probs'],
            'datetime': processing_data[k]['progress'],
            'ctime': processing_data[k]['ctime']
        }
        wanted_results.append(temp)

    return wanted_results


with open(r"D:\Desktop\Utility\【S12 全球总决赛】小组赛 10 月 16 日 GAM vs TES_英雄联盟.json", 'r',
          encoding="UTF-8") as fp:
    data = fp.read()
data = json.loads(data)
# print(data[0])

wanted_data = []
rated_data = []
for item in data:
    temp_data = {"progress": datetime.timedelta(minutes=(item.get("progress", 0) // 60000)),
                 "content": re.sub(r'\s+', '', item.get("content", 0).strip()),
                 "ctime": datetime.datetime.utcfromtimestamp(item.get("ctime", 0))}
    wanted_data.append(temp_data)

rated_data = rating(wanted_data)

# 情感分析曲线
df = pd.DataFrame(rated_data)
df['datetime'] = df['datetime'].apply(lambda x: datetime.datetime.utcfromtimestamp(x.total_seconds()))
grouped = df.groupby(df['datetime'].dt.minute)
means = grouped.mean()
means.plot()
plt.show()
plt.savefig('scatter_plot.png')

# 词云
counts = {}
for content in wanted_data:
    text = content['content']
    counts[text] = counts.get(text, 0) + 1
wordcloud = WordCloud(font_path=r'C:\Windows\Fonts\simhei.ttf',
                      background_color='white',
                      max_words=50,
                      width=1000,
                      height=860,
                      margin=2).generate_from_frequencies(counts)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
