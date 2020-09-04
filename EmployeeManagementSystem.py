def addemployee():
   def submitadd():
       id=idval.get()
       name=nameval.get()
       mobile=mobileval.get()
       email=emailval.get()
       address=addressval.get()
       gender=genderval.get()
       dob=dobval.get()
       addedtime=time.strftime("%H:%M:%S")
       addeddate=time.strftime("%d/%m/%Y")
       try:
          strr='insert into employeedata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
          mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addedtime,addeddate))
          con.commit()
          res=messagebox.askyesnocancel('Notifications','Id {} Name {} Added Sucessfully and want to clean the form'.format(id,name),parent=addroot)
          if(res==True):
               idval.set('')
               nameval.set('')
               mobileval.set('')
               emailval.set('')
               addressval.set('')
               genderval.set('')
               dobval.set('')
       except:
           messagebox.showerror('Notification', 'Id Already Exist Try Another Id',parent=addroot)
       strr = 'select * from employeedata1'
       mycursor.execute(strr)
       datas = mycursor.fetchall()
       employeetable.delete(*employeetable.get_children())
       for i in datas:
          vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
          employeetable.insert('',END,values=vv)



   addroot=Toplevel(master=DataEntryFrame)
   addroot.grab_set()
   addroot.geometry('470x470+220+200')
   addroot.title('Add Employees')
   addroot.config(bg="cyan")
   addroot.resizable(False,False)

   ######################Add employee labels##################
   idlabel=Label(addroot,text="Enter Id:",bg="cyan",font=('times',20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
   idlabel.place(x=10,y=10)

   namelabel = Label(addroot, text="Enter Name:", bg="cyan", font=('times', 20, "bold"), relief=GROOVE, borderwidth=3,
                   width=12, anchor="w")
   namelabel.place(x=10, y=70)

   mobilelabel = Label(addroot, text="Enter Mobile No.:", bg="cyan", font=('times', 20, "bold"), relief=GROOVE, borderwidth=3,
                   width=12, anchor="w")
   mobilelabel.place(x=10, y=130)

   emaillabel = Label(addroot, text="Enter Email:", bg="cyan", font=('times', 20, "bold"), relief=GROOVE, borderwidth=3,
                   width=12, anchor="w")
   emaillabel.place(x=10, y=190)

   genderlabel = Label(addroot, text="Enter Gender:", bg="cyan", font=('times', 20, "bold"), relief=GROOVE, borderwidth=3,
                   width=12, anchor="w")
   genderlabel.place(x=10, y=250)

   addresslabel = Label(addroot, text="Enter Address:", bg="cyan", font=('times', 20, "bold"), relief=GROOVE, borderwidth=3,
                   width=12, anchor="w")
   addresslabel.place(x=10, y=310)

   doblabel = Label(addroot, text="Enter D.O.B:", bg="cyan", font=('times', 20, "bold"), relief=GROOVE, borderwidth=3,
                   width=12, anchor="w")
   doblabel.place(x=10, y=370)


   ##################Add employee Entry
   idval=StringVar()
   nameval = StringVar()
   mobileval = StringVar()
   emailval = StringVar()
   genderval = StringVar()
   addressval = StringVar()
   dobval = StringVar()

   identry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
   identry.place(x=250,y=10)

   nameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
   nameentry.place(x=250, y=70)

   mobileentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
   mobileentry.place(x=250, y=130)

   emailentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
   emailentry.place(x=250, y=190)

   genderentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
   genderentry.place(x=250, y=250)

   addressentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
   addressentry.place(x=250, y=310)

   dobentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
   dobentry.place(x=250, y=370)


##################Add Button
   submitbtn=Button(addroot,text="Submit",font=("roman",15,"bold"),width=20,activebackground="cyan",activeforeground="white",bg="red",command=submitadd)
   submitbtn.place(x=150,y=420)
   addroot.mainloop()

def searchemployee():
        def submitsearch():
            id = idval.get()
            name = nameval.get()
            mobile = mobileval.get()
            email = emailval.get()
            address = addressval.get()
            gender = genderval.get()
            dob = dobval.get()
            addeddate = time.strftime("%d/%m/%Y")

            if(id!=''):
                strr='select * from employeedata1 where id=%s'
                mycursor.execute(strr,(id))
                datas=mycursor.fetchall()
                employeetable.delete(*employeetable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    employeetable.insert('', END, values=vv)

            elif (name!= ''):
                strr = 'select * from employeedata1 where name=%s'
                mycursor.execute(strr, (name))
                datas = mycursor.fetchall()
                employeetable.delete(*employeetable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    employeetable.insert('', END, values=vv)

            elif (mobile!= ''):
                strr = 'select * from employeedata1 where mobile=%s'
                mycursor.execute(strr, (mobile))
                datas = mycursor.fetchall()
                employeetable.delete(*employeetable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    employeetable.insert('', END, values=vv)
            elif (email!= ''):
                strr = 'select * from employeedata1 where email=%s'
                mycursor.execute(strr, (email))
                datas = mycursor.fetchall()
                employeetable.delete(*employeetable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    employeetable.insert('', END, values=vv)
            elif (address!= ''):
                strr = 'select * from employeedata1 where address=%s'
                mycursor.execute(strr, (address))
                datas = mycursor.fetchall()
                employeetable.delete(*employeetable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    employeetable.insert('', END, values=vv)

            elif (gender!= ''):
                strr = 'select * from employeedata1 where gender=%s'
                mycursor.execute(strr, (gender))
                datas = mycursor.fetchall()
                employeetable.delete(*employeetable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    employeetable.insert('', END, values=vv)

            elif (dob!= ''):
                strr = 'select * from employeedata1 where dob=%s'
                mycursor.execute(strr, (dob))
                datas = mycursor.fetchall()
                employeetable.delete(*employeetable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    employeetable.insert('', END, values=vv)


            elif (addeddate!= ''):
                strr = 'select * from employeedata1 where addeddate=%s'
                mycursor.execute(strr,(addeddate))
                datas = mycursor.fetchall()
                employeetable.delete(*employeetable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    employeetable.insert('', END, values=vv)

        searchroot = Toplevel(master=DataEntryFrame)
        searchroot.grab_set()
        searchroot.geometry('470x540+220+200')
        searchroot.title('Search Employees')
        searchroot.config(bg="orange")
        searchroot.resizable(False, False)

        ######################search employee labels##################
        idlabel = Label(searchroot, text="Enter Id:", bg="cyan", font=('times', 20, "bold"), relief=GROOVE, borderwidth=3,
                        width=12, anchor="w")
        idlabel.place(x=10, y=10)

        namelabel = Label(searchroot, text="Enter Name:", bg="cyan", font=('times', 20, "bold"), relief=GROOVE,
                          borderwidth=3,
                          width=12, anchor="w")
        namelabel.place(x=10, y=70)

        mobilelabel = Label(searchroot, text="Enter Mobile No.:", bg="cyan", font=('times', 20, "bold"), relief=GROOVE,
                            borderwidth=3,
                            width=12, anchor="w")
        mobilelabel.place(x=10, y=130)

        emaillabel = Label(searchroot, text="Enter Email:", bg="cyan", font=('times', 20, "bold"), relief=GROOVE,
                           borderwidth=3,
                           width=12, anchor="w")
        emaillabel.place(x=10, y=190)

        genderlabel = Label(searchroot, text="Enter Gender:", bg="cyan", font=('times', 20, "bold"), relief=GROOVE,
                            borderwidth=3,
                            width=12, anchor="w")
        genderlabel.place(x=10, y=250)

        addresslabel = Label(searchroot, text="Enter address:", bg="cyan", font=('times', 20, "bold"), relief=GROOVE,
                             borderwidth=3,
                             width=12, anchor="w")
        addresslabel.place(x=10, y=310)

        doblabel = Label(searchroot, text="Enter D.O.B:", bg="cyan", font=('times', 20, "bold"), relief=GROOVE,
                         borderwidth=3,
                         width=12, anchor="w")
        doblabel.place(x=10, y=370)

        datelabel = Label(searchroot, text="Enter D.O.B:", bg="cyan", font=('times', 20, "bold"), relief=GROOVE,
                         borderwidth=3,
                         width=12, anchor="w")
        datelabel.place(x=10, y=430)

        ##################search employee Entry
        idval = StringVar()
        nameval = StringVar()
        mobileval = StringVar()
        emailval = StringVar()
        genderval = StringVar()
        addressval = StringVar()
        dobval = StringVar()
        dateval=StringVar()

        identry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
        identry.place(x=250, y=10)

        nameentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
        nameentry.place(x=250, y=70)

        mobileentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
        mobileentry.place(x=250, y=130)

        emailentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
        emailentry.place(x=250, y=190)

        genderentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
        genderentry.place(x=250, y=250)

        addressentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
        addressentry.place(x=250, y=310)

        dobentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
        dobentry.place(x=250, y=370)

        dateentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
        dateentry.place(x=250, y=430)
        ##################search Button
        submitbtn = Button(searchroot, text="Submit", font=("roman", 15, "bold"), width=20, activebackground="cyan",
                           activeforeground="white", bg="red", command=submitsearch)
        submitbtn.place(x=150, y=480)
        searchroot.mainloop()


def deleteemployee():
   cc=employeetable.focus()
   content=employeetable.item(cc)
   pp=content['values'][0]
   strr='delete from employeedata1 where id=%s'
   mycursor.execute(strr,(pp))
   con.commit()
   messagebox.showinfo('Notification', 'Id {} deleted sucessfully'.format(pp))
   strr = 'select * from employeedata1'
   mycursor.execute(strr)
   datas = mycursor.fetchall()
   employeetable.delete(*employeetable.get_children())
   for i in datas:
       vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
       employeetable.insert('', END, values=vv)




def updateemployee():
    def submitupdate():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date=dateval.get()
        time=timeval.get()

        strr='update employeedata1 set name=%s,mobile=%s, email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Notification', 'Id{} Modified Sucessfully'.format(id),parent=updateroot)
        strr = 'select * from employeedata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        employeetable.delete(*employeetable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            employeetable.insert('', END, values=vv)

        

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x585+220+160')
    updateroot.title('Update Employess Details')
    updateroot.config(bg="orange")
    updateroot.resizable(False, False)

    ######################update employee labels##################
    idlabel = Label(updateroot, text="Update Id:", bg="cyan", font=('times', 20, "bold"), relief=GROOVE, borderwidth=3,
                    width=12, anchor="w")
    idlabel.place(x=10, y=10)

    namelabel = Label(updateroot, text="Update Name:", bg="cyan", font=('times', 20, "bold"), relief=GROOVE,
                      borderwidth=3,
                      width=12, anchor="w")
    namelabel.place(x=10, y=70)

    mobilelabel = Label(updateroot, text="Update Mobile :", bg="cyan", font=('times', 20, "bold"), relief=GROOVE,
                        borderwidth=3,
                        width=12, anchor="w")
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(updateroot, text="Update Email:", bg="cyan", font=('times', 20, "bold"), relief=GROOVE,
                       borderwidth=3,
                       width=12, anchor="w")
    emaillabel.place(x=10, y=190)

    genderlabel = Label(updateroot, text="Update Gender:", bg="cyan", font=('times', 20, "bold"), relief=GROOVE,
                        borderwidth=3,
                        width=12, anchor="w")
    genderlabel.place(x=10, y=250)

    addresslabel = Label(updateroot, text="Update address:", bg="cyan", font=('times', 20, "bold"), relief=GROOVE,
                         borderwidth=3,
                         width=12, anchor="w")
    addresslabel.place(x=10, y=310)

    doblabel = Label(updateroot, text="Update D.O.B:", bg="cyan", font=('times', 20, "bold"), relief=GROOVE,
                     borderwidth=3,
                     width=12, anchor="w")
    doblabel.place(x=10, y=370)

    datelabel = Label(updateroot, text="Update Date:", bg="cyan", font=('times', 20, "bold"), relief=GROOVE,
                      borderwidth=3,
                      width=12, anchor="w")
    datelabel.place(x=10, y=430)

    timelabel = Label(updateroot, text="Update Time:", bg="cyan", font=('times', 20, "bold"), relief=GROOVE,
                      borderwidth=3,
                      width=12, anchor="w")
    timelabel.place(x=10, y=490)

    ##################update employee Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    genderval = StringVar()
    addressval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval=StringVar()

    identry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    genderentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=250)

    addressentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=310)

    dobentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    dateentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)

    timeentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=timeval)
    timeentry.place(x=250, y=490)
    ##################update Button
    submitbtn = Button(updateroot, text="Submit", font=("roman", 15, "bold"), width=20, activebackground="cyan",
                       activeforeground="white", bg="red", command=submitupdate)
    submitbtn.place(x=150, y=540)
    updateroot.mainloop()

    cc=employeetable.focus()
    content=employeetable.item(cc)
    pp=content['values']
    if (len(pp)!=0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])



def showsemployee():
    strr = 'select * from employeedata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    employeetable.delete(*employeetable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        employeetable.insert('', END, values=vv)


def exportemployee():
    ff=filedialog.asksaveasfilename()
    gg=employeetable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content=employeetable.item(i)
        pp=content['values']
        id.append(pp[0]), name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8]),
        dd=['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time']
        df=pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
        paths=r'{}.csv'.format(ff)
        df.to_csv(paths,index=False)
        messagebox.showinfo('Notifications',"Student data is saved{}".format(paths))



def exitemployee():
    res=messagebox.askyesnocancel('Notifications','DO you want to exit')
    if(res==True):
        root.destroy()



##########################################################Connection of database
def Connectdb():
    def submitdb():
        global con,mycursor
        host=hostval.get()
        user=userval.get()
        password=passwordval.get()
       

        try:
             con=pymysql.connect(host="localhost",user="root",password="")
             mycursor=con.cursor()
        except:
              messagebox.showerror('Notification','Data is incorrect Please try again')
              return
        try:
           strr='create database employeemanagementsystem1'
           mycursor.execute(strr)
           strr='Use employeemanagementsystem1'
           mycursor.execute(strr)
           strr='create table employeedata1(id int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50))'
           mycursor.execute(strr)

           strr = 'alter table employeedata1 modify column id int not null'
           mycursor.execute(strr)
           strr = 'alter table employeedata1 modify column id int primary key'
           mycursor.execute(strr)

           messagebox.showinfo('Notification','Database created and Now you are connected to the Database ', parent=dbroot)


        except:
            strr='use employeemanagementsystem1'
            mycursor.execute(strr)
            messagebox.showinfo('Notification',"Now you are connected to the Database", parent=dbroot)
        dbroot.destroy()


    dbroot=Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.resizable(False,False)
    dbroot.config(bg='cyan')

    ########################################Connectionlabel#########

    hostlabel=Label(dbroot,text="Enter host:",bg='cyan',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel=Label(dbroot,text="Enter User:",bg='cyan',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    userlabel.place(x=10,y=70)

    passwordlabel=Label(dbroot,text="Enter Password:",bg='cyan',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    passwordlabel.place(x=10,y=130)


    #######Coonectdb Entry
    hostval=StringVar()
    userval=StringVar()
    passwordval=StringVar()


    hostentry=Entry(dbroot,font=('roman',15,'bold'),bd=5)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5)
    userentry.place(x=250, y=70)

    passwordentry = Entry(dbroot, show='*', font=('roman', 15, 'bold'), bd=5)
    passwordentry.place(x=250, y=130)


    #################################################Connectdb button
    submitbutton=Button(dbroot,text='Submit',font=('roman',15,'bold'),width=20,activebackground='black',activeforeground="white",command=submitdb)
    submitbutton.place(x=150,y=190)

    dbroot.mainloop()


###########################################################################
def tick():
    time_string=time.strftime('%H:%M:%S')
    date_string=time.strftime('%d/%m/%Y')
    clock.config(text='Date:'+date_string+"\n"+"Time:"+time_string)
    clock.after(200,tick)
#######################################################################Intro Slider
import random
colors=["red","green","cyan","cyan","cyan","red2","cyan"]
def IntroLabelColorTick():
    fg=random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(500,IntroLabelColorTick)



def IntroLabelTick():
  global count,text
  if(count>=len(ss)):
    count=0
    text=''
    SliderLabel.config(text=text)
  else:
    text=text+ss[count]
    SliderLabel.config(text=text)
    count +=1
  SliderLabel.after(200,IntroLabelTick)




from tkinter import*
from tkinter import Toplevel
import time
from tkinter import messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import pandas
root=Tk()
root.title('employee Management System')
root.config(bg='cyan')
root.geometry('1200x700+300+20')
root.resizable(False,False)


####################Frames###################
DataEntryFrame=Frame(root,bg="black",relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)

frontlabel=Label(DataEntryFrame,text='Welcome  Employees',width=25,font=('arial',22,'italic bold'),bg='red')
frontlabel.pack(side=TOP,expand=True)

addbtn=Button(DataEntryFrame,text='1.Add employee', width=25, font=('chillar',20,'bold'),bd=6,bg='brown',activebackground='cyan',relief=GROOVE,activeforeground='white',command=addemployee)
addbtn.pack(side=TOP,expand=True)

searchbtn=Button(DataEntryFrame, text='2.Search employee',width=25, font=('chillar',20,'bold'),bd=6,bg='brown',activebackground='cyan',relief=GROOVE,activeforeground='white',command=searchemployee)
searchbtn.pack(side=TOP,expand=True)

deletebtn=Button(DataEntryFrame, text='3.Delete employee',width=25, font=('chillar',20,'bold'),bd=6,bg='brown',activebackground='cyan',relief=GROOVE,activeforeground='white',command=deleteemployee)
deletebtn.pack(side=TOP,expand=True)

updatebtn=Button(DataEntryFrame, text='4.Update employee',width=25, font=('chillar',20,'bold'),bd=6,bg='brown',activebackground='cyan',relief=GROOVE,activeforeground='white',command=updateemployee)
updatebtn.pack(side=TOP,expand=True)

showallbtn=Button(DataEntryFrame, text='5.Show All',width=25, font=('chillar',20,'bold'),bd=6,bg='brown',activebackground='cyan',relief=GROOVE,activeforeground='white',command=showsemployee)
showallbtn.pack(side=TOP,expand=True)

exportbtn=Button(DataEntryFrame, text='6.Export Data',width=25, font=('chillar',20,'bold'),bd=6,bg='brown',activebackground='cyan',relief=GROOVE,activeforeground='white',command=exportemployee)
exportbtn.pack(side=TOP,expand=True)

exitbtn=Button(DataEntryFrame, text='7.Exit',width=25, font=('chillar',20,'bold'),bd=6,bg='brown',activebackground='cyan',relief=GROOVE,activeforeground='white',command=exitemployee)
exitbtn.pack(side=TOP,expand=True)


ShowDataFrame = Frame(root,bg="white",relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=620,height=600)


################ShowDataFarmedatabase#########################
style=ttk.Style()
style.configure('Treeview.Heading',font=('arial',20,'bold'),foreground='black')
style.configure('Treeview',font=('times', 15,'bold'),foreground='black',background='white')
scroll_x=Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y=Scrollbar(ShowDataFrame,orient=VERTICAL)

employeetable=Treeview(ShowDataFrame, columns=('Id','Name',"Mobile","Email",'Address','Gender','D.O.B','Date','Time'),
                      yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x.config(command=employeetable.xview)
scroll_y.config(command=employeetable.yview)
employeetable.heading('Id',text='Id')
employeetable.heading('Name',text='Name')
employeetable.heading('Mobile',text='Mobile')
employeetable.heading('Email',text='Email')
employeetable.heading('Address',text='Address')
employeetable.heading('Gender',text='Gender')
employeetable.heading('D.O.B',text='D.O.B')
employeetable.heading('Date',text='Date')
employeetable.heading('Time',text='Time')

employeetable['show']='headings'
employeetable.column('Id',width=100)
employeetable.column('Name',width=200)
employeetable.column('Mobile',width=200)
employeetable.column('Email',width=300)
employeetable.column('Address',width=200)
employeetable.column('Gender',width=100)
employeetable.column('D.O.B',width=150)
employeetable.column('Date',width=150)
employeetable.column('Time',width=150)



employeetable.pack(fill=BOTH,expand=1)

#################################################################Slider
ss="Welcome To Employee Management System"
count=0
text=""

####################################
SliderLabel=Label(root,text=ss,font=("arial",30,"italic bold"),relief=RIDGE,borderwidth=5,width=30,bg="black")
SliderLabel.place(x=260,y=0)
IntroLabelTick()
IntroLabelColorTick()


###########################################
clock=Label(root,font=('times',14,'bold'),relief=RIDGE,borderwidth=4,bg='orange')
clock.place(x=0,y=0)
tick()
################################################Connect database
connectbutton=Button(root,text="Database Login",width=17,font=("arial",15,"italic bold"),relief=RIDGE,borderwidth=4,bg="orange",activebackground="white",activeforeground="black",command=Connectdb)
connectbutton.place(x=996,y=0)



root.mainloop()