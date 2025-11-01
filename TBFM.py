import tkinter as tk
from tkinter import messagebox
import os
def about():
    messagebox.showinfo("TBFM","TBFM v1.0 (Tkinter Based Form Maker)\nCreated by Caron\n© 2025 Caron Software")
def seticon(windows):
    windows.iconbitmap("TBFM.ico")

def open1():# Second Part
    global sizevar
    tk.Label(win1, text="Enter size of the new window:").grid(padx=270, pady=10)
    sizevar = tk.StringVar(value="800x600")
    tk.OptionMenu(win1, sizevar, "800x600", "1600x600", "1920x1080").grid(padx=280, pady=10)
    tk.Button(win1, text="Start", command=start).grid(padx=290, pady=10)# Go To start

def start():
    windowinfo = tk.Toplevel()
    windowinfo.geometry("200x200")
    windowinfo.title("TBFM")
    seticon(windowinfo)
    tk.Label(windowinfo, text="Enter name of the new file:").grid()
    entrys = tk.Entry(windowinfo)
    entrys.grid(padx=10, pady=10)
    # Go Past createfile
    def createfile():
        global filename
        def yesask():
            with open(filename, "w",encoding='utf-8') as f:
                f.write("# This Code Has Been Writted By TBFM\n# Created by Caron\n# © 2025 Caron Software\nimport tkinter as tk\nfrom tkinter import messagebox\nwin1 = tk.Tk()\n")
            asklevel.destroy()
            windowinfo.destroy()
            openwin2(filename)
        def noask():
            asklevel.destroy()
        filename = entrys.get().strip()
        if not filename:
            messagebox.showerror("Error", "Please enter a file name.")
            return
        if not filename.endswith(".py"):
            filename += ".py"
        if not os.path.exists(filename):
            with open(filename, "w",encoding='utf-8') as f:
                f.write("# This Code Has Been Writted By TBFM\n# Created by Caron\n# © 2025 Caron Software\nimport tkinter as tk\nfrom tkinter import messagebox\nwin1 = tk.Tk()\n")
            windowinfo.destroy()
            openwin2(filename)# Go To openwin2
        else:
            asklevel = tk.Toplevel()
            asklevel.geometry("400x200")
            tk.Label(asklevel, text='This File Already Exists.\nDo You Want The Files Containing\nTo Be ReWrittin?').grid(row=0,column=2)
            tk.Button(asklevel, text='Yes',width=5,command=yesask).grid(row=1,column=2)
            tk.Button(asklevel, text='No',width=5,command=noask).grid(row=1,column=3)
    tk.Button(windowinfo, text="Continue", command=createfile).grid(pady=10)# Go To createfile

