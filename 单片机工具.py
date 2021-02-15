import os
import pyperclip
count = 1
while True:
    string_out = ""
    os.system("cls")
    string = input()
    lenth  = len(string)
    string_list = list(string)
    string_out = ("char code texts_" + str(count) + "[" + str(lenth) + "][" + str(lenth * 2) + "] " "= { ")
    for i in range(0, lenth):
        string_out += ('"' + str(string_list[i]) + '"' + ("" if i + 1 == lenth else ", "))
    string_out += " };"
    count += 1
    pyperclip.copy(string_out)
    print("OK")
    input()
    
