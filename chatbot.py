import tkinter as tk
import brain

# batting rule
def generate_response(command):
    command = command.lower()

    if command in ["close", "exit", "bye", "quit"]:
        root.after(2000, root.destroy)
        response = "Goodbye! Take care!"

    elif command.startswith("calculate"):
        response = brain.calculator(command)

    elif "random fact" in command:
        response = brain.random_fact()

    else:
        response = brain.askLLM(command)

    return response


# bowling rule
def send_message():
    user_msg = entry.get()
    chat_box.insert(tk.END, f"You: {user_msg}\n")
    entry.delete(0, tk.END)

    bot_reply = generate_response(user_msg)
    chat_box.insert(tk.END, f"Chip: {bot_reply}\n\n")
    chat_box.see(tk.END)


# stadium construction
root = tk.Tk()
root.title("Simple Chatbot")
root.geometry("500x500")

chat_box = tk.Text(root, wrap=tk.WORD)
entry = tk.Entry(root)
send = tk.Button(root, text="SEND", command=send_message)

chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
entry.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)
send.pack(side=tk.RIGHT, padx=10, pady=10)

# greeting message
chat_box.insert(tk.END, f"{brain.greet()}\n\n")

# starting the game
root.mainloop()

