import os
import pygame


pygame.init()
pygame.mixer.init()


music_folder = "musics/"


music_files = [f for f in os.listdir(music_folder) if f.lower().endswith(('.mp3', '.wav', '.ogg'))]
if not music_files:
    print("No music files found in", music_folder)
    pygame.quit()
    exit()


current_index = 0

def play_music(index):
    """Load and play the music file at the specified index."""
    track_path = os.path.join(music_folder, music_files[index])
    try:
        pygame.mixer.music.load(track_path)
        pygame.mixer.music.play()
        print(f"Now playing: {music_files[index]}")
    except Exception as e:
        print("Error playing", music_files[index], ":", e)

def stop_music():
    """Stop the current music."""
    pygame.mixer.music.stop()
    print("Music stopped.")

def next_music():
    """Advance to the next track and play it."""
    global current_index
    current_index = (current_index + 1) % len(music_files)
    play_music(current_index)

def previous_music():
    """Go back to the previous track and play it."""
    global current_index
    current_index = (current_index - 1) % len(music_files)
    play_music(current_index)

# Create a basic window so we can capture keyboard events
screen = pygame.display.set_mode((500, 150))
pygame.display.set_caption("Music Player")

# Setup a font for instructions
font = pygame.font.Font(None, 28)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for key presses
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:       # P key for play/resume
                play_music(current_index)
            elif event.key == pygame.K_s:     # S key for stop
                stop_music()
            elif event.key == pygame.K_n:     # N key for next track
                next_music()
            elif event.key == pygame.K_b:     # B key for previous track
                previous_music()

    # Clear screen and display instructions
    screen.fill((30, 30, 30))
    instructions = [
        "Press P to Play",
        "Press S to Stop",
        "Press N for Next track",
        "Press B for Previous track",
        "Close the window to exit."
    ]
    for i, line in enumerate(instructions):
        text_surface = font.render(line, True, (255, 255, 255))
        screen.blit(text_surface, (20, 20 + i * 25))
    pygame.display.flip()

pygame.quit()