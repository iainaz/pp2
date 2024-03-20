import pygame
import sys
pygame.mixer.init()

_songs=["c:\\Users\\Администратор\\Downloads\\abintro.mp3","c:\\Users\\Администратор\\Downloads\\angry_birds.mp3","c:\\Users\\Администратор\\Downloads\\aboutro.mp3"]
screen=pygame.display.set_mode((500,500))
clock=pygame.time.Clock()
def play_prev_song():
    global _songs
    _songs = [_songs[-1]] + _songs[:-1]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
def play_next_song():
        global _songs
        _songs=_songs[1:]+[_songs[0]]
        pygame.mixer.music.load(_songs[0])
        pygame.mixer.music.play()

pygame.mixer.music.load(_songs[0])
pygame.mixer.music.play()
pygame.mixer.music.set_endevent(pygame.USEREVENT+1)

done=False
pause=False
vol=1.0
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        elif event.type==pygame.USEREVENT+1:
            play_next_song()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                pause=not pause
                if pause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key==pygame.K_UP:
                vol+=0.1
                pygame.mixer.music.set_volume(vol)
            elif event.key==pygame.K_DOWN:
                vol-=0.1
                pygame.mixer.music.set_volume(vol)
            elif event.key==pygame.K_RIGHT:
                play_next_song()
            elif event.key==pygame.K_LEFT:
                play_prev_song()
    clock.tick(60)
sys.exit()