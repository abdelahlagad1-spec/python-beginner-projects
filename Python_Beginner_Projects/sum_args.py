# # def sum_all(*args):
# #     return sum(args)

# # numbers = [1, 2, 3, 4, 5]
# # print(f"Sum of {numbers} = {sum_all(*numbers)}")
# # programming برنامج ضخم ذات واجه جامده جدا 
# import ttkbootstrap as ttk
# from ttkbootstrap.constants import *

# app = ttk.Window(themename="darkly")
# app.title("Smart App 🔥")
# app.geometry("400x400")

# title = ttk.Label(app, text="Smart App", font=("Arial", 18))
# title.pack(pady=20)

# ttk.Button(app, text="To Do List", bootstyle=SUCCESS).pack(pady=10)
# ttk.Button(app, text="Calculator", bootstyle=INFO).pack(pady=10)
# ttk.Button(app, text="Notes", bootstyle=WARNING).pack(pady=10)

# app.mainloop()
# # البدء في البرنامج
import customtkinter as ctk
import random
import json
import os
import sqlite3
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("900x600")
app.title("Ultimate App 💀🔥")

# ================= DATABASE =================
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")
conn.commit()

# ================= FRAMES =================
login_frame = ctk.CTkFrame(app)
main_frame = ctk.CTkFrame(app)

# ================= LOGIN =================
def show_login():
    main_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)

def show_main():
    login_frame.pack_forget()
    main_frame.pack(fill="both", expand=True)

def login():
    user = username_entry.get()
    pwd = password_entry.get()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (user, pwd))
    result = cursor.fetchone()

    if result:
        show_main()
    else:
        login_status.configure(text="Wrong login", text_color="red")

def signup():
    user = username_entry.get()
    pwd = password_entry.get()

    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user, pwd))
    conn.commit()
    login_status.configure(text="Account created!", text_color="green")

# UI LOGIN
ctk.CTkLabel(login_frame, text="Login System", font=("Arial", 24)).pack(pady=20)
username_entry = ctk.CTkEntry(login_frame, placeholder_text="Username")
username_entry.pack(pady=10)
password_entry = ctk.CTkEntry(login_frame, placeholder_text="Password", show="*")
password_entry.pack(pady=10)

ctk.CTkButton(login_frame, text="Login", command=login).pack(pady=5)
ctk.CTkButton(login_frame, text="Sign Up", command=signup).pack(pady=5)

login_status = ctk.CTkLabel(login_frame, text="")
login_status.pack()

# ================= MAIN UI =================
sidebar = ctk.CTkFrame(main_frame, width=200)
sidebar.pack(side="left", fill="y")

content = ctk.CTkFrame(main_frame)
content.pack(side="right", expand=True, fill="both")

def clear():
    for w in content.winfo_children():
        w.destroy()

# ================= DASHBOARD =================
def dashboard():
    clear()
    ctk.CTkLabel(content, text="🔥 Dashboard", font=("Arial", 22)).pack(pady=20)
    ctk.CTkLabel(content, text=f"Time: {datetime.now()}").pack()

# ================= TODO =================
tasks = []

def todo():
    clear()
    ctk.CTkLabel(content, text="📝 ToDo", font=("Arial", 20)).pack()

    entry = ctk.CTkEntry(content)
    entry.pack(pady=5)

    box = ctk.CTkTextbox(content, height=250)
    box.pack()

    def add():
        t = entry.get()
        if t:
            tasks.append(t)
            box.insert("end", f"- {t}\n")
            entry.delete(0, "end")

    def save():
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)

    ctk.CTkButton(content, text="Add", command=add).pack(pady=5)
    ctk.CTkButton(content, text="Save", command=save).pack()

# ================= CALCULATOR =================
def calc():
    clear()
    ctk.CTkLabel(content, text="🧮 Calculator", font=("Arial", 20)).pack()

    entry = ctk.CTkEntry(content)
    entry.pack()

    def run():
        try:
            entry.insert(0, eval(entry.get()))
        except:
            entry.delete(0, "end")
            entry.insert(0, "Error")

    ctk.CTkButton(content, text="=", command=run).pack()

