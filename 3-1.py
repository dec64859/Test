import tkinter as tk
import time

class Car:
    body01=None
    body02=None
    l_wheel=None
    r_wheel=None
    
    def __init__(self,x,y,size,color):
        self.x=x
        self.y=y
        self.size=size
        self.color=color

    def car_c(self,x,y,size,color):
    #長方形小
        self.body01=canvas.create_rectangle(
            100*size+x, 50*size+y, 200*size+x, 100*size+y,
            fill=color,
            tag="rect_001"
        )
    #長方形大
        self.body02=canvas.create_rectangle(
            50*size+x, 100*size+y, 250*size+x, 180*size+y,
            fill=color,
            tag="rect_002"
        )
    #左車輪
        self.l_wheel=canvas.create_oval(
            50*size+x, 180*size+y, 80*size+x, 210*size+y,
            fill="BLACK",
            tag="oval_001"
        )
    #右車輪
        self.r_wheel=canvas.create_oval(
            220*size+x, 180*size+y, 250*size+x, 210*size+y,
            fill="BLACK",
            tag="oval_002"
        )
    
    def car_move(self, x, y):
        canvas.move(self.body01, x, y)
        canvas.move(self.body02, x, y)
        canvas.move(self.l_wheel, x, y)
        canvas.move(self.r_wheel, x, y)
        
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

car1=Car(40, 40, 1/5, "BLUE")
car1.car_c(40, 40, 1/5, "BLUE")
move_change=True
current_x = 40
x=0
while True:
    current_x += x
    car1.car_move(x, 0)
    if(move_change):
        x=5
    else:
        x=-5  
    if(current_x>600-200/5):
        move_change=False
    elif(current_x<0):
        move_change=True      
    time.sleep(0.02)
    frm.update()

#画面をそのまま表示
