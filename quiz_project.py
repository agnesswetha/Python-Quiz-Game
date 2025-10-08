# -------------------------------------------------------------
# 🎓 Academic Mini Project - "Python Programming Quiz Game"
# -------------------------------------------------------------
# 📘 Project Title   : Python Programming Quiz Game
# 🧑‍💻 Developed By   : A. Agnes Swetha & S. Nivika
# 🏫 Academic Year   : 1st Year, 2nd Semester
# 🗓️ Duration        : March 2023 - April 2023
# 💻 IDE Used        : Spyder (Python 3)
# 🧠 Language Used   : Python (Tkinter GUI)
# -------------------------------------------------------------
# 📄 Description:
# This project is a GUI-based Python Quiz Game designed to test
# users’ knowledge of Python programming concepts. It presents
# 10 multiple-choice questions, tracks the user’s score, and
# displays the final result with an interactive and colorful
# interface.
#
# 🧩 Key Features:
#  - Graphical interface using Tkinter
#  - Next / Previous / Exit navigation buttons
#  - Tracks selected answers for review
#  - Attractive color scheme and modern layout
#  - Final "Thank You" message and exit confirmation
#
# 🏁 Purpose:
# Created as an academic mini project to strengthen Python and
# GUI development skills, while building a fun and educational
# quiz application.
# -------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox

# ------------------------------
# QUIZ DATA (Python Related)
# ------------------------------
questions = [
    {"question": "What is the correct file extension for Python files?",
     "options": [".pyth", ".pt", ".py", ".pyt"], "answer": ".py"},
    {"question": "Which keyword is used to create a function in Python?",
     "options": ["function", "def", "create", "fun"], "answer": "def"},
    {"question": "Which of the following is a mutable data type in Python?",
     "options": ["Tuple", "List", "String", "Integer"], "answer": "List"},
    {"question": "How do you start a comment in Python?",
     "options": ["//", "/*", "#", "<!--"], "answer": "#"},
    {"question": "Which of these functions is used to get user input in Python 3?",
     "options": ["get()", "raw_input()", "input()", "scan()"], "answer": "input()"},
    {"question": "What is the output of len('Hello World')?",
     "options": ["10", "11", "12", "None"], "answer": "11"},
    {"question": "What is the correct way to create a dictionary in Python?",
     "options": ["{key: value}", "(key, value)", "[key = value]", "dict[key] = value"], "answer": "{key: value}"},
    {"question": "Which of the following is used to define a block of code in Python?",
     "options": ["Braces {}", "Indentation", "Parentheses ()", "Quotation marks"], "answer": "Indentation"},
    {"question": "What is the output of print(2 ** 3)?",
     "options": ["6", "8", "9", "5"], "answer": "8"},
    {"question": "Which library in Python is used for data analysis?",
     "options": ["numpy", "math", "pandas", "tkinter"], "answer": "pandas"}
]

# ------------------------------
# QUIZ LOGIC
# ------------------------------
current_question = 0
score = 0
user_answers = [None] * len(questions)

# ------------------------------
# FUNCTIONS
# ------------------------------
def load_question():
    """Loads the current question and its options into the GUI."""
    question_label.config(
        text=f"Q{current_question + 1}: {questions[current_question]['question']}")
    for i, option in enumerate(questions[current_question]['options']):
        radio_buttons[i].config(text=option, value=option)
    var.set(user_answers[current_question] if user_answers[current_question] else None)


def next_question():
    """Moves to the next question after saving the current answer."""
    global current_question

    selected_option = var.get()
    if not selected_option:
        messagebox.showwarning("⚠️ Warning", "Please select an option before proceeding.")
        return

    user_answers[current_question] = selected_option

    if current_question < len(questions) - 1:
        current_question += 1
        load_question()
    else:
        calculate_score()


def prev_question():
    """Moves back to the previous question."""
    global current_question
    if current_question > 0:
        current_question -= 1
        load_question()


def calculate_score():
    """Calculates and displays the user's final score and thank you message."""
    global score
    score = sum(1 for i, ans in enumerate(user_answers)
                if ans == questions[i]["answer"])

    messagebox.showinfo("Quiz Completed 🎉",
                        f"✅ You scored {score}/{len(questions)}!\n\nThank you for playing our Python Quiz Game 💙")
    thank_you_screen()


def exit_quiz():
    """Shows warning before exiting the quiz."""
    response = messagebox.askyesno("Exit Quiz ⚠️",
                                   "If you exit now, your score and progress will be lost.\nDo you still want to quit?")
    if response:
        messagebox.showinfo("Restart Required", "You exited the quiz! Restart to play again 🎯")
        root.destroy()


def thank_you_screen():
    """Displays a thank you message after completing the quiz."""
    for widget in root.winfo_children():
        widget.destroy()

    root.config(bg="#1E1E2F")

    thank_label = tk.Label(root, text="🎉 THANK YOU 🎉",
                           font=("Helvetica", 28, "bold"),
                           fg="#FEE715", bg="#1E1E2F")
    thank_label.pack(pady=40)

    dev_label = tk.Label(root, text="Developed by: A. Agnes Swetha & S. Nivika",
                         font=("Arial", 16), fg="#F5F5F5", bg="#1E1E2F")
    dev_label.pack(pady=10)

    msg_label = tk.Label(root, text="We hope you enjoyed our Python Quiz Game 💫",
                         font=("Arial", 14), fg="#F5F5F5", bg="#1E1E2F")
    msg_label.pack(pady=30)

    exit_btn = tk.Button(root, text="Exit Game 🚪", command=root.destroy,
                         font=("Arial", 14, "bold"), bg="#FEE715", fg="#1E1E2F", width=15)
    exit_btn.pack(pady=20)

# ------------------------------
# GUI SETUP
# ------------------------------
root = tk.Tk()
root.title("🐍 Python Programming Quiz Game 🧠")
root.geometry("800x600")
root.config(bg="#222831")

# Heading
title_label = tk.Label(root, text="🐍 Welcome to Python Quiz 🧠",
                       font=("Helvetica", 24, "bold"),
                       fg="#FFD369", bg="#222831")
title_label.pack(pady=25)

# Question
question_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"),
                          wraplength=700, justify="left", bg="#222831", fg="#EEEEEE")
question_label.pack(pady=20)

# Options
var = tk.StringVar()
radio_buttons = []
for i in range(4):
    rb = tk.Radiobutton(root, text="", variable=var, value="",
                        font=("Arial", 14), bg="#393E46",
                        fg="#FFD369", selectcolor="#00ADB5", anchor="w")
    rb.pack(fill="x", padx=100, pady=5)
    radio_buttons.append(rb)

# Navigation Buttons
frame = tk.Frame(root, bg="#222831")
frame.pack(pady=30)

prev_button = tk.Button(frame, text="⬅️ Previous", command=prev_question,
                        font=("Arial", 12, "bold"), bg="#00ADB5", fg="white", width=12)
prev_button.grid(row=0, column=0, padx=10)

next_button = tk.Button(frame, text="Next ➡️", command=next_question,
                        font=("Arial", 12, "bold"), bg="#00ADB5", fg="white", width=12)
next_button.grid(row=0, column=1, padx=10)

exit_button = tk.Button(frame, text="Exit 🚪", command=exit_quiz,
                        font=("Arial", 12, "bold"), bg="#FF5722", fg="white", width=12)
exit_button.grid(row=0, column=2, padx=10)

# Start quiz
load_question()

root.mainloop()
