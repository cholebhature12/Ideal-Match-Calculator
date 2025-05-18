import tkinter as tk
import os

def welcome_screen():
    welcome = tk.Tk()
    welcome.title("Welcome 💖")
    welcome.geometry("400x300")
    welcome.configure(bg="#ffe6e6")

    title = tk.Label(welcome, text="Welcome to Love Calculator!", font=("Arial", 16, "bold"), bg="#ffe6e6", fg="#ff4d6d")
    title.pack(pady=30)

    loading_text = tk.Label(welcome, text="Loading...", font=("Arial", 14), bg="#ffe6e6")
    loading_text.pack(pady=10)

    heart1 = tk.Label(welcome, text="💖", font=("Arial", 30), bg="#ffe6e6")
    heart1.pack()
    heart2 = tk.Label(welcome, text="💘", font=("Arial", 30), bg="#ffe6e6")
    heart2.pack()
    heart3 = tk.Label(welcome, text="❤", font=("Arial", 30), bg="#ffe6e6")
    heart3.pack()

    # Make hearts animate by moving slightly
    def animate_hearts():
        for heart in [heart1, heart2, heart3]:
            heart.place(x=150 + (5 if heart.winfo_x()%2==0 else -5), y=heart.winfo_y()+5)

    def close_welcome():
        welcome.destroy()

    welcome.after(500, animate_hearts)
    welcome.after(1500, animate_hearts)
    welcome.after(2500, animate_hearts)
    welcome.after(5000, close_welcome)  # After 5 seconds, close the welcome screen.

    welcome.mainloop()

welcome_screen()  # <<< Add this here FIRST

root = tk.Tk()
root.title("LOVE CALCULATOR")
root.geometry("400x300")
root.configure(bg="#ffe6e6")

answers = {}
question_counter = 1  # To number questions correctly across all windows

# ----------------------------------
def write_answers_to_file(username, user_vars):
    global question_counter
    with open(username + ".txt", "a", encoding="utf-8") as f:
        for ans in user_vars:
            f.write(f"Q{question_counter}: {ans}\n")
            question_counter += 1

# ----------------------------------
def open_window_template(username, title, questions, next_func):
    win = tk.Toplevel(root)
    win.title(title)
    win.configure(bg="#fff0f5")

    user_vars = []

    for index, (q, options) in enumerate(questions):
        tk.Label(win, text=f"{index+1}. {q}", bg="#fff0f5", font=("Arial", 12, "bold"), anchor="w").pack(pady=(10, 0), padx=20, anchor="w")
        var = tk.StringVar(value="None")
        user_vars.append(var)

        for opt in options:
            tk.Radiobutton(win, text=opt, variable=var, value=opt, bg="#fff0f5", font=("Arial", 11)).pack(anchor="w", padx=40)

    def save_and_next():
        answers[title] = [var.get() for var in user_vars]
        write_answers_to_file(username, answers[title])
        win.destroy()
        next_func(username)

    tk.Button(win, text="Next ➡", bg="#ff99c8", font=("Arial", 12), command=save_and_next).pack(pady=20)

# ----------------------------------
def open_window_1(username):
    questions = [
        ("What's your love language?", ["Words of Affirmation", "Acts of Service", "Receiving Gifts", "Quality Time"]),
        ("How do you show affection?", ["Surprise with gifts", "Do something helpful", "Say 'I love you' often", "Plan a date"]),
        ("How often do you want to talk or text during the day?", ["All day every day 😍", "A few check-ins", "Just at night", "Whenever something comes up"])
    ]
    open_window_template(username, "window1", questions, open_window_2)

# ----------------------------------
def open_window_2(username):
    questions = [
        ("What's more important to you?", ["Career success", "Family & relationships", "Freedom to travel", "Having fun and enjoying the moment"]),
        ("Where do you see yourself in 5 years?", ["Settled down with a family", "Traveling the world", "Building my dream job", "Living with my partner and pets"]),
        ("How do you handle conflict?", ["Talk it out immediately", "Need space first", "Get emotional", "Try to laugh it off"])
    ]
    open_window_template(username, "window2", questions, open_window_3)

# ----------------------------------
def open_window_3(username):
    questions = [
        ("Your ideal date night is…", ["Netflix and cuddles", "Amusement park", "Cooking together", "Stargazing"]),
        ("Pick a pet you'd love to have together:", ["dog", "cat", "bunny", "no pets, just us"]),
        ("Which movie genre do you love most?", ["romance", "comedy", "horror", "action"])
    ]
    open_window_template(username, "window3", questions, open_window_4)

