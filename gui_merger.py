from tkinter import ttk,Tk,Grid,Label,Button,N,E,W,S
from tkinter import filedialog
from merge import merger

filelist=list()

def browsefunc():
    global filelist
    filenames = filedialog.askopenfilenames()
    pathlabel.config(text=str(filenames).strip('()'))
    filelist = [ele for ele in filenames]
    print(type(filelist))


def merge_wrapper():
    global filelist

    if len(filelist)==0:
        pathlabel.config(text="You have not selected any files")
    else:
        print(filelist)
        merger(filelist)
        filelist=[]
        pathlabel.config(text="Files merged into product.pdf" )

root=Tk()
root.title("Pdf Merger")
mainframe=ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

headinglabel=Label(mainframe,text="PDF Merger")
headinglabel.grid(column=1,row=0,sticky=(N))
instrlabel=Label(mainframe,text="Select the files in the order you want them merged")
instrlabel.grid(column=1,row=1,sticky=(N))
browsebutton=Button(mainframe, text="Browse", command=browsefunc)
browsebutton.grid(column=2,row=2,sticky=(W,E))
pathlabel=Label(mainframe)
pathlabel.grid(column=1,row=2,sticky=(W,E))
exitbutton=Button(mainframe,text="Exit", command=lambda: root.destroy())
exitbutton.grid(column=1,row=3)
mergebutton=Button(mainframe, text="Merge", command=merge_wrapper)
mergebutton.grid(column=0,row=3,padx=30)

root.mainloop()
