import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, nm, sid, ag, grd):
        self.name = nm
        self.id = sid
        self.age = ag
        self.grade = grd

class SMSManager:
    def __init__(self):
        self.students = []

    def add(self, nm, sid, ag, grd):
        student = Student(nm, sid, ag, grd)
        self.students.append(student)
        messagebox.showinfo("Success", "Student added successfully.")

    def disp(self):
        if not self.students:
            messagebox.showinfo("No Students", "No student records found.")
        else:
            display_info = "Student Details:\n"
            for student in self.students:
                display_info += f"Name: {student.name}, ID: {student.id}, Age: {student.age}, Grade: {student.grade}\n"
            messagebox.showinfo("Student Records", display_info)

    def search(self, sid):
        for student in self.students:
            if student.id == sid:
                messagebox.showinfo("Student Found",
                                    f"Name: {student.name}, ID: {student.id}, Age: {student.age}, Grade: {student.grade}")
                return
        messagebox.showinfo("Student Not Found", f"No student found with ID: {sid}")

    def delete(self, sid):
        for student in self.students:
            if student.id == sid:
                self.students.remove(student)
                messagebox.showinfo("Success", "Student record deleted successfully.")
                return
        messagebox.showinfo("Student Not Found", f"No student found with ID: {sid}")

    def update(self, sid, nm, grd):
        for student in self.students:
            if student.id == sid:
                student.name = nm
                student.grade = grd
                messagebox.showinfo("Success", "Student record updated successfully.")
                return
        messagebox.showinfo("Student Not Found", f"No student found with ID: {sid}")

def add_w():
    def add():
        nm = name_entry.get()
        sid = id_entry.get()
        ag = age_entry.get()
        grd = grade_entry.get()
        mgr.add(nm, sid, ag, grd)
        add_w.destroy()

    add_w = tk.Toplevel(root)
    add_w.title("Add Student")
    tk.Label(add_w, text="Name:").grid(row=0, column=0)
    tk.Label(add_w, text="ID:").grid(row=1, column=0)
    tk.Label(add_w, text="Age:").grid(row=2, column=0)
    tk.Label(add_w, text="Grade:").grid(row=3, column=0)
    name_entry = tk.Entry(add_w)
    name_entry.grid(row=0, column=1)
    id_entry = tk.Entry(add_w)
    id_entry.grid(row=1, column=1)
    age_entry = tk.Entry(add_w)
    age_entry.grid(row=2, column=1)
    grade_entry = tk.Entry(add_w)
    grade_entry.grid(row=3, column=1)
    tk.Button(add_w, text="Add", command=add, bg="gray").grid(row=4, column=0, columnspan=2)

def disp():
    mgr.disp()

def search_w():
    def search():
        sid = id_entry.get()
        mgr.search(sid)

    search_w = tk.Toplevel(root)
    search_w.title("Search Student")
    tk.Label(search_w, text="ID:").grid(row=0, column=0)
    id_entry = tk.Entry(search_w)
    id_entry.grid(row=0, column=1)
    tk.Button(search_w, text="Search", command=search, bg="gray").grid(row=1, column=0, columnspan=2)

def delete_w():
    def delete():
        sid = id_entry.get()
        mgr.delete(sid)

    delete_w = tk.Toplevel(root)
    delete_w.title("Delete Student")
    tk.Label(delete_w, text="ID:").grid(row=0, column=0)
    id_entry = tk.Entry(delete_w)
    id_entry.grid(row=0, column=1)
    tk.Button(delete_w, text="Delete", command=delete, bg="gray").grid(row=1, column=0, columnspan=2)

def update_w():
    def update():
        sid = id_entry.get()
        nm = name_entry.get()
        grd = grade_entry.get()
        mgr.update(sid, nm, grd)

    update_w = tk.Toplevel(root)
    update_w.title("Update Student")
    tk.Label(update_w, text="ID:").grid(row=0, column=0)
    tk.Label(update_w, text="Name:").grid(row=1, column=0)
    tk.Label(update_w, text="Grade:").grid(row=2, column=0)
    id_entry = tk.Entry(update_w)
    id_entry.grid(row=0, column=1)
    name_entry = tk.Entry(update_w)
    name_entry.grid(row=1, column=1)
    grade_entry = tk.Entry(update_w)
    grade_entry.grid(row=2, column=1)
    tk.Button(update_w, text="Update", command=update, bg="gray").grid(row=3, column=0, columnspan=2)

def exit_p():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

mgr = SMSManager()

root = tk.Tk()
root.geometry("400x400")
root.title("Student Management System")

tk.Button(root, text="Accept Details", command=add_w, bg="gray").pack(pady=5)
tk.Button(root, text="Display Details", command=disp, bg="gray").pack(pady=5)
tk.Button(root, text="Search Details", command=search_w, bg="gray").pack(pady=5)
tk.Button(root, text="Delete Details", command=delete_w, bg="gray").pack(pady=5)
tk.Button(root, text="Update Details", command=update_w, bg="gray").pack(pady=5)
tk.Button(root, text="Exit", command=exit_p, bg="gray").pack(pady=5)

root.mainloop()
