# -*- coding: utf-8 -*-
"""
Created on Mon May  6 20:36:33 2019

@author: sumit
"""
a1 = 0; a2  =0; a3 =0; a4 =0; a5 =0; a6 =0; a7 =0; a8 =0; a9 =0; a10  =0;a11 =0;
'''def sound():
    import winsound
    winsound.Beep(1500, 1)
    winsound.Beep(1500, 1)
    winsound.Beep(2500, 1599)'''
# last value taking gui 
from tkinter import *
def get_val1():
    def spc1():
        global a1
        xucl =62.80189
        xlcl = 62.72601
        rucl = 32
        rlcl = 0.1391
        print((e1.get(), e2.get(),e3.get()))
        y = int(e1.get())+  int(e2.get())+  int(e3.get())
        x_bar = y/3
        r_bar = max(int(e1.get()),  int(e2.get()),  int(e3.get())) - min(int(e1.get()),  int(e2.get()),  int(e3.get()))
        print('xbar: ',x_bar,' and r_bar: ', r_bar)
        if  x_bar>xucl:
            a1 =1
        if x_bar<xlcl:
            a1 =1
        if r_bar>rucl:
            a1 =1
        if r_bar<=rlcl:
            a1 =1
        if a1 !=0:
            b = Button(root, text="                        NDE  Brg   high  temp                    ",width=21, height=2,  bg="red", command =hello1 ).place(x=20,y=a)
            #sound()
    master = Tk()
    master.geometry('+700+100')
    Label(master, text="in1").grid(row=0)
    Label(master, text="in2").grid(row=1)
    Label(master, text="in3").grid(row=2)
    
    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    
    Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='Calculate', command=spc1).grid(row=3, column=1, sticky=W, pady=4)

    mainloop( )

##################################################################################################################
##################################################################################################################
def get_val2():
    def spc2():
        global a2
        xucl =50 
        xlcl = 10
        rucl = 32
        rlcl = 0
        print((e1.get(), e2.get(),e3.get()))
        y = int(e1.get())+  int(e2.get())+  int(e3.get())
        x_bar = y/3
        r_bar = max(int(e1.get()),  int(e2.get()),  int(e3.get())) - min(int(e1.get()),  int(e2.get()),  int(e3.get()))
        print('xbar: ',x_bar,' and r_bar: ', r_bar)
        if  x_bar>=xucl:
            a2 =1
        if x_bar<=xlcl:
            a2 =1
        if r_bar>=rucl:
            a2 =1
        if r_bar<=rlcl:
            a2 =1
        if a2 !=0:
            b = Button(root, text="                 Coil 1 fail               ",width=21, height=2,  bg="red", command =hello2 ).place(x=20,y=a+60)
            sound()
    master = Tk()
    master.geometry('+700+100')
    Label(master, text="in1").grid(row=0)
    Label(master, text="in2").grid(row=1)
    Label(master, text="in3").grid(row=2)
    
    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    
    Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='Calculate', command=spc2).grid(row=3, column=1, sticky=W, pady=4)

    mainloop( )
##################################################################################################################
##################################################################################################################
def get_val3():
    def spc3():
        global a3
        xucl =50 
        xlcl = 10
        rucl = 32
        rlcl = 0
        print((e1.get(), e2.get(),e3.get()))
        y = int(e1.get())+  int(e2.get())+  int(e3.get())
        x_bar = y/3
        r_bar = max(int(e1.get()),  int(e2.get()),  int(e3.get())) - min(int(e1.get()),  int(e2.get()),  int(e3.get()))
        print('xbar: ',x_bar,' and r_bar: ', r_bar)
        if  x_bar>=xucl:
            a3 =1
        if x_bar<=xlcl:
            a3 =1
        if r_bar>=rucl:
            a3 =1
        if r_bar<=rlcl:
            a3 =1
        if a3 !=0:
            b = Button(root, text="                 Coil 2 fail               ",width=21, height=2,  bg="red", command =hello3 ).place(x=20,y=a+120)
            sound()
    master = Tk()
    master.geometry('+700+100')
    Label(master, text="in1").grid(row=0)
    Label(master, text="in2").grid(row=1)
    Label(master, text="in3").grid(row=2)
    
    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    
    Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='Calculate', command=spc3).grid(row=3, column=1, sticky=W, pady=4)

    mainloop( )
