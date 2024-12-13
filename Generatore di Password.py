# GENERATORE DI PASSWORD CASUALE
'''
Creare un Generatore di Password con TIPOLOGIE MULTIPLE
OBIETTIVO: Creare programma che permette all'utente di scgliere tipo di password e numero di password da generare.
SPECIFICHE
INPUT
- Numero di password da generare
- Lunghezza password con un minimo di 8 caratteri
- Il tipo di password:
• solo stringhe 
• alfanumerica
• password completa (lettere, numeri, caratteri speciali)
- Evitare ripetizioni di password (OPZIONALE)
--------------------------------------------------------------------------------------------------
FUNZIONI:
- Funzione principale -> Avvia codice
- Funzione Menu       -> Preferenze
- Funzione Verifica   -> Password ripetuta
- Funzione Generatore -> Genera Password

UTILIZZO:
- Variabili
- Condizioni
- Cicli           -> FOR - WHILE
- Libreria\Modulo -> RANDOM - STRING
'''
# 1. IMPORTARE:  Libreria\Modulo -> RANDOM - STRING

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
root.geometry("400x400") 

# VARIABILI PER INTERFACCIA
num_password_entry = tk.Entry(root, bg='white', fg='black', insertbackground='black', font=('LANE A', 10))
length_entry = tk.Entry(root, bg='white', fg='black', insertbackground='black', font=('LANE A', 10))
password_type_var = tk.IntVar(value=1)
avoid_repeats_var = tk.BooleanVar()
require_all_types_var = tk.BooleanVar()

# LAYOUT PER L'INTERFACCIA CON PADDING
tk.Label(root, text="NUMERO DI PASSWORD DA GENERARE:", bg='#ececec', fg='black', font=('LANE A', 14)).grid(row=0, column=0, pady=(20, 0), padx=(20, 20))
num_password_entry.grid(row=0, column=1, pady=(20, 0), padx=(20, 20))

tk.Label(root, text="LUNGHEZZA PASSWORD:", bg='#ececec', fg='black', font=('LANE A', 14)).grid(row=1, column=0, padx=(20, 20))
length_entry.grid(row=1, column=1, padx=(20, 20))

tk.Label(root, text="TIPO DI PASSWORD:", bg='#ececec', fg='black', font=('LANE A', 14)).grid(row=2, column=0, padx=(20, 20))

# BUTTONS
tk.Radiobutton(root, text="SOLO NUMERICI", variable=password_type_var, value=1, bg='#ececec', fg='black', font=('LANE A', 12)).grid(row=2, column=1, sticky='w', padx=(20, 20))
tk.Radiobutton(root, text="SOLO LETTERE", variable=password_type_var, value=2, bg='#ececec', fg='black', font=('LANE A', 12)).grid(row=3, column=1, sticky='w', padx=(20, 20))
tk.Radiobutton(root, text="ALFANUMERICA", variable=password_type_var, value=3, bg='#ececec', fg='black', font=('LANE A', 12)).grid(row=4, column=1, sticky='w', padx=(20, 20))
tk.Radiobutton(root, text="COMPLETA", variable=password_type_var, value=4, bg='#ececec', fg='black', font=('LANE A', 12)).grid(row=5, column=1, sticky='w', padx=(20, 20))

tk.Checkbutton(root, text="EVITARE CARATTERI RIPETUTI", variable=avoid_repeats_var, bg='#ececec', fg='black', font=('LANE A', 12)).grid(row=6, columnspan=2, sticky='w', padx=(20, 20))
tk.Checkbutton(root, text="INCLUDERE TUTTI I TIPI DI CARATTERE", variable=require_all_types_var, bg='#ececec', fg='black', font=('LANE A', 12)).grid(row=7, columnspan=2, sticky='w', padx=(20, 20))

tk.Button(root, text="GENERA PASSWORD", command=generate_multiple_passwords, bg='lightblue', fg='black', font=('LANE A', 14)).grid(row=8, columnspan=2, pady=(10, 0), padx=(20, 20))

result_label = tk.Label(root, bg='#ececec', fg='black', font=('LANE A', 20), justify='center')
result_label.grid(row=9, columnspan=2) 

root.mainloop()
