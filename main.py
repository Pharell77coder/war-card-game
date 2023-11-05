import random
import tkinter as tk

from PIL import Image, ImageTk

root = tk.Tk()
root.title('Jeu de Cartes - Pharell')
root.geometry("1000x600")
root.iconbitmap('Assets/autre/icône.ico')
root.configure(background="green")
fond = "green"


def resize_cards(card):
    """

    :param card:
    :return:
    """
    our_card_img = Image.open(card)

    our_card_resize_image = our_card_img.resize((150, 218))

    global our_card_image
    our_card_image = ImageTk.PhotoImage(our_card_resize_image)

    return our_card_image


def shuffle():
    """

    :return:
    """
    suits = ["clubs", "spades", "diamonds", "hearts"]
    values = range(2, 15)

    global deck
    deck = []
    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')
    deck.append(f'15_of_red')
    deck.append(f'15_of_black')

    global dealer, player, dscore, pscore
    dealer, player, dscore, pscore = [], [], [], []

    dealer_card = random.choice(deck)
    deck.remove(dealer_card)
    dealer.append(dealer_card)

    global dealer_image
    dealer_image = resize_cards(f'Assets/img/langfr-150px-0{dealer_card}.svg.png')
    dealer_label.config(image=dealer_image)

    player_card = random.choice(deck)
    deck.remove(player_card)
    player.append(player_card)

    global player_image
    player_image = resize_cards(f'Assets/img/langfr-150px-0{player_card}.svg.png')
    player_label.config(image=player_image)

    root.title(f'Jeu de Cartes - {len(deck)} cartes restantes')
    score(dealer_card, player_card)


def deal_cards():
    """

    :return:
    """
    try:
        dealer_card = random.choice(deck)
        deck.remove(dealer_card)
        dealer.append(dealer_card)

        global dealer_image
        dealer_image = resize_cards(f'Assets/img/langfr-150px-0{dealer_card}.svg.png')
        dealer_label.config(image=dealer_image)

        player_card = random.choice(deck)
        deck.remove(player_card)
        player.append(player_card)

        global player_image
        player_image = resize_cards(f'Assets/img/langfr-150px-0{player_card}.svg.png')
        player_label.config(image=player_image)

        score(dealer_card, player_card)


    except:
        if dscore.count("x") == pscore.count("x"):
            root.title(f'Game Over! égalité! {dscore.count("x")} à {pscore.count("x")}')
        elif dscore.count("x") < pscore.count("x"):
            root.title(f'Game Over! le joueur a gagné! {dscore.count("x")} à {pscore.count("x")}')
        elif dscore.count("x") > pscore.count("x"):
            root.title(f'Game Over! le marchand a gagné!{dscore.count("x")} à {pscore.count("x")}')


def score(dealer_card, player_card):
    """

    :param dealer_card:
    :param player_card:
    :return:
    """
    dealer_card = int(dealer_card.split("_", 1)[0])
    player_card = int(player_card.split("_", 1)[0])

    if dealer_card == player_card:
        score_label.config(text="égalité ! Encore une fois!", bg=fond)

    elif dealer_card > player_card:
        score_label.config(text="Le marchand a gagné!", bg=fond)
        dscore.append("x")

    elif dealer_card < player_card:
        score_label.config(text="Le joueur a gagné!", bg=fond)
        pscore.append("x")

    root.title(f'Le marchand : {dscore.count("x")} -  {pscore.count("x")} : Le joueur')


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

score_label = tk.Label(root, text="", bg=fond)
score_label.pack(pady=20)

shuffle_button = tk.Button(root, text="Mélange la pioche", font='arial', command=shuffle)
shuffle_button.pack(pady=20)

card_button = tk.Button(root, text="Prendre une carte", font="arial", command=deal_cards)
card_button.pack(pady=20)

quit_button = tk.Button(root, text="Quittez le jeu", font="arial", bg='red', command=root.destroy)
quit_button.pack(pady=20)

shuffle()
root.mainloop()

