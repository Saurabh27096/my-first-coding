from tkinter import*
import time
import random 
def Slider():
        global count,sliderWords
        text = '    TYPING SPEED TEST GAME     '
        if(count >= len(text)):
            count = 0
            sliderWords = ''
        sliderWords += text[count]
        count += 1
        global l1
        l1.configure(text=sliderWords)       
        l1.after(200,Slider)  
start=0
def intermidiate(): 
      fa.destroy()
      global word       
      word=["When I've built up my savings, I'll be able to travel to Mexico.","Wouldn't it be lovely to enjoy a week soaking up the culture.",
      'The plots failed because of some trusted friends of the king.','After the death of the king, everyone wanted to be a king.',
      'War does not bring anything good to the common people.',"If opportunity doesn't knock, build a door.",
      "You can build a site right now by opening up a text editor like Notepad.","For a moment she considered his response before typing.",
      "Since it is a fairly common task, however, it is something that is \neasily found in any browser.",
      "For a change, the right place to look for the best deals in web design \nand hosting is not by typing those words into \nyour favorite search engine."]
      secondpage()
def biggner():
    fa.destroy()
    global word
    word = ["telephone, television, tennis, terrible, test, than, their, then, there, therefore","a b c d e f g h i j k l m n o p q r s t u v w x y z",
    "neighbour, neither, newspaper, next, night, nine, no, noble, noise","abcdefghijklmnopqrstuvwxyz",
    "Apple ,Machine, Main, Make, Male, Man, Many, Map, mark, market, marry"]
    secondpage()
def exp():
    fa.destroy()
    global word
    word=["q ,.;* then : , + ,:- 4 ;8 j h",
    "In in the 1950s, O. Penrose and L. Onsager related the quality of superfluidity\nto the long-range order displayed by a highly correlated bosonic system.",
    "Closely related to the frictionless flow of a superfluid is the resistanceless current-flow \nin certain materials at low enough temperatures, discovered by H. Kamerlingh \nOnnes in 1911,and reaching a full theoretical explanation based on the approaches \nof J. Bardeen, L. N. Cooper and J.R. Schrieffer in 1957, who derived a microscopic \ntheory based on phonon-mediated interactions between the electrons of the material. \nThe fermionic helium isotope 3He, for instance , undergoes at a temperature of \n3mK a phase transition analogous to superconductivity,with its atoms behaving like \nconduction electrons, pairing up to bosonic entities, which enter a condensed state."]
    secondpage()
##############################################################  firstpage function
root=Tk()
root.geometry("1245x670")
root.resizable(width=FALSE, height=FALSE)
#root.minsize(1090,670)
#root.maxsize(1090,670)
root.iconbitmap("E:/CoolIcons/logo.ico")   
root.title("Typing speed test")
def firstpage():
    global fa
    fa= Frame(root)
    fa.pack(fill='both')
    #bg=PhotoImage(file="background3.png")
    #my_lable= Label(fa, image=bg)
    #my_lable.image = bg
    #my_lable.place(x=0,y=0)
    fa.configure(bg="gray11")     
    f11=Frame(fa,borderwidth=10,bg="blue",relief=SUNKEN)
    f11.pack(pady=100,side="top")    
    l11=Label(f11,text="   TEST YOUR SPEED  ",font="comic 50 bold",bg="red",fg="pink",pady=20) 
    l11.pack(pady=20,padx=20)
    button11=Button(fa,text="  BEGINNER  ",font="comic  20 bold",bg="red",fg="yellow",command=biggner,relief=GROOVE,borderwidth=15)
    button11.place(x=50,y=500)      
    button12=Button(fa,text="INTERMEDIATE",font="comic  20 bold",bg="red",fg="yellow",command=intermidiate,relief=GROOVE,borderwidth=15)
    button12.place(x=480,y=500)     
    button13=Button(fa,text="    Advanced    ",font="comic  20 bold",bg="red",fg="yellow",command=exp,relief=GROOVE,borderwidth=15)
    button13.place(x=900,y=500)
    l22=Label(fa,text="                      CHOOSE YOUR CATEGORY              ",font="comic 20 bold")
    l22.pack(pady=670)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  secondpage function
def secondpage():
    global f2
    f2=Frame(root,width=1090,height=670)
    f2.pack(fill='x')
    #f2.winfo_toplevel().geometry("1000x670")
    def first():
        f2.destroy()
        firstpage()   
    def entry():
         global wordintry
         wordintry=Entry(f2,font= "comic  20 bold",justify="center",relief=SUNKEN,borderwidth=10)   
         wordintry.pack(padx=50,pady=30)
         wordintry.focus_set()   #this is for entering string without any key
