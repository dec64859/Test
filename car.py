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

#長方形を描画
canvas.create_rectangle(
    100, 50, 200, 100,
    fill="BLACK",
    tag="rect_001"
)
canvas.create_rectangle(
    50, 100, 250, 180,
    fill="BLACK",
    tag="rect_002"
)
canvas.create_oval(
    50, 180, 80, 210,
    fill="BLACK",
    tag="oval_001"
)
canvas.create_oval(
    220, 180, 250, 210,
    fill="BLACK",
    tag="oval_002"
)

Name=tk.Label(
    frm,
    text="Hibiki Hori",
    font=("MSゴシック", "20", "bold"),
    background="#fff"
)

Name.place(x=80, y=220)

#画面をそのまま表示
frm.mainloop()