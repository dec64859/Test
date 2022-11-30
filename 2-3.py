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
    
def car_delete(x, y, size):
    canvas.create_rectangle(
        50*size+x, 50*size+y, 255*size+x, 215*size+y,
        fill="White",
        width=0,
        tag="rect_delete_001"
    )

#数値の入力
def inputval():
    val = input()
    try:            
        val = int(val)
        gyou = val/10
        gyou = int(gyou)
        retu = val%10

        if(val < 0 or 99 <val):
            print('Error')
            return inputval()
        else:
            car_delete(45*retu, 45*gyou, 1/5)
            return inputval()
            
    except:
        print('Error')
        return inputval()

#10x10の描画
for i in range(10):
    for j in range(10):
        if((i+j)%2==0):
            car(45*j, 45*i, 1/5, "Blue")
        else:
            car(45*j, 45*i, 1/5, "Red")
 
inputval()

#画面をそのまま表示
frm.mainloop()