from tkinter import *
import tkinter.ttk as ttk

class Application(Tk):
        def __init__(self, parent):


            Tk.__init__(self, parent)
            self.parent = parent
            self.initialize()
            self.title("Data anomaly detection")
            self.listcontrol = {"Vide":"vide","Space":"space"}
            self.mainloop()

        def initialize(self):

            self.control_menu = Frame(self)
            self.control_menu.pack()

            self.control_text = LabelFrame(self.control_menu,text="Add control",width=330,height=300, labelanchor='n')
            self.control_text.grid(row=1, column=1)
            self.sp_Button = Button(self.control_text, text="Add Simple control")
            self.sp_Button.grid(row=1, column=1, padx=10, pady=10)
            self.cp_Butoon = Button(self.control_text, text="Add Complex control")
            self.cp_Butoon.grid(row=1, column=2, padx=10, pady=10)

            self.conf_text = LabelFrame(self.control_menu, text="Configure control", width=530, height=100,
                                           labelanchor='n')
            self.conf_text.grid(row=2, column=1)

        def add_sp_control(self):
            control = self.ttk.Combobox(self.conf_text,textvariable="Simple control",\
        values=list(self.listcontrol.values()),state='readonly')
            control.grid(row=3, column=1)


toto = Application(None)
toto.mainloop()




"""
        self.sel_place = StringVar()
        self.capital = DoubleVar()
        self.duree = DoubleVar()
        self.taux = DoubleVar()
        self.resultat = DoubleVar()
        self.selection = StringVar()
        self.capital.set(0)
        self.taux.set(0)

        self.grid()
        self.frame_conf = Frame(self)
        self.frame_conf.pack(side="left",expand=1,fill="both")
        self.frame_text=LabelFrame(self.frame_conf,text="Paramètres",width=330,height=300,labelanchor='n')
        self.frame_text.grid(row=2,column=1,sticky="nw",padx=20,pady=10)
        self.frame_res = Frame(self)
        self.frame_res.pack(side="right",expand=1,fill="both")
        self.frame_text2=LabelFrame(self.frame_conf,text="Type simulation",width=200,height=200,labelanchor='n')
        self.frame_text2.grid(row=1,column=1,sticky="nw",padx=20,pady=10)
        self.frame_text3=LabelFrame(self.frame_res,text="Résultat",width=200,height=300, labelanchor='n')
        self.frame_text3.grid(row=1,column=1,sticky="nw",padx=10,pady=10)

        self.txt_conf1=Label(self.frame_text,text="Capital")
        self.txt_conf1.grid(row=1,column=1,sticky="w",padx=3)
        self.txt_conf2=Label(self.frame_text,text="Taux d'intêret")
        self.txt_conf2.grid(row=2,column=1,sticky="w",padx=3)
        self.txt_conf3=Label(self.frame_text,text="Durée année")
        self.txt_conf3.grid(row=3, column=1, sticky="w", padx=3)
        self.txt_typeconf=Label(self.frame_text2,text="Type de placement")
        self.txt_typeconf.grid(row=1,column=1,sticky="w", padx=3)
        self.txt_res=Label(self.frame_text3,text="Gains")
        self.txt_res.grid(row=1,column=1,sticky="w",padx=3,pady=5)
        self.txt_res=Label(self.frame_text3,textvariable=self.resultat)
        self.txt_res.grid(row=1,column=2,padx=3,pady=5)

        self.ent_cap=Entry(self.frame_text,width=7,textvariable=self.capital,justify="right")
        self.ent_cap.grid(row=1, column=2, padx=15)
        self.ent_tx=Entry(self.frame_text,width=7,textvariable=self.taux,justify="right")
        self.ent_tx.grid(row=2, column=2)
        self.ent_dur = Entry(self.frame_text, width=7,textvariable=self.duree,justify="right")
        self.ent_dur.grid(row=3, column=2)
        self.lplace=ttk.Combobox(self.frame_text2,textvariable=self.sel_place,\
        values=list(self.simf.taux_int.values()),state='readonly')
        self.lplace.grid(row=1, column=2,padx=15,pady=5)
        self.ex=Button(self.frame_text,text="Exécuter",command=self.fn)
        self.ex.grid(row=1,column=3,padx=15)

    def fn(self):
        self.simf.txi_capital=self.capital.get()
        self.simf.tx_txi=self.taux.get()
        self.simf.txi_nb_annee=self.duree.get()
        self.selection = self.sel_place.get()

        if self.selection == "Intérêt composé":
            self.resultat.set(self.simf.int_composee())

        if self.selection == "Intérêt valeur acquise":
            self.resultat.set(self.simf.int_val_acquise())



toto = Application(None)
toto.title='lol'
toto.mainloop()"""