def openwin2(filename):
    global win2
    win2 = tk.Toplevel()
    win2.geometry(sizevar.get())
    with open(filename, "a",encoding='utf-8') as f:
        f.write(f"win1.geometry('{sizevar.get()}')\n")
    win2.title("TBFM")
    seticon(win2)
    #------------------------------
    # Add Defs:
    #------------------------------
    def addtextbox():
        def Continue():
            try:
                col = int(entry12.get())
                row = int(entry14.get())
                tk.Entry(win2).grid(column=col, row=row)
                win3.destroy()
                with open(filename, "r",encoding='utf-8') as f:
                    existing = f.read()
                count = existing.count("tk.Entry(")
                varname = chr(97 + count)  # 97 = 'a'
                with open(filename, "a",encoding='utf-8') as f:
                    f.write(f"{varname} = tk.Entry(win1)\n{varname}.grid(column={col}, row={row})\n")
            except ValueError:
                messagebox.showerror("Error", "Please enter valid integers for row and column.")# make the code reconize a=...


        win3 = tk.Toplevel()
        win3.geometry("200x200")
        win3.title("TBFM")
        seticon(win3)
        tk.Label(win3, text="Enter Column:").grid()
        entry12 = tk.Entry(win3)
        entry12.grid(padx=20)
        tk.Label(win3, text="Enter Row:").grid()
        entry14 = tk.Entry(win3)
        entry14.grid(padx=20)
        tk.Button(win3, text="Continue", command=Continue).grid(pady=10)# Go To Continue
    #------------------------------
    def addlabel():
        def Continue2():
            try:
                col = int(entry22.get())
                row = int(entry24.get())
                labeltext = entry25.get()
                tk.Label(win2, text=labeltext).grid(column=col, row=row)
                win4.destroy()
                with open(filename, "a",encoding='utf-8') as f:
                    f.write(f"tk.Label(win1, text='{labeltext}').grid(column={col}, row={row})\n")
            except ValueError:
                messagebox.showerror("Error", "Please enter valid integers for row and column.")

        win4 = tk.Toplevel()
        win4.geometry("200x200")
        win4.title("TBFM")
        seticon(win4)
        tk.Label(win4, text="Enter Column:").grid()
        entry22 = tk.Entry(win4)
        entry22.grid(padx=20)
        tk.Label(win4, text="Enter Row:").grid()
        entry24 = tk.Entry(win4)
        entry24.grid(padx=20)
        tk.Label(win4, text="Enter Label").grid()
        entry25 = tk.Entry(win4)
        entry25.grid(padx=20)
        tk.Button(win4, text="Continue", command=Continue2).grid(pady=10)# Go To Continue2
    #------------------------------
    def addbutton():
        #==============================
        def buttonfunction1():# Go Past buttonfunction1:
            winbutton2 = tk.Toplevel()
            winbutton2.geometry("400x400")
            winbutton2.title("TBFM")
            seticon(winbutton2)
            tk.Label(winbutton2,text="What Will This Button Do?").grid(row=1, column=0)

            def continuebutton():
                def continuebutton3():
                    pass
                def continuebutton2(entry):
                    usercode = entry.get().replace("\\n", "\n").replace("\\t", "\t")

                    # Save the code to file
                    with open(filename, "a", encoding="utf-8") as f:
                        indentedcode = usercode.replace("\n", "\n    ")
                        f.write(f"def customfunc():\n    {indentedcode}\n")
                        f.write(f"tk.Button(win1, text='{text1}', command=customfunc,width={wid1}).grid(row={row1},column={col1})\n")

                    # Create the button in real time
                    def customfunc(usercode=usercode, winbutton3=winbutton3):
                        try:
                            exec(usercode)
                            winbutton3.destroy()
                        except Exception as e:
                            messagebox.showerror("Error", f"An error occurred:\n{e}")

                    tk.Button(win2, text=text1, command=customfunc, width=wid1).grid(row=row1, column=col1)
                    messagebox.showinfo("TBFM", f"Button Saved To {filename}!")

                # continuebutton Starts Here:
                if func4var.get() == True:
                    winbutton3 = tk.Toplevel()
                    winbutton3.geometry("400x400")
                    winbutton3.title("TBFM")
                    seticon(winbutton3)

                    col1 = int(en1.get())
                    row1 = int(en2.get())
                    wid1 = int(en3.get())
                    text1 = en4.get()
                    winbutton.destroy()
                    winbutton2.destroy()
                    winbutton3.columnconfigure(0, weight=1)
                    winbutton3.columnconfigure(1, weight=1)

                    tk.Label(winbutton3, text="Enter Command:").grid(row=0, column=0, sticky="w")
                    entry1 = tk.Entry(winbutton3)
                    entry1.grid(row=0, column=1, sticky="ew", padx=10, pady=5)

                    tk.Button(
                        winbutton3, text="Continue",
                        command=lambda: continuebutton2(entry1)
                    ).grid(row=1, column=0, columnspan=2, pady=10)
                    tk.Button(
                        winbutton3, text="Don't Add Command",
                        command=continuebutton3
                    ).grid(row=2, column=0, pady=10, columnspan=2)

            #------------------------------
            func1var = tk.BooleanVar()# Not Working Till V2
            func2var = tk.BooleanVar()# Not Working Till V2
            func3var = tk.BooleanVar()# Not Working Till V2
            func4var = tk.BooleanVar()

            func1_cb = tk.Checkbutton(winbutton2,text="Get An Entry's Text",variable=func1var)# Not Working Till V2
            func2_cb = tk.Checkbutton(winbutton2,text="Match Something Using Option 1",variable=func2var)# Not Working Till V2
            func3_cb = tk.Checkbutton(winbutton2,text="Open A TopLevel()", variable=func3var)# Not Working Till V2
            func1_cb.config(state="disabled")
            func2_cb.config(state="disabled")
            func3_cb.config(state="disabled")
            func4_cb = tk.Checkbutton(winbutton2,text="Custom...",variable=func4var)

            func1_cb.grid(row=2, column=0)
            func2_cb.grid(row=2, column=2)
            func3_cb.grid(row=3, column=0)
            func4_cb.grid(row=3, column=2)
            tk.Button(winbutton2,text="Continue",width=10,command=continuebutton).grid(row=4,column=0)# Go To continuebutton
        #==============================# Go Past buttonfunction1.
        winbutton = tk.Toplevel()
        winbutton.geometry("200x400")
        winbutton.title("TBFM")
        seticon(winbutton)
        # winsave
        winbutton.columnconfigure(0, weight=1)
        tk.Label(winbutton,text="Enter Column:").grid()
        en1 = tk.Entry(winbutton)
        en1.grid(row=1, column=0, sticky="ew", padx=20)
        tk.Label(winbutton,text="Enter Row:").grid(row=2, column=0, sticky="ew", padx=20)
        en2 = tk.Entry(winbutton)
        en2.grid(row=3, column=0, sticky="ew", padx=20)
        tk.Label(winbutton,text="Enter Width:").grid(row=4, column=0, sticky="ew", padx=20)
        en3 = tk.Entry(winbutton)
        en3.grid(row=5, column=0, sticky="ew", padx=20)
        tk.Label(winbutton,text="Enter Text:").grid(row=6, column=0, sticky="ew", padx=20)
        en4 = tk.Entry(winbutton)
        en4.grid(row=7, column=0, sticky="ew", padx=20)
        tk.Button(winbutton,text="Click To Enter Function",width=20,command=buttonfunction1).grid()# Go To buttonfunction1
    #------------------------------
    def save():
        def yes():
            with open(filename, "a",encoding='utf-8') as f:
                f.write("win1.mainloop()\n")
            messagebox.showinfo("TBFM","Saved!")# Tkinter Based Form Maker Or For Short, TBFM
            winsave.destroy()
            win2.destroy()
        def no():
            winsave.destroy()
        winsave = tk.Toplevel()
        winsave.geometry("200x200")
        winsave.title("TBFM")
        seticon(winsave)
        tk.Label(winsave,text=f"Save File As {filename}?").grid()
        tk.Button(winsave,text="Yes",command=yes).grid()
        tk.Button(winsave,text="No",command=no)

        #------------------------------
        # Add Defs.
        #------------------------------
    menu = tk.Menu(win2)# Menu Part
    file = tk.Menu(menu, tearoff=0)
    file.add_command(label="Exit", command=lambda : win2.destroy())
    file.add_command(label="Save",command=save)
    menu.add_cascade(label="File", menu=file)

    options = tk.Menu(menu, tearoff=0)
    options.add_command(label="New TextBox", command=addtextbox)
    options.add_command(label="New Label", command=addlabel)
    options.add_command(label="New Button", command=addbutton)
    menu.add_cascade(label="New", menu=options)

    win2.config(menu=menu)


# Start Of The Code
win1 = tk.Tk()
win1.geometry("800x600")
win1.title("TBFM")
seticon(win1)
win1.resizable(False, False)
tk.Button(win1, text='Make New Window', command=open1, width=50).grid(padx=250, pady=10)# Go To open1
menu = tk.Menu(win1)
file = tk.Menu(menu, tearoff=0)
file.add_command(label="Exit", command=lambda : win1.destroy())
file.add_command(label="About", command=about)
menu.add_cascade(label="File", menu=file)
win1.config(menu=menu)
win1.mainloop()