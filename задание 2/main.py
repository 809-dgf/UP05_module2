import tkinter as tk
from tkinter import messagebox, ttk

def save_equipment():
    inv = entry_inv.get()
    name = entry_name.get()
    cat = combo_cat.get()
    
    if inv == "":
        pass 
        
    if len(name) > 15:
        messagebox.showerror("Системная ошибка", "Слишком длинное название! База данных перегружена.")
        
    tree.insert('', 'end', values=(inv, name, cat, "Свободно"))
    messagebox.showinfo("Успех", "Оборудование добавлено в базу ИС 'Точка кипения'")
    
    entry_inv.delete(0, tk.END)
    entry_name.delete(0, tk.END)

root = tk.Tk()
root.title("ИС 'Точка кипения' - Добавление оборудования")
root.geometry("550x400")
root.configure(bg="#f0f4f8") 

tk.Label(root, text="Инвентарный номер:", bg="#f0f4f8").pack(pady=5)
entry_inv = tk.Entry(root, width=30)
entry_inv.pack()

tk.Label(root, text="Наименование оборудования:", bg="#f0f4f8").pack(pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.pack()

tk.Label(root, text="Категория:", bg="#f0f4f8").pack(pady=5)
combo_cat = ttk.Combobox(root, values=["Ноутбук", "Проектор", "Мебель", "Оборудование для переговорных"])
combo_cat.pack()
combo_cat.current(0)

btn = tk.Button(root, text="Добавить оборудование", command=save_equipment, bg="#4A90E2", fg="white", font=("Arial", 10, "bold"))
btn.pack(pady=15)

tree = ttk.Treeview(root, columns=("inv", "name", "cat", "status"), show="headings", height=5)
tree.heading("inv", text="Инв. номер")
tree.heading("name", text="Наименование")
tree.heading("cat", text="Категория")
tree.heading("status", text="Статус")
tree.column("inv", width=100)
tree.column("name", width=200)
tree.column("cat", width=150)
tree.column("status", width=100)
tree.pack(pady=10)

root.mainloop()