##################################################################################################################
##################################################################################################################
def get_val4():
    def spc4():
        global a4
        xucl =50 
        xlcl = 10
        rucl = 32
        rlcl = 0
        print((e1.get(), e2.get(),e3.get()))
        y = int(e1.get())+  int(e2.get())+  int(e3.get())
        x_bar = y/3
        r_bar = max(int(e1.get()),  int(e2.get()),  int(e3.get())) - min(int(e1.get()),  int(e2.get()),  int(e3.get()))
        print('xbar: ',x_bar,' and r_bar: ', r_bar)
        if  x_bar>=xucl:
            a4 =1
        if x_bar<=xlcl:
            a4 =1
        if r_bar>=rucl:
            a4 =1
        if r_bar<=rlcl:
            a4 =1
        if a4 !=0:
            b = Button(root, text="                 Coil 3 fail               ",width=21, height=2,  bg="red", command =hello4 ).place(x=20,y=a+180)
            sound()
    master = Tk()
    master.geometry('+700+100')
    Label(master, text="a1").grid(row=0)
    Label(master, text="a2").grid(row=1)
    Label(master, text="a3").grid(row=2)
    
    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    
    Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='Calculate', command=spc4).grid(row=3, column=1, sticky=W, pady=4)

    mainloop( )



# all the branch function to make the branch red 
b = 20
# when the insert button is pressed this code will be executed : 


def inse():
    
    root = Tk()
    
    root.title('SPC and FTA')
    # display the menu
    mainframe = Frame(root)
    mainframe.grid(column =0, row =0, sticky= (N,W,E,S))
    root.geometry('+500+100')
    mainframe.columnconfigure(0, weight = 1)
    mainframe.rowconfigure(0, weight =1)
    mainframe.pack(pady = 150, padx = 150)
    menubar = Menu(root)
    menubar.add_command(label = 'hello')
    menubar.add_command (label = 'quit')
    root.config(menu= menubar)
    b= 20
    a = 50
    #### for column 1 buttons #####################################################33
    c = Button(root, text="                        NDE  Brg   high  temp                    ",width=21, height=2,  bg="cyan", command =get_val1 ).place(x=10,y=a)
    c = Button(root, text="                 Coil 1 fail               ",width=b, height=2,  bg="cyan", command =get_val2 ).place(x=10,y=a+60)
    c = Button(root, text="                 Coil 2 fail               ",width=b, height=2,  bg="cyan", command =get_val3 ).place(x=10,y=a+120)
    c = Button(root, text="                 Coil 3 fail               ",width=b, height=2,  bg="cyan", command =get_val4 ).place(x=10,y=a+180)



# please apply this function to show the failure : if the value is grater than 0 it means there is a failure. 
def FTA():
    b= 20
    a = 100
    #### for column 1 buttons #####################################################33
    if a1 !=0:
        b = Button(root, text="                        NDE  Brg   high  temp                    ",width=21, height=2,  bg="red", command =hello1 ).place(x=10,y=a)
    if a2 != 0:
        b = Button(root, text="                 Coil 1 fail               ",width=b, height=2,  bg="green", command =hello2 ).place(x=10,y=a+60)
    if a3 != 0:
        b = Button(root, text="                 Coil 2 fail               ",width=b, height=2,  bg="green", command =hello3 ).place(x=10,y=a+120)
    if a4 != 0:
        b = Button(root, text="                 Coil 3 fail               ",width=b, height=2,  bg="green", command =hello4 ).place(x=10,y=a+180)
    if a5 != 0:    
        b = Button(root, text="DE Bearing Temp High         ",width=b, height=2,  bg="green", command =hello5 ).place(x=10,y=a+240)
    if a6 != 0:    
        b = Button(root, text="Motion current fluctuation   ",width=b, height=2,  bg="green", command =hello6 ).place(x=10,y=a+300)
    ### for column 2 buttons ########################
    if a7 != 0:    
        b = Button(root, text="     Shaft 3_4 fail  ",width=b, height=2,  bg="green", command =hello7 ).place(x=190,y=a)
    if a8 != 0:    
        b = Button(root, text=" Vibration32_4 Y ",width=b, height=2,  bg="green", command =hello8 ).place(x=190,y=a+60)
    if a9 != 0:    
        b = Button(root, text="High Temp 32-4",width=b, height=2,  bg="green", command =hello9 ).place(x=190,y=a+120)
    if a10 != 0:   
        b = Button(root, text=" Vibration32_4 X ",width=b, height=2,  bg="green", command =hello10 ).place(x=190,y=a+180)



