#이미지 회전및 흐리게 
# PIL 모듈에서 몇 개의 클래스를 포함시킨다.
from PIL import Image, ImageTk,ImageFilter
import tkinter as tk

# 윈도우를 생성하고 윈도우 안에 캔버스를 생성한다
window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

img = Image.open("D:\\lenna.png")
out = img.filter(ImageFilter.BLUR) #이미지를 흐리게 만든다.
#out = img.rotate(45)    #이미지를 회전시킨다

tk_img = ImageTk.PhotoImage(out)
canvas.create_image(250, 250, image=tk_img)

window.mainloop()
