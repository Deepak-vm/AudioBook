import tkinter as tk
from PIL import Image, ImageTk
import pyttsx3
import PyPDF2

Bg = "#BEEFC7"

app = tk.Tk()
app.geometry('750x750')
app.title('AUDIO BOOK')
app.configure(bg=Bg)

main_frame = tk.Frame(app)

# page 1 
page1 = tk.Frame(main_frame)

# image = Image.open("C:\\python\\Foa_project\\audiobooks.jpeg")
# imageResized = image.resize((200, 200), Image.ANTIALIAS)
# image1 = ImageTk.PhotoImage(imageResized)

# logo = tk.Label(page1, image=image1, bg=Bg)
# logo.pack()

page_1_lb = tk.Label(page1, text='Hello, Welcome to audioBook!', font=('Bold', 20))
page_1_lb.pack()

def click():
    page1.pack_forget()
    page3.pack_forget()
    page4.pack_forget()
    page5.pack_forget()
    page2.pack()

enter1 = tk.Button(page1, text="ENTER",bg=Bg,  width=20, command=click)
enter1.pack(pady=(40, 0))

def click2():
    page1.pack_forget()
    page2.pack_forget()
    page3.pack_forget()
    page4.pack_forget()
    page5.pack()
    
about = tk.Button(page1 , text="ABOUT " , width=20 , command=click2)
about.pack()

page1.pack(pady=100)

#page2

page2 = tk.Frame(main_frame)

page2_lb = tk.Label(page2, text='Choose the type of file', font=('Bold', 20))
page2_lb.pack()

def click1(event):
    if event == "enter2":
        page2.pack_forget()
        page3.pack_forget()
        page5.pack_forget()
        page4.pack()
    elif event == "enter3":
        page2.pack_forget()
        page3.pack()

enter2 = tk.Button(page2, text="PDF file",  font=('Bold', 20) , command=lambda:click1("enter2"))
enter2.pack(pady=(40, 0))

enter3 = tk.Button(page2, text="Type Text",  font=('Bold', 20) , command=lambda:click1("enter3"))
enter3.pack(pady=(40, 0))

def back6():
    page4.pack_forget()
    page3.pack_forget()
    page2.pack_forget()
    page5.pack_forget()
    page1.pack()
back6_btn= tk.Button(page2, text="Back"  , bg=Bg , command=back6) 
back6_btn.pack(side=tk.LEFT , pady=(40 , 0)  )

page2.pack(pady=100)

#page 3
page3 = tk.Frame(main_frame)

enter_text = tk.Label(page3, text="Please enter the text", font=('Bold', 20))
enter_text.pack(pady=(40, 0))


Enter_text_box = tk.Entry(page3, font=(20))
Enter_text_box.pack(pady=(40 , 0))


def talk():
    entered_text = Enter_text_box.get()
    speaker = pyttsx3.init()
    speaker.setProperty('rate', -0.6)
    speaker.say(entered_text)
    speaker.runAndWait()
enter = tk.Button(page3, text="PLAY" , command=talk)
enter.pack(pady=(40, 0))



def back1():
    page3.pack_forget()
    page4.pack_forget()
    page5.pack_forget()
    page2.pack()
back1_btn= tk.Button(page3, text="Back"  , command=back1) 
back1_btn.pack(side=tk.BOTTOM , pady=(40 , 0) )



page3.pack(pady=100)

# page 4

page4 = tk.Frame(main_frame)

enter_text1 = tk.Label(page4, text="Copy paste the path of the pdf", font=('Bold', 20))
enter_text1.pack(pady=(40, 0))


Enter_text1_box = tk.Entry(page4, font=(20))
Enter_text1_box.pack(pady=(40 , 0))

def click():
    page1.pack_forget()
    page3.pack_forget()
    page4.pack_forget()
    page5.pack_forget()
    page6.pack()

enter1 = tk.Button(page4, text="ENTER",bg=Bg,  width=20, command=click)
enter1.pack(pady=(40, 0))

def back2():
    page4.pack_forget()
    page3.pack_forget()
    page1.pack_forget()
    page5.pack_forget()
    page2.pack()
back2_btn= tk.Button(page4, text="Back"  , bg=Bg , command=back2) 
back2_btn.pack(side=tk.LEFT , pady=(100, 100) )

page4.pack(pady=100)    

#page6

page6 = tk.Frame(main_frame)

enter_text3 = tk.Label(page6, text="Enter the page number ", font=('Bold', 20))
enter_text3.pack(pady=(40, 0))

Enter_text3_box = tk.Entry(page6, font=(20))
Enter_text3_box.pack(pady=(40 , 0))


# book =   Enter_text1_box.get()
# reader = PyPDF2.PdfReader(book)

# print(text)
def talk2():
    book =   Enter_text1_box.get()
    reader = PyPDF2.PdfReader(book)
    len(reader.pages)
    x = Enter_text3_box.get()
    text=reader.pages[x].extract_text()
    
    speaker1 = pyttsx3.init()
    speaker1.setProperty('rate', -0.6)
    speaker1.say(text)
    speaker1.runAndWait()
enter = tk.Button(page6, text="PLAY" , command=talk2)
enter.pack(pady=(40, 0))



def back2():
    page4.pack_forget()
    page3.pack_forget()
    page1.pack_forget()
    page5.pack_forget()
    page2.pack()
back2_btn= tk.Button(page4, text="Back"  , bg=Bg , command=back2) 
back2_btn.pack(side=tk.LEFT , pady=(100, 100) )

page4.pack(pady=100)

#page5
page5 = tk.Frame(main_frame)
# image2 = Image.open("C:\\Users\\HP\\Downloads\\jklulogo.jpeg")
# imageResized = image2.resize((200, 200), Image.ANTIALIAS)
# image2 = ImageTk.PhotoImage(imageResized)


# logo = tk.Label(page5, image=image2, bg=Bg)
# logo.pack()

page5_lb1  = tk.Label(page5 , text="FSM PROJECT" , font=('Bold', 20) )
page5_lb2  = tk.Label(page5 , text="SUBMITTED BY :- " , font=('Bold', 20) )
page5_lb3  = tk.Label(page5 , text="DEEPAK VISHWAKARMA (2022btech027)" , font=('Bold', 15) )
page5_lb4  = tk.Label(page5 , text="KUSHAL SANGAVAT (2022btech052)" , font=('Bold', 15))
page5_lb1.pack()

page5_lb2.pack()
page5_lb3.pack()
page5_lb4.pack()

def back5():
    page4.pack_forget()
    page3.pack_forget()
    page2.pack_forget()
    page5.pack_forget()
    page1.pack()
back5_btn= tk.Button(page5, text="Back"  , bg=Bg , command=back5) 
back5_btn.pack(side=tk.LEFT , pady=(100, 100) )

page5.pack(pady=100)

main_frame.pack(fill=tk.BOTH, expand=True)
app.mainloop()