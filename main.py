import os
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import glob
import shutil
import pygame
pygame.mixer.init()

def rename0():
    pygame.mixer.music.load('KeypressReturn.ogg')
    pygame.mixer.music.play(loops=0)
    filename: str = filedialog.askopenfilename(initialdir="C:\\Users\\" + os.getlogin(), title="choisissez un fichier",
                                               filetypes=(("fichiers pdf", "*.pdf"), ("fichiers mp4", "*.mp4"),
                                                          ("tous fichiers", "*.*")))
    myfen = Tk()
    myfen.title('Renommer')
    Label(myfen, text='Entrer le nouveau nom', font=('calibri', 30)).grid(row=0, column=0, sticky='N E S w', pady=5,padx=5)
    entree = Entry(myfen)
    entree.grid(row=1, column=1, sticky='N E S w', pady=5, padx=5)
    pth = os.path.dirname(filename)
    b = os.path.splitext(os.path.basename(filename))[-1]

    def Valider():
        pygame.mixer.music.load('KeypressReturn.ogg')
        pygame.mixer.music.play(loops=0)
        os.rename(filename, pth + '\\' + entree.get()+b)
        pygame.mixer.music.load('Dock.ogg')
        pygame.mixer.music.play(loops=0)
        messagebox.showinfo(title='infos', message='le fichier a éte renommé avec succès')
        myfen.destroy()
    Button(myfen, text='Valider', command=Valider).grid(row=2, column=1, sticky='N E S W', padx=5, pady=5)
    myfen.mainloop()


def rename1():
    pygame.mixer.music.load('KeypressReturn.ogg')
    pygame.mixer.music.play(loops=0)
    director = filedialog.askdirectory(initialdir="C:\\Users\\" + os.getlogin(), title='choisir le repertoire cible')
    mywin = Tk()
    mywin.title('Renommer')
    Label(mywin, text='Entrer ', font=('calibri', 30)).grid(row=0, column=1, sticky='N E S w', pady=5, padx=5)
    entree = Entry(mywin)
    entree.grid(row=1, column=1, sticky='N E S w', pady=5, padx=5)
    lisfich = []
    def Valider():
        for i in glob.glob(director + '\\' + '*.*'):
            lisfich.append(i)
        for elt in lisfich:
            pth = os.path.dirname(elt)
            os.rename(elt, pth + '\\' + entree.get() + os.path.basename(elt))
            pygame.mixer.music.load('Dock.ogg')
            pygame.mixer.music.play(loops=0)
        mywin.destroy()
        messagebox.showinfo(title='infos', message='le fichiers ont éte renommés avec succès')

    Button(mywin, text='Valider', command=Valider).grid(row=2, column=1, sticky='N E S W', padx=5, pady=5)

    mywin.mainloop()


def rename2():
    pygame.mixer.music.load('KeypressReturn.ogg')
    pygame.mixer.music.play(loops=0)
    director = filedialog.askdirectory(initialdir='C:\\Users\\' + os.getlogin(), title='choisir le repertoire cible')
    mywin = Tk()
    mywin.title('Renommer')
    Label(mywin, text='Entrer ', font=('calibri', 30)).grid(row=0, column=1, sticky='N E S w', pady=5, padx=5)
    entree = Entry(mywin)
    entree.grid(row=1, column=1, sticky='N E S w', pady=5, padx=5)
    lisfich = []

    def Valider():
        for i in glob.glob(director + '\\'+'*.*'):
            lisfich.append(i)
        for elt in lisfich:
            pth = os.path.dirname(elt)
            a = os.path.splitext(os.path.basename(elt))[0]
            b = os.path.splitext(os.path.basename(elt))[-1]
            os.rename(elt, pth + '\\' + a + entree.get())
            pygame.mixer.music.load('Dock.ogg')
            pygame.mixer.music.play(loops=0)
        mywin.destroy()
        messagebox.showinfo(title='infos', message='le fichiers ont éte renommés avec succès')

    Button(mywin, text='Valider', command=Valider).grid(row=2, column=1, sticky='N E S W', padx=5, pady=5)

    mywin.mainloop()