def hello1():
    
    
    # NOTE: the subgraph name needs to begin with 'cluster' (all lowercase)
    #       so that Graphviz recognizes it as a special cluster subgraph
    from graphviz import Digraph
    g = Digraph('G', filename='cluster.gv')
    with g.subgraph(name='cluster_0') as c:
        c.attr(style='filled')
        c.attr(color='white')
        c.edges([('Or Gate1', 'NDE Bearing damage'), ('NDE Bearing damage','Or Gate4'), ('Or Gate4','NDE Brg high temp')])
        #c.attr(label='process #1')
    g.edge('Compressor Failure', 'Or Gate0')
    g.edge('Or Gate0', 'Driver motor subsystem fail')
    g.edge('Driver motor subsystem fail','Or Gate1')
    # make the gates and blocks colorful: failed condition: red 
    g.node('NDE Bearing damage', shape='rectangle', style = 'filled', color = 'red')
    g.node('Compressor Failure', shape='rectangle', style = 'filled', color = 'red')
    g.node('Driver motor subsystem fail', shape='rectangle', style = 'filled', color = 'red')
    g.node('Or Gate1', shape='triangle', style = 'filled', color = 'red')
    g.node('Or Gate0', shape='triangle', style = 'filled', color = 'red')
    g.node('Or Gate4', shape='triangle', style = 'filled', color = 'red')
    g.node('NDE Bearing damage', shape='rectangle', style = 'filled', color = 'red')
    g.node('NDE Brg high temp', shape='rectangle', style = 'filled', color = 'red')
    g.view()

def hello():
    print('hi i am sumit')
################################################################### Coil 2 fail ###########
def hello2():
    # NOTE: the subgraph name needs to begin with 'cluster' (all lowercase)
    #       so that Graphviz recognizes it as a special cluster subgraph
    from graphviz import Digraph
    g = Digraph('G', filename='cluster.gv')
    with g.subgraph(name='cluster_0') as c:
        c.attr(style='filled')
        c.attr(color='white')
        c.edges([('Or Gate1', 'Stator coil fail'), ('Stator coil fail','Or Gate_1'), ('Or Gate_1','Coil 1 fail')])
        #c.attr(label='process #1')
    g.edge('Compressor Failure', 'Or Gate0')
    g.edge('Or Gate0', 'Driver motor subsystem fail')
    g.edge('Driver motor subsystem fail','Or Gate1')
    # make the gates colorful
    g.node('Stator coil fail', shape='rectangle', style = 'filled', color = 'red')
    g.node('Compressor Failure', shape='rectangle', style = 'filled', color = 'red')
    g.node('Driver motor subsystem fail', shape='rectangle', style = 'filled', color = 'red')
    g.node('Or Gate1', shape='triangle', style = 'filled', color = 'red')
    g.node('Or Gate0', shape='triangle', style = 'filled', color = 'red')
    g.node('Or Gate_1', shape='triangle', style = 'filled', color = 'red')
    g.node('Coil 1 fail', shape='rectangle', style = 'filled', color = 'red')
    g.view()
