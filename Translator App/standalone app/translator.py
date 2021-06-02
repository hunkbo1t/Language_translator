from google_trans import google_translator
from constant import DEFAULT_SERVICE_URLS, LANGUAGES
from tkinter import *
import tkinter.ttk as tk
from tkinter import messagebox

trs = google_translator(DEFAULT_SERVICE_URLS)


def work(text, key):
    trs_text = (trs.translate(text, lang_tgt=key, lang_src='auto'))
    return trs_text


def get_key(val):								# function to return key for any value
    for key, value in LANGUAGES.items():
        if val == value:
            return key
    return "key doesn't exist"


def retrive_input():
    try:
            # get inputTextArea.text
        __input = list(intxt.get("1.0", END).split('\n'))
        detect = str(to_cb.get())  # get lang user wishes to translate to
        key = str(get_key(detect))  # geting key from value
        __output = work(__input, key)[2:-7]  # trim the result string
        outtxt.delete(1.0, END)  # clear outputTextArea
        outtxt.insert(1.0, ''.join(__output))  # patch Results
    except:
        messagebox.showerror('Error','Connectivity Issue. Check internet connection')


# Window
window = Tk()
var1, var2 = StringVar(), StringVar()
var1.set('english')  # default
var2.set('Select language')
data = list(LANGUAGES.values())  # ComboBox Items

# Text Area
intxt = Text(window, height=10, width=40,
             fg='gray', wrap=WORD)  # input Textarea
intxt.place(x=10, y=10)
outtxt = Text(window, height=10, width=40, fg='blue',
              wrap=WORD)  # output Textarea
outtxt.place(x=348, y=10)

# ComboBox
# Select lang to translate
from_cb = tk.Combobox(window, state='readonly', textvariable=var1, values=data)
from_cb.place(x=10, y=185)
to_cb = tk.Combobox(window, state='readonly', textvariable=var2,
                    values=data)  # resulting translatino lang
to_cb.place(x=348, y=185)

# Clear Button
from_cls_btn = tk.Button(window, text='Clear', command=lambda: intxt.delete(
    1.0, END))  # clear input textarea
from_cls_btn.place(x=260, y=185)
to_cls_btn = tk.Button(window, text='Clear', command=lambda: outtxt.delete(
    1.0, END))  # clear output textarea
to_cls_btn.place(x=600, y=185)

# Miscellaneous
submitbtn = tk.Button(window, width=14, text='Translate',
                      command=retrive_input)  # translate Button
submitbtn.place(x=500, y=185)
lbl = Label(window, text="[default='english']",
            fg='gray').place(x=156, y=185)  # infoLabel

# Final Declarations
window.title('Translator')
window.geometry("685x230+30+120")
window.resizable(False, False)
window.iconbitmap('.\\icon.ico')
window.mainloop()
