import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\n""di seluruh tempat", 0.07),
        ("di seluruh dunia", 0.07),
        ("di manapun lagu cinta ini terputar", 0.08),
        ("aku bergeleng kecil dan tersenyum tipis", 0.08),
        ("andai lagu ini tertulis olehku...""\n", 0.09),   
    ]
    delays = [0.1, 2.0, 3.6, 6.3, 9.5]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()
        
if __name__ == "__main__":
    sing_song()