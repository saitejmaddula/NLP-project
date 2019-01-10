import pandas as pd
from textblob import TextBlob
from tkinter import *
from tkinter import ttk
data=pd.read_csv("C:/Users/saitej/Desktop/nlpproject/Amazon_Unlocked_Mobile.csv")
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
    Label(root,text=k,font=("Courier", 25)).pack()        
    Label(root,text=re[0],fg='green').pack()
    Label(root,text=re[1],fg='green').pack()
    Label(root,text=re[2],fg='green').pack()
    Label(root,text=re[3],fg='green').pack()
    Label(root,text=re[4],fg='green').pack()  
    p="averagerating="+str(truerating) 
    Label(root,text=p,font=("Courier", 44)).pack()      
                                
    
    
dropVar=StringVar()
dropVar.set("Select a choice")
dropMenu1 = OptionMenu(root,dropVar,*myprod).pack()
B1=Button(root,text="OK",command=onpres)
B1.pack(side="top", padx=54, pady=4)
root.title("Reviewmeter")



    
root.mainloop()

       
    
    