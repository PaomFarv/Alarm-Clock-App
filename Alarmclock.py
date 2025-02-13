import customtkinter as ctk
import datetime,pygame

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

alarm_time = None

def check_alarm():
   
    global alarm_time
    if not alarm_time:
        return  

    local_time = datetime.datetime.now()
    current_time = local_time.strftime("%H:%M:%S")
    sound = "Alarmsound.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(sound)
    if current_time == alarm_time:
        time_label.configure(text="Time UP!", font=("Bahnschrift SemiBold", 70))
        feedback_label.configure(text="Alarm ringing!", font=("Arial", 15, "bold"))
        pygame.mixer.music.play()
        return 

    app.after(1000, check_alarm) 

def set_alarm():
    
    global alarm_time
    alarm_time = f"{selected_hours.get()}:{selected_mins.get()}:{selected_secs.get()}"

    if alarm_time != "00:00:00":
        feedback_label.configure(text="Alarm set successfully!")
        app.after(3000, popup_hide)
        check_alarm() 

def popup_hide():
    feedback_label.configure(text="")

def show_in_display():

    global alarm_time
    alarm_time = f"{selected_hours.get()}:{selected_mins.get()}:{selected_secs.get()}"
    time_label.configure(text=alarm_time)

app = ctk.CTk()
app.title("Alarm Clock")
app.geometry("390x500")
app.iconbitmap("ac.ico")

title_frame = ctk.CTkFrame(master=app, fg_color="transparent")
title_frame.pack(pady=10)

app_title1 = ctk.CTkLabel(master=title_frame, text="Alarm", font=("Segoe UI Black", 50), text_color="#3CB47E")
app_title1.pack(side="left", padx=5)

app_title2 = ctk.CTkLabel(master=title_frame, text="Clock", font=("Segoe UI Black", 50))
app_title2.pack(side="left", padx=5)

main_frame = ctk.CTkFrame(master=app, border_width=1)
main_frame.pack(expand=True, fill="both", padx=20, pady=20)

display = ctk.CTkFrame(master=main_frame, fg_color="transparent", width=350, height=70)
display.pack(padx=10, pady=10)

time_label = ctk.CTkLabel(master=display, text="00:00:00", width=350, height=70, font=("Bahnschrift SemiBold", 80))
time_label.pack(fill="both", expand=True)

btn_frames = ctk.CTkFrame(master=main_frame, fg_color="transparent")
btn_frames.pack(pady=10)

selected_hours = ctk.StringVar()
selected_mins = ctk.StringVar()
selected_secs = ctk.StringVar()

hours = ctk.CTkOptionMenu(master=btn_frames, values=[f"{i:02d}" for i in range(24)],
                          dropdown_hover_color="#308a3f", width=80, fg_color="black", font=("Arial", 15, "bold"),
                          variable=selected_hours)
hours.pack(side='left', padx=5)
hours.set("00")

mins = ctk.CTkOptionMenu(master=btn_frames, values=[f"{i:02d}" for i in range(60)],
                         dropdown_hover_color="#308a3f", width=80, fg_color="black", font=("Arial", 15, "bold"),
                         variable=selected_mins)
mins.pack(side='left', padx=5)
mins.set("00")

seconds = ctk.CTkOptionMenu(master=btn_frames, values=[f"{i:02d}" for i in range(60)],
                            dropdown_hover_color="#308a3f", width=80, fg_color="black", font=("Arial", 15, "bold"),
                            variable=selected_secs)
seconds.pack(side='left', padx=5)
seconds.set("00")

update_button = ctk.CTkButton(master=main_frame, text="Update", command=show_in_display, font=("Arial", 15, "bold"),
                              fg_color="#25805D")
update_button.pack(pady=20)

set_button = ctk.CTkButton(master=main_frame, text="Set Alarm", command=set_alarm, font=("Arial", 15, "bold"),
                           fg_color="#25805D")
set_button.pack()

feedback_label = ctk.CTkLabel(master=main_frame, text="", width=10, height=3, font=("Arial", 15))
feedback_label.pack(pady=20)

app.mainloop()