################################################################### Coil 2 fail ###########
def hello3():
    from graphviz import Digraph
    g = Digraph('G', filename='cluster.gv')
    with g.subgraph(name='cluster_0') as c:
        c.attr(style='filled')
        c.attr(color='white')
        c.edges([('Or Gate1', 'Stator coil fail'), ('Stator coil fail','Or Gate_1'), ('Or Gate_1','Coil 2 fail')])
        #c.attr(label='process #1')
    g.edge('Compressor Failure', 'Or Gate0')
    g.edge('Or Gate0', 'Driver motor subsystem fail')
    g.edge('Driver motor subsystem fail','Or Gate1')
    # make the gates colorful
    g.node('Stator coil fail', shape='rectangle', style = 'filled', color = 'red')
    g.node('Compressor Failure', shape='rectangle', style = 'filled', color = 'red')
    g.node('Driver motor subsystem fail', shape='rectangle', style = 'filled', color = 'red')
    g.node('Or Gate1', shape='triangle', style = 'filled', color = 'red')
    g.node('Or Gate0', shape='triangle', style = 'filled', color = 'red')
    g.node('Or Gate_1', shape='triangle', style = 'filled', color = 'red')
    g.node('Coil 2 fail', shape='rectangle', style = 'filled', color = 'red')
    g.view()
################################################################### Coil 3 fail ###########
def hello4():
    from graphviz import Digraph
    g = Digraph('G', filename='cluster.gv')
    with g.subgraph(name='cluster_0') as c:
        c.attr(style='filled')
        c.attr(color='white')
        c.edges([('Or Gate1', 'Stator coil fail'), ('Stator coil fail','Or Gate_1'), ('Or Gate_1','Coil 3 fail')])
        #c.attr(label='process #1')
    g.edge('Compressor Failure', 'Or Gate0')
    g.edge('Or Gate0', 'Driver motor subsystem fail')
    g.edge('Driver motor subsystem fail','Or Gate1')
    # make the gates colorful
    g.node('Stator coil fail', shape='rectangle', style = 'filled', color = 'red')
    g.node('Compressor Failure', shape='rectangle', style = 'filled', color = 'red')
    g.node('Driver motor subsystem fail', shape='rectangle', style = 'filled', color = 'red')
    g.node('Or Gate1', shape='triangle', style = 'filled', color = 'red')
    g.node('Or Gate0', shape='triangle', style = 'filled', color = 'red')
    g.node('Or Gate_1', shape='triangle', style = 'filled', color = 'red')
    g.node('Coil 3 fail', shape='rectangle', style = 'filled', color = 'red')
    g.view()
def hello7():
    from graphviz import Digraph
    g = Digraph('G', filename='cluster.gv')
    #c.attr(label='process #1')
    g.edge('Compressor Failure', 'Or Gate0')
    g.edge('Or Gate0', 'Compression subsystem fail')
    g.edge('Compression subsystem fail','Pinion shaft assy II fail')
    g.edge('Pinion shaft assy II fail', 'Or Gate9')
    g.edge('Or Gate9', 'Shaft 3_4 fail')
    
    # make the gates colorful
    g.node('Compressor Failure', shape='rectangle', style = 'filled', color = 'red')
    g.node('Compression subsystem fail', shape='rectangle', style = 'filled', color = 'red')
    g.node('Or Gate9', shape='triangle', style = 'filled', color = 'red')
    g.node('Or Gate0', shape='triangle', style = 'filled', color = 'red')
    g.node('Pinion shaft assy II fail', shape='rectangle', style = 'filled', color = 'red')
    g.node('Shaft 3_4 fail', shape='rectangle', style = 'filled', color = 'red')
    g.view()
def hello():
    print('hi i am sumit')
def hello5():
    from graphviz import Digraph
    g = Digraph('G', filename='cluster.gv')
    with g.subgraph(name='cluster_0') as c:
        c.attr(style='filled')
        c.attr(color='white')
        c.edges([('Or Gate1', 'DE Bearing Temp High'), ('DE Bearing Temp High','Vibration31_4 Y')])
        #c.attr(label='process #1')
    g.edge('Compressor Failure', 'Or Gate0')
    g.edge('Or Gate0', 'Driver motor subsystem fail')
    g.edge('Driver motor subsystem fail','Or Gate1')
    # make the gates colorful
    g.node('DE Bearing Temp High', shape='rectangle', style = 'filled', color = 'red')
    g.node('Compressor Failure', shape='rectangle', style = 'filled', color = 'red')
    g.node('Driver motor subsystem fail', shape='rectangle', style = 'filled', color = 'red')
    g.node('Or Gate1', shape='triangle', style = 'filled', color = 'red')
    g.node('Or Gate0', shape='triangle', style = 'filled', color = 'red')
    g.node('Vibration31_4 Y', shape='rectangle', style = 'filled', color = 'red')
    g.view()
