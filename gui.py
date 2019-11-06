# -*- coding: UTF-8 -*-

from tkinter import *
from tkinter import font
from tkinter.ttk import Combobox
from tokenizer import Tokenizer
from tagger import Tagger
from tkinter import filedialog
import tkinter.scrolledtext as tkscrolled
import pandas as pd

# main window
root = Tk()
root.geometry('800x800')
root.title('Part Of Speech Tagger')


fileName = '' #global variable for the selected file
tags = []     #global variable for the generated tags 
flag = False  #global variable for the accuracy button (user handling)

times = font.Font(family='times', size=12, weight='normal') #the font used for all the buttons

frame1 = Frame(root)
frame1.pack(fill=X)

frame2 = Frame(root)
frame2.pack(fill=X)

frame3 = Frame(root)
frame3.pack(fill=X)

frame4 = Frame(root)
frame4.pack(fill=BOTH)


doc_label = Label(frame1, text="Document's Content:", font=('times', 16, 'normal'))
doc_label.pack(side=LEFT, padx=(20,0),pady=(10,0))

doc = tkscrolled.ScrolledText(frame2, width=60, height=15, wrap='word')
doc.pack(fill=X, padx=(20,20), pady=(4,0))

def browseFiles():
    doc.configure(state='normal')
    doc.delete('1.0', END)
    global fileName 
    fileName = filedialog.askopenfilename(filetypes=(("Corpus Files", ".txt"),("all files","*.*")))
    content = open(fileName,"r",encoding='utf-8').read()
    doc.tag_configure('tag-right', justify='right')
    doc.insert(END, content, 'tag-right')
    doc.configure(state='disabled')
     
browse_button = Button(frame1, width=10, text='Browse', command=browseFiles)
browse_button['font'] = times
browse_button.pack(side=RIGHT, padx=(0,40), pady=(10,0))  



tokenizer_textbox = tkscrolled.ScrolledText(frame4, width=20, height=25, wrap='word')
tokenizer_textbox.pack(fill=Y, side=LEFT, padx=(20,0), pady=(5,10))

def tokenizeTheFile():
    if not fileName:
        print("please choose a file first!!")
    else:
        tokenizer_textbox.configure(state='normal')
        tokenizer_textbox.delete('1.0', END)
        token = Tokenizer(fileName)
        result = token.tokenize()
        tokenizer_textbox.tag_configure('tag-right', justify='right')
        for word in result:
            tokenizer_textbox.insert(END, word+'\n', 'tag-right')
        tokenizer_textbox.configure(state='disabled')

tokenize_button = Button(frame3, width=10, text='Tokenizer', command=tokenizeTheFile)
tokenize_button['font'] = times
tokenize_button.pack(side=LEFT, padx=(50,0), pady=(20,0))



tagger_textbox = tkscrolled.ScrolledText(frame4, width=20, height=25, wrap='word')
tagger_textbox.pack(fill=Y, side=RIGHT, padx=(0,20), pady=(5,10))

def tagWords():
    if not fileName:
        print("please choose a file first!!")
    else:
        global flag
        global tags
        flag = True
        tagger_textbox.configure(state='normal')
        tagger_textbox.delete('1.0', END)
        token = Tokenizer(fileName)
        result = token.tokenize()
        tagger = Tagger()
        tags = tagger.tag(result)
        tagger_textbox.tag_configure('tag-right', justify='right')
        for i in range(len(result)):
            tagger_textbox.insert(END, result[i]+"-->"+tags[i]+'\n', 'tag-right')
        tagger_textbox.configure(state='disabled')
        
tag_button = Button(frame3, width=10, text='Tag', command=tagWords)
tag_button['font'] = times
tag_button.pack(side=RIGHT, padx=(0,60), pady=(20,0))



gc_label = Label(frame3, text="Golden Corpus:", font=('times', 14, 'normal'))
gc_label.pack(side=TOP, padx=(0,10), pady=(20,0))

gc_list = ["الأخلاق الرياضية قيم ومبادئ", "الرياضة و شهر رمضان المبارك", "ظاهرة العنف والتعصب الرياضي", "فوائد الرياضة وأضرارها", "مواجهة السرطان بالرياضة","تقنية الفضاء","تقنية الواقع المعزز","مركبة ذاتية القيادة","واقع افتراضي","سيارات بدون سائق في شوارع بريطانيا قريباً"]
combo = Combobox(frame3, values=gc_list, width=30)
combo.set("Choose your Golden Corpus")
combo.pack(side=TOP, padx=(0,10), pady=(0,0))


accuracy_textbox = Text(frame4, width=16, height=1)

def calcAccuracy():
    if combo.get() == "Choose your Golden Corpus" or flag == False:
        print("please choose a file and click the tag button first!!")
    else:
        counter = 0
        accuracy_textbox.configure(state='normal')
        accuracy_textbox.delete('1.0', END)
        path = "Corpus\\GoldenCorpus\\" + combo.get() +".xlsx"
        df = pd.read_excel(path, header=None, names=["words","tags"])
        for i in range(len(tags)):
            if tags[i] == df.tags[i]:
                counter += 1
        accuracy = (counter/len(df.tags)) * 100
        accuracy_textbox.insert(END, "     %.2f" % accuracy+"%")
        accuracy_textbox.configure(state='disabled')
    
accuracy_button = Button(frame4, width=15, text="Calculate Accuracy", command=calcAccuracy)
accuracy_button['font'] = times
accuracy_button.pack(side=TOP, padx=(0,15), pady=(60,0))
accuracy_textbox.pack(side=TOP, padx=(0,15), pady=(5,0))


root.mainloop()