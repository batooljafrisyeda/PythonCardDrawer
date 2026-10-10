import tkinter as tk
import random
from PIL import Image, ImageTk
from pygame import mixer
from pathlib import Path
import time

mixer.init()
base_dir = Path(__file__).resolve().parent
shuffle_sound = mixer.Sound(str(base_dir / "Sounds" / "shuffle.mp3"))

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
all_cards = []
for suit in suits:
    for rank in ranks:
        all_cards.append((rank, suit))

previous_rank = None

def draw_card():
    card_label.config(image=back_photo)
    window.update()
    shuffle_sound.play()
    for _ in range(8):
        rank, suit = random.choice(all_cards)

        rank_file = rank.lower()
        suit_file = suit.lower()
        filename = base_dir / "Cards" / f"{rank_file}_of_{suit_file}.png"
        image = Image.open(filename)
        image = image.resize((200, 300))
        photo = ImageTk.PhotoImage(image)
        card_label.config(image=photo)
        card_label.image = photo
        window.update()
        time.sleep(0.05)

    global previous_rank
    while True:
        rank = random.choice(ranks)
        if rank != previous_rank:
            break

    suit = random.choice(suits)
    rank_file = rank.lower()
    suit_file = suit.lower()
    filename = f"Cards/{rank_file}_of_{suit_file}.png"
    image = Image.open(filename)
    image = image.resize((200, 300))
    photo = ImageTk.PhotoImage(image)
    previous_rank = rank
    card_label.config(image=photo)
    card_label.image = photo

window = tk.Tk()
window.title("Card Drawer")

window.geometry("400x500")

back_image = Image.open(base_dir / "Cards" / "back.png")
back_image = back_image.resize((200, 300))
back_photo = ImageTk.PhotoImage(back_image)

title = tk.Label(
    window,
    text="🎴 Card Drawer 🎴",
    font=("Arial", 18)
)
title.pack(pady=20)

card_label = tk.Label(
    window,
    bd=5,
    relief="raised",
    image=back_photo
)

card_label.pack(pady=30)

draw_button = tk.Button(
    window,
    text="Draw Card",
    font=("Arial", 14),
    command=draw_card
)
draw_button.pack()

window.mainloop()