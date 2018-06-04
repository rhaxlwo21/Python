import tkinter as tk

# 파일 메뉴에서 "열기"를 선택하였을 때 호출되는 함수
def open():
    pass
#파일 메뉴에서 "종료"를 선택하였을 때 호출되는 함수
def quit():
    window.quit()
def help():
    pass
def blur():
    pass
def sharpen():
    pass

# 윈도우를 생성한다
window = tk.Tk()

# Menu()를 사용하여 윈도우 안에 메뉴를 생성한다.
menubar = tk.Menu(window)
imgbar = tk.Menu(window)

# 메뉴바 안에 "파일" 메뉴를 생성한다.
filemenu = tk.Menu(menubar)
fileimg = tk.Menu(imgbar)

#"파일" 메뉴 안에 "열기" 메뉴항목을 추가한다.
filemenu.add_command(label="열기", command=open)
filemenu.add_command(label="종료", command=quit)
filemenu.add_command(label="도움말", command=help)
fileimg.add_command(label="흐리게", command=blur)
fileimg.add_command(label="선명하게", command=sharpen)

# "파일" 메뉴를 누르면 아래로 다른 메뉴가 확장되도록 한다.
menubar.add_cascade(label="파일", menu=filemenu)
menubar.add_cascade(label="이미지", menu=fileimg)

#윈도우 창의 메뉴로 menubar를 지정한다
window.config(menu=menubar)
window.mainloop()
