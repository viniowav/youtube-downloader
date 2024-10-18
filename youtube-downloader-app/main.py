from youtubesearchpython import*
from yt_dlp import*
from os import*
from tkinter import*


root=Tk()
root.geometry('900x600')
root.title('YouTube Downloader')
root.config(bg='#2F2F32')
root.iconbitmap()

btn_arq = Button(root, text = "Arquivo")
btn_edit = Button(root, text = "Editar")
btn_see = Button(root, text = "Ver")
btn_tools = Button(root, text = "Ferramentas")
btn_help = Button(root, text = "Ajuda")

btn_arq.pack()
btn_edit.pack()
btn_see.pack()
btn_tools.pack()
btn_help.pack()

root.mainloop()
