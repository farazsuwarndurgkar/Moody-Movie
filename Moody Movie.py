import imdb
from tkinter import *
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from pygame import mixer

win = Tk()
win.iconbitmap("Moody Movie.ico")
win.geometry("270x480")
win.title("Moody Movie")
win.configure(bg='lavender')

def note():
    showinfo("Moody Movie Info","sad-drama\nDisgust-Musical\nAnger-Family\nAnticipation-Thriller\nFear-Sport\nEnjoyment-Thriller\nTrust-Western\nSurprise- Film-Noir")
    #alert(title="Moody Movie Info",text="sad-drama\nDisgust-Musical\nAnger-Family\nAnticipation-Thriller\nFear-Sport\nEnjoyment-Thriller\nTrust-Western\nSurprise- Film-Noir",button='OK')
    return True

def clear():
    data.set("")
    return True

def toggle(tog=[0]):
    tog[0]= not tog[0]
    if tog[0]:
        win.configure(bg='gray')
    else:
        win.configure(bg='lavender')
    return True

def movie():
    ia = imdb.IMDb()
    keyword = data.get()
    result=[]
    search = ia.get_keyword(keyword)
    for i in range(5):
        result.append(search[i])
        #print(*result,sep="\n")
        #showinfo("Moody Movie result",search[i])
        #Label(win, text = search[i],font =("Times", 14)).grid()
        #print(search[i])
        print(result)
    return True

def music():
    mixer.init()
    file = 'lol.mp3'
    mixer.music.load(file)
    mixer.music.play()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    mixer.music.pause()

                if event.key == pygame.K_r:
                    mixer.music.unpause()
                if event.key == pygame.K_q:
                    running = False
    

def exit():
    quit()

open_img = Image.open("mm.jpg")
render_img = ImageTk.PhotoImage(open_img)
main_image = Label(win, image = render_img)
main_image.image = render_img
main_image.grid(row = 0, columnspan = 1)

Label(win, text="Welcome to\n Moody Movie", bg='lavender', font =("Times", 20, "bold")).grid()
data = StringVar(win)
data.set("Enter Mood or Genre")
Label(win, text = "How's Your Mood Today?",bg='lavender',font =("Times", 14, "bold")).grid(pady=10)
entry1= Entry(win, textvariable=data,font =("Times", 11, "italic"), width=30).grid(padx=10)
button1=Button(win, text="Search!",width=12,font =("Times", 11, "bold"), command=movie).grid(pady=10)
button2=Button(win, text="Info",width=12,font =("Times", 11, "bold"), command=note).grid(pady=10)
button3=Button(win, text="Clear",width=12,font =("Times", 11, "bold"), command=clear).grid(pady=10)
button4=Button(win, text="Theme",width=12,font =("Times", 11, "bold"), command=toggle).grid(pady=10)
button5=Button(win, text="Music",width=12,font =("Times", 11, "bold"), command=music).grid(pady=10)
button6=Button(win, text="Exit",width=12,font =("Times", 11, "bold"), command=exit).grid(pady=10)

win.mainloop()
