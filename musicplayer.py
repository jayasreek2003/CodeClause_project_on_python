import pygame
import os

pygame.init()

screen = pygame.display.set_mode((300, 200))

pygame.display.set_caption("Music Player")

music_dir = "C:\\Users\\jayas\\OneDrive\\Documents\\mymusic"

music_files = [file for file in os.listdir(music_dir) if file.endswith(".mp3")]


current_song_index = 0

pygame.mixer.music.load(os.path.join(music_dir, music_files[current_song_index]))

pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                current_song_index = (current_song_index + 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_dir, music_files[current_song_index]))
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_song_index = (current_song_index - 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_dir, music_files[current_song_index]))
                pygame.mixer.music.play()
pygame.quit()
