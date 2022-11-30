import tkinter as tk

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

def car(x, y, size, color):
    #長方形小
    canvas.create_rectangle(
        100*size+x, 50*size+y, 200*size+x, 100*size+y,
        fill=color,
        tag="rect_001"
    )
    #長方形大
    canvas.create_rectangle(
        50*size+x, 100*size+y, 250*size+x, 180*size+y,
        fill=color,
        tag="rect_002"
    )
    #左車輪
    canvas.create_oval(
        50*size+x, 180*size+y, 80*size+x, 210*size+y,
        fill="BLACK",
        tag="oval_001"
    )
    #右車輪
    canvas.create_oval(
        220*size+x, 180*size+y, 250*size+x, 210*size+y,
        fill="BLACK",
        tag="oval_002"
    )
    
car = car(45, 45, 1/5, "Blue")

canvas.move(car, 200, 0)

#画面をそのまま表示
frm.mainloop()