############################################set backgroung pic
    #bg=PhotoImage(file="background3.png")
    #my_lable= Label(f2, image=bg)
    #my_lable.image = bg
    #my_lable.place(x=0,y=0)
    f2.configure(bg="gray11")
    def clear():
        wordintry.destroy()
        entry()
        global l2,l4,l6,l8
        random.shuffle(word)
        ############################################
        global stg1
        stg1=word[0]
        ##########################################
        l2.configure(text=word[0])
        #global start,end
        #start =time.time()
        global start
        start=time.time()
        l4.configure(text='') 
        l6.configure(text='')
        l8.configure(text='')
    wordintery=""
    random.shuffle(word)
    def startgame(event):
        global end,wordintry,l1
        end=time.time()
        total=end-start
        string=str(total)
    ############   label for showing time 
        string2=wordintry.get()
        length=len(string2)
        wpm=(60*length)/(5*total)
        global l2,l4,l6,l8
    ###########################################
        from difflib import SequenceMatcher
        global per
        per= int((SequenceMatcher(None, stg1,string2).ratio())*100)
    #########################################
        l3=Label(f2,text='Time:    ',font= "comic  20 bold",bg="brown")
        l3.place(x=10,y=530)
        l4=Label(f2,text=string[:4:]+"sec",font= "comic  20 bold",bg="brown") 
        l4.place(x=100,y=530)     
        l5=Label(f2,text="WPM:  ",font= "comic  20 bold",bg="brown")
        l5.place(x=330,y=530)
        l6=Label(f2,text=int(wpm),font= "comic  20 bold",bg="brown",padx=15)
        l6.place(x=420,y=530)
        l7=Label(f2,text="Accuracy : ",font= "comic  20 bold",bg="brown",padx=5)
        l7.place(x=550,y=530)
        l8=Label(f2,text=str(per)+str("%"),font= "comic  20 bold",bg="brown")
        l8.place(x=700,y=530)
        if(wordintry.get()==l2['text']):
            print("mathed")
        else:
            random.shuffle(word)
        wordintry.delete(0,END)
        wordintry.destroy()
    f1=Frame(f2,borderwidth=30,bg="blue",relief=SUNKEN)
    f1.pack(side="top")
    global count,sliderWords
    count = 0
    sliderWords = ''
    global l1
    l1=Label(f1,text="",font= "comic  30 bold",bg="brown")
    l1.pack(padx=20,pady=20)
    Slider()
    button11=Button(f2,text=" HOME ",font="comic  20 bold",bg="red",fg="yellow",command=first,relief=GROOVE,borderwidth=10)
    button11.pack(side="bottom")
    button112=Button(root,text=" EXIT ",font="comic  20 bold",bg="red",fg="yellow",command=root.destroy,relief=GROOVE,borderwidth=10)
    button112.place(x=1000,y=600)
    ############################## beggen fun for start button 
    def beggen():
         global l12
         l12.destroy()
         global l2,l4,l6,l8
         random.shuffle(word)
         random.shuffle(word)
         random.shuffle(word)
         random.shuffle(word)
         global stg1
         stg1=word[0]
################################  Restart button
         button2=Button(f2,text="Restart",font="comic  30 bold",bg="red",fg="yellow",command=clear,relief=GROOVE,borderwidth=10)
         button2.place(x=800,y=480)
         q=Label(f2,text='',bg="red")
         q.pack(side="left",pady=300)
         l2=Label(f2,text=word[0],font= "comic  20 bold",bg="gray",fg="blue")
         l2.pack(padx=50,side="top",pady=10)
         l4=Label()
         l6=Label()
         l8=Label()
         button1.destroy()
         entry()
         global start         
         start =time.time()
###########################################################################    start button
    button1=Button(f2,text="START",font="arial  30 bold",bg="red",fg="yellow",command=beggen,relief=GROOVE,borderwidth=15)
    button1.pack(padx=50,pady=150,side=TOP)
    global l12
    l12=Label(f2,text="   Enter Text And Hit Enter Button   ",bg="black",font= "Times 20 bold italic",fg="gray")
    l12.pack()
    global l2,l4,l6,l8
    root.bind('<Return>',startgame)
firstpage()
root.mainloop()