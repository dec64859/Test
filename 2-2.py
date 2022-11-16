import tkinter as tk

#Tkクラス生成
frm = tk.Tk()
#画面サイズ
frm.geometry('1000x700')
#画面タイトル
frm.title('tk')

#フォーム上に描画エリアを作成
canvas = tk.Canvas(
    frm,
    width=1000,
    height=700,
    background="#fff"
)
canvas.pack()

def car(x, y, size, color):
    canvas.create_rectangle(
        100*size+x, 50*size+y, 200*size+x, 100*size+y,
        fill=color,
        tag="rect_001"
    )
    canvas.create_rectangle(
        50*size+x, 100*size+y, 250*size+x, 180*size+y,
        fill=color,
        tag="rect_002"
    )
    canvas.create_oval(
        50*size+x, 180*size+y, 80*size+x, 210*size+y,
        fill="BLACK",
        tag="oval_001"
    )
    canvas.create_oval(
        220*size+x, 180*size+y, 250*size+x, 210*size+y,
        fill="BLACK",
        tag="oval_002"
    )

for i in range(1, 6):
    for v in range(1, 6):
        car (i, v, 1/4, "BLUE")
        car (i, v, 1/4, "RED")

#画面をそのまま表示
frm.mainloop()