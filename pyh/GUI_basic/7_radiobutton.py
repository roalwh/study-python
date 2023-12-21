from tkinter import *

root = Tk()
root.title("nado GUI")
root.geometry("640x480")

Label(root, text="메뉴를 선택하세요").pack()

burger_var = IntVar()
btn_vurger1 = Radiobutton(root,text="햄버거", value=1, variable=burger_var)
btn_vurger1.select()
btn_vurger2 = Radiobutton(root,text="치즈햄버", value=2, variable=burger_var)
btn_vurger3 = Radiobutton(root,text="치킨버거", value=3, variable=burger_var)
btn_vurger1.pack()
btn_vurger2.pack()
btn_vurger3.pack()

Label(root, text="음료를 선택하세요").pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라" ,variable=drink_var)
btn_drink1.select() 
btn_drink2 = Radiobutton(root, text="사이다", value="사이다" ,variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get()) # 선택된 라디오 버튼 값 조회
    print(drink_var.get()) # 음료중 선택된 값을 출력

btn = Button(root,text="주문", command=btncmd)
btn.pack()


root.mainloop()