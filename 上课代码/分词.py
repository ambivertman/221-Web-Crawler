import jieba

text = open("./三国演义.txt", 'r', encoding='utf-8').read()
ws = jieba.lcut(text)
counts = {}

for w in ws:
    if len(w) == 1:
        continue
    else:
        counts[w] = counts.get(w, 0) + 1

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(15):
    w, n = items[i]
    print(w, n)
