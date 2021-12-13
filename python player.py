


from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title('Codemy.com MP3 Player')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x300")
pygame.mixer.init()

def add_song():
    song = filedialog.askopenfilename(initialdir='/Users/apple1/Desktop/audio', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
    song = song.replace("/Users/apple1/Desktop/audio", "")
    song = song.replace(".mp3", "")
    song_box.insert(END, song)
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='/Users/apple1/Desktop/audio', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))

    for song in songs:
        song = song.replace("/Users/apple1/Desktop/audio", "")
        song = song.replace(".mp3", "")
        song_box.insert(END, song)

def play():
    song = song_box.get(ACTIVE)
    song = f'/Users/apple1/Desktop/audio{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

def next_song():
    next_one = song_box.curselection()
    next_one = next_one[0]+1
    song = song_box.get(next_one)

    song = f'/Users/apple1/Desktop/audio{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_box.selection_clear(0, END)

    song_box.activate(next_one)

    song_box.selection_set(next_one, last=None)

def previous_song():
    next_one = song_box.curselection()
    next_one = next_one[0] - 1
    song = song_box.get(next_one)

    song = f'/Users/apple1/Desktop/audio{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_box.selection_clear(0, END)

    song_box.activate(next_one)

    song_box.selection_set(next_one, last=None)

def delete_song():
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()

def delete_all_songs():
    song_box.delete(0, END)
    pygame.mixer.music.stop()
global paused
paused = False

def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused =False


    else:
        pygame.mixer.music.pause()
        paused = True

song_box = Listbox(root, bg="black", fg="green", width =60)
song_box.pack(pady=20)

back_btn_img = PhotoImage(file='/Users/apple1/Downloads/back.png')
forward_btn_img = PhotoImage(file='/Users/apple1/Downloads/forward.png')
play_btn_img = PhotoImage(file='/Users/apple1/Downloads/play.png')
pause_btn_img = PhotoImage(file='/Users/apple1/Downloads/pause.png')
stop_btn_img = PhotoImage(file='/Users/apple1/Downloads/stop.png')

controls_frame = Frame(root)
controls_frame.pack()

back_button = Button(controls_frame, image=back_btn_img, borderwidth=0, command=previous_song)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0, command=next_song)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)

back_button.grid(row=0, column=0)
forward_button.grid(row=0, column=1)
play_button.grid(row=0, column=2)
pause_button.grid(row=0, column=3)
stop_button.grid(row=0, column=4)

my_menu = Menu(root)
root.config(menu=my_menu)

add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song To Playlist", command=add_song)
add_song_menu.add_command(label="Add Many Songs To Playlist", command=add_many_songs)

remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete A Song From Playlist", command=delete_song)
remove_song_menu.add_command(label="Delete All Songs From Playlist", command=delete_all_songs)

root.mainloop()