import re
content = None
arr = []
result_words = ["" for i in range(26)]
words = ["the", "be", "of", "and", "to", "in", "he", "have", "has", "it", "that", "for", "they", "with", "as", "not", "on", "she", "at", "by", "this", "he", "but", "often", "play", "like"]

def analysis(ws):
    asb = [0 for i in range(26)]
    for i in range(26):
        for j in range(len(words)):
            if re.search(words[j].upper(), ws[i]) != None:
                asb[i] += 1
    if max(asb) > 0:
        print("机器筛查结果：%s (仅供参考)" % ws[asb.index(max(asb))])
    else:
        print("暂时还找不到符合条件的呀！")
try:
    with open("source.txt", "r") as f:
        content = re.sub("[^A-Za-z]", "", f.read())
except FileNotFoundError:
    content = re.sub("[^A-Za-z]", "", input("请输入你要破译的字符："))
for word in content.upper():
    word_ascii = ord(word)
    for i in range(26):
        result = word_ascii + i
        if result > 90:
            result = 64 + (result - 90)
        arr.append(chr(result))
for i in range(26):
    print("第%d种可能：\t" % (i + 1), end="")
    for j in range(len(content)):
        result_words[i] += arr[26 * j + i]
    print(result_words[i])
analysis(result_words)