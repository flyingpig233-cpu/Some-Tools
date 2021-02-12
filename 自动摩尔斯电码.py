# -*- coding: GBK -*-

from pynput.mouse import Button, Controller
import time
mouse = Controller()
words = {" ": "F", "A": "12", "B": "2111", "C": "2121", "D": "211", "E": "1", "F": "1121", "G": "221", "H": "1111", "I": "11", "J": "1222", "K": "212", "L": "1211", "M": "22", "N": "21", "O": "222", "P": "1221", "Q": "2212", "R": "121", "S": "111", "T": "2", "U": "112", "V": "1112", "W": "122", "X": "2112", "Y": "2122", "Z": "2211",
        "1": "12222", "2": "11222", "3": "11122", "4": "11112", "5": "11111", "6": "21111", "7": "22111", "8": "22211", "9": "22221", "0": "22222", "?": "112211", ",": "221122", ".": "121212", "!": "2221", "'": "122221", "=": "21112", "/": "21121", ":": "222111", "-": "211112", '"': "121121", "@": "122121"}
base_speed = float(input("请输入一个滴的时间："))
click_point = (686, 817)
while True:
    obj = input("请输入想要发送的信息：").upper()
    mouse.position = click_point
    for i in obj:
        word_value = words[i]
        for j in word_value:
            if j != "F":
                mouse.press(Button.left)
                if j == "1":
                    time.sleep(base_speed)
                if j == "2":
                    time.sleep(base_speed * 3)
                mouse.release(Button.left)
                time.sleep(base_speed)
            else:
                time.sleep(base_speed * 4)
        time.sleep(base_speed * 3)



