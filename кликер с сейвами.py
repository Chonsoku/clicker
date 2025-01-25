import tkinter as tk
import pickle
import os

root = tk.Tk()
root.title("Кликер")

click_count = 0
click_count2 = 0

rainbow_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
rainbow_colors2 = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
current_color_index = 0
current_color_index2 = 0

def save_progress1():
    with open('clicker1_progress.pkl', 'wb') as f:
        pickle.dump(click_count, f)
        pickle.dump(rainbow_colors, f)

def load_progress1():
    global click_count, rainbow_colors, current_color_index
    if os.path.exists('clicker1_progress.pkl'):
        with open('clicker1_progress.pkl', 'rb') as f:
            click_count = pickle.load(f)
            rainbow_colors = pickle.load(f)
    else:
        click_count = 0

def save_progress2():
    with open('clicker2_progress.pkl', 'wb') as f:
        pickle.dump(click_count2, f)
        pickle.dump(rainbow_colors2, f)

def load_progress2():
    global click_count2, rainbow_colors2, current_color_index2
    if os.path.exists('clicker2_progress.pkl'):
        with open('clicker2_progress.pkl', 'rb') as f:
            click_count2 = pickle.load(f)
            rainbow_colors2 = pickle.load(f)
    else:
        click_count2 = 0

def button_click():
    global click_count, current_color_index
    click_count += 1
    count_label.config(text=f"Количество нажатий: {click_count}")
    save_progress1()

    click_button.config(bg=rainbow_colors[current_color_index])

    current_color_index = (current_color_index + 1) % len(rainbow_colors)

count_label = tk.Label(root, text="Количество нажатий: 0", font=('Courier', 24))
count_label.pack()

click_button = tk.Button(root, text="Нажми меня!", command=button_click, font=('Courier', 24), bg='red', fg='white')
click_button.pack()

def button_click2():
    global click_count2, current_color_index2
    click_count2 += 1
    count_label2.config(text=f"Количество нажатий: {click_count2}")
    save_progress2()

    click_button2.config(bg=rainbow_colors2[current_color_index2])

    current_color_index2 = (current_color_index2 + 1) % len(rainbow_colors2)

count_label2 = tk.Label(root, text="Количество нажатий: 0", font=('Courier', 24))
count_label2.pack()

click_button2 = tk.Button(root, text="Нажми меня!", command=button_click2, font=('Courier', 24), bg='red', fg='white')
click_button2.pack()

load_progress1()
load_progress2()

count_label.config(text=f"Количество нажатий: {click_count}")
count_label2.config(text=f"Количество нажатий: {click_count2}")

root.mainloop()