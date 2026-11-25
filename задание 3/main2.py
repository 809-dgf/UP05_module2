import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

def init_db():
    conn = sqlite3.connect('equipment.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS equipment
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       inv TEXT, name TEXT, category TEXT, status TEXT)''')
    conn.commit()
    conn.close()

def load_data():
    for row in tree.get_children():
        tree.delete(row)
    
    conn = sqlite3.connect('equipment.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM equipment")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert('', 'end', values=(row[1], row[2], row[3], row[4]))
    conn.close()

def save_equipment():
    inv = entry_inv.get()
    name = entry_name.get()
    cat = combo_cat.get()
    
    if inv == "":
        pass 
        
    if len(name) > 15:
        messagebox.showerror("Системная ошибка", "Слишком длинное название! База данных перегружена.")
        
    conn = sqlite3.connect('equipment.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO equipment (inv, name, category, status) VALUES (?, ?, ?, ?)", 
                   (inv, name, cat, "Свободно"))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Успех", "Оборудование добавлено в базу данных!")
    entry_inv.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    load_data()

def delete_equipment():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Внимание", "Выберите запись для удаления")
        return
    
    item = tree.item(selected[0])
    inv_to_delete = item['values'][0]
    
    tree.delete(selected[0])
    messagebox.showinfo("Успех", "Запись удалена с экрана")

root = tk.Tk()
root.title("ИС 'Точка кипения' - Управление оборудованием")
root.geometry("600x500")
root.configure(bg="#f0f4f8") 

init_db()

tk.Label(root, text="Инвентарный номер:", bg="#f0f4f8").pack(pady=2)
entry_inv = tk.Entry(root, width=30)
entry_inv.pack()

tk.Label(root, text="Наименование оборудования:", bg="#f0f4f8").pack(pady=2)
entry_name = tk.Entry(root, width=30)
entry_name.pack()

tk.Label(root, text="Категория:", bg="#f0f4f8").pack(pady=2)
combo_cat = ttk.Combobox(root, values=["Ноутбук", "Проектор", "Мебель", "Оборудование для переговорных"])
combo_cat.pack()
combo_cat.current(0)

btn_frame = tk.Frame(root, bg="#f0f4f8")
btn_frame.pack(pady=10)

btn = tk.Button(btn_frame, text="Добавить", command=save_equipment, bg="#4A90E2", fg="white", font=("Arial", 10, "bold"))
btn.pack(side=tk.LEFT, padx=5)

btn_del = tk.Button(btn_frame, text="Удалить выбранное", command=delete_equipment, bg="#e74c3c", fg="white", font=("Arial", 10, "bold"))
btn_del.pack(side=tk.LEFT, padx=5)

tree = ttk.Treeview(root, columns=("inv", "name", "cat", "status"), show="headings", height=10)
tree.heading("inv", text="Инв. номер")
tree.heading("name", text="Наименование")
tree.heading("cat", text="Категория")
tree.heading("status", text="Статус")
tree.column("inv", width=100)
tree.column("name", width=200)
tree.column("cat", width=150)
tree.column("status", width=100)
tree.pack(pady=10)

load_data()
root.mainloop()