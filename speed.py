import tkinter as tk
import random
import time

# Create a list of sample text for typing test
sample_text = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a high-level programming language.",
    "Practice makes perfect.",
    "Keep calm and code on.",
    "Hello, World!",
    "Coding is fun!",
]

# Function to start the typing test
def start_typing_test():
    global start_time
    start_time = time.time()
    text_to_type.set(random.choice(sample_text))
    entry.delete(0, tk.END)
    entry.config(state=tk.NORMAL)
    entry.focus()

# Function to check typing accuracy and speed
def check_typing():
    typed_text = entry.get()
    original_text = text_to_type.get()
    correct_chars = sum(1 for a, b in zip(typed_text, original_text) if a == b)
    total_chars = max(len(typed_text), len(original_text))
    accuracy = (correct_chars / total_chars) * 100
    elapsed_time = time.time() - start_time
    words_per_minute = (len(typed_text) / 5) / (elapsed_time / 60)

    result_text = f"Accuracy: {accuracy:.2f}%\nSpeed: {words_per_minute:.2f} WPM"
    result_label.config(text=result_text)
    entry.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Speed Typing Test")

# Create text label for typing
text_to_type = tk.StringVar()
text_label = tk.Label(root, textvariable=text_to_type, font=("Helvetica", 16))
text_label.pack(pady=20)

# Create entry field for typing
entry = tk.Entry(root, font=("Helvetica", 16), state=tk.DISABLED)
entry.pack()

# Create start button
start_button = tk.Button(root, text="Start Typing Test", command=start_typing_test, font=("Helvetica", 12))
start_button.pack(pady=10)

# Create check button
check_button = tk.Button(root, text="Check Typing", command=check_typing, font=("Helvetica", 12))
check_button.pack(pady=10)

# Create result label
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

# Run the GUI event loop
root.mainloop()
