import tkinter as tk
import cv2
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("1000x700")
window.title('My first window')
header = tk.Label(window, text="WELCOME!", fg='navy blue', bg='light blue', font=('Andale Mono', 16, 'bold'))
header.pack()
window.configure(bg="light blue")

username_label = tk.Label(window, text="Username", font=('Andale Mono', 12, 'bold'), bg='light blue', fg='navy blue')
username_label.pack(pady=30)
username_entry = tk.Entry(window, relief='sunken', font=('Andale Mono', 12, 'bold'), bg='brown', fg='white',
                          borderwidth=0)
username_entry.pack()

password_label = tk.Label(window, text='Password', font=('Andale Mono', 12, 'bold'), bg='light blue', fg='navy blue')
password_label.pack(pady=20)
username_password = tk.Entry(window, relief='sunken', show='*', font=('Andale Mono', 12, 'bold'), bg='brown',
                             fg='white', borderwidth=0)
username_password.pack()

video_stream = None
video_screen = None
video_speed = 33


def gif_video_display():
    global video_stream, video_screen, video_speed


    video_name = "/Users/kajalprabhakar/Desktop/my-snowglobe/gui.mp4"

    video_stream = cv2.VideoCapture(video_name)

    if video_screen is None:
        video_screen = tk.Label(window, bg="black")

        video_screen.pack(pady=20, fill="both", expand=True)
    fps = video_stream.get(cv2.CAP_PROP_FPS)
    video_speed = int(1000 / fps) if fps > 0 else 33
    play_next_frame()


def play_next_frame():
    global video_stream, video_screen, video_speed

    if video_stream is not None:
        success, picture = video_stream.read()

        if success:
            normal_colors = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)


            tk_picture = ImageTk.PhotoImage(image=Image.fromarray(normal_colors))


            video_screen.config(image=tk_picture)
            video_screen.image = tk_picture


            window.after(video_speed, play_next_frame)
        else:

            video_stream.release()


def login():
    password = username_password.get()

    if password == '':
        show_password_label = tk.Label(window, text='no password entered', bg='light blue', fg='navy',
                                       font=('Andale Mono', 12, 'bold'))
        show_password_label.pack(pady=6)
    else:
        show_password_label = tk.Label(window, text=password, bg='light blue', fg='navy',
                                       font=('Andale Mono', 12, 'bold'))
        show_password_label.pack(pady=6)
        gif_label = tk.Label(window, text='do you want a suprise????', font=('Andale Mono', 12, 'bold'),
                             bg='light blue', fg='navy blue')
        gif_label.pack(pady=6)
        gif_entry_no = tk.Button(window, text='no 🗿', relief='sunken', font=('Andale Mono', 12, 'bold'), bg='brown',
                                 fg='brown', borderwidth=0)
        gif_entry_no.pack(pady=6)
        gif_entry_yes = tk.Button(window, text='yes 🤫', relief='sunken', font=('Andale Mono', 12, 'bold'), bg='brown',
                                  fg='brown', borderwidth=0, command=gif_video_display)
        gif_entry_yes.pack(pady=6)


show_password = tk.Button(window, command=login, text='show password', font=('Andale Mono', 12, 'bold'),
                          bg='light blue', fg='navy blue')
show_password.pack(pady=20)

window.mainloop()
