import tkinter as tk

#Tkクラス生成
frm = tk.Tk()
#画面サイズ
frm.geometry('1000x600')
#画面タイトル
frm.title('tk')

#フォーム上に描画エリアを作成
canvas = tk.Canvas(
    frm,
    width=1000,
    height=600,
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

#10x10の描画
for i in range(10):
    for j in range(10):
        if((i+j)%2==0):
            car(45*j, 45*i, 1/5, "Blue")
        else:
            car(45*j, 45*i, 1/5, "Red")



#画面をそのまま表示
frm.mainloop()