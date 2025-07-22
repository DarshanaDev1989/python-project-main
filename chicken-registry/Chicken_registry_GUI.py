import csv
import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk


path = "chicken.csv"

def load():
    try:
        chicken = []
        with open(path, 'r', newline='') as file:
            reader = csv.reader(file)
            column_name = next(reader)
            for i in reader:
                chicken.append(i[0])
        return chicken
    except FileNotFoundError:
        print("File not found")
        return []
    except Exception as e:
        print("An error occurred:", e)
        return []

def append(name):
    try:
        with open(path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name])
            print("Chicken written to the file successfully!")
    except PermissionError:
        print("Permission denied when writing to the file.")
    except Exception as e:
        print("An error occurred:", e)

def view_chickens():
    chickens = load()
    if not chickens:
        messagebox.showinfo("Chickens", "No chickens found.")
        return
    info = "\n".join(chickens)
    messagebox.showinfo("All Chickens", info)

def add_chicken():
    name = simpledialog.askstring("Input", "Enter chicken name:")
    if name:
        append(name)
        messagebox.showinfo("Success", f"{name} added successfully!")

def update_chicken():
    chicken=load()
    name = simpledialog.askstring("Input", "Enter chicken name to be updated:")
    if name:
        index=chicken.index(name)
        up_name=simpledialog.askstring("Input", "Enter new chicken name to be updated:")
        chicken[index]=up_name
        try:
            with open(path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["name"])  
                for i in chicken:
                    writer.writerow([i])
        except Exception as e:
            print("An error occurred while updating:", e)
        messagebox.showinfo("Success", f"{up_name} updated successfully!")
    else:
         messagebox.showinfo("Not Found", f"'{name}' was not found in the list.")
def delete_chicken():
    chicken=load()
    name = simpledialog.askstring("Input", "Enter chicken name to be deleted:")
    if name in chicken:
        chicken.remove(name)
        try:
            with open(path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["name"])  
                for i in chicken:
                    writer.writerow([i])
        except Exception as e:
            print("An error occurred while updating:", e)
        messagebox.showinfo("Success", f"{name} deleted successfully!")
    else:
        messagebox.showinfo("Not Found", f"'{name}' was not found in the list.")

def main():
    win = tk.Tk()
    win.title("Chicken Registry App")
    win.geometry('400x200')
    win.resizable(False,False)
     # Load the image
    image = Image.open("chicken.jpeg")
    image = image.resize((150, 150))  # Resize the image to fit the label
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(win, image=photo)
    label.pack(side=tk.LEFT)
    btn_view = tk.Button(win, text="View Chicken Names", fg="blue", command=view_chickens)
    btn_view.pack(pady=10)

    btn_add = tk.Button(win, text="Add Chicken Name", fg="green", command=add_chicken)
    btn_add.pack(pady=10)

    btn_update = tk.Button(win, text="Update Chicken Name", fg="green", command=update_chicken)
    btn_update.pack(pady=10)

    btn_delete = tk.Button(win, text="Delete Chicken Name", fg="green", command=delete_chicken)
    btn_delete.pack(pady=10)

    win.mainloop()

main()
