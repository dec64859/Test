import tkinter as tk
import time

class Cannonball:
    ball=None
    
    def __init__(self,x,y,size,color):
        self.x=x
        self.y=y
        self.size=size
        self.color=color

    def ball_create(self,x,y,size,color):
        self.ball=canvas.create_oval(
            100*size+x, 50*size+y, 150*size+x, 100*size+y,
            fill=color,
            tag="rect_001"
        )
    
    def ball_move(self, x, y):
        canvas.move(self.ball, x, y)
        
def cannon(x,y,size,color):
    #長方形小
    canvas.create_rectangle(
        100*size+x, 50*size+y, 150*size+x, 100*size+y,
        fill=color,
        tag="rect_001"
    )
    #長方形大
    canvas.create_rectangle(
        50*size+x, 100*size+y, 200*size+x, 150*size+y,
        fill=color,
        tag="rect_002"
    )
        
#Tkクラス生成
frm = tk.Tk()
#画面サイズ
frm.geometry('600x400')
#画面タイトル
frm.title('tk')

#フォーム上に描画エリアを作成
canvas = tk.Canvas(
    frm,
    width=600,
    height=400,
    background="#fff"
)
canvas.pack()

cannon(200, 300, 1/3, "GREEN")

ball1=Cannonball(200, 300-50/3, 1/3, "BLACK")
ball1.ball_create(200, 300-50/3, 1/3, "BLACK")
move_change=True
current_y=300-50/3
y=0
while True:
    current_y += y
    ball1.ball_move(0, y)
    if(move_change):
        y=-5     
    time.sleep(0.02)
    frm.update()

#画面をそのまま表示