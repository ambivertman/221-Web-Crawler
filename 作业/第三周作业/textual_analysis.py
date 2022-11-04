import jieba
import matplotlib.pyplot as plt
import matplotlib
import wordcloud


# 读取文本
def getFile(filepath):
    f = open(filepath, 'r', encoding='utf-8')
    text = f.read()
    f.close()
    return text


# 读取停用词
def getStopwords(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


# 统计词频
def wordFreq(filepath, text, topn):
    words = jieba.lcut(text.strip())
    counts = {}
    filepath_stopwords = input("请输入停用词文件的绝对路径(不需要手动添加转义字符):").replace('\\', '/')
    stopwords = getStopwords(filepath_stopwords)
    for word in words:
        if len(word) == 1:
            continue  # 剔除一些无意义的单字
        elif word not in stopwords:
            counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)  # 将分词得到词频词典转换为列表并排序
    output_path = filepath[0:-4] + '_词频统计.txt'
    f = open(output_path, 'w', encoding='utf-8')
    for i in range(topn):
        word, count = items[i]
        f.writelines(f"{word}\t{count}\n")
    f.close()
    print(f"文件已输出至:{output_path}")
    return output_path


# 输出词频直方图
def output_plot(filepath):
    f = open(filepath, 'r', encoding='utf-8')
    matplotlib.rcParams['font.family'] = 'SimHei'
    labels = []
    values = []
    for line in f.readlines():
        curline = line.strip().split('\t')
        labels.append(curline[0])
        values.append(int(curline[1]))

    plt.bar(labels, values)
    plt.show()


# 输出词云
def output_wordcloud(filepath):
    text = getFile(filepath)
    wcloud = wordcloud.WordCloud(font_path=r'C:\Windows\Fonts\simhei.ttf',
                                 background_color='white',
                                 max_words=20,
                                 width=1000,
                                 height=860,
                                 margin=2
                                 ).generate(text)
    wcloud.to_file(filepath[:-4] + '_词云.png')
    print(f"文件已输出至:{filepath[:-4] + '_词云.png'}")


if __name__ == '__main__':
    filepath = input("请输入文件的绝对路径(不需要手动添加转义字符):").replace('\\', '/')
    topn = eval(input("请输入n的值:"))
    text = getFile(filepath)
    output_path = wordFreq(filepath, text, topn)
    flag = True
    while (flag):
        print('''词频统计已完成!
        请选择输出的模式:
        1.输出词频直方图
        2.输出词云
        3.打印词频统计信息
        0.退出\n''')
        case = eval(input("输入相应序号以执行:"))
        if case == 1:
            output_plot(output_path)
        elif case == 2:
            output_wordcloud(output_path)
        elif case == 3:
            output_txt = getFile(output_path)
            print(output_txt)
        else:
            flag = False
