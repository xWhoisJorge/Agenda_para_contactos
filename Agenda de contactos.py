import tkinter as tk

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    contact_list.append((name, phone, email))
    clear_entries()
    update_listbox()

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

def update_listbox():
    listbox.delete(0, tk.END)
    for i, (name, phone, email) in enumerate(contact_list):
        listbox.insert(i, f"{name} - {phone} - {email}")

def delete_contact():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        del contact_list[index]
        update_listbox()

root = tk.Tk()
root.title("Contact Manager")
root.geometry("400x400")
root.config(bg="lightblue")

label_name = tk.Label(root, text="Name", bg="lightblue")
label_phone = tk.Label(root, text="Phone", bg="lightblue")
label_email = tk.Label(root, text="Email", bg="lightblue")
entry_name = tk.Entry(root, width=30)
entry_phone = tk.Entry(root, width=30)
entry_email = tk.Entry(root, width=30)
button_add = tk.Button(root, text="Add Contact", command=add_contact, bg="green", fg="white")
button_delete = tk.Button(root, text="Delete Contact", command=delete_contact, bg="red", fg="white")
listbox = tk.Listbox(root, height=10, width=60)

label_name.pack(pady=10)
entry_name.pack(pady=10)
label_phone.pack(pady=10)
entry_phone.pack(pady=10)
label_email.pack(pady=10)
entry_email.pack(pady=10)
button_add.pack(pady=10)
button_delete.pack(pady=10)
listbox.pack(pady=10)

contact_list = []

root.mainloop()
