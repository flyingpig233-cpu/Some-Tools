import re
result_words = ["" for i in range(26)]
arr = []
words = ["the", "be", "of", "and", "to", "in", "he", "that", "I", "a", "can", "'re", "have", "has", "it", "that", "for", "they", "with", "as", "not", "on", "she", "at", "by", "this", "he", "but", "often", "play", "like", "'s"]


def analysis(ws):
    asb = [0 for i in range(26)]
    for i in range(26):
        for j in range(len(words)):
            if re.search(words[j].lower(), ws[i].lower()) != None:
                asb[i] += 1
    if max(asb) > 0:
        a = ws[asb.index(max(asb))]
        print("机器筛查结果：%s (仅供参考)" % a)
    else:
        print("暂时还找不到符合条件的呀！")
        
        
        
try:
    with open("source.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    content = input("请输入你要破译的字符：")

for word in content:
    word_ascii = ord(word)
    if  64 < word_ascii < 91:
        for i in range(26):
            result = word_ascii + i
            if result > 90:
                result = 64 + (result - 90)
            arr.append(chr(result))
    elif 96 < word_ascii < 123:
        for i in range(26):
            result = word_ascii + i
            if result > 122:
                result = 96 + (result - 122)
            arr.append(chr(result))
    else:
        for i in range(26):
            arr.append(word)


for i in range(26):
    print("第%d种可能：\t" % (i + 1), end="")
    for j in range(len(content)):
        result_words[i] += arr[26 * j + i]
    print(result_words[i])
analysis(result_words)
    
    
    
    
    