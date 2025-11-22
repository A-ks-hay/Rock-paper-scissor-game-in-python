import tkinter as tk
import random

def play(user_choice):
    item_list = ["Rock", "Paper", "Scissor"]
    comp_choice = random.choice(item_list)

    result_text = f"Your Choice: {user_choice}\nComputer Choice: {comp_choice}\n\n"

    if user_choice == comp_choice:
        result_text += "Result: It's a Tie!"
    elif user_choice == "Rock":
        if comp_choice == "Paper":
            result_text += "Result: Paper covers Rock → Computer Wins!"
        else:
            result_text += "Result: Rock smashes Scissor → You Win!"
    elif user_choice == "Paper":
        if comp_choice == "Scissor":
            result_text += "Result: Scissor cuts Paper → Computer Wins!"
        else:
            result_text += "Result: Paper covers Rock → You Win!"
    elif user_choice == "Scissor":
        if comp_choice == "Rock":
            result_text += "Result: Rock smashes Scissor → Computer Wins!"
        else:
            result_text += "Result: Scissor cuts Paper → You Win!"

    result_label.config(text=result_text)



# GUI Setup

root = tk.Tk()
root.title("Rock Paper Scissor Game")
root.geometry("400x400")
root.config(bg="#f3f3f3")

title = tk.Label(root, text="Rock • Paper • Scissor", font=("Arial", 20, "bold"), bg="#c11616")
title.pack(pady=20)

btn_frame = tk.Frame(root, bg="#cd5151")
btn_frame.pack(pady=20)

rock_btn = tk.Button(btn_frame, text="Rock", font=("Arial", 14), width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(btn_frame, text="Paper", font=("Arial", 14), width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissor_btn = tk.Button(btn_frame, text="Scissor", font=("Arial", 14), width=10, command=lambda: play("Scissor"))
scissor_btn.grid(row=0, column=2, padx=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f3f3f3", justify="left")
result_label.pack(pady=20)

root.mainloop()
