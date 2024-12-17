import random
import string
import tkinter as tk
from tkinter import messagebox

# FUNZIONE PER GENERARE PASSWORD
def generate_password(length, password_type, avoid_repeats, require_all_types):
    if password_type == 1:
        characters = string.digits
    elif password_type == 2:
        characters = string.ascii_letters
    elif password_type == 3:
        characters = string.ascii_letters + string.digits
    elif password_type == 4:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = []
    while len(password) < length:
        char = random.choice(characters)
        if avoid_repeats and char in password:
            continue
        password.append(char)

    if require_all_types:
        if password_type == 3:
            if not (any(c.isalpha() for c in password) and any(c.isdigit() for c in password)):
                return generate_password(length, password_type, avoid_repeats, require_all_types)
        elif password_type == 4:
            if not (any(c.isalpha() for c in password) and any(c.isdigit() for c in password) and any(c in string.punctuation for c in password)):
                return generate_password(length, password_type, avoid_repeats, require_all_types)

    return ''.join(password)

# FUNZIONE PER GENERARE PASSWORD MULTIPLE
def generate_multiple_passwords():
    try:
        num_password = int(num_password_entry.get())
        length = int(length_entry.get())
        password_type = password_type_var.get()
        avoid_repeats = avoid_repeats_var.get()
        require_all_types = require_all_types_var.get()

        if length < 8:
            messagebox.showerror("Errore", "La lunghezza minima è 8 caratteri.")
            return
        
        passwords = []
        for _ in range(num_password):
            pwd = generate_password(length, password_type, avoid_repeats, require_all_types)
            passwords.append(pwd)

        result_label.config(text='\n'.join(f'Password {i + 1}: {pwd}' for i, pwd in enumerate(passwords)))
    except ValueError:
        messagebox.showerror("Errore", "Inserisci valori validi.")

# INTERFACCIA GRAFICA
root = tk.Tk()
root.title("SIMULATORE DI PASSWORD")
root.configure(bg='#ececec')

# PADDING FINESTRA
root.geometry("550x400") 

# VARIABILI PER INTERFACCIA
num_password_entry = tk.Entry(root, bg='white', fg='black', insertbackground='black', font=('JetBrainsMonoNL-Thin', 14))
length_entry = tk.Entry(root, bg='white', fg='black', insertbackground='black', font=('JetBrainsMonoNL-Thin', 14))
password_type_var = tk.IntVar(value=1)
avoid_repeats_var = tk.BooleanVar()
require_all_types_var = tk.BooleanVar()

# LAYOUT PER L'INTERFACCIA CON PADDING
tk.Label(root, text="Numero di Password da Generare:", bg='#ececec', fg='black', font=('JetBrainsMonoNL-Thin', 14)).grid(row=0, column=0, pady=(20, 0), padx=(20, 20))
num_password_entry.grid(row=0, column=1, pady=(20, 0), padx=(20, 20))

tk.Label(root, text="Lunghezza Password:", bg='#ececec', fg='black', font=('JetBrainsMonoNL-Thin', 14)).grid(row=1, column=0, padx=(20, 20))
length_entry.grid(row=1, column=1, padx=(20, 20))

tk.Label(root, text="Tipo di Password:", bg='#ececec', fg='black', font=('JetBrainsMonoNL-Thin', 14)).grid(row=2, column=0, padx=(20, 20))

# BUTTONS
tk.Radiobutton(root, text="Solo Numerici", variable=password_type_var, value=1, bg='#ececec', fg='black', font=('JetBrainsMonoNL-Thin', 12)).grid(row=2, column=1, sticky='w', padx=(20, 20))
tk.Radiobutton(root, text="Solo Lettere", variable=password_type_var, value=2, bg='#ececec', fg='black', font=('JetBrainsMonoNL-Thin', 12)).grid(row=3, column=1, sticky='w', padx=(20, 20))
tk.Radiobutton(root, text="Alfanumerica", variable=password_type_var, value=3, bg='#ececec', fg='black', font=('JetBrainsMonoNL-Thin', 12)).grid(row=4, column=1, sticky='w', padx=(20, 20))
tk.Radiobutton(root, text="Completa", variable=password_type_var, value=4, bg='#ececec', fg='black', font=('JetBrainsMonoNL-Thin', 12)).grid(row=5, column=1, sticky='w', padx=(20, 20))

tk.Checkbutton(root, text="Evitare Caratteri Ripetuti", variable=avoid_repeats_var, bg='#ececec', fg='black', font=('JetBrainsMonoNL-Thin', 12)).grid(row=6, columnspan=2, sticky='w', padx=(20, 20))
tk.Checkbutton(root, text="Includere tutti i tipi di carattere", variable=require_all_types_var, bg='#ececec', fg='black', font=('JetBrainsMonoNL-Thin', 12)).grid(row=7, columnspan=2, sticky='w', padx=(20, 20))

tk.Button(root, text="Genera Password", command=generate_multiple_passwords, bg='lightblue', fg='black', font=('JetBrainsMonoNL-Thin', 12)).grid(row=8, columnspan=2, pady=(10, 0), padx=(20, 20))

result_label = tk.Label(root, bg='#ececec', fg='black', font=('JetBrainsMonoNL-Thin', 14), justify='center')
result_label.grid(row=9, columnspan=2) 

root.mainloop()