# ----------------------------------
def open_window_4(username):
    questions = [
        ("What does love mean to you?", ["Being completely yourself with someone", "Growing together", "Loyalty and safety", "Passion and attraction"]),
        ("How do you feel about surprises?", ["LOVE them! 🎁", "They’re okay sometimes", "Depends on the person", "Hate them 😬"]),
        ("What’s your vibe in a relationship?", ["Soft and romantic 🧸", "Playful and teasing 😜", "Loyal and solid like a rock ⛰", "Deep and emotional 🌊"])
    ]
    open_window_template(username, "window4", questions, open_window_5)

# ----------------------------------
def open_window_5(username):
    questions = [
        ("What’s your morning style?", ["Rise and shine!", "Give me 10 more mins", "I’m a zombie until coffee", "Up early but quiet", "Depends on my mood"]),
        ("How do you recharge after a long day?", ["Alone time with music or a book 🎧📖", "Hanging out with friends 🥳", "Talking with my partner 💕", "Sleeping early 😴"]),
        ("How do you feel about chores?", ["I’ll do them if we do them together", "I like to keep things clean", "Meh... I’ll do it eventually", "I outsource whenever I can", "I’m super organized and on schedule"]),
    ]
    open_window_template(username, "window5", questions, open_final_screen)

# ----------------------------------
def open_final_screen(username):
    final = tk.Toplevel(root)
    final.title("🎊 Done!")
    final.configure(bg="#ffe6e6")

    tk.Label(final, text=f"Thanks for playing, {username}!", font=("Arial", 14, "bold"), bg="#ffe6e6").pack(pady=20)
    tk.Label(final, text="Stay tuned to calculate your love score 💕", font=("Arial", 12), bg="#ffe6e6").pack(pady=10)

    if not os.path.exists("participants.txt"):
        open("participants.txt", "w", encoding="utf-8").close()

    with open("participants.txt", "r", encoding="utf-8") as f:
        users = f.read().splitlines()

    users = [u for u in users if u != username]

    def compare_with(other_user):
        show_compatibility(username, other_user)

    for user in users:
        tk.Button(final, text=user, bg="#ffb3d9", font=("Arial", 11), command=lambda u=user: compare_with(u)).pack(pady=2)

# ----------------------------------
def show_compatibility(user1, user2):
    def read_answers(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            return None
        return [line.strip().split(": ")[1] for line in lines if line.startswith("Q")]

    answers1 = read_answers(user1 + ".txt")
    answers2 = read_answers(user2 + ".txt")

    if not answers1 or not answers2:
        win = tk.Toplevel(root)
        win.title("Oops!")
        win.configure(bg="#fff0f5")
        tk.Label(win, text=f"One of the users hasn’t completed the quiz yet.\nPlease make sure both {user1} and {user2} play first!", font=("Arial", 12), bg="#fff0f5", wraplength=300, justify="center").pack(padx=20, pady=30)
        return

    common = sum(a1 == a2 for a1, a2 in zip(answers1, answers2))
    total = min(len(answers1), len(answers2))
    score = int((common / total) * 100) if total > 0 else 0

    win = tk.Toplevel(root)
    win.title("💖 Compatibility Result")
    win.configure(bg="#fff0f5")
    msg = f"Your compatibility score with {user2} is: {score}%"
    tk.Label(win, text=msg, font=("Arial", 14, "bold"), bg="#fff0f5").pack(padx=20, pady=30)

# ----------------------------------
def savename():
    global question_counter
    question_counter = 1
    username = entry1.get().strip()
    if not username:
        result_label.config(text="Name cannot be empty!")
        return

    with open(username + ".txt", "w", encoding="utf-8") as f:
        f.write(f"Hello, {username}\n")

    if not os.path.exists("participants.txt"):
        open("participants.txt", "w", encoding="utf-8").close()

    if username not in open("participants.txt", "r", encoding="utf-8").read():
        with open("participants.txt", "a", encoding="utf-8") as f:
            f.write(username + "\n")

    open_window_1(username)

# UI Layout
tk.Label(root, text="Enter your Name:", bg="#ffe6e6", font=("Arial", 12)).pack(pady=5)
entry1 = tk.Entry(root, font=("Arial", 12))
entry1.pack(pady=5)

tk.Button(root, text="Start 💘", font=("Arial", 12, "bold"), bg="#ff99c8", command=savename).pack(pady=15)

result_label = tk.Label(root, text="", bg="#ffe6e6", font=("Arial", 14, "bold"), wraplength=300, justify="center")
result_label.pack(pady=10)

root.mainloop()