def hello6():
    from graphviz import Digraph
    g = Digraph('G', filename='cluster.gv')
    with g.subgraph(name='cluster_0') as c:
        c.attr(style='filled')
        c.attr(color='white')
        c.edges([('Or Gate1', 'Motor current fluctuation')])
        #c.attr(label='process #1')
    g.edge('Compressor Failure', 'Or Gate0')
    g.edge('Or Gate0', 'Driver motor subsystem fail')
    g.edge('Driver motor subsystem fail','Or Gate1')
    # make the gates colorful
    g.node('Motor current fluctuation', shape='rectangle', style = 'filled', color = 'red')
    g.node('Compressor Failure', shape='rectangle', style = 'filled', color = 'red')
    g.node('Driver motor subsystem fail', shape='rectangle', style = 'filled', color = 'red')
    g.node('Or Gate1', shape='triangle', style = 'filled', color = 'red')
    g.node('Or Gate0', shape='triangle', style = 'filled', color = 'red')
    g.view()
def hello8():
    print('hi i am sumit')
def hello9():
    print('hi i am sumit')
def hello10():
    print('hi i am sumit')
def hello11():
    print('hi i am sumit')


###############################################################################
##############################33 GUI tkinter###################################
from tkinter import * 
root = Tk()

root.title('SPC and FTA')
root.geometry('+100+100')
# display the menu
mainframe = Frame(root)
mainframe.grid(column =0, row =0, sticky= (N,W,E,S))
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight =1)
mainframe.pack(pady = 250, padx = 500)
menubar = Menu(root)
menubar.add_command(label = 'hello')
menubar.add_command (label = 'quit')
root.config(menu= menubar)
b= 20
a = 100
################################################################## Name and Nomenclature########################
NDE = "                        NDE  Brg   high  temp, 0.0205                    "
#### for column 1 buttons #####################################################33
b = Button(root, text=NDE,width=21, height=2,  bg="green", command =hello1 ).place(x=20,y=a)
b = Button(root, text="         Coil 1 fail, 0.0190          ",width=b, height=2,  bg="green", command =hello2 ).place(x=20,y=a+60)
b = Button(root, text="         Coil 2 fail, 0.0190          ",width=b, height=2,  bg="green", command =hello3 ).place(x=20,y=a+120)
b = Button(root, text="         Coil 3 fail, 0.0190          ",width=b, height=2,  bg="green", command =hello4 ).place(x=20,y=a+180)
b = Button(root, text="DE Brg Temp High, 0.0205    ",width=b, height=2,  bg="green", command =hello5 ).place(x=20,y=a+240)
b = Button(root, text="Motor current fluct.  , 0.0206",width=b, height=2,  bg="green", command =hello6 ).place(x=20,y=a+300)
### for column 2 buttons ########################
b = Button(root, text="   Shaft 3_4 fail, 0.1098    ",width=b, height=2,  bg="green", command =hello7 ).place(x=190,y=a)
b = Button(root, text=" Vibration32_4 Y, 0.0198 ",width=b, height=2,  bg="green", command =hello8 ).place(x=190,y=a+60)
b = Button(root, text="  High Temp 32-4, 0.019",width=b, height=2,  bg="green", command =hello9 ).place(x=190,y=a+120)
b = Button(root, text=" Vibration32_4 X, 0.0198 ",width=b, height=2,  bg="green", command =hello10 ).place(x=190,y=a+180)
b = Button(root, text="High Temp 31-4, 0.019  ",width=b, height=2,  bg="green", command =hello11 ).place(x=190,y=a+240)
b = Button(root, text="  Vibration31_4 Y, 0.019  ",width=b, height=2,  bg="green", command =hello ).place(x=190,y=a+300)
###### for column 3 buttons #############################
b = Button(root, text="     Vibration31_4 X, 0.019     ",width=b, height=2,  bg="green", command =hello ).place(x=340,y=a)
b = Button(root, text="Flow Molecular sieve, 0.019 ",width=b, height=2,  bg="green", command =hello ).place(x=340,y=a+60)
b = Button(root, text="   Outlet air pressure, 0.019  ",width=b, height=2,  bg="green", command =hello ).place(x=340,y=a+120)
b = Button(root, text="          Spindle fail, 0.019        ",width=b, height=2,  bg="green", command =hello1).place(x=340,y=a+180)
b = Button(root, text="     IGV opening fail, 0.019    ",width=b, height=2,  bg="green", command =hello ).place(x=340,y=a+240)
b = Button(root, text="      Brg1 high temp, 0.019    ",width=b, height=2,  bg="green", command =hello ).place(x=340,y=a+300)
############ for column 4 buttons #####################################
b = Button(root, text="   Vibration11_2 Y, 0.019  ",width=b, height=2,  bg="green", command =hello ).place(x=510,y=a)
b = Button(root, text="Lubrication p low, 0.019 ",width=b, height=2,  bg="green", command =hello ).place(x=510,y=a+60)
b = Button(root, text="  Vibration11_2 X, 0.019   ",width=b, height=2,  bg="green", command =hello ).place(x=510,y=a+120)
b = Button(root, text="  Vibration21_2 Y, 0.019   ",width=b, height=2,  bg="green", command =hello ).place(x=510,y=a+180)
b = Button(root, text="   Vibration21_2 X, 0.019  ",width=b, height=2,  bg="green", command =hello ).place(x=510,y=a+240)
b = Button(root, text="  Brg1 high temp, 0.019   ",width=b, height=2,  bg="green", command =hello ).place(x=510,y=a+300)
############ ror column 5 buttons ##########################3
b = Button(root, text="  Brg2 high temp, 0.019     ",width=b, height=2,  bg="green", command =hello ).place(x=660,y=a)
b = Button(root, text="    Shaft displaced, 0.019    ",width=b, height=2,  bg="green", command =hello ).place(x=660,y=a+60)
b = Button(root, text="Inlet air temp high1, 0.019",width=b, height=2,  bg="green", command =hello ).place(x=660,y=a+120)
b = Button(root, text="Inlet air temp high2, 0.019",width=b, height=2,  bg="green", command =hello ).place(x=660,y=a+180)
b = Button(root, text="Inlet air temp high3, 0.019",width=b, height=2,  bg="green", command =hello ).place(x=660,y=a+240)
b = Button(root, text="Inlet air temp high4, 0.019",width=b, height=2,  bg="green", command =hello ).place(x=660,y=a+300)
############## for column 6 buttons 
b = Button(root, text="    Shaft 1_2 fail, 0.019  ",width=b, height=2,  bg="green", command =hello ).place(x=820,y=a)
b = Button(root, text="High Temp 21-2, 0.019",width=b, height=2,  bg="green", command =hello ).place(x=820,y=a+60)
b = Button(root, text="High Temp 11-2, 0.019",width=b, height=2,  bg="green", command =hello ).place(x=820,y=a+120)
#b = Button(root, text="component34",width=b, height=2,  bg="lightblue", command =hello ).place(x=710,y=a+180)
b = Button(root, text="Analyze",width=10, height=2,  bg='yellow', command =FTA ).place(x=10,y=30)
b = Button(root, text="Insert",width=10, height=2,  bg='cyan', command =inse ).place(x=700,y=30)
b = Button(root, text="Generate Report",width=20, height=2,  bg='yellow', command =hello ).place(x=190,y=30)

#b.pack(side = 'left')
#actionBtn = Button(root, text="Enter", width=15, height=2, command=quit).place(x=0, y=0)

    

root.mainloop()
