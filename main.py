import pygame
import tkinter as tk
from tkinter import filedialog, ttk


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Spotify do Paraguai")
        self.root.geometry("500x350")
        self.root.config(bg="aquamarine3")
        
        self.playing = False
        self.paused = False

        pygame.mixer.init()
 
        self.music_files = []
        self.current_index = 0

        self.create_widgets()

    def create_widgets(self):
        self.button_frame = tk.Frame(self.root, bg="lightblue")
        self.button_frame.pack(pady=20)
        
        self.open_button = tk.Button(self.button_frame, text="Open", command=self.open_file, bg='aquamarine1', fg='black')
        self.open_button.grid(row=0, column=0, padx=10)

        self.play_button = tk.Button(self.button_frame, text="Play", command=self.play_music, bg='aquamarine1', fg='black')
        self.play_button.grid(row=0, column=1, padx=10)

        self.pause_button = tk.Button(self.button_frame, text="Pause", command=self.pause_music, bg='aquamarine1', fg='black')
        self.pause_button.grid(row=0, column=2, padx=10)
        
        self.restart_button = tk.Button(self.button_frame, text='Restart', command=self.restart_music, bg='aquamarine1', fg='black')
        self.restart_button.grid(row=0, column=3, padx=10)
        
        self.prev_button = tk.Button(self.button_frame, text="Previous", command=self.previous_music, bg="aquamarine1", fg="black")
        self.prev_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        self.next_button = tk.Button(self.button_frame, text="Next", command=self.next_music, bg="aquamarine1", fg="black")
        self.next_button.grid(row=1, column=2, columnspan=2, padx=10, pady=10)
        
        
        self.volume_label = tk.Label(self.root, text="Volume", bg="lightblue")
        self.volume_label.pack()
        
        self.volume_slider = ttk.Scale(self.root, from_=0, to=1, orient='horizontal', command=self.set_volume)
        self.volume_slider.set(0.5)
        self.volume_slider.pack(pady=10)


    def open_file(self):
        self.music_files = filedialog.askopenfilenames(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if self.music_files:
            self.current_index = 0
            pygame.mixer.music.load(self.music_files[self.current_index])

    def play_music(self):
        if not self.playing:
            pygame.mixer.music.play()
            self.playing = True
            self.paused = False
        elif self.paused:
            pygame.mixer.music.unpause()
            self.paused = False

    def pause_music(self):
        if self.playing and not self.paused:
            pygame.mixer.music.pause()
            self.paused = True
            
    def restart_music(self):
        if self.playing:
            pygame.mixer.music.rewind()
            
    def next_music(self):
        if self.music_files:
            self.current_index = (self.current_index + 1) % len(self.music_files)
            pygame.mixer.music.load(self.music_files[self.current_index])
            pygame.mixer.music.play()

    def previous_music(self):
        if self.music_files:
            self.current_index = (self.current_index - 1) % len(self.music_files)
            pygame.mixer.music.load(self.music_files[self.current_index])
            pygame.mixer.music.play()    
    
    
    def set_volume(self, val):
        volume = float(val)
        pygame.mixer.music.set_volume(volume)


if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()


