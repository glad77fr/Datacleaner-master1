import tkinter as tk

fenetre = tk.Tk()

champ_label = tk.Label(fenetre, text= "Salut les nazes")

champ_label.pack()

bouton_quiter = tk.Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quiter.pack()

var_case = 3
case = tk.Checkbutton(fenetre, text="Ne plus poser cette question", variable=var_case)
case.pack()

liste = tk.Listbox(fenetre)
liste.pack()

liste.insert('end',"Pierre")

fenetre.mainloop()