def rename3():
    pygame.mixer.music.load('KeypressReturn.ogg')
    pygame.mixer.music.play(loops=0)
    director = filedialog.askdirectory(initialdir='C:\\Users\\' + os.getlogin(), title='choisir le repertoire cible')
    lisfich = []
    for i in glob.glob(director + '\\' + '*.*'):
        lisfich.append(i)
        lisfich.sort(key=os.path.getctime)
    i = -1
    pth = os.path.dirname(lisfich[-1])
    vb = os.listdir(pth)
    #for elt in lisfich:
    while i < len(lisfich) - 1:
        i += 1
        os.rename(lisfich[i], pth + '\\' + str(i) + '.' + vb[i])
    pygame.mixer.music.load('Dock.ogg')
    pygame.mixer.music.play(loops=0)
    messagebox.showinfo(title='infos', message='le fichiers ont éte renommés avec succès')  # if fau revoir


def rename4():
    pygame.mixer.music.load('KeypressReturn.ogg')
    pygame.mixer.music.play(loops=0)
    director = filedialog.askdirectory(initialdir='C:\\Users\\' + os.getlogin(), title='choisir le repertoire cible')
    mywin = Tk()
    mywin.title('Renommer')
    Label(mywin, text='Entrer ', font=('calibri', 30)).grid(row=0, column=1, sticky='N E S w', pady=5, padx=5)
    entree = Entry(mywin)
    entree.grid(row=1, column=1, sticky='N E S w', pady=5, padx=5)
    lisfich = []

    def Valider():
        for i in glob.glob(director + '\\' + '*.*'):
            lisfich.append(i)
        for elt in lisfich:
            pth = os.path.dirname(elt)
            a = os.path.splitext(os.path.basename(elt))[0]
            os.rename(elt, pth + '\\' + a + entree.get())
            pygame.mixer.music.load('Dock.ogg')
            pygame.mixer.music.play(loops=0)
        mywin.destroy()
        messagebox.showinfo(title='infos', message='le fichiers ont éte renommés avec succès')

    Button(mywin, text='Valider', command=Valider).grid(row=2, column=1, sticky='N E S W', padx=5, pady=5)

    mywin.mainloop()


def Create():
    director = filedialog.askdirectory(initialdir='C:\\Users\\' + os.getlogin(), title='Enregistrer sous')
    mywin = Tk()
    mywin.title('Renommer')
    Label(mywin, text='Entrer ', font=('calibri', 30)).grid(row=0, column=1, sticky='N E S w', pady=5, padx=5)
    entree = Entry(mywin)
    entree.grid(row=1, column=1, sticky='N E S w', pady=5, padx=5)

    def Creer():
        a = director + '\\' + entree.get()
        a = str(a)
        try:
            os.mkdir(a)
            pygame.mixer.music.load('Dock.ogg')
            pygame.mixer.music.play(loops=0)
            messagebox.showinfo(title='infos', message=f'le dossier {entree.get()} a été créé avec succès')
            mywin.destroy()
        except FileExistsError:
            while FileExistsError:
                messagebox.showerror(title='Erreur', message='Veuillez entrer un nom pour votre dossier')
                ent = Entry(mywin)
                b = director + '\\' + ent.get()
                b = str(b)
                os.mkdir(b)
                pygame.mixer.music.load('Dock.ogg')
                pygame.mixer.music.play(loops=0)

                messagebox.showinfo(title='infos', message=f'le dossier {entree.get()} a été créé avec succès')
                mywin.destroy()
    Button(mywin, text='Creer', command=Creer).grid(row=2, column=1, sticky='N E S W', padx=5, pady=5)
    mywin.mainloop()

