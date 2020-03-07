import pandas as pd
from textblob import TextBlob
from tkinter import *
from tkinter import ttk
data=pd.read_csv("E:/books/sem 5/nlpproject/Amazon_Unlocked_Mobile.csv")
reviews=data['Reviews']
ratings=data['Rating']
products=data['Product Name']
myprod=[]
myprod=set(products)
root=Tk()
#T= Text(root, height=1, width=30)
#T.pack()
def onpres():
    k=dropVar.get()
    j=0;
    re=[]
    while(j<=286):
        try:
            if products[j]==dropVar.get():
                re.append(reviews[j])
        except:
            pass        
        j=j+1 
    s=0;       
    for i in re:
        analysis = TextBlob(i)
        score=analysis.sentiment.polarity
        if(score>0.45):
            s=s+5;
        elif score>0.25 and score<0.45:
            s=s+4;
        elif score>0.1 and score<0.25:
            s=s+3;
        elif score>-0.05 and score<0.1:
            s=s+2
        else:
            s=s+1;
    truerating=s/len(re)
    truerating=round(truerating,2);
    Label(root,text=k,font=("Courier", 25),wraplength=800).pack()        
    Label(root,text="1 ."+ re[0],fg='green',wraplength=1000).pack()
    Label(root,text="2 ."+re[1],fg='green',wraplength=1000).pack()
    Label(root,text="3 ."+re[2],fg='green',wraplength=1000).pack()
    Label(root,text="4 ."+re[3],fg='green',wraplength=1000).pack()
    Label(root,text="5 ."+re[4],fg='green',wraplength=1000).pack()  
    p="averagerating="+str(truerating) 
    Label(root,text=p,font=("Courier", 44)).pack()      
                                

def fun():
    global frame,root,dropVar
    frame.destroy()
    main=Frame(root)
    dropVar=StringVar()
    dropVar.set("Select a choice")
    dropMenu1 = OptionMenu(root,dropVar,*myprod).pack()
    B1=Button(root,text="OK",command=onpres)
    B1.pack(side="top", padx=54, pady=4)
    root.title("Reviewmeter")
frame=Frame(root)
frame.place(relx=0.3,rely=0.2,width=500,height=500)
fr=Frame(root)
report=Frame()
l = Label(frame,text="Welcome")
l.place(x=225,y=70)
name=Label(frame,text="Name")
name.place(x=150,y=100)
nm_entry=Entry(frame)
nm_entry.place(x=200,y=100)
k=Label(frame,text="Password")
k.place(x=144,y=130)
reg_entry=Entry(frame)
reg_entry.place(x=200,y=130)
b=Button(frame,text="Login",command=fun)
b.place(x=225,y=190)




    
root.mainloop()

       
    
    
