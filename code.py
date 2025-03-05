import tkinter as tk
from tkinter import messagebox

class EbookManagement:
    def __init__(self, master):
        self.master = master
        self.master.title("E-Books' Digital Management System")
        self.master.geometry("400x400")
        self.master.config(bg='#E19898')

        self.books = []
        self.lend_list = []

        # Labels
        self.login_label = tk.Label(self.master, text="E-Books' Digital Management System", font=("Helvetica", 16), bg='#AC7088', fg='white')
        self.login_label.pack()
        self.username_label = tk.Label(self.master, text="Username", font=("Helvetica", 12), bg='#E19898', fg='white')
        self.username_label.pack()
        self.username_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.username_entry.pack()
        self.password_label = tk.Label(self.master, text="Password", font=("Helvetica", 12), bg='#E19898', fg='white')
        self.password_label.pack()
        self.password_entry = tk.Entry(self.master, font=("Helvetica", 12), show="*")
        self.password_entry.pack()

        # Login
        self.login_button = tk.Button(self.master, text="Login", command=self.login, font=("Helvetica", 12))
        self.login_button.pack()

        # Register
        self.register_button = tk.Button(self.master, text="Register", command=self.register, font=("Helvetica", 12))
        self.register_button.pack()

        self.username = ""
        self.password = ""
        self.managers = []

    def login(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        for manager in self.managers:
            if self.username == manager[0] and self.password == manager[1]:
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
                self.login_label.destroy()
                self.username_label.destroy()
                self.username_entry.destroy()
                self.password_label.destroy()
                self.password_entry.destroy()
                self.login_button.destroy()
                self.register_button.destroy()
                self.ebook_management_screen()
                return
        messagebox.showerror("Error", "Invalid username or password")

    def register(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.managers.append([self.username, self.password])
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def ebook_management_screen(self):
        self.add_book_label = tk.Label(self.master, text="Add E-book", font=("Helvetica", 16), bg='#E19898', fg='white')
        self.add_book_label.pack()
        self.add_book_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.add_book_entry.pack()
        self.add_book_button = tk.Button(self.master, text="Add E-book", command=self.add_book, font=("Helvetica", 12))
        self.add_book_button.pack()
        self.remove_book_label = tk.Label(self.master, text="Remove E-book", font=("Helvetica", 16), bg='#E19898', fg='white')
        self.remove_book_label.pack()
        self.remove_book_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.remove_book_entry.pack()
        self.remove_book_button = tk.Button(self.master, text="Remove E-book", command=self.remove_book, font=("Helvetica", 12))
        self.remove_book_button.pack()
        self.issue_book_label = tk.Label(self.master, text="Issue E-book", font=("Helvetica", 16), bg='#E19898', fg='white')
        self.issue_book_label.pack()
        self.issue_book_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.issue_book_entry.pack()
        self.issue_book_button = tk.Button(self.master, text="Issue E-book", command=self.issue_book, font=("Helvetica", 12))
        self.issue_book_button.pack()
        self.view_books_button = tk.Button(self.master, text="View E-books", command=self.view_books, font=("Helvetica", 12))
        self.view_books_button.pack()
        self.view_issued_books_button = tk.Button(self.master, text="View Issued E-books", command=self.view_issued_books, font=("Helvetica", 12))
        self.view_issued_books_button.pack()

    def add_book(self):
        ebook = self.add_book_entry.get()
        self.books.append(ebook)
        messagebox.showinfo("Success", "E-book added successfully")
        self.add_book_entry.delete(0, tk.END)

    def remove_book(self):
        ebook = self.remove_book_entry.get()
        if ebook in self.books:
            self.books.remove(ebook)
            messagebox.showinfo("Success", "E-book removed successfully")
        else:
            messagebox.showerror("Error", "E-book not found")
        self.remove_book_entry.delete(0, tk.END)

    def issue_book(self):
        ebook = self.issue_book_entry.get()
        if ebook in self.books:
            self.lend_list.append(ebook)
            self.books.remove(ebook)
            messagebox.showinfo("Success", "E-book issued successfully")
        else:
            messagebox.showerror("Error", "E-book not found")
        self.issue_book_entry.delete(0, tk.END)

    def view_books(self):
        message = "\n".join(self.books)
        messagebox.showinfo("E-books", message)

    def view_issued_books(self):
        message = "\n".join(self.lend_list)
        messagebox.showinfo("Issued E-books", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = EbookManagement(root)
    root.mainloop()