def about():
    myr = Tk()
    a = Label(myr,
              text='À propos \n je m\'appelle ZONGO T Achille Caleb \n Ce programme permet de réaliser des taches répétitives en un seul clic  par exemple quand vous voulez renommer et classer des fichiers en masse\nVous pouvez me contacter  par whatsApp  au  +22656311497 ou par e-mail zongoachille06@gmail.com \n Toute modification ou appropriation du script sans l’avis de l’auteur est interdite.',bg='white')
    a.grid()
    Button(myr, text='retour', command=myr.destroy).grid()
    myr.mainloop()

def move():
    pygame.mixer.music.load('KeypressReturn.ogg')
    pygame.mixer.music.play(loops=0)
    fichiers = filedialog.askopenfilenames(title='Selectionner', initialdir='C:\\Users\\' + os.getlogin())
    destiny = filedialog.askdirectory(title='Deplacer vers', initialdir='C:\\Users\\' + os.getlogin())
    fichier = fichiers[0]
    shutil.move(fichier,destiny)
    pygame.mixer.music.load('Dock.ogg')
    pygame.mixer.music.play(loops=0)
    messagebox.showinfo(title='infos', message=f'Deplacés avec succès')

my_window = Tk()
my_window.title("Renommeur de fichiers")
my_window.geometry("445x560")
my_window.iconphoto(False, PhotoImage(file='icone.png'))
Label(my_window, text="Bienvenue !", font=('times new roman', 20,'bold'),relief=GROOVE,bg='white',fg='green').grid(row=0, column=0, sticky='N E S W', pady=5, padx=5,columnspan=3)

# création de la barre des menus
menuBar = Menu(my_window)
# création du menu principale
menuOption = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Options', menu=menuOption)
# création des sous menus
menuOption.add_command(label='Nouveau dossier', command=Create)
menuOption.add_command(label='À propos', command=about)
menuOption.add_command(label='quitter', command=my_window.quit)
# configuration
my_window.config(menu=menuBar)
photo = PhotoImage(file='renommer0.png')
img = photo.subsample(9, 9)
Label(my_window, text='Renommer un fichier',font=('JetBrain Mono',12)).grid(row=1, column=0, sticky='w', pady=5, padx=5)
Button(my_window, image=img, command=rename0).grid(row=2, column=0, sticky='w', pady=5, padx=5)
photo1 = PhotoImage(file='renommer_debut.png')
img1 = photo1.subsample(3, 3)
Label(my_window, text='Renommer au début',font=('JetBrain Mono',12)).grid(row=1, column=1, sticky='w', pady=5, padx=5)
Button(my_window, image=img1, command=rename1).grid(row=2, column=1, sticky='w', pady=5, padx=5)

photo2 = PhotoImage(file='renommer_fin.png')
img2 = photo2.subsample(3, 3)
Label(my_window, text='Renommer à la fin',font=('JetBrain Mono',12)).grid(row=3, column=0, sticky='w', pady=5, padx=5)
Button(my_window, image=img2, command=rename2).grid(row=4, column=0, sticky='w', pady=5, padx=5)

photo3 = PhotoImage(file='renommer_ordre.png')
img3 = photo3.subsample(9, 9)
Label(my_window, text='Renommer pour ordonner',font=('JetBrain Mono',12)).grid(row=3, column=1, sticky='w', pady=5, padx=5)
Button(my_window, image=img3, command=rename3).grid(row=4, column=1, sticky='w', pady=5, padx=5)
photo4 = PhotoImage(file='extentions.png')
img4 = photo4.subsample(3, 3)
Label(my_window, text='Renommer les extensions',font=('JetBrain Mono',12)).grid(row=5, column=0, sticky='w', pady=5, padx=5)
Button(my_window, image=img4, command=rename4).grid(row=6, column=0, sticky='w', pady=5, padx=5)
photo5 = PhotoImage(file='move5.png')
img5 = photo5.subsample(7, 7)
Label(my_window, text='Deplacer des fichiers',font=('JetBrain Mono',12)).grid(row=5, column=1, sticky='w', pady=5, padx=5)
Button(my_window, image=img5, command=move).grid(row=6, column=1, sticky='w', pady=5, padx=5)
my_window.mainloop()
os.system("pause")
a = input("")