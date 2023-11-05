import tkinter as tk
from tkinter.constants import *
import random
from PIL import Image, ImageTk


root = tk.Tk()
root.title('Jeu de Cartes - Pharell')
root.geometry("950x550")
root.iconbitmap('Assets/autre/icône.ico')
root.configure(background="green")

def resize_cards(card):
    our_card_img = Image.open(card)

    our_card_resize_image = our_card_img.resize((150, 218))

    global our_card_image
    our_card_image = ImageTk.PhotoImage(our_card_resize_image)

    return our_card_image

def shuffle():
    suits = ["clubs", "spades", "diamonds", "hearts"]
    values = range(2, 15)

    global deck
    deck = []
    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')
    deck.append(f'15_of_red')
    deck.append(f'15_of_black')
    
    global dealer, player
    dealer, player = [], []

    card = random.choice(deck)
    deck.remove(card)
    dealer.append(card)
    dealer_label.config(text=card)

    global dealer_image
    dealer_image = resize_cards(f'Assets/img/langfr-150px-0{card}.svg.png')
    dealer_label.config(image=dealer_image)

    card = random.choice(deck)
    deck.remove(card)
    player.append(card)
    player_label.config(text=card)

    global player_image
    player_image = resize_cards(f'Assets/img/langfr-150px-0{card}.svg.png')
    player_label.config(image=player_image)

    root.title(f'Jeu de Cartes - {len(deck)} cartes restantes')

def deal_cards():
    try:
        card = random.choice(deck)
        deck.remove(card)
        dealer.append(card)
        dealer_label.config(text=card)

        card = random.choice(deck)
        deck.remove(card)
        player.append(card)
        player_label.config(text=card)

    except:
        root.title(f'Jeu de Cartes - Il ya plus de cartes dans le paquet')

myframe = tk.Frame(root, bg='green')
myframe.pack(pady=20)

dealer_frame = tk.LabelFrame(myframe, text="Marchand", bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

player_frame = tk.LabelFrame(myframe, text="Joueur", bd=0)
player_frame.grid(row=0, column=1, ipadx=20)

dealer_label = tk.Label(dealer_frame, text="Aucune carte piochez")
dealer_label.pack(pady=20)

player_label = tk.Label(player_frame, text="Aucune carte piochez")
player_label.pack(pady=20)

shuffle_button = tk.Button(root, text="Mélange la pioche", font='arial', command=shuffle)
shuffle_button.pack(pady=20)

card_button = tk.Button(root, text="Prendre une carte", font="arial", command=deal_cards)
card_button.pack(pady=20)

quit_button = tk.Button(root, text="    Quittez le jeu    ", font="arial", bg='red', command=root.destroy)
quit_button.pack(pady=20)

root.mainloop()