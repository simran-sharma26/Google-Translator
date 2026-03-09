# use pip install googletrans==3.1.0a0
# use pip install gTTs
from tkinter  import *
from tkinter import ttk # bring combo box
from deep_translator import GoogleTranslator

def translate_text():
    input_text = source_text.get("1.0", END)
    src_lang = languages[source_combo.get()]
    dest_lang = languages[dest_combo.get()]
    translated = GoogleTranslator(source=src_lang, target=dest_lang).translate(input_text)
    
    dest_text.delete("1.0", END)
    dest_text.insert(END, translated)


root=Tk()
root.title("Translator")
#fixing the geometry of translator
root.geometry("500x600")
root.minsize(300,200)
root.maxsize(800,800)
root.config(bg="grey")
#giving the tag to translator
text=Label(text="Google Translator",bg="olive",fg="white",font=("Time New Roman ",20,"bold"),padx=30 , pady=15,borderwidth=3,relief=SUNKEN)
text.pack(anchor="w",fill="x") #text.place(x=100,y=100,height=100,width=200)
#creating source file 
source_label=Label(text="Source text",bg="red",fg="white",font=("Time New Roman",15,"bold"))
source_label.pack(anchor="n", fill=X)
# creating frame
frame=Frame()
frame.pack()
#creating combo box
#list1=list(LANGUAGES.values())
#languages = ["en","hi","fr","de","es","ja","ru","ar"]
languages = GoogleTranslator().get_supported_languages(as_dict=True)
list1 = list(languages.keys())
source_combo = ttk.Combobox(frame, values=list1)
#source_combo=ttk.Combobox(frame,values=list1)
source_combo.pack(anchor="w")
source_combo.set("select")
#creating button
#source_button= Button(frame,text="Translate")
source_button = Button(frame, text="Translate", command=translate_text)
source_button.pack(anchor="e")
#creating input field
source_text=Text(frame,width=800,height=10,font=("Time New Roman ",10,"bold"),wrap=WORD)
source_text.pack(anchor=W)

#creating destination 
dest_label=Label(text="Destination",bg="red",fg="white",font=("Time New Roman",15,"bold"))
dest_label.pack(fill=X)
frame1=Frame()
frame1.pack()
dest_combo = ttk.Combobox(frame1, values=list1)
#dest_combo=ttk.Combobox(frame1,values=list1)
dest_combo.set("Select")
dest_combo.pack(anchor=W)
dest_text=Text(frame1,font=("Time New Roman", 10 ,"bold"))
dest_text.pack(anchor=W)



root.mainloop()
