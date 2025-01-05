import time
import tkinter as tk
import pygame

is_running = True

def prefilled_text(event):
    if user_input.get("1.0",tk.END).strip() == "Type Here...":
        user_input.delete("1.0",tk.END)

def check_alarm():
    global is_running
    if is_running:
        pygame.mixer.init()
        pygame.mixer.music.load("Alarmsound.mp3")

        local_time = time.localtime()
        formated_time = time.strftime('%H:%M:%S',local_time)

        if user_input.get("1.0",tk.END).strip() == formated_time:
            user_input.delete("1.0",tk.END)
            user_input.insert("1.0","WAKE UP!!")
            pygame.mixer.music.play()
            sound_play()
        else:
            root.after(1000,check_alarm)
    else:
        return

def sound_play():
    if pygame.mixer.music.get_busy():
        root.after(1000,sound_play)
    else:
        label_0.config(text="")

def set_alarm():
    global is_running
    if is_running:
        check_alarm()
        label_0.config(text="Alarm set successfully!")
        root.after(3000,clear_message) 

def reset():
    global is_running
    is_running = False
    user_input.delete("1.0",tk.END)
    label_0.config(text="Alarm reset successful.")
    root.after(3000,clear_message)

def clear_message():
    label_0.config(text="")

root = tk.Tk()
root.title("Alarm Clock")
root.geometry("330x450")
root.config(bg="#3D3D3D")

user_input = tk.Text(root,font=("Arial",35),width=10,height=1,bg="#F5ECD5",fg="Black",border=10)
user_input.pack(pady=20)

user_input.bind("<FocusIn>",prefilled_text)
user_input.insert("1.0","Type Here...")

guide = tk.Label(text="Example Input: 20:10:50 , 17:40:00")
guide.pack()

button_ac = tk.Button(text="Set Alarm",font=("Bahnschrift SemiBold",25),height=1,width=10,
                      bg="#578E7E",fg="#F5ECD5",command=set_alarm,border=5,relief="raised")
button_ac.pack(pady=10)

button_reset = tk.Button(text="Reset",font=("Bahnschrift SemiBold",25),height=1,width=6,
                      bg="#578E7E",fg="#F5ECD5",command=reset,border=5,relief="raised")
button_reset.pack()

label_0 = tk.Label(text="")
label_0.pack(pady=20)

root.mainloop()