# ================= GAME =================
def game():
    clear()
    number = random.randint(1, 10)

    ctk.CTkLabel(content, text="🎮 Guess Game", font=("Arial", 20)).pack()

    entry = ctk.CTkEntry(content)
    entry.pack()

    label = ctk.CTkLabel(content, text="")
    label.pack()

    def check():
        try:
            if int(entry.get()) == number:
                label.configure(text="🔥 Win")
            else:
                label.configure(text="❌ Wrong")
        except:
            label.configure(text="Invalid")

    ctk.CTkButton(content, text="Check", command=check).pack()

# ================= NOTES =================
def notes():
    clear()
    ctk.CTkLabel(content, text="📒 Notes", font=("Arial", 20)).pack()

    text = ctk.CTkTextbox(content, height=300)
    text.pack()

    def save():
        with open("notes.json", "w") as f:
            json.dump({"notes": text.get("1.0", "end")}, f)

    ctk.CTkButton(content, text="Save", command=save).pack()

# ================= PASSWORD =================
def password():
    clear()
    ctk.CTkLabel(content, text="🔑 Password", font=("Arial", 20)).pack()

    entry = ctk.CTkEntry(content)
    entry.pack()

    def gen():
        chars = "abc123!@#XYZ"
        pwd = "".join(random.choice(chars) for _ in range(10))
        entry.delete(0, "end")
        entry.insert(0, pwd)

    ctk.CTkButton(content, text="Generate", command=gen).pack()

# ================= SYSTEM =================
def system():
    clear()
    ctk.CTkLabel(content, text="💻 System", font=("Arial", 20)).pack()

    ctk.CTkLabel(content, text=os.name).pack()
    ctk.CTkLabel(content, text=os.getcwd()).pack()

# ================= MODE =================
def mode():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")

def ai_chat():
    clear()

    ctk.CTkLabel(content, text="🤖 AI Chat", font=("Arial", 20)).pack()

    chat_box = ctk.CTkTextbox(content, height=300)
    chat_box.pack(pady=10)

    entry = ctk.CTkEntry(content)
    entry.pack()

    def reply(msg):
        msg = msg.lower()

        if "hello" in msg:
            return "Hi 👋"
        elif "how are you" in msg:
            return "I'm fine 😎"
        elif "name" in msg:
            return "I'm your AI 🤖"
        elif "bye" in msg:
            return "Goodbye 👋"
        else:
            return "I don't understand 🤔"

    def send():
        user_msg = entry.get()
        chat_box.insert("end", f"You: {user_msg}\n")

        bot = reply(user_msg)
        chat_box.insert("end", f"AI: {bot}\n\n")

        entry.delete(0, "end")

    ctk.CTkButton(content, text="Send", command=send).pack(pady=5)

score = 0

def game():
    global score
    clear()

    number = random.randint(1, 10)

    label = ctk.CTkLabel(content, text=f"Score: {score}")
    label.pack()

    entry = ctk.CTkEntry(content)
    entry.pack()

    result = ctk.CTkLabel(content, text="")
    result.pack()

    def check():
        global score
        try:
            if int(entry.get()) == number:
                score += 1
                result.configure(text="🔥 Correct")
            else:
                result.configure(text="❌ Wrong")

            label.configure(text=f"Score: {score}")
        except:
            result.configure(text="Invalid")

    ctk.CTkButton(content, text="Check", command=check).pack()
# ================= SIDEBAR =================
ctk.CTkButton(sidebar, text="Dashboard", command=dashboard).pack(pady=5)
ctk.CTkButton(sidebar, text="ToDo", command=todo).pack(pady=5)
ctk.CTkButton(sidebar, text="Calculator", command=calc).pack(pady=5)
ctk.CTkButton(sidebar, text="Game", command=game).pack(pady=5)
ctk.CTkButton(sidebar, text="Notes", command=notes).pack(pady=5)
ctk.CTkButton(sidebar, text="Password", command=password).pack(pady=5)
ctk.CTkButton(sidebar, text="System", command=system).pack(pady=5)
ctk.CTkButton(sidebar, text="Mode", command=mode).pack(pady=5)
ctk.CTkButton(sidebar, text="AI Chat", command=ai_chat).pack(pady=5)

ctk.CTkButton(sidebar, text="Logout", command=show_login).pack(pady=20)

show_login()
app.mainloop()