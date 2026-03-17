import tkinter as tk
import subprocess
import time
import threading

import os
os.environ["PIBOOTH_VKEYBOARD"] = "0"


# Identifiants autorisés
ADMIN_USER = "rpi"
ADMIN_PASS = "rpi"

def launch_pibooth():
    root.destroy()
    subprocess.Popen(["pibooth"])

def launch_desktop():
    root.destroy()
    subprocess.Popen(["startx"])

def check_login():
    user = entry_user.get()
    pwd = entry_pass.get()
    if user == ADMIN_USER and pwd == ADMIN_PASS:
        login_win.destroy()
        launch_desktop()
    else:
        lbl_error.config(text="Identifiants incorrects")

def open_login():
    global login_win, entry_user, entry_pass, lbl_error
    login_win = tk.Toplevel(root)
    login_win.title("Admin Login")
    login_win.geometry("300x200")

    tk.Label(login_win, text="Utilisateur:").pack(pady=5)
    entry_user = tk.Entry(login_win)
    entry_user.pack()

    tk.Label(login_win, text="Mot de passe:").pack(pady=5)
    entry_pass = tk.Entry(login_win, show="*")
    entry_pass.pack()

    lbl_error = tk.Label(login_win, text="", fg="red")
    lbl_error.pack(pady=5)

    tk.Button(login_win, text="Valider", command=check_login).pack(pady=10)

def auto_start():
    time.sleep(5)
    try:
        root.destroy()
    except:
        pass
    subprocess.Popen(["pibooth"])

root = tk.Tk()
root.title("Démarrage")
root.geometry("800x480")
root.configure(bg="black")

label = tk.Label(root, text="Démarrage de Pibooth en cours...", font=("Arial", 24), fg="white", bg="black")
label.pack(expand=True)

# Bouton discret ⚙ en bas à droite
btn_admin = tk.Button(root, text="⚙", font=("Arial", 12), command=open_login, bg="black", fg="white", bd=0)
btn_admin.place(relx=0.98, rely=0.95, anchor="se")

# Thread pour auto lancer Pibooth après 5s
threading.Thread(target=auto_start, daemon=True).start()

root.mainloop()
