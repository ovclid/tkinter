import tkinter as tk
import random
import time

win = tk.Tk()
win.geometry("500x400")

temp = ["가위", "바위", "보"]
win_con = {"가위" : "보", "바위" : "가위","보" : "바위"}

com_btn1 = tk.Button(text = "??")
com_btn1.place(x=250, y=100, width=150, height =30)
cnt = 0
my_win = 0
com_win = 0
draw = 0

def rsp(my):
    global cnt, my_win, com_win, draw
    
    cnt = cnt + 1
    com_btn1.config(fg = "red")
    com_btn1.invoke()
    
    t = random.choice(temp)
    com_btn1.config(text = t)
    com_btn1.config(fg = "blue")
    
    if my == t:
        draw = draw + 1
        print("비김")
    elif win_con[my] == t:
        my_win = my_win + 1
        print("이김")
    else:
        com_win = com_win + 1
        print("you lose")
    print("총 : ", cnt, "  승리: ", my_win, "  패배: ", com_win, "  비김: ", draw, "\n")
    
    return

def set_mine1():
    rsp("가위")
   
    
def set_mine2():
    rsp("바위")

def set_mine3():
    rsp("보")
    
btn1 = tk.Button(text = "가위", command = set_mine1)
btn1.place(x=30, y=40, width=150, height =30)

btn2 = tk.Button(text = "바위", command = set_mine2)
btn2.place(x=30, y=100, width=150, height =30)

btn3 = tk.Button(text = "보", command = set_mine3)
btn3.place(x=30, y=150, width=150, height =30)





win.mainloop()
