from tkinter import *
actualText ="";temp1=0;temp2=0;temp3=0;btnType=0;oFlag=0
##---------------------------------------------------------------------##
def fillUp(sth,append):
    global actualText;global showText
    if append=="yes":
        actualText=actualText+str(sth)
    else:
        actualText=str(sth)           
    showText.delete("1.0","end")
    showText.insert("1.0",actualText)   
##---------------------------------------------------------------------##
def add_to_showText(sth):
    global actualText;global temp1;global temp2;global temp3;global btnType  
    global showText;global oFlag
    if oFlag==0:     
        if sth=='+' or sth=='-' or sth=='*' or sth=='/':  
            btnType=1   
        elif sth=='(':
            btnType=2;temp2=1;temp3=0
        elif sth==')':
            btnType=2;temp2=0;temp3=1
        elif sth=='.':  
            btnType=3
        else :
            btnType=4;temp2=0    
  
        if temp1==0:
            if btnType==3:
               if temp3!=1:
                    fillUp(sth,"yes")
                    temp3=1
                    temp2=1
            if btnType==2:
                fillUp(sth,"yes")              
            if actualText!="" :   
                if btnType==1 and temp2!=1:
                    fillUp(sth,"yes")
                    temp2=1
                    temp3=0              
            if temp2==1:
                if btnType==4:
                    fillUp(sth,"yes")
                if temp3!=1 and btnType==3:
                    fillUp(sth,"yes")
                    temp3=1         
            elif temp2==0:
                if btnType==4:
                    fillUp(sth,"yes")
                    temp2=0              
            
        elif temp1!=0:
            if btnType==1:
                fillUp(sth,"yes")
            else:
                fillUp(sth,"no")
            temp1=0
            
        my_str=showText.get("1.0","end-1c")  
        if len(my_str)==40:
            oFlag=1
            showText.delete("1.0","end")
            showText.insert("1.0","40 Char Limit, Press del!")           
 ##---------------------------------------------------------------------##            
def calculate():
    global actualText
    global btnType;global temp1;global temp2;global temp3
    global oFlag
    
    if btnType!=1 and btnType!=3:
        btnType=0
        if actualText!="":     
            try:
                result=str(round(eval(actualText),4))
                showText.delete("1.0","end")
                showText.insert("1.0",result)
                actualText=result
            except ZeroDivisionError:
                showText.delete("1.0","end")
                showText.insert("1.0","Can't divide by Zero!")
                actualText=""     
            except SyntaxError:
                showText.delete("1.0","end")
                showText.insert("1.0","Syntax Error!")
            except:
                showText.delete("1.0","end")
                showText.insert("1.0","Expression Error!")
                actualText=""              
            temp1=1;temp2=0;temp3=0;oFlag=0
##---------------------------------------------------------------------##
def clear():
    global actualText
    global oFlag
    global btnType;global temp1;global temp2;global temp3
    actualText=""
    showText.delete("1.0","end")
    showText.insert("1.0","0")
    btnType=0;temp1=0;temp2=0;temp3=0;oFlag=0
##---------------------------------------------------------------------##        
def dummydel():
    global actualText
    global oFlag
    global btnType;global temp1;global temp2;global temp3
    
    if oFlag==1:
        showText.delete("1.0","end")
        showText.insert("1.0", actualText)
        oFlag=0
    elif oFlag!=1:
        btnType=0
        if actualText!="":
            showText.delete("end-2c")
            actualText = actualText[:-1]
        t1=actualText.replace('-', '+')
        t2=t1.replace('*', '+')
        t3=t2.replace('/', '+')
        t4=t3.split("+")        
        last=t4.pop()
        
        if last!="":
            if last.find(".")!=-1:
                temp3=1;temp2=1
            else:
                temp3=0;temp2=0
        else:
            temp3=0;temp2=1      
##---------------------------------------------------------------------##             
window=Tk()
window.title("CALCULATOR")
window.geometry("356x494")
window.resizable(False,False)
window.config(background='lightblue')

showText=Text(window,height=2,width=20,takefocus=0,
              bg="black", fg="lightgreen", font=("Arial",20))
showText.grid(row=0,column=0,columnspan=4)
showText.insert("1.0","0")
showText.bind("<Key>", lambda e: "break")
##---------------------------------------------------------------------##
def btnHandling(w,s,r,c,bgc,fgc):
    numBtn = Button(w,text=s,bg=bgc,fg=fgc,activebackground='blue',
                    bd=3,relief=SOLID,command=lambda:add_to_showText(s),
                    height=3, width=7, font=("Arial",14))
    numBtn.grid(row=r,column=c)
##---------------------------------------------------------------------##
def btnHandling2(w,s,r,c,bgc,fgc,fn):
    opBtn = Button(w,text=s,bg=bgc,fg=fgc,activebackground='blue',
                    bd=3,relief=SOLID,command=lambda:fn(),
                    height=3, width=7, font=("Arial",14))
    opBtn.grid(row=r,column=c)
##---------------------------------------------------------------------##       
btn_1           =btnHandling(window,'1',2,0,'yellow','black')
btn_2           =btnHandling(window,'2',2,1,'yellow','black')
btn_3           =btnHandling(window,'3',2,2,'yellow','black')
btn_4           =btnHandling(window,'4',4,0,'yellow','black')
btn_5           =btnHandling(window,'5',4,1,'yellow','black')
btn_6           =btnHandling(window,'6',4,2,'yellow','black')
btn_7           =btnHandling(window,'7',6,0,'yellow','black')
btn_8           =btnHandling(window,'8',6,1,'yellow','black')
btn_9           =btnHandling(window,'9',6,2,'yellow','black')
btn_0           =btnHandling(window,'0',8,1,'yellow','black')
btn_p           =btnHandling(window,'.',8,2,'yellow','black')
btn_parenOpen   =btnHandling(window,'(',10,1,'grey','black')
btn_parenClose  =btnHandling(window,')',10,2,'grey','black')
btn_plus        =btnHandling(window,'+',2,3,'grey','black')
btn_minus       =btnHandling(window,'-',4,3,'grey','black')
btn_mul         =btnHandling(window,'*',6,3,'grey','black')
btn_div         =btnHandling(window,'/',8,3,'grey','black')
##---------------------------------------------------------------------##
btnHandling2(window,"=",10,3,'green','yellow',calculate)
btnHandling2(window,"C",10,0,'red','black',clear)
btnHandling2(window,"del",8,0,'red','black',dummydel) 
##---------------------------------------------------------------------